"""use case for creating a company"""

from math import ceil
from typing import List, Tuple
from company_server.application.exceptions.paginate_company_errors import (
    InvalidQueryAttributeError,
    InvalidSortAttributeError,
)
from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company


class PaginateCompany:
    """use case for creating a company"""

    repository: ICompanyRepository

    def __init__(self, repository: ICompanyRepository):
        self.repository = repository

    def execute(
        self, start: int, limit: int, sort: str, direction: str, query: dict
    ) -> Tuple[List[Company], int, int]:
        """method to execute"""
        valid_attributes = ["company_name", "trading_name", "cnpj", "cnae"]

        if sort and sort not in valid_attributes:
            raise InvalidSortAttributeError(f"Invalid sort attribute: {sort}")

        # Check if query attributes are valid
        for attribute in query.keys():
            if attribute not in valid_attributes:
                raise InvalidQueryAttributeError(
                    f"Invalid query attribute: {attribute}"
                )

        if not direction:
            direction = "desc"
        elif direction not in ["asc", "desc"]:
            raise ValueError("Invalid direction. It must be 'asc' or 'desc'.")

        companies, total_items = self.repository.paginate(
            start, limit, sort, direction, query
        )
        total_pages = ceil(total_items / limit)

        return companies, total_items, total_pages
