from psycopg2 import OperationalError
import pytest
from company_server.application.exceptions.paginate_company_errors import (
    InvalidQueryAttributeError,
    InvalidSortAttributeError,
)
from company_server.application.use_case.paginate_company import PaginateCompany

from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company
from company_server.domain.entities.UUIDGenerator import UUIDGenerate
from company_server.infra.repository.in_memory.company_memory_repository import (
    CompanyInMemoryRepository,
)

company_name = f"company_{UUIDGenerate.generate()}"


@pytest.fixture(name="setup")
def setup_paginate_company() -> ICompanyRepository:
    """test setup"""

    try:
        company_repo = CompanyInMemoryRepository()
        # company_repo = CompanyPGRepository()

        companies = [
            Company.create(
                "47858309000180", company_name, "Empresa Fantasia 2", "654321"
            ),
            Company.create(
                "45.030.406/0001-55", company_name, "Empresa Fantasia 1", "123456"
            ),
            Company.create(
                "95025985000116", company_name, "Empresa Fantasia 5", "987654"
            ),
            Company.create(
                "89740705000159", company_name, "Empresa Fantasia 3", "789012"
            ),
            Company.create(
                "37972367000187", company_name, "Empresa Fantasia 4", "543210"
            ),
        ]
        for company in companies:
            company_repo.save(company)
        yield company_repo

        for company in companies:
            company_repo.remove_company(company.id)
    except OperationalError as error:
        pytest.skip(f"Skipping test. Unable to connect to the database: {error}")


def test_paginate_company_with_sort_limit_query(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    limit = 2
    query = {"company_name": company_name}
    sort = "trading_name"
    direction = "asc"

    result = paginate_company.execute(0, limit, sort, direction, query)

    assert len(result) == 2
    assert result[0].trading_name == "Empresa Fantasia 1"
    assert result[1].trading_name == "Empresa Fantasia 2"

    result1 = paginate_company.execute(1, limit, sort, direction, query)
    assert len(result1) == 2
    assert result1[0].trading_name == "Empresa Fantasia 3"
    assert result1[1].trading_name == "Empresa Fantasia 4"

    result2 = paginate_company.execute(2, limit, sort, direction, query)
    assert len(result2) == 1
    assert result2[0].trading_name == "Empresa Fantasia 5"


def test_paginate_company_with_direction(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    limit = 5
    query = {"company_name": company_name}
    sort = "trading_name"

    desc_companies = paginate_company.execute(0, limit, sort, "desc", query)

    assert desc_companies[0].trading_name == "Empresa Fantasia 5"
    assert desc_companies[1].trading_name == "Empresa Fantasia 4"
    assert desc_companies[2].trading_name == "Empresa Fantasia 3"
    assert desc_companies[3].trading_name == "Empresa Fantasia 2"
    assert desc_companies[4].trading_name == "Empresa Fantasia 1"

    asc_companies = paginate_company.execute(0, limit, sort, "asc", query)

    assert asc_companies[0].trading_name == "Empresa Fantasia 1"
    assert asc_companies[1].trading_name == "Empresa Fantasia 2"
    assert asc_companies[2].trading_name == "Empresa Fantasia 3"
    assert asc_companies[3].trading_name == "Empresa Fantasia 4"
    assert asc_companies[4].trading_name == "Empresa Fantasia 5"


def test_paginate_company_with_query(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    limit = 5
    query = {"company_name": company_name, "cnae": "654321"}
    sort = "trading_name"

    result = paginate_company.execute(0, limit, sort, "asc", query)

    assert len(result) == 1

    assert result[0].cnae == "654321"


def test_paginate_company_with_invalid_query(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    query = {"any_query": "any_query"}

    with pytest.raises(InvalidQueryAttributeError) as exc_info:
        paginate_company.execute(0, 5, "trading_name", "asc", query)

    assert str(exc_info.value) == "Invalid query attribute: any_query"


def test_paginate_company_with_invalid_sort(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    sort = "any_sort"

    with pytest.raises(InvalidSortAttributeError) as exc_info:
        paginate_company.execute(0, 5, sort, "asc", {})

    assert str(exc_info.value) == "Invalid sort attribute: any_sort"


def test_paginate_company_without_parameters(setup):
    """Test paginate company"""
    company_repo = setup
    paginate_company = PaginateCompany(company_repo)

    query = {}
    sort = ""

    result = paginate_company.execute(0, 1, sort, "asc", query)
    assert len(result) > 0
