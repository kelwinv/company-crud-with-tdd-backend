"""company repository"""

from typing import Dict, List, Optional
from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company


class CompanyInMemoryRepository(ICompanyRepository):
    """company repository in memory"""

    companies: Dict[str, Company]

    def __init__(self):
        self.companies = {}

    def save(self, companyData: Company):
        self.companies[companyData.cnpj.cnpj] = companyData

    def get_by_cnpj(self, cnpj: str) -> Optional[Company]:
        return self.companies.get(cnpj, None)

    def get_all(self) -> List[Company]:
        return list(self.companies.values())
