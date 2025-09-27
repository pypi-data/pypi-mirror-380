"""CNN-based OCR handlers for 4-character lowercase captchas."""

from __future__ import annotations

import logging
import string
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from captcha_ocr_devkit.core.handlers.base import (
    BaseEvaluateHandler,
    BaseOCRHandler,
    BaseTrainHandler,
    EvaluationResult,
    HandlerResult,
    TrainingConfig,
)

from captcha_ocr_devkit.examples.handlers.ocr_common import (
    TorchHandlerDependencyMixin,
    OCRDataset,
    collate_batch,
    format_dependency_error,
    resolve_device,
    set_seed,
    _missing_dependencies,
    TORCH_AVAILABLE,
    torch,
    nn,
    optim,
    DataLoader,
    random_split,
)
from captcha_ocr_devkit.examples.handlers.transformer_handler import TransformerPreprocessHandler

CNN_HANDLER_VERSION = "1.20250923.1900"
CNN_DEPENDENCIES = ["torch", "torchvision", "pillow", "numpy"]
CNN_REQUIREMENTS_FILE = "cnn_handler-requirements.txt"
DEFAULT_NUM_CHARACTERS = 4
DEFAULT_ALPHABET = list(string.ascii_lowercase)
DEFAULT_IMG_HEIGHT = TransformerPreprocessHandler.DEFAULT_IMG_HEIGHT
DEFAULT_IMG_WIDTH = TransformerPreprocessHandler.DEFAULT_IMG_WIDTH


class CNNDependencyMixin(TorchHandlerDependencyMixin):
    """Override requirements file defaults for CNN handlers."""

    REQUIREMENTS_FILE = CNN_REQUIREMENTS_FILE


LOGGER = logging.getLogger(__name__)
if not LOGGER.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    LOGGER.addHandler(handler)
    LOGGER.propagate = False
if LOGGER.getEffectiveLevel() > logging.INFO:
    LOGGER.setLevel(logging.INFO)


def _ensure_torch_available() -> None:
    if not TORCH_AVAILABLE:
        raise RuntimeError("PyTorch is required for CNN handlers. Please install torch and torchvision.")


def _normalize_alphabet(alphabet: Union[str, Sequence[str]]) -> List[str]:
    if isinstance(alphabet, str):
        candidates = list(alphabet)
    else:
        candidates = [str(ch) for ch in alphabet if str(ch)]
    normalized: List[str] = []
    seen = set()
    for item in candidates:
        symbol = item[0]
        if symbol not in seen:
            normalized.append(symbol)
            seen.add(symbol)
    return normalized or DEFAULT_ALPHABET.copy()


def _is_valid_label(label: str, alphabet_set: set[str], num_characters: int) -> bool:
    return len(label) == num_characters and all(ch in alphabet_set for ch in label)


def _filter_dataset_samples(
    dataset: OCRDataset,
    alphabet_set: set[str],
    num_characters: int,
) -> Tuple[int, int]:
    original = len(dataset.samples)
    dataset.samples = [
        (path, label)
        for path, label in dataset.samples
        if _is_valid_label(label, alphabet_set, num_characters)
    ]
    return original, len(dataset.samples)


class CNNPreprocessHandler(CNNDependencyMixin, TransformerPreprocessHandler):
    """Resize and normalize captcha images for the CNN pipeline."""

    DESCRIPTION = "Resize captcha images and normalize them for CNN OCR training and inference."
    SHORT_DESCRIPTION = "Preprocess captcha images for CNN OCR."
    REQUIRED_DEPENDENCIES = CNN_DEPENDENCIES
    HANDLER_ID = "cnn_preprocess"

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info["version"] = CNN_HANDLER_VERSION
        return info


class ResidualBlock(nn.Module):
    """Residual block with batch normalization and dropout."""

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, dropout: float = 0.1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.dropout = nn.Dropout2d(dropout)

        # Skip connection
        self.skip = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.skip = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        residual = self.skip(x)

        out = torch.relu(self.bn1(self.conv1(x)))
        out = self.dropout(out)
        out = self.bn2(self.conv2(out))

        out += residual
        return torch.relu(out)


