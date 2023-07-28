"""company repository"""

from typing import Dict, List, Optional, Tuple
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
        self,
        start: int,
        page_limit: int,
        page_sort: str,
        page_dir: str,
        page_query: dict,
    ) -> Tuple[List[Company], int]:
        """get paginated and sorted list of companies"""
        company_paginated = list(self.companies.values())
        self.sort_companies(page_sort, company_paginated, page_dir)
        self.query_companies(page_query, company_paginated)

        start_index = start * page_limit
        end_index = start_index + page_limit
        return company_paginated[start_index:end_index], len(company_paginated)

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
