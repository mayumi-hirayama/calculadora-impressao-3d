from calculos import calcular_custo
import pytest

def test_custo():
    resultado = calcular_custo(50, 200, 2, 1, 30)
    assert resultado['custo_filam'] == 10.0
    assert resultado['custo_energia'] == 0.2
    assert resultado['lucro'] == pytest.approx(8.976)