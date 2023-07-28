from flask import Blueprint, request, jsonify
from company_server.application.exceptions.create_company_error import (
    DuplicateCnpjError,
)
from company_server.application.exceptions.paginate_company_errors import (
    InvalidQueryAttributeError,
    InvalidSortAttributeError,
)
from company_server.application.use_case.create_company import CreateCompany
from company_server.application.use_case.paginate_company import PaginateCompany
from company_server.infra.repository.postgress_repository.company_pg_repository import (
    CompanyPGRepository,
)

company_blueprint = Blueprint("company", __name__)

company_repo = CompanyPGRepository()


@company_blueprint.route("/company", methods=["POST"])
def create_company():
    """Route /company POST Create a new company"""
    data = request.json

    # Verificar campos obrigatórios
    if (
        "cnpj" not in data
        or "company_name" not in data
        or "trading_name" not in data
        or "cnae" not in data
    ):
        return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

    try:
        CreateCompany(company_repo).execute(
            data["cnpj"],
            data["company_name"],
            data["trading_name"],
            data["cnae"],
        )
        return jsonify({"message": "Empresa cadastrada com sucesso"}), 201
    except DuplicateCnpjError:
        return jsonify({"error": "duplicate cnpj", "status": 400}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@company_blueprint.route("/companies", methods=["GET"])
def get_all_companies():
    """Route /company GET paginate companies"""

    start = int(request.args.get("start", 0))
    limit = int(request.args.get("limit", 10))

    sort = request.args.get("sort", "")
    direction = request.args.get("dir", "asc")

    query = {}
    for key, value in request.args.items():
        if key in ["company_name", "trading_name", "cnpj", "cnae"]:
            query[key] = value

    try:
        paginate_company = PaginateCompany(company_repo)
        companies, total_items, total_pages = paginate_company.execute(
            start, limit, sort, direction, query
        )
        print(companies[0].__dict__)

        # Formato de retorno da resposta
        response = {
            "companies": [company.to_json() for company in companies],
            "total_items": total_items,
            "total_pages": total_pages,
        }

        return jsonify(response), 200
    except (InvalidSortAttributeError, InvalidQueryAttributeError) as error:
        return jsonify({"error": str(error)}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 500
