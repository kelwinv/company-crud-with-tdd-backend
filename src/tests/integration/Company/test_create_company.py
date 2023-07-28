"""test create company"""
from typing import List
from psycopg2 import OperationalError
import pytest

from company_server.application.use_case.create_company import CreateCompany
from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company
from company_server.domain.entities.CNPJ import CNPJ

from company_server.infra.repository.in_memory.company_memory_repository import (
    CompanyInMemoryRepository,
)

# from company_server.infra.repository.postgress_repository.company_pg_repository import (
#     CompanyPGRepository,
# )

_test_company_ids: List[str] = []


@pytest.fixture(name="setup")
def setup_create_company() -> ICompanyRepository:
    """test setup"""

    try:
        company_repo = CompanyInMemoryRepository()
        # company_repo = CompanyPGRepository()
        return company_repo
    except OperationalError as error:
        pytest.skip(f"Skipping test. Unable to connect to the database: {error}")


def test_create_company(setup):
    """Testar um CNPJ válido."""
    company_repo = setup
    create_company = CreateCompany(company_repo)

    cnpj = "49430512000187"
    company_name = "Empresa Razão Social"
    trading_name = "Empresa Fantasia"
    cnae = "123456"

    company_id = create_company.execute(cnpj, company_name, trading_name, cnae)
    _test_company_ids.append(company_id)
    print(company_id)

    assert isinstance(company_id, str)

    saved_company = company_repo.get_by_cnpj(cnpj)
    assert saved_company is not None
    print(saved_company.id)

    assert str(saved_company.id) == company_id


def test_duplicate_cnpj(setup):
    """test duplicate cnpj"""
    company_repo = setup
    create_company = CreateCompany(company_repo)
    cnpj = "49430512000187"
    company_name = "Empresa Razão Social"
    trading_name = "Empresa Fantasia"
    cnae = "123456"

    company_id = create_company.execute(cnpj, company_name, trading_name, cnae)
    _test_company_ids.append(company_id)

    with pytest.raises(ValueError):
        create_company.execute(cnpj, "Outra Razão Social", "Outra Fantasia", "654321")


def test_create_another_company(setup):
    """test create 2 company"""
    company_repo = setup
    create_company = CreateCompany(company_repo)

    company_name = "Empresa Razão Social"
    trading_name = "Empresa Fantasia"
    cnae = "123456"

    # Executar o caso de uso com um CNPJ diferente deve ser bem-sucedido
    cnpj = "49430512000187"
    company_id = create_company.execute(cnpj, company_name, trading_name, cnae)
    cnpj2 = "01517766000100"
    company_id2 = create_company.execute(cnpj2, company_name, trading_name, cnae)
    _test_company_ids.extend([company_id, company_id2])

    # test company 1
    saved_company: Company = company_repo.get_by_cnpj(cnpj)
    assert saved_company is not None
    assert str(saved_company.id) == company_id
    assert isinstance(saved_company.cnpj, CNPJ)
    assert saved_company.cnpj.cnpj == cnpj
    assert saved_company.company_name == company_name
    assert saved_company.trading_name == trading_name
    assert saved_company.cnae == cnae

    # test company 2
    saved_company2: Company = company_repo.get_by_cnpj(cnpj2)
    assert saved_company2 is not None
    assert str(saved_company2.id) == company_id2
    assert isinstance(saved_company2.cnpj, CNPJ)
    assert saved_company2.cnpj.cnpj == cnpj2
    assert saved_company2.company_name == company_name
    assert saved_company2.trading_name == trading_name
    assert saved_company2.cnae == cnae


@pytest.fixture(autouse=True)
def cleanup_created_companies(request, setup):
    """Clean up the created companies after each test"""
    yield

    for company_id in _test_company_ids:
        setup.remove_company(company_id)

    # Clear the global list of company IDs
    _test_company_ids.clear()
