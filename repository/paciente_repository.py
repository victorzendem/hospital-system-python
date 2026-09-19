class PacienteRepository:
    def __init__(self):
        self.pacientes = {}
        self.proximo_id = 1
        
    def salvar(self, paciente):
        paciente.id = self.proximo_id
        self.proximo_id += 1
        self.pacientes[paciente.id] = paciente

    def listar_todos(self):
        return list(self.pacientes.values())
    
    
    def buscar_por_id(self, id):
        return self.pacientes.get(id)


    def buscar_por_cpf(self, cpf):
        for paciente in self.pacientes.values():
            if paciente.cpf == cpf:
                return paciente
        return None

    def excluir(self, id):\
        self.pacientes.pop(id)
