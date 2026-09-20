from exceptions.paciente_exception import PacienteInvalidoException, PacienteException
from repository.paciente_repository import PacienteRepository
from services.paciente_service import PacienteService

repository = PacienteRepository()
service = PacienteService(repository)


try:
    paciente123 = service.cadastrar("Celso", "1111111111", 20)

    print("Paciente cadastrado com suceso!")

except PacienteInvalidoException as erro:
    print("Erro de validação:", erro)

except PacienteException as erro:
    print("Erro do paciente:", erro)