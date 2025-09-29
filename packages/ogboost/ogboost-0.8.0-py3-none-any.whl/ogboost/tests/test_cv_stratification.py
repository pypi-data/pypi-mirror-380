import numpy as np
import warnings
import pytest
from ogboost import GradientBoostingOrdinal
from sklearn.model_selection import StratifiedKFold, KFold


class TestCVStratification:
    """Test stratification functionality in CV early stopping."""
    
    @pytest.fixture
    def balanced_data(self):
        """Create balanced synthetic data where stratification should work."""
        np.random.seed(42)
        n_samples = 100
        n_features = 5
        n_classes = 4
        
        X = np.random.randn(n_samples, n_features)
        # Create balanced classes with 25 samples each
        y = np.repeat(np.arange(n_classes), n_samples // n_classes)
        
        return X, y
    
    @pytest.fixture 
    def imbalanced_data(self):
        """Create imbalanced data where stratification should fail for some splits."""
        np.random.seed(42)
        n_samples = 50
        n_features = 5
        
        X = np.random.randn(n_samples, n_features)
        # Create imbalanced classes: [30, 10, 5, 5] samples
        y = np.concatenate([
            np.full(30, 0),
            np.full(10, 1), 
            np.full(5, 2),
            np.full(5, 3)
        ])
        
        return X, y
    
    def test_balanced_data_uses_stratified_kfold(self, balanced_data):
        """Test that balanced data uses StratifiedKFold when validation_stratify=True."""
        X, y = balanced_data
        
        model = GradientBoostingOrdinal(
            n_estimators=5,
            cv_early_stopping_splits=5,
            validation_stratify=True,
            random_state=42
        )
        
        # This should not raise any warnings and should complete successfully
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            model.fit(X, y)
        
        # Verify model was trained successfully
        assert hasattr(model, '_cv_path')
        assert len(model._cv_path['cv_loss']) > 0
        
    def test_imbalanced_data_falls_back_with_warning(self, imbalanced_data):
        """Test that imbalanced data falls back to KFold with RuntimeWarning."""
        X, y = imbalanced_data
        
        model = GradientBoostingOrdinal(
            n_estimators=5,
            cv_early_stopping_splits=6,  # More splits than samples in smallest classes
            validation_stratify=True,
            random_state=42
        )
        
        # Should emit a RuntimeWarning about falling back to unstratified KFold
        with pytest.warns(RuntimeWarning, match="validation_stratify=True but at least one class has fewer than"):
            model.fit(X, y)
        
        # Verify model was still trained successfully
        assert hasattr(model, '_cv_path')
        assert len(model._cv_path['cv_loss']) > 0
        
    def test_validation_stratify_false_always_uses_kfold(self, balanced_data):
        """Test that validation_stratify=False always uses KFold."""
        X, y = balanced_data
        
        model = GradientBoostingOrdinal(
            n_estimators=5,
            cv_early_stopping_splits=5,
            validation_stratify=False,
            random_state=42
        )
        
        # This should not raise any warnings
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            model.fit(X, y)
        
        # Verify model was trained successfully
        assert hasattr(model, '_cv_path')
        assert len(model._cv_path['cv_loss']) > 0
        
    def test_no_cv_early_stopping_ignores_stratify(self, balanced_data):
        """Test that when cv_early_stopping_splits is None, validation_stratify only affects holdout."""
        X, y = balanced_data
        
        model = GradientBoostingOrdinal(
            n_estimators=5,
            cv_early_stopping_splits=None,
            n_iter_no_change=3,
            validation_stratify=True,
            random_state=42
        )
        
        # This should use the regular holdout method, not CV
        model.fit(X, y)
        
        # Verify it used holdout method (has _path but not _cv_path)
        assert hasattr(model, '_path')
        assert not hasattr(model, '_cv_path')
        
    def test_edge_case_exactly_enough_samples(self):
        """Test edge case where minimum class count exactly equals n_splits."""
        np.random.seed(42)
        X = np.random.randn(20, 3)
        # Create classes with exactly 5 samples each (4 classes)
        y = np.repeat(np.arange(4), 5)
        
        model = GradientBoostingOrdinal(
            n_estimators=3,
            cv_early_stopping_splits=5,  # Exactly equal to min class count
            validation_stratify=True,
            random_state=42
        )
        
        # Should work without warnings since min_count >= n_splits
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            model.fit(X, y)
        
        assert hasattr(model, '_cv_path')
        
    def test_edge_case_single_sample_classes(self):
        """Test edge case with very small classes."""
        np.random.seed(42)
        X = np.random.randn(10, 3)
        # Create classes with [5, 3, 1, 1] samples
        y = np.concatenate([
            np.full(5, 0),
            np.full(3, 1),
            np.full(1, 2),
            np.full(1, 3)
        ])
        
        model = GradientBoostingOrdinal(
            n_estimators=3,
            cv_early_stopping_splits=3,
            validation_stratify=True,
            random_state=42
        )
        
        # Should fall back with warning since some classes have < 3 samples
        with pytest.warns(RuntimeWarning, match="validation_stratify=True but at least one class has fewer than"):
            model.fit(X, y)
        
        assert hasattr(model, '_cv_path')