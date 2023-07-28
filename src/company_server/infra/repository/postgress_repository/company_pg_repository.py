"""company repository"""

from typing import List, Optional
from peewee import DoesNotExist
from company_server.application.exceptions.create_company_error import (
    DuplicateCnpjError,
)

from company_server.domain.Repository.i_company_repository import ICompanyRepository
from company_server.domain.entities.Company import Company
from company_server.infra.repository.postgress_repository.model.company_model import (
    CompanyModel,
)


class CompanyPGRepository(ICompanyRepository):
    """company repository in memory"""

    def save(self, company_data: Company) -> str:
        """save company"""
        try:
            company_model = self._entity_to_model(company_data)
            _id = CompanyModel.create(
                id=company_model.id,
                cnpj=company_model.cnpj,
                company_name=company_model.company_name,
                trading_name=company_model.trading_name,
                cnae=company_model.cnae,
            )

            return _id
        except Exception as error:
            raise DuplicateCnpjError(error) from error

    def get_by_cnpj(self, cnpj: str) -> Optional[Company]:
        try:
            company_data = CompanyModel.get(CompanyModel.cnpj == cnpj)
            if company_data is None:
                return None
            return self._model_to_entity(company_data)
        except DoesNotExist:
            return None

    def get_all(self) -> List[Company]:
        company_models = CompanyModel.select()
        return [
            self._model_to_entity(company_model) for company_model in company_models
        ]

    def remove_company(self, company_id) -> None:
        """remove company by id"""
        CompanyModel.delete_by_id(company_id)

    def _entity_to_model(self, company_entity: Company) -> CompanyModel:
        return CompanyModel(
            id=company_entity.id,
            cnpj=company_entity.cnpj.cnpj,
            company_name=company_entity.company_name,
            trading_name=company_entity.trading_name,
            cnae=company_entity.cnae,
        )

    def _model_to_entity(self, company_model: CompanyModel) -> Company:
        return Company(
            id=company_model.id,
            cnpj=company_model.cnpj,
            company_name=company_model.company_name,
            trading_name=company_model.trading_name,
            cnae=company_model.cnae,
        )
