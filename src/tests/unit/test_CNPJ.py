"""CNPJ test suite"""

import re
import pytest
from company_server.domain.entities.CNPJ import CNPJ


def test_valid_cnpj():
    """Testar um CNPJ válido."""
    cnpj_str = "49.430.512/0001-87"
    cnpj = CNPJ(cnpj_str)
    assert str(cnpj) == "49430512000187"


def test_valid_cnpj_with_number():
    """Testar um CNPJ válido com numero."""
    cnpj_str = "49430512000187"
    cnpj = CNPJ(cnpj_str)
    assert str(cnpj) == "49430512000187"


def test_invalid_cnpj_verification_digit():
    """Testar um CNPJ inválido (dígitos verificadores incorretos)."""
    cnpj_str = "49.430.512/0001-80"
    with pytest.raises(ValueError, match=re.escape("Invalid CNPJ")):
        CNPJ(cnpj_str)


def test_invalid_cnpj_same_digits():
    """Testar um CNPJ inválido (todos os dígitos são iguais)."""
    cnpj_str = "00.000.000/0000-00"
    with pytest.raises(
        ValueError, match=re.escape("Invalid CNPJ (all digits are the same).")
    ):
        CNPJ(cnpj_str)


def test_invalid_cnpj_length():
    """Testar um CNPJ inválido (comprimento inválido)."""
    cnpj_str = "12345678901234567890"
    with pytest.raises(ValueError, match=re.escape("Invalid CNPJ length.")):
        CNPJ(cnpj_str)
