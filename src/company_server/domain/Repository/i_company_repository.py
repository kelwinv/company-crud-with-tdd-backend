"""inteface from company_repository """

from abc import ABC, abstractmethod
from typing import List, Optional

from company_server.domain.entities.Company import Company


class ICompanyRepository(ABC):
    """internal class"""

    @abstractmethod
    def save(self, company_data: Company) -> str:
        """save a company"""

    @abstractmethod
    def get_by_cnpj(self, cnpj: str) -> Optional[Company]:
        """get a company"""

    @abstractmethod
    def get_all(self) -> List[Company]:
        """get all company"""

    @abstractmethod
    def remove_company(self, company_id: str) -> None:
        """remove a company"""
