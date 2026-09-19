class PacienteRepository:
    def __init__(self):
        self.pacientes = []
        self.proximo_id = 1
        
    def salvar(self, paciente):
        paciente.id = self.proximo_id
        self.proximo_id += 1
        self.pacientes.append(paciente)

    def listar_todos(self):
        return self.pacientes
    
    
    def buscar_por_id(self, id):
        for paciente in self.pacientes:
            if paciente.id == id:
                return paciente
            return None

    def buscar_por_cpf(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def excluir(self, id):
        for paciente in self.pacientes:
            if paciente.id == id:
                self.pacientes.remove(paciente)
        return