"""company model"""

from peewee import CharField, UUIDField

from company_server.infra.repository.postgress_repository.base_pg_repository import (
    BasePGModel,
)


class CompanyModel(BasePGModel):
    """company model"""

    id = UUIDField(primary_key=True, unique=True)
    cnpj = CharField(max_length=14, unique=True)
    company_name = CharField(max_length=255)
    trading_name = CharField(max_length=255)
    cnae = CharField(max_length=10)

    class Meta:
        table_name = "company"


CompanyModel.create_table()
