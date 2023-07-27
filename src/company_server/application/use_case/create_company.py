"""use case for creating a company"""

from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company


class CreateCompany:
    """use case for creating a company"""

    repository: ICompanyRepository

    def __init__(self, repository: ICompanyRepository):
        self.repository = repository

    def execute(
        self, cnpj: str, company_name: str, trading_name: str, cnae: str
    ) -> str:
        """method to execute"""

        # Verificar se a empresa já existe no repositório
        if self.repository.get_by_cnpj(cnpj):
            raise ValueError("Company with the same CNPJ already exists.")

        # Criar uma nova instância da empresa
        company = Company.create(cnpj, company_name, trading_name, cnae)

        # Salvar a empresa no repositório
        self.repository.save(company)

        return company.id