class AttentionModule(nn.Module):
    """Channel and spatial attention module."""

    def __init__(self, channels: int):
        super().__init__()
        # Channel attention
        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(channels, channels // 8, 1),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels // 8, channels, 1),
            nn.Sigmoid()
        )

        # Spatial attention
        self.spatial_attention = nn.Sequential(
            nn.Conv2d(2, 1, kernel_size=7, padding=3),
            nn.Sigmoid()
        )

    def forward(self, x):
        # Channel attention
        ca = self.channel_attention(x)
        x = x * ca

        # Spatial attention
        avg_pool = torch.mean(x, dim=1, keepdim=True)
        max_pool, _ = torch.max(x, dim=1, keepdim=True)
        spatial_input = torch.cat([avg_pool, max_pool], dim=1)
        sa = self.spatial_attention(spatial_input)
        x = x * sa

        return x


class CNNClassifier(nn.Module):
    """Optimized CNN with residual blocks, attention, and multi-scale features."""

    def __init__(self, num_classes: int, num_characters: int, in_channels: int = 1, use_optimized: bool = True, dropout: float = 0.2):
        super().__init__()
        self.num_characters = num_characters
        self.num_classes = num_classes
        self.use_optimized = use_optimized

        if use_optimized:
            # Optimized architecture with residual blocks and attention
            # Initial feature extraction
            self.stem = nn.Sequential(
                nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3, bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
            )

            # Residual blocks with progressive channel increase
            self.layer1 = self._make_layer(64, 64, 2, stride=1, dropout=dropout)
            self.layer2 = self._make_layer(64, 128, 2, stride=2, dropout=dropout)
            self.layer3 = self._make_layer(128, 256, 2, stride=2, dropout=dropout)
            self.layer4 = self._make_layer(256, 512, 2, stride=2, dropout=dropout)

            # Attention modules
            self.attention1 = AttentionModule(128)
            self.attention2 = AttentionModule(256)
            self.attention3 = AttentionModule(512)

            # Multi-scale feature fusion (MPS compatible)
            self.feature_fusion = nn.Sequential(
                nn.AdaptiveAvgPool2d((1, 1)),  # MPS compatible global pooling
                nn.Flatten(),
                nn.Linear(512, 1024),
                nn.ReLU(inplace=True),
                nn.Dropout(dropout),
                nn.Linear(1024, 512),
                nn.ReLU(inplace=True),
                nn.Dropout(dropout)
            )

            # Character-specific heads
            self.character_heads = nn.ModuleList([
                nn.Sequential(
                    nn.Linear(512, 256),
                    nn.ReLU(inplace=True),
                    nn.Dropout(dropout / 2),
                    nn.Linear(256, num_classes)
                ) for _ in range(num_characters)
            ])
        else:
            # Basic architecture (original)
            self.encoder = nn.Sequential(
                nn.Conv2d(in_channels, 64, kernel_size=3, padding=1),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2, 2),
                nn.Conv2d(64, 128, kernel_size=3, padding=1),
                nn.BatchNorm2d(128),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2, 2),
                nn.Conv2d(128, 256, kernel_size=3, padding=1),
                nn.BatchNorm2d(256),
                nn.ReLU(inplace=True),
                nn.AdaptiveAvgPool2d((1, 1)),
            )
            self.head = nn.Linear(256, num_classes * num_characters)

    def _make_layer(self, in_channels: int, out_channels: int, blocks: int, stride: int = 1, dropout: float = 0.1):
        layers = []
        layers.append(ResidualBlock(in_channels, out_channels, stride, dropout))
        for _ in range(1, blocks):
            layers.append(ResidualBlock(out_channels, out_channels, 1, dropout))
        return nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.use_optimized:
            # Optimized forward pass
            x = self.stem(x)
            x = self.layer1(x)

            x = self.layer2(x)
            x = self.attention1(x)

            x = self.layer3(x)
            x = self.attention2(x)

            x = self.layer4(x)
            x = self.attention3(x)

            # Feature fusion
            features = self.feature_fusion(x)

            # Character-specific predictions
            char_outputs = []
            for head in self.character_heads:
                char_outputs.append(head(features))

            # Stack character predictions
            char_logits = torch.stack(char_outputs, dim=1)  # [batch, num_chars, num_classes]
            return char_logits
        else:
            # Basic forward pass
            features = self.encoder(x)
            features = features.view(features.size(0), -1)
            logits = self.head(features)
            return logits.view(x.size(0), self.num_characters, self.num_classes)


