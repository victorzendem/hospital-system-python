class PacienteException(Exception):
    pass

class PacienteInvalidoException(PacienteException):
    pass

class PacienteNaoEncontradoException(PacienteException):
    pass

class CpfDuplicadoException(PacienteException):
    pass
