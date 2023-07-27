from company_server.domain.entities.Company import Company


def start():
    cnpj = "12345678000199"
    company_name = "Company Name"
    trading_name = "Trading Name"
    cnae = "123456"

    company = Company(cnpj, company_name, trading_name, cnae)


if __name__ == "__main__":
    start()