def _labels_to_tensor(labels: Sequence[str], alphabet_map: Dict[str, int], num_characters: int) -> torch.Tensor:
    indices = []
    for label in labels:
        indices.extend(alphabet_map[ch] for ch in label[:num_characters])
    return torch.tensor(indices, dtype=torch.long).view(len(labels), num_characters)


def _logits_to_predictions(
    logits: torch.Tensor,
    alphabet: Sequence[str],
    num_characters: int,
) -> List[str]:
    top_indices = logits.argmax(dim=-1).cpu().tolist()
    predictions: List[str] = []
    for sample in top_indices:
        chars = [alphabet[idx] for idx in sample[:num_characters]]
        predictions.append("".join(chars))
    return predictions


def _compute_char_accuracy(predictions: Sequence[str], labels: Sequence[str]) -> float:
    if not predictions:
        return 0.0
    total_chars = sum(len(label) for label in labels)
    correct = 0
    for pred, label in zip(predictions, labels):
        correct += sum(1 for p, t in zip(pred, label) if p == t)
    return correct / max(1, total_chars)


class CNNTrainHandler(CNNDependencyMixin, BaseTrainHandler):
    """Train the CNN OCR model on fixed-length captcha datasets."""

    DESCRIPTION = "Train a compact CNN that predicts four lowercase characters with multi-head classification."
    SHORT_DESCRIPTION = "Train CNN OCR for 4-char captchas."
    REQUIRED_DEPENDENCIES = CNN_DEPENDENCIES
    HANDLER_ID = "cnn_train"

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        cfg = config or {}
        self.img_h = int(cfg.get("img_height", DEFAULT_IMG_HEIGHT))
        self.img_w = int(cfg.get("img_width", DEFAULT_IMG_WIDTH))
        self.num_workers = int(cfg.get("num_workers", 0))
        self.device_name = cfg.get("device", "auto")
        self.log_interval = max(0, int(cfg.get("log_interval", 50)))
        self.weight_decay = float(cfg.get("weight_decay", 1e-4))
        self.alphabet = _normalize_alphabet(cfg.get("alphabet", DEFAULT_ALPHABET))
        self.num_characters = int(cfg.get("num_characters", DEFAULT_NUM_CHARACTERS))
        self.alphabet_map = {ch: idx for idx, ch in enumerate(self.alphabet)}

        # Optimized architecture settings
        self.use_optimized = cfg.get("use_optimized", True)
        self.dropout = float(cfg.get("dropout", 0.2))
        self.label_smoothing = float(cfg.get("label_smoothing", 0.1))
        self.cosine_annealing = cfg.get("cosine_annealing", True)
        self.early_stopping_patience = int(cfg.get("early_stopping_patience", 10))

    def train(self, config: TrainingConfig) -> HandlerResult:
        missing = _missing_dependencies()
        if missing:
            return HandlerResult(success=False, error=format_dependency_error(missing, self._install_hint()))

        _ensure_torch_available()

        input_dir = config.input_dir
        if not input_dir.exists():
            return HandlerResult(success=False, error=f"Training data directory not found: {input_dir}")

        set_seed(config.seed)
        device = resolve_device(config.device if config.device != "auto" else self.device_name)

        try:
            dataset = OCRDataset(
                input_dir,
                self.img_h,
                self.img_w,
                requirements_override=self._requirements_override(),
            )
        except Exception as exc:
            return HandlerResult(success=False, error=str(exc))

        alphabet_set = set(self.alphabet)
        original_count, filtered_count = _filter_dataset_samples(dataset, alphabet_set, self.num_characters)
        if filtered_count == 0:
            return HandlerResult(
                success=False,
                error="No samples match the CNN handler constraints (length and alphabet).",
            )
        removed = original_count - filtered_count

        val_split = float(config.validation_split)
        total_samples = len(dataset)
        val_size = 0
        if total_samples > 1 and val_split > 0:
            val_size = max(1, int(total_samples * val_split))
            if val_size >= total_samples:
                val_size = max(1, total_samples // 5)
        train_size = total_samples - val_size
        if train_size <= 0:
            train_size = max(1, total_samples - 1)
            val_size = total_samples - train_size

        if val_size > 0 and random_split is not None:
            train_ds, val_ds = random_split(dataset, [train_size, val_size])
        else:
            train_ds, val_ds = dataset, None

        train_loader = DataLoader(
            train_ds,
            batch_size=config.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
            collate_fn=collate_batch,
        )
        if self.log_interval:
            setattr(train_loader, "_log_interval", self.log_interval)
            setattr(train_loader, "_total_epochs", config.epochs)

        val_loader = None
        if val_ds is not None:
            val_loader = DataLoader(
                val_ds,
                batch_size=config.batch_size,
                shuffle=False,
                num_workers=self.num_workers,
                collate_fn=collate_batch,
            )

        model = CNNClassifier(
            num_classes=len(self.alphabet),
            num_characters=self.num_characters,
            use_optimized=self.use_optimized,
            dropout=self.dropout
        )
        model.to(device)
        criterion = nn.CrossEntropyLoss(label_smoothing=self.label_smoothing)
        optimizer = optim.AdamW(model.parameters(), lr=config.learning_rate, weight_decay=self.weight_decay)

        # Learning rate scheduler
        if self.cosine_annealing:
            scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config.epochs)
        else:
            scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=config.epochs//3, gamma=0.1)

        history: List[Dict[str, Any]] = []
        best_accuracy = -1.0
        best_char_accuracy = -1.0
        patience_counter = 0

        LOGGER.info(
            "CNN training configured: version=%s epochs=%d, batches=%d, device=%s, log_interval=%d",
            CNN_HANDLER_VERSION,
            config.epochs,
            len(train_loader),
            device,
            self.log_interval,
        )

        for epoch in range(1, config.epochs + 1):
            if self.log_interval:
                setattr(train_loader, "_epoch_index", epoch)
            LOGGER.info("Epoch %d/%d started", epoch, config.epochs)
            print(
                f"[CNNTrainHandler] epoch {epoch}/{config.epochs} started (version {CNN_HANDLER_VERSION})",
                flush=True,
            )

            model.train()
            running_loss = 0.0
            total_items = 0
            for batch_index, (inputs, labels, _) in enumerate(train_loader, start=1):
                inputs = inputs.to(device)
                targets = _labels_to_tensor(labels, self.alphabet_map, self.num_characters).to(device)
                logits = model(inputs)
                loss = criterion(logits.view(-1, logits.size(-1)), targets.view(-1))
                optimizer.zero_grad()
                loss.backward()

                # Gradient clipping
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

                optimizer.step()

                batch_size = inputs.size(0)
                running_loss += loss.item() * batch_size
                total_items += batch_size

                if self.log_interval and batch_index % self.log_interval == 0:
                    LOGGER.info(
                        "CNN training (epoch %d/%d) batch %d/%d avg_loss=%.4f",
                        epoch,
                        config.epochs,
                        batch_index,
                        len(train_loader),
                        running_loss / max(1, total_items),
                    )

            train_loss = running_loss / max(1, total_items)

            val_accuracy = None
            val_char_accuracy = None
            if val_loader is not None:
                model.eval()
                total = 0
                correct = 0
                correct_chars = 0
                with torch.no_grad():
                    for inputs, labels, _ in val_loader:
                        inputs = inputs.to(device)
                        logits = model(inputs)
                        predictions = _logits_to_predictions(logits, self.alphabet, self.num_characters)
                        total += len(labels)
                        correct += sum(1 for pred, truth in zip(predictions, labels) if pred == truth)
                        correct_chars += sum(
                            sum(1 for p, t in zip(pred, truth) if p == t)
                            for pred, truth in zip(predictions, labels)
                        )
                val_accuracy = correct / max(1, total)
                val_char_accuracy = correct_chars / max(1, total * self.num_characters)

            LOGGER.info(
                "Epoch %d/%d finished: loss=%.4f%s",
                epoch,
                config.epochs,
                train_loss,
                (
                    f", val_acc={val_accuracy:.4f}, val_char_acc={val_char_accuracy:.4f}"
                    if val_accuracy is not None
                    else ""
                ),
            )
            extra = ""
            if val_accuracy is not None:
                extra = f", val_acc={val_accuracy:.4f}, val_char_acc={val_char_accuracy:.4f}"
            print(
                f"[CNNTrainHandler] epoch {epoch}/{config.epochs} finished loss={train_loss:.4f}{extra}",
                flush=True,
            )

            history.append(
                {
                    "epoch": epoch,
                    "loss": train_loss,
                    "val_accuracy": val_accuracy,
                    "val_char_accuracy": val_char_accuracy,
                }
            )

            # Learning rate scheduling
            scheduler.step()

            # Model checkpointing and early stopping
            should_save = val_loader is None or (val_accuracy is not None and val_accuracy >= best_accuracy)
            if should_save:
                if val_accuracy is not None:
                    best_accuracy = max(best_accuracy, val_accuracy)
                    patience_counter = 0
                if val_char_accuracy is not None:
                    best_char_accuracy = max(best_char_accuracy, val_char_accuracy)
                checkpoint = {
                    "model": model.state_dict(),
                    "alphabet": self.alphabet,
                    "num_characters": self.num_characters,
                    "img_h": self.img_h,
                    "img_w": self.img_w,
                    "use_optimized": self.use_optimized,
                    "dropout": self.dropout,
                    "handler_version": CNN_HANDLER_VERSION,
                }
                if not self.save_model(checkpoint, config.output_path):
                    return HandlerResult(success=False, error="Failed to save optimized CNN checkpoint")
            else:
                patience_counter += 1
                if patience_counter >= self.early_stopping_patience:
                    LOGGER.info(f"Early stopping triggered after {epoch} epochs")
                    break

        metadata = {
            "device": str(device),
            "total_samples": total_samples,
            "removed_samples": removed,
            "alphabet_size": len(self.alphabet),
            "handler_version": CNN_HANDLER_VERSION,
        }
        result_data = {
            "model_path": str(config.output_path),
            "history": history,
            "best_val_accuracy": best_accuracy if best_accuracy >= 0 else None,
            "best_val_char_accuracy": best_char_accuracy if best_char_accuracy >= 0 else None,
        }

        return HandlerResult(success=True, data=result_data, metadata=metadata)

    def save_model(self, model_data: Any, output_path: Path) -> bool:
        try:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save(model_data, str(output_path))
            return True
        except Exception:
            return False

    def load_model(self, model_path: Path) -> Any:
        _ensure_torch_available()
        return torch.load(str(model_path), map_location="cpu")

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": CNN_HANDLER_VERSION,
            "description": self.get_description(),
            "short_description": self.get_short_description(),
            "dependencies": self.get_dependencies(),
            "dependency_status": self.get_dependency_status(),
            "missing_dependencies": self.get_missing_dependencies(),
            "requirements_file": str(self._requirements_file_path()),
            "install_hint": self._install_hint(),
            "img_height": self.img_h,
            "img_width": self.img_w,
            "alphabet": self.alphabet,
            "num_characters": self.num_characters,
            "device": self.device_name,
            "weight_decay": self.weight_decay,
            "num_workers": self.num_workers,
            "log_interval": self.log_interval,
        }


