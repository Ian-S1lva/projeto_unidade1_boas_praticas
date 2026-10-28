INICIO_HORARIO_DE_ATENDIMENTO = 8
FIM_HORARIO_DE_ATENDIMENTO = 18

DURACAO_MINIMA = 0

HORARIOS = {
    "OITO_DA_MANHA" : 8,
    "NOVE_DA_MANHA" : 9,
    "DEZ_DA_MANHA" : 10,
    "ONZE_DA_MANHA" : 11,
    "MEIO_DIA" : 12,
    "UMA_DA_TARDE" : 13,
    "DUAS_DA_TARDE" : 14,
    "TRES_DA_TARDE" : 15,
    "QUATRO_DA_TARDE" : 16,
    "CINCO_DA_TARDE" : 17,
    "SEIS_DA_NOITE" : 18
}

TEMPO_DE_ATENDIMENTO = {
    "MEIA_HORA" : 30,
    "UMA_HORA" : 60,
    "DUAS_HORAS" : 120,
    "TRES_HORAS" : 180,
}

class atendimento:
    def __init__(self, paciente, medico, data, horario, duracao):

        for arg in [paciente, medico, data, horario, duracao]:
          if arg is None:
            raise ValueError(f"{arg} não admite valor Nulo.")

        if not (INICIO_HORARIO_DE_ATENDIMENTO <= horario < FIM_HORARIO_DE_ATENDIMENTO):
            raise ValueError("O horário de atendimento é das 8 até antes das 18.")

        if not duracao > DURACAO_MINIMA:
            raise ValueError("Duração de atendimento não pode ser 0.")

        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.horario = horario
        self.duracao = duracao

class gerenciador_de_atendimentos:
  def __init__(self):
    self.lista_atendimentos = []

  def _get_atendimento(self, data, horario, paciente=None, medico=None):
    if (paciente is None) and (medico is None):
      raise ValueError("É necessário especificar um paciente ou um médico.")

    for idx, atendimento in enumerate(self.lista_atendimentos):
      if (atendimento.paciente == paciente or atendimento.medico == medico) and atendimento.data == data and atendimento.horario == horario:
        return idx, atendimento

    return None

  def _conflito_horario(self, data, horario, medico):
    return self._get_atendimento(data=data, horario=horario, medico=medico) is not None

  def _adicionar_atendimento(self, paciente, medico, data, horario, duracao):

    if not self._conflito_horario(data=data, horario=horario, medico=medico):
      self.lista_atendimentos.append(atendimento(paciente, medico, data, horario, duracao))
      return True

    return False

  def adicionar_atendimento(self, paciente, medico, data, horario, duracao):
    if self._adicionar_atendimento(paciente, medico, data, horario, duracao):
      print(f"Atendimento adicionado para {paciente}")
    else:
      print("Horario ocupado")

  def _remarca_atendimento(self, paciente, data, horario, nova_data, novo_horario):
    idx, atendimento = self._get_atendimento(data=data,horario=horario,paciente=paciente)
    if not self._conflito_horario(data=nova_data, horario=novo_horario, medico=atendimento.medico):
      self.lista_atendimentos[idx].data = nova_data
      self.lista_atendimentos[idx].horario = novo_horario
      return True

    return False

  def remarca_atendimento(self, paciente, data, horario, nova_data, novo_horario):
    if self._remarca_atendimento(paciente, data, horario, nova_data, novo_horario):
      print("Remarcado")
    else:
      print("Horario ocupado")

  def lista(self,data):
    for atendimento in self.lista_atendimentos:
      if atendimento.data == data:
        print(f"{atendimento.horario} {atendimento.paciente} {atendimento.medico} MARCADO")


lista_atendimentos = gerenciador_de_atendimentos()
lista_atendimentos.adicionar_atendimento("Ana", "Dr. Silva", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], TEMPO_DE_ATENDIMENTO["MEIA_HORA"])
lista_atendimentos.adicionar_atendimento("Bruno", "Dr. Silva", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], TEMPO_DE_ATENDIMENTO["MEIA_HORA"])
lista_atendimentos.adicionar_atendimento("Carla", "Dra. Souza", "2026-10-05", HORARIOS["DUAS_DA_TARDE"], TEMPO_DE_ATENDIMENTO["UMA_HORA"])
lista_atendimentos.remarca_atendimento("Ana", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], "2026-10-06", HORARIOS["DEZ_DA_MANHA"])
lista_atendimentos.lista("2026-10-05")