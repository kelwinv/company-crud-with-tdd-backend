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

    def remove_company(self, company_id: str) -> None:
        """remove company by id"""
        for cnpj, company in self.companies.items():
            if company.id == company_id:
                del self.companies[cnpj]
                break
