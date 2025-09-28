# File: src/samudra_ai/__init__.py
from .core import SamudraAI, SamudraAI2
from .data_loader import load_and_mask_dataset
from .trainer import prepare_training_data, plot_training_history
from .evaluator import evaluate_model
from .preprocess_dcpp import preprocess_dcpp

__version__ = "1.2.5"
__all__ = [
    'SamudraAI',
    'SamudraAI2',
    'load_and_mask_dataset',
    'prepare_training_data',
    'plot_training_history',
    'evaluate_model',
    "preprocess_dcpp",
]