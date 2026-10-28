# ========================================================================
# Para fácil manutenção em um único local, optou-se por implementar as
# regras de negócios relativas a horario e duracao em um único lugar
# por meio de constantes globais, ao invés de constantes locais nos
# métodos que fazem sua validação.
# ========================================================================

INICIO_HORARIO_DE_ATENDIMENTO = 8
FIM_HORARIO_DE_MARCAR_ATENDIMENTO = 17
FIM_HORARIO_DE_ATENDIMENTO = 18
MINUTOS_PARA_HORAS = 1/60

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

DURACAO_MINIMA = 15 
DURACAO_MAXIMA = 120
INTERVALO_DE_DURACAO = 15
DURACAO_ACEITA = [duracao for duracao in range(DURACAO_MINIMA,DURACAO_MAXIMA+1,INTERVALO_DE_DURACAO)]

class atendimento:
    """Representa um atendimento médico agendado.

    Armazena as informações referentes ao paciente, ao médico responsável,
    à data, ao horário e à duração do atendimento.

    Attributes:
        paciente: Identificação ou nome do paciente atendido.
        medico: Identificação ou nome do médico responsável.
        data: Data do atendimento no formato AAAA-MM-DD.
        horario: Horário de início do atendimento, expresso em horas.
        duracao: Duração do atendimento em minutos.
    """
    def __init__(self, paciente, medico, data, horario, duracao):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.horario = horario
        self.duracao = duracao

