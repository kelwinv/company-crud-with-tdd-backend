import uuid

from company_server.domain.entities.CNPJ import CNPJ
from company_server.domain.entities.UUIDGenerator import UUIDGenerate


class Company:
    """Company"""

    def __init__(self, id, cnpj, company_name, trading_name, cnae):
        self.id = id
        self.cnpj = CNPJ(cnpj)
        self.company_name = company_name
        self.trading_name = trading_name
        self.cnae = cnae

        # self._validate_input()

    @classmethod
    def create(
        cls, cnpj: str, company_name: str, trading_name: str, cnae: str
    ) -> "Company":
        """create a new Company"""
        _id = UUIDGenerate.generate()

        return cls(_id, cnpj, company_name, trading_name, cnae)

    def _validate_input(self):
        required_fields = ["id", "cnpj", "company_name", "trading_name", "cnae"]
        for field in required_fields:
            if not getattr(self, field):
                raise ValueError(f"Field '{field}' is required.")
