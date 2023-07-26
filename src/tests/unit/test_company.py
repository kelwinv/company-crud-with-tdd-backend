"""Company test suite"""
import pytest
from company_server.domain.entities.CNPJ import CNPJ
from company_server.domain.entities.Company import Company
from company_server.domain.entities.UUIDGenerator import UUIDGenerate


def test_create_company():
    """Test creating a company with a valid CNPJ"""
    id = UUIDGenerate.generate()
    cnpj_str = "49430512000187"
    company_name = "Company Name"
    trading_name = "Trading Name"
    cnae = "123456"

    company = Company(id, cnpj_str, company_name, trading_name, cnae)

    assert isinstance(company.id, str)
    assert isinstance(company.cnpj, CNPJ)
    assert company.company_name == company_name
    assert company.trading_name == trading_name
    assert company.cnae == cnae


def test_create_company_without_id():
    """Test creating a company with a valid CNPJ"""
    cnpj_str = "49.430.512/0001-87"
    company_name = "Company Name"
    trading_name = "Trading Name"
    cnae = "123456"

    company = Company.create(cnpj_str, company_name, trading_name, cnae)

    assert isinstance(company.id, str)
    assert isinstance(company.cnpj, CNPJ)
    assert company.company_name == company_name
    assert company.trading_name == trading_name
    assert company.cnae == cnae


def test_create_company_invalid_cnpj():
    """Test creating a company with an invalid CNPJ"""
    cnpj = "1234567800019"  # Invalid CNPJ (less digits)
    company_name = "Company Name"
    trading_name = "Trading Name"
    cnae = "123456"

    with pytest.raises(ValueError):
        company = Company.create(cnpj, company_name, trading_name, cnae)


def test_create_company_missing_fields():
    """Test creating a company with missing required fields"""
    id = UUIDGenerate.generate()
    cnpj = "12345678000199"
    company_name = "Company Name"
    trading_name = ""
    cnae = ""

    with pytest.raises(ValueError):
        company = Company(id, cnpj, company_name, trading_name, cnae)
