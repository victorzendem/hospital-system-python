from model import paciente
from model.paciente import Paciente
from repository.paciente_repository import PacienteRepository

class PacienteService:

    def __init__(self,repository):
        self.repository = repository
        
        
    def cadastrar(self, nome, cpf, idade):
        
        paciente_existente = self.repository.buscar_por_cpf(cpf)
        
        if paciente_existente is not None:
            raise ValueError("já existe um paciente com esse cpf.")

        paciente = Paciente(None, nome, cpf, idade)
        self.repository.salvar(paciente)
        return paciente



    def buscar_por_id(self, id):
        paciente = self.repository.buscar_por_id(id)

        if paciente is None:
            raise ValueError("Paciente não encontrado.")

        return paciente



    def listar_todos(self):
        return self.repository.listar_todos()
    
    def buscar_por_cpf(self, cpf):
        
        paciente = self.repository.buscar_por_cpf(cpf)
        
        if paciente is None:
            raise ValueError("Paciente não encontrado.")

        return paciente
    
    
    