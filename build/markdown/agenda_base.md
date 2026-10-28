# agenda_base module

### *class* agenda_base.atendimento(paciente, medico, data, horario, duracao)

Base: `object`

Representa um atendimento médico agendado.

Armazena as informações referentes ao paciente, ao médico responsável,
à data, ao horário e à duração do atendimento.

#### paciente

Identificação ou nome do paciente atendido.

#### medico

Identificação ou nome do médico responsável.

#### data

Data do atendimento no formato AAAA-MM-DD.

#### horario

Horário de início do atendimento, expresso em horas.

#### duracao

Duração do atendimento em minutos.

### *class* agenda_base.gerenciador_de_atendimentos

Base: `object`

Gerencia os agendamentos de atendimentos médicos.

Mantém uma lista de atendimentos e disponibiliza operações para
adicionar, remarcar e consultar atendimentos por data. Verifica
conflitos de horário por médico, valida os horários e as durações
permitidos e verifica o formato das datas informadas.

#### lista_atendimentos

Lista de objetos da classe atendimento,
contendo os atendimentos registrados na agenda.

#### adicionar_atendimento(paciente, medico, data, horario, duracao)

Adiciona um atendimento à agenda.

Valida os argumentos informados, verifica se o horário está entre
as 8h00 e as 17h00 e se a duração está entre 15 e 120 minutos, em
intervalos de 15 minutos. Além disso verifica se o atendimento
termina dentro do horário de funcionamento (18h00) e se data está
no formato AAAA-MM-DD. Em seguida, tenta adicionar o atendimento à agenda.

* **Parâmetros:**
  * **paciente** – Identificação ou nome do paciente.
  * **medico** – Identificação ou nome do médico responsável.
  * **data** – Data do atendimento no formato AAAA-MM-DD.
  * **horario** – Horário de início do atendimento, expresso em horas.
  * **duracao** – Duração do atendimento em minutos.
* **Retorna:**
  None. Imprime uma mensagem informando se o atendimento foi adicionado ou se o horário está ocupado.
* **Levanta:**
  * **ValueError** – Se algum argumento obrigatório for None.
  * **ValueError** – Se o horário de início estiver fora do intervalo permitido para agendamentos.
  * **ValueError** – Se a duração não estiver entre os valores aceitos.
  * **ValueError** – Se o atendimento ultrapassar o horário limite de funcionamento.

#### lista(data)

Lista os atendimentos agendados para uma data específica.

Valida se data não é nulo e o formato, imprimindo os atendimentos
encontrados para essa data, incluindo horário, paciente e médico.

* **Parâmetros:**
  **data** – Data dos atendimentos a consultar, no formato AAAA-MM-DD.
* **Retorna:**
  None. Imprime no console os atendimentos encontrados.
  Cada atendimento é exibido com horário, paciente, médico
  e a indicação de que está marcado.
* **Levanta:**
  * **ValueError** – Se a data não for informada (None).
  * **ValueError** – Se a data estiver em formato inválido ou representar uma data inexistente.

#### remarca_atendimento(paciente, data, horario, nova_data, novo_horario)

Remarca um atendimento existente. Valida os argumentos,
verifica se os horários estão entre as 8h00 e as 17h00 e
se o novo horário de atendimento termina dentro do horário
de funcionamento (18h00). Além disso, valida se as datas
informadas estão no formato AAAA-MM-DD. Em seguida, tenta
transferir o atendimento para a nova data e horário.

* **Parâmetros:**
  * **paciente** – Identificação ou nome do paciente.
  * **data** – Data atual do atendimento no formato AAAA-MM-DD.
  * **horario** – Horário atual do atendimento, expresso em horas.
  * **nova_data** – Nova data do atendimento no formato AAAA-MM-DD.
  * **novo_horario** – Novo horário de início, expresso em horas.
* **Retorna:**
  None. Imprime uma mensagem informando se o atendimento foi
  remarcado ou se o novo horário está ocupado.
* **Levanta:**
  * **ValueError** – Se algum argumento obrigatório for None.
  * **ValueError** – Se o horário atual ou o novo horário estiver fora do intervalo permitido para agendamentos.
  * **ValueError** – Se a data atual ou a nova data estiver em formato inválido ou representar uma data inexistente.
  * **ValueError** – Se o atendimento, considerando sua duração original, ultrapassar o horário limite de funcionamento.
