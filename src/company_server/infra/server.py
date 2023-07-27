from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os dados das empresas em memória
empresas = []


# Endpoint para cadastrar uma nova empresa
@app.route("/empresas", methods=["POST"])
def cadastrar_empresa():
    data = request.json

    # Verificar campos obrigatórios
    if (
        "CNPJ" not in data
        or "NomeRazao" not in data
        or "NomeFantasia" not in data
        or "CNAE" not in data
    ):
        return jsonify({"error": "Campos obrigatórios não fornecidos"}), 400

    # Verificar se o CNPJ já está cadastrado
    cnpj = data["CNPJ"]
    if any(empresa["CNPJ"] == cnpj for empresa in empresas):
        return jsonify({"error": "CNPJ já cadastrado"}), 409

    empresas.append(data)
    return jsonify({"message": "Empresa cadastrada com sucesso"}), 201


# Endpoint para editar um cadastro de empresa existente
@app.route("/empresas/<string:cnpj>", methods=["PUT"])
def editar_empresa(cnpj):
    data = request.json

    # Verificar se a empresa com o CNPJ fornecido existe
    empresa = next((e for e in empresas if e["CNPJ"] == cnpj), None)
    if not empresa:
        return jsonify({"error": "Empresa não encontrada"}), 404

    # Permitir alterar apenas os campos NomeFantasia e CNAE
    if "NomeFantasia" in data:
        empresa["NomeFantasia"] = data["NomeFantasia"]
    if "CNAE" in data:
        empresa["CNAE"] = data["CNAE"]

    return jsonify({"message": "Empresa atualizada com sucesso"}), 200


# Endpoint para remover um cadastro de empresa existente com base no CNPJ
@app.route("/empresas/<string:cnpj>", methods=["DELETE"])
def remover_empresa(cnpj):
    global empresas
    empresas = [e for e in empresas if e["CNPJ"] != cnpj]
    return jsonify({"message": "Empresa removida com sucesso"}), 200


# Endpoint de listagem de empresas com suporte à paginação, ordenação e limite de registros por página
@app.route("/empresas", methods=["GET"])
def listar_empresas():
    # Obter parâmetros de paginação e ordenação
    start = int(request.args.get("start", 0))
    limit = int(request.args.get("limit", 10))
    sort = request.args.get("sort", "CNPJ")
    dir = request.args.get("dir", "asc")

    # Ordenar a lista de empresas com base no campo escolhido
    empresas_ordenadas = sorted(
        empresas, key=lambda x: x[sort], reverse=dir.lower() == "desc"
    )

    # Aplicar paginação
    empresas_paginadas = empresas_ordenadas[start : start + limit]

    return jsonify(empresas_paginadas), 200


if __name__ == "__main__":
    app.run(debug=True)
