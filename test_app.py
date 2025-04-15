import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """
    Test 2 (na maksymalną ocenę 5): Sprawdza, czy długość listy predykcji jest większa od 0 i czy odpowiada liczbie próbek testowych.
    """
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Lista predykcji powinna zawierać co najmniej jeden element."
    assert len(preds) == len(y_test), f"Długość predykcji ({len(preds)}) nie zgadza się z liczbą próbek testowych ({len(y_test)})."

def test_predictions_value_range():
    """
    Test 3 (na maksymalną ocenę 5): Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie: Dla zbioru Iris mamy 3 klasy (0, 1, 2).
    """
    preds, _ = train_and_predict()
    assert all(pred in [0, 1, 2] for pred in preds), f"Predykcje powinny być w zakresie 0-2, ale znaleziono: {set(preds)}"

def test_model_accuracy():
    """
    Test 4 (na maksymalną ocenę 5): Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    accuracy = get_accuracy()
    assert accuracy >= 0.7, f"Dokładność modelu powinna wynosić co najmniej 70%, ale wynosi {accuracy:.2f}"
