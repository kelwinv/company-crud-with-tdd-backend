"""CNPJ entity"""


class CNPJ:
    def __init__(self, cnpj: str):
        self.cnpj = self._format_cnpj(cnpj)
        self._validate()

    def _format_cnpj(self, cnpj: str) -> str:
        return "".join(filter(str.isdigit, cnpj))

    def _validate(self):
        if not self.cnpj:
            raise ValueError("CNPJ is empty.")

        if len(self.cnpj) != 14:
            raise ValueError("Invalid CNPJ length.")

        if self.cnpj == self.cnpj[0] * 14:
            raise ValueError("Invalid CNPJ (all digits are the same).")

        self._has_valid_verification_digits()

    def _has_valid_verification_digits(self):
        def calculate_verification_digit(peso, len_digits):
            soma = 0
            for i in range(len_digits):
                soma += int(self.cnpj[i]) * peso
                peso -= 1
                if peso == 1:
                    peso = 9
            digito = soma % 11
            return 0 if digito < 2 else 11 - digito

        if int(self.cnpj[12]) != calculate_verification_digit(5, 12):
            raise ValueError("Invalid CNPJ (invalid first verification digit).")
        # Cálculo do segundo dígito verificador

        if int(self.cnpj[13]) != calculate_verification_digit(6, 13):
            raise ValueError("Invalid CNPJ (invalid second verification digit).")

    def __str__(self) -> str:
        return self.cnpj

    def __repr__(self) -> str:
        return f"CNPJ('{self.cnpj}')"


if __name__ == "__main__":
    cnpj_str = "49.430.512/0001-87"
    CNPJ(cnpj_str)
