# projeto_unidade1_boas_praticas
## o que é

Sistema para gerenciamento de atendimentos médicos. Incluí funcionalidades para: 

* cadastrar atendimento com informações do agendamento como paciente, médico, dia, horário e outros
* remarcar agendamento
* listar atendimentos do dia 

## estrutura

As pastas do projeto estão organizadas no diretório 'projeto_unidade1_boas_praticas' da seguinte forma:

* 'docs/build/markdown': documentação do projeto em markdown gerada pela ferramenta sphinx
* 'docs/source': pasta com demais arquivos gerados pela ferramenta sphinx para criar a documentação
* 'meu_projeto': arquivo com o código executável 'agenda_base.py'

## como executar

Verifique o Python instalado:

* python --version

Estando no diretório 'projeto_unidade1_boas_praticas' execute o arquivo 'agenda_base.py' com o comando:

* python ./meu_projeto/agenda_base.py

## como gerar a documentação

Verifique se os pacotes necessários estão instalados:

* pip install sphinx sphinx-markdown-builder

Para regerar a documentação do zero, remova a pasta 'docs' e 'meu_projeto/__pycache__'.

Para recriar do zero, crie 'docs' sem nada:

* mkdir docs

Entre na pasta docs:

* cd docs

Dentro da pasta docs, execute:

* sphinx-quickstart

O Shipnx vai pedir para configurar: nome do projeto, nome do autor, versão do projeto, a linguagem que está escrita a documentação (selecionar pt_BR), e se o projeto deve ser dividido nas pastas 'build' e 'source' (para reproduzir a estrutura do projeto selecione sim 'Y').

Configure o arquivo conf.py. Ele deve possuir as extensões:

    ```
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx_markdown_builder'
    ]
    ```

e deve possuir em seu topo:

    ```
    import os
    import sys
    sys.path.insert(0, os.path.abspath('/workspaces/projeto_unidade1_boas_praticas/meu_projeto'))
    ```

Observação: '/workspaces/projeto_unidade1_boas_praticas/meu_projeto' deve ser o caminho absoluto para a pasta 'meu_projeto', ele deve ser adaptado caso a execução não seja feita no codespace.

Em seguinda, retorne para a pasta principal:

* cd ..

Estando em 'projeto_unidade1_boas_praticas' gere os arquivos para documentaçao Sphinx executando:

* sphinx-apidoc -o ./docs/source/ -f ./meu_projeto

Em seguida, execute:

* sphinx-build -b markdown ./docs/source ./docs/build/markdown

Gerando a documentacao em markown em 'build/markdown'.

## autoria

Projeto de autoria do graduando Ian Silva Cruz de Medeiros do curso Bacharelado em Tecnologia da Informação pela UFRN (Natal/RN), como trabalho da Unidade 1 da disciplina de Boas Práticas de Programação (DIM0501) 



 o que é o sistema, como compilar e executar, como gerar a documentação e quem fez.
