"""Seed of companies """
import random
import uuid

import argparse
from faker import Faker
from company_server.domain.entities.CNPJ import CNPJ

from company_server.infra.db.model.company_model import CompanyModel

# Inicialize o objeto Faker
fake = Faker()

# Lista de códigos CNAE fictícios para preencher a tabela
cnae_list = ["123456", "654321", "789012", "098765"]


# Função para gerar um CNPJ válido
def generate_valid_cnpj():
    """generate valid cnpj"""

    def calculate_digit(cnpj, weights):
        total = sum(int(cnpj[i]) * weights[i] for i in range(len(weights)))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    cnpj_base = [random.randint(0, 9) for _ in range(12)]
    digit1 = calculate_digit(cnpj_base, weights=[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    digit2 = calculate_digit(
        cnpj_base + [digit1], weights=[6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    )

    cnpj_base.extend([digit1, digit2])
    return "".join(str(d) for d in cnpj_base)


# Função para criar registros de exemplo na tabela CompanyModel
def seed_companies(number_of_companies):
    """Generate a seed from company"""
    ids_created = []
    for _ in range(number_of_companies):
        cnpj = generate_valid_cnpj()
        company_name = fake.company()
        trading_name = fake.company_suffix()
        cnae = random.choice(cnae_list)
        CNPJ(cnpj)

        _id = CompanyModel.create(
            id=uuid.uuid4(),
            cnpj=cnpj,
            company_name=company_name,
            trading_name=trading_name,
            cnae=cnae,
        )
        ids_created.append(str(_id))

    print(f"Seed concluído com sucesso!, {number_of_companies} foram criadas.")
    print(f"ids gerados: {ids_created}.")


def start():
    """Start the interpreter with some arguments"""
    parser = argparse.ArgumentParser(description="Preenche dados no banco")
    parser.add_argument(
        "quantity",
        type=int,
        help="Especifique a quantidade de empresas que deseja adicionar",
    )

    args = parser.parse_args()
    seed_companies(args.quantity)


if __name__ == "__main__":
    seed_companies(25)
