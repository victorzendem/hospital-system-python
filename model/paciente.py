from exceptions.paciente_exception import PacienteInvalidoException


class Paciente:
    def __init__(self, id, nome, cpf, idade):

        self._validar_nome(nome)
        self._validar_cpf(cpf)
        self._validar_idade(idade)


        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def _validar_nome(self, nome):
        if not nome or not nome.strip():
            raise PacienteInvalidoException("O nome do paciente é obrigatório.")

    def _validar_cpf(self,cpf):

        if not isinstance(cpf, str):
            raise PacienteInvalidoException("O CPF deve ser um texto.")

        if len(cpf) != 11 or not cpf.isdigit():
            raise PacienteInvalidoException("O CPF deve conter exatamente 11 dígitos.")

        
    def _validar_idade(self, idade):

        if not isinstance(idade, int):
            raise PacienteInvalidoException("A idade precisa ser um número inteiro.")

        if idade < 0:
            raise PacienteInvalidoException("A idade não pode ser negativa.")
