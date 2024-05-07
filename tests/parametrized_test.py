import pytest

from src.hex_converter import hexadecimal_to_decimal  # noqa: F401

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


def test_converter():
    assert hexadecimal_to_decimal("1") == 1
    assert hexadecimal_to_decimal("2") == 2