class CNNEvaluateHandler(CNNDependencyMixin, BaseEvaluateHandler):
    """Evaluate CNN OCR checkpoints on labeled datasets."""

    DESCRIPTION = "Evaluate CNN OCR checkpoints and report captcha- and character-level accuracy."
    SHORT_DESCRIPTION = "Evaluate CNN captcha OCR checkpoints."
    REQUIRED_DEPENDENCIES = CNN_DEPENDENCIES
    HANDLER_ID = "cnn_evaluate"

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        cfg = config or {}
        self.batch_size = int(cfg.get("batch_size", 32))
        self.device_name = cfg.get("device", "auto")
        self.num_workers = int(cfg.get("num_workers", 0))

    def evaluate(self, model_path: Path, test_data_path: Path) -> HandlerResult:
        missing = _missing_dependencies()
        if missing:
            return HandlerResult(success=False, error=format_dependency_error(missing, self._install_hint()))

        _ensure_torch_available()

        if not model_path.exists():
            return HandlerResult(success=False, error=f"Checkpoint not found: {model_path}")
        if not test_data_path.exists():
            return HandlerResult(success=False, error=f"Test data directory not found: {test_data_path}")

        checkpoint = torch.load(str(model_path), map_location="cpu")
        alphabet = _normalize_alphabet(checkpoint.get("alphabet", DEFAULT_ALPHABET))
        num_characters = int(checkpoint.get("num_characters", DEFAULT_NUM_CHARACTERS))
        img_h = int(checkpoint.get("img_h", DEFAULT_IMG_HEIGHT))
        img_w = int(checkpoint.get("img_w", DEFAULT_IMG_WIDTH))
        use_optimized = checkpoint.get("use_optimized", False)  # Default to basic for old models
        dropout = checkpoint.get("dropout", 0.2)

        try:
            dataset = OCRDataset(
                test_data_path,
                img_h,
                img_w,
                requirements_override=self._requirements_override(),
            )
        except Exception as exc:
            return HandlerResult(success=False, error=str(exc))

        alphabet_set = set(alphabet)
        original_count, filtered_count = _filter_dataset_samples(dataset, alphabet_set, num_characters)
        if filtered_count == 0:
            return HandlerResult(success=False, error="No valid samples found for evaluation.")

        loader = DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            collate_fn=collate_batch,
        )

        device = resolve_device(self.device_name)
        model = CNNClassifier(
            num_classes=len(alphabet),
            num_characters=num_characters,
            use_optimized=use_optimized,
            dropout=dropout
        )
        model.load_state_dict(checkpoint["model"])
        model.to(device)
        model.eval()

        records: List[Tuple[Path, str, str]] = []
        with torch.no_grad():
            for inputs, labels, paths in loader:
                inputs = inputs.to(device)
                logits = model(inputs)
                preds = _logits_to_predictions(logits, alphabet, num_characters)
                records.extend(zip(paths, labels, preds))

        predictions = [pred for _, _, pred in records]
        ground_truth = [label for _, label, _ in records]
        metrics = self.calculate_metrics(predictions, ground_truth)
        metrics.total_samples = len(dataset)
        metrics.correct_predictions = sum(1 for pred, truth in zip(predictions, ground_truth) if pred == truth)

        LOGGER.info(
            "CNN evaluation processed %d samples: accuracy=%.4f, char_accuracy=%.4f (%d correct)",
            metrics.total_samples,
            metrics.accuracy,
            metrics.character_accuracy,
            metrics.correct_predictions,
        )

        metadata = {
            "device": str(device),
            "handler_version": CNN_HANDLER_VERSION,
            "filtered_samples": filtered_count,
            "original_samples": original_count,
        }
        data = {
            "model_path": str(model_path),
            "test_data_path": str(test_data_path),
            "accuracy": metrics.accuracy,
            "character_accuracy": metrics.character_accuracy,
            "predictions": [
                {
                    "path": str(path),
                    "label": label,
                    "prediction": pred,
                    "correct": pred == label,
                }
                for path, label, pred in records
            ],
        }

        return HandlerResult(success=True, data=data, metadata=metadata)

    def calculate_metrics(self, predictions: List[str], ground_truth: List[str]) -> EvaluationResult:
        total = len(ground_truth)
        correct = sum(1 for pred, truth in zip(predictions, ground_truth) if pred == truth)
        char_accuracy = _compute_char_accuracy(predictions, ground_truth)
        return EvaluationResult(
            accuracy=correct / max(1, total),
            total_samples=total,
            correct_predictions=correct,
            character_accuracy=char_accuracy,
        )

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": CNN_HANDLER_VERSION,
            "description": self.get_description(),
            "short_description": self.get_short_description(),
            "dependencies": self.get_dependencies(),
            "dependency_status": self.get_dependency_status(),
            "missing_dependencies": self.get_missing_dependencies(),
            "requirements_file": str(self._requirements_file_path()),
            "install_hint": self._install_hint(),
            "batch_size": self.batch_size,
            "device": self.device_name,
        }


class CNNOCRHandler(CNNDependencyMixin, BaseOCRHandler):
    """Inference handler that wraps the CNN OCR classifier."""

    DESCRIPTION = "Predict 4-character lowercase captchas using a CNN classifier with multi-head outputs."
    SHORT_DESCRIPTION = "Inference for CNN captcha OCR."
    REQUIRED_DEPENDENCIES = CNN_DEPENDENCIES
    HANDLER_ID = "cnn_ocr"

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        cfg = config or {}
        self.device_name = cfg.get("device", "auto")
        self.alphabet = _normalize_alphabet(cfg.get("alphabet", DEFAULT_ALPHABET))
        self.num_characters = int(cfg.get("num_characters", DEFAULT_NUM_CHARACTERS))
        self.img_h = int(cfg.get("img_height", DEFAULT_IMG_HEIGHT))
        self.img_w = int(cfg.get("img_width", DEFAULT_IMG_WIDTH))
        self.model: Optional[CNNClassifier] = None
        self.device: Optional[torch.device] = None

    def load_model(self, model_path: Path) -> bool:
        missing = _missing_dependencies()
        if missing:
            raise RuntimeError(format_dependency_error(missing, self._install_hint()))

        _ensure_torch_available()

        try:
            checkpoint = torch.load(str(model_path), map_location="cpu")
            stored_alphabet = checkpoint.get("alphabet")
            if stored_alphabet:
                self.alphabet = _normalize_alphabet(stored_alphabet)
            self.num_characters = int(checkpoint.get("num_characters", self.num_characters))
            self.img_h = int(checkpoint.get("img_h", self.img_h))
            self.img_w = int(checkpoint.get("img_w", self.img_w))
            use_optimized = checkpoint.get("use_optimized", False)
            dropout = checkpoint.get("dropout", 0.2)

            self.model = CNNClassifier(
                num_classes=len(self.alphabet),
                num_characters=self.num_characters,
                use_optimized=use_optimized,
                dropout=dropout
            )
            self.model.load_state_dict(checkpoint["model"])
            self.device = resolve_device(self.device_name)
            self.model.to(self.device)
            self.model.eval()
            return True
        except Exception as exc:  # pragma: no cover - defensive branch
            raise RuntimeError(f"Failed to load CNN OCR checkpoint: {exc}")

    def predict(self, processed_image: Any) -> HandlerResult:
        missing = _missing_dependencies()
        if missing:
            return HandlerResult(success=False, error=format_dependency_error(missing, self._install_hint()))
        if self.model is None or self.device is None:
            return HandlerResult(success=False, error="Model not loaded. Call load_model() first.")

        try:
            if isinstance(processed_image, torch.Tensor):
                tensor = processed_image
                metadata: Dict[str, Any] = {}
            else:
                preprocess = CNNPreprocessHandler(
                    "temp",
                    {
                        "img_height": self.img_h,
                        "img_width": self.img_w,
                        "requirements_file": self._requirements_override(),
                    },
                )
                preprocess_result = preprocess.process(processed_image)
                if not preprocess_result.success:
                    return preprocess_result
                tensor = preprocess_result.data
                metadata = preprocess_result.metadata or {}

            if tensor.dim() == 3:
                tensor = tensor.unsqueeze(0)
            tensor = tensor.to(self.device)

            logits = self.model(tensor)
            prediction = _logits_to_predictions(logits, self.alphabet, self.num_characters)[0]

            metadata.update(
                {
                    "handler_version": CNN_HANDLER_VERSION,
                    "alphabet": self.alphabet,
                    "num_characters": self.num_characters,
                }
            )
            return HandlerResult(success=True, data=prediction, metadata=metadata)
        except Exception as exc:  # pragma: no cover - defensive branch
            return HandlerResult(success=False, error=str(exc))

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": CNN_HANDLER_VERSION,
            "description": self.get_description(),
            "short_description": self.get_short_description(),
            "dependencies": self.get_dependencies(),
            "dependency_status": self.get_dependency_status(),
            "missing_dependencies": self.get_missing_dependencies(),
            "requirements_file": str(self._requirements_file_path()),
            "install_hint": self._install_hint(),
            "alphabet": self.alphabet,
            "num_characters": self.num_characters,
            "device": self.device_name,
        }


__all__ = [
    "CNNPreprocessHandler",
    "CNNTrainHandler",
    "CNNEvaluateHandler",
    "CNNOCRHandler",
]
