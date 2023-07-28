"""company repository"""

from typing import Dict, List, Optional
from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company


class CompanyInMemoryRepository(ICompanyRepository):
    """company repository in memory"""

    companies: Dict[str, Company]

    def __init__(self):
        self.companies = {}

    def save(self, company_data: Company):
        """save company data"""
        self.companies[company_data.cnpj.cnpj] = company_data

    def get_by_cnpj(self, cnpj: str) -> Optional[Company]:
        """get company by cnpj"""
        return self.companies.get(cnpj, None)

    def get_all(self) -> List[Company]:
        """get all company"""
        return list(self.companies.values())

    def paginate(
        self, start: int, limit: int, sort: str, direction: str, query: dict
    ) -> List[Company]:
        """get paginated and sorted list of companies"""
        company_paginated = list(self.companies.values())
        self.sort_companies(sort, company_paginated, direction)
        self.query_companies(query, company_paginated)

        start_index = start * limit
        end_index = start_index + limit
        return company_paginated[start_index:end_index]

    def sort_companies(
        self, sort: str, company_paginated: List[Company], direction: str
    ):
        """sort the list of companies based on the given sort fields and direction"""
        if not sort:
            return
        is_descending = direction == "desc"
        company_paginated.sort(
            key=lambda company: getattr(company, sort), reverse=is_descending
        )

    def query_companies(self, query: dict, company_paginated: List[Company]):
        """Query the companies"""
        for attribute, value in query.items():
            company_paginated[:] = [
                company
                for company in company_paginated
                if getattr(company, attribute) == value
            ]

    def remove_company(self, company_id: str) -> None:
        """remove company by id"""
        for cnpj, company in self.companies.items():
            if company.id == company_id:
                del self.companies[cnpj]
                break