class gerenciador_de_atendimentos:
  """Gerencia os agendamentos de atendimentos médicos.

  Mantém uma lista de atendimentos e disponibiliza operações para
  adicionar, remarcar e consultar atendimentos por data. Verifica
  conflitos de horário por médico, valida os horários e as durações
  permitidos e verifica o formato das datas informadas.

  Attributes:
      lista_atendimentos: Lista de objetos da classe atendimento,
          contendo os atendimentos registrados na agenda.
  """
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
  
  def _validar_data(self, data):
    # ========================================================================
    # Para evitar uso de bibliotecas externas e manter a função simples,
    # a validação de datas verifica apenas se o formato é AAAA-MM-DD, 
    # se o mês está entre 1-12 e se o dia está entre 1-31.
    # Desse modo formatos incorretos são removidos, mas datas inexistentes
    # ainda são aceitas. 
    # Ex.: "2008-02-31" é aceito, mas fevereiro não tem dia 31.
    #
    # TODO: implementar regex e calendário
    # ========================================================================
    ano, mes, dia = data.split("-")

    if len(ano) == 4 and len(mes) == 2 and len(dia) == 2:
      try:
        ano = int(ano)
        mes = int(mes)
        dia = int(dia)

        if (1 <= mes <= 12) and (1 <= dia <= 31):
          return True
      except ValueError:
        return False
    
    return False

  def _adicionar_atendimento(self, paciente, medico, data, horario, duracao):

    if not self._conflito_horario(data=data, horario=horario, medico=medico):
      self.lista_atendimentos.append(atendimento(paciente, medico, data, horario, duracao))
      return True

    return False
  
  def adicionar_atendimento(self, paciente, medico, data, horario, duracao):
    """Adiciona um atendimento à agenda.

    Valida os argumentos informados, verifica se o horário está entre
    as 8h00 e as 17h00 e se a duração está entre 15 e 120 minutos, em
    intervalos de 15 minutos. Além disso verifica se o atendimento 
    termina dentro do horário de funcionamento (18h00) e se data está
    no formato AAAA-MM-DD. Em seguida, tenta adicionar o atendimento à agenda.

    Args:
        paciente: Identificação ou nome do paciente.
        medico: Identificação ou nome do médico responsável.
        data: Data do atendimento no formato AAAA-MM-DD.
        horario: Horário de início do atendimento, expresso em horas.
        duracao: Duração do atendimento em minutos.

    Returns:
        None. Imprime uma mensagem informando se o atendimento foi
        adicionado ou se o horário está ocupado.

    Raises:
        ValueError: Se algum argumento obrigatório for None.
        ValueError: Se o horário de início estiver fora do intervalo
            permitido para agendamentos.
        ValueError: Se a duração não estiver entre os valores aceitos.
        ValueError: Se o atendimento ultrapassar o horário limite
            de funcionamento.
    """
    argumentos = {
        "paciente":paciente,
        "medico":medico, 
        "data":data, 
        "horario":horario,         
        "duracao":duracao
        }

    for arg in argumentos:
      if argumentos[arg] is None:
        raise ValueError(f"Campo {arg} não pode ser nulo. Todos os campos (paciente, data, horario, nova_data, novo_horario) devem ser preenchidos.")

    if not (INICIO_HORARIO_DE_ATENDIMENTO <= horario <= FIM_HORARIO_DE_MARCAR_ATENDIMENTO):
      raise ValueError(f"O horário de atendimento é das {INICIO_HORARIO_DE_ATENDIMENTO} até antes das {FIM_HORARIO_DE_MARCAR_ATENDIMENTO}.")

    if not duracao in DURACAO_ACEITA:
      raise ValueError(f"A duração não pode ser {duracao}. As duração deve estar entre 15 e 120 minutos, em intervalos multiplos de 15 minutos.")

    if horario +  duracao * MINUTOS_PARA_HORAS > FIM_HORARIO_DE_ATENDIMENTO:
      raise ValueError(f"Não é possível marcar um atendimento às {horario} horas com {duracao} minutos de duração. Pois o último atendimento deve terminar antes das 18 horas.")

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
    """Remarca um atendimento existente. Valida os argumentos, 
    verifica se os horários estão entre as 8h00 e as 17h00 e 
    se o novo horário de atendimento termina dentro do horário 
    de funcionamento (18h00). Além disso, valida se as datas 
    informadas estão no formato AAAA-MM-DD. Em seguida, tenta
    transferir o atendimento para a nova data e horário.

    Args:
        paciente: Identificação ou nome do paciente.
        data: Data atual do atendimento no formato AAAA-MM-DD.
        horario: Horário atual do atendimento, expresso em horas.
        nova_data: Nova data do atendimento no formato AAAA-MM-DD.
        novo_horario: Novo horário de início, expresso em horas.

    Returns:
        None. Imprime uma mensagem informando se o atendimento foi
        remarcado ou se o novo horário está ocupado.

    Raises:
        ValueError: Se algum argumento obrigatório for None.
        ValueError: Se o horário atual ou o novo horário estiver fora
            do intervalo permitido para agendamentos.
        ValueError: Se a data atual ou a nova data estiver em formato
            inválido ou representar uma data inexistente.
        ValueError: Se o atendimento, considerando sua duração original,
            ultrapassar o horário limite de funcionamento.
    """
    argumentos = {
        "paciente":paciente, 
        "data":data, 
        "horario":horario, 
        "nova_data":nova_data, 
        "novo_horario":novo_horario
        }

    for arg in argumentos:
      if argumentos[arg] is None:
        raise ValueError(f"Campo {arg} não pode ser nulo. Todos os campos (paciente, data, horario, nova_data, novo_horario) devem ser preenchidos.")

    for hora in [horario, novo_horario]:
      if not (INICIO_HORARIO_DE_ATENDIMENTO <= hora < FIM_HORARIO_DE_MARCAR_ATENDIMENTO):
        raise ValueError(f"O horário {hora} é inválido. O horário de atendimento é das {INICIO_HORARIO_DE_ATENDIMENTO} até antes das {FIM_HORARIO_DE_MARCAR_ATENDIMENTO}.")

    _, atendimento = self._get_atendimento(paciente=paciente,data=data,horario=horario)
    if novo_horario +  atendimento.duracao * MINUTOS_PARA_HORAS > FIM_HORARIO_DE_ATENDIMENTO:
      raise ValueError(f"Não é possível marcar um atendimento às {novo_horario} horas com {atendimento.duracao} minutos de duração. Pois o último atendimento deve terminar antes das 18 horas.")
    
    for formato_data in [data, nova_data]:
      if not self._validar_data(formato_data):
        raise ValueError(f"A data {formato_data} não está em um formato válido. Data deve ser no formato AAAA-MM-DD")

    if self._remarca_atendimento(paciente, data, horario, nova_data, novo_horario):
      print("Remarcado")
    else:
      print("Horario ocupado")

  def lista(self,data):
    """Lista os atendimentos agendados para uma data específica.

    Valida se data não é nulo e o formato, imprimindo os atendimentos
    encontrados para essa data, incluindo horário, paciente e médico.

    Args:
        data: Data dos atendimentos a consultar, no formato AAAA-MM-DD.

    Returns:
        None. Imprime no console os atendimentos encontrados.
        Cada atendimento é exibido com horário, paciente, médico
        e a indicação de que está marcado.

    Raises:
        ValueError: Se a data não for informada (None).
        ValueError: Se a data estiver em formato inválido ou representar
            uma data inexistente.
    """
    argumentos = [data]

    if any(arg is None for arg in argumentos):
        raise ValueError("O campo (data) deve ser preenchido.")
    
    if not self._validar_data(data):
      raise ValueError(f"A data {data} não está em um formato válido. Data deve ser no formato AAAA-MM-DD")

    for atendimento in self.lista_atendimentos:
      if atendimento.data == data:
        print(f"{atendimento.horario} {atendimento.paciente} {atendimento.medico} MARCADO")


lista_atendimentos = gerenciador_de_atendimentos()
lista_atendimentos.adicionar_atendimento("Ana", "Dr. Silva", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], 30)
lista_atendimentos.adicionar_atendimento("Bruno", "Dr. Silva", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], 30)
lista_atendimentos.adicionar_atendimento("Carla", "Dra. Souza", "2026-10-05", HORARIOS["DUAS_DA_TARDE"], 60)
lista_atendimentos.remarca_atendimento("Ana", "2026-10-05", HORARIOS["NOVE_DA_MANHA"], "2026-10-06", HORARIOS["DEZ_DA_MANHA"])
lista_atendimentos.lista("2026-10-05")