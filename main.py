from model.paciente import Paciente
from repository.paciente_repository import PacienteRepository
from services.paciente_service import PacienteService


repository = PacienteRepository()
service = PacienteService(repository)



paciente = service.cadastrar(
    "Victor Zendem",
    "1234",
    20
)

paciente2 = service.cadastrar(
    "João",
    "12345",
    19
)


print("PACIENTES:")


for paciente3 in service.listar_todos():
    print(paciente3.nome)
    
    
paciente_buscar = service.buscar_por_cpf("1234")

print(paciente_buscar.nome)