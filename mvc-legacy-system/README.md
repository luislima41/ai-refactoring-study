# 🧩 Sistema Legado (MVC)# Sistema Legado (MVC)# 🧩 Sistema Legado (MVC)



Sistema de gerenciamento de usuários implementado em MVC, usado como entrada para o processo de refatoração automatizada.



## 📁 EstruturaSistema de gerenciamento de usuários implementado em MVC, usado como entrada para o processo de refatoração automatizada.Este repositório contém o sistema original desenvolvido sob o padrão Model-View-Controller (MVC), utilizado como base para o processo de refatoração automatizada apresentado no Trabalho de Conclusão de Curso "Automatização da Refatoração de Sistemas Estruturados em MVC para a Clean Architecture Mediada por Inteligência Artificial".



```

mvc-legacy-system/

├── models/user_model.py         # Modelo de dados## 📁 Estrutura## 📖 Descrição

├── views/user_view.py           # Interface de apresentação

├── controllers/user_controller.py   # Lógica de controle

└── main.py                      # Ponto de entrada

``````Sistema de gerenciamento de usuários implementado seguindo o padrão arquitetural MVC (Model-View-Controller), uma das abordagens mais tradicionais para desenvolvimento de aplicações web.



## 🚀 Execuçãomvc-legacy-system/



```bash├── models/user_model.py         # Modelo de dados## 📁 Estrutura do Projeto

pip install -r requirements.txt

python main.py├── views/user_view.py           # Interface de apresentação

```

├── controllers/user_controller.py   # Lógica de controle```

## 📊 Métricas

└── main.py                      # Ponto de entradamvc-legacy-system/

- 4 arquivos Python

- 250 linhas de código```├── models/                   # Camada Model

- 1 classe, 26 funções

- Complexidade ciclomática: 40│   └── user_model.py        # Modelo de dados do usuário



## 🔄 Refatoração## 🚀 Execução├── views/                    # Camada View



Este sistema serve como entrada para `../auto-refactor-script/`.│   └── user_view.py         # Interface de apresentação



Resultado refatorado: `../clean-architecture-system/````bash├── controllers/              # Camada Controller


pip install -r requirements.txt│   └── user_controller.py   # Lógica de controle

python main.py├── main.py                   # Ponto de entrada

```└── README.md                 # Este arquivo

```

## 📊 Métricas

## 🎯 Padrão MVC

- 4 arquivos Python

- 250 linhas de código### Model (Modelo)

- 1 classe, 26 funçõesResponsável pela lógica de dados e regras de negócio. Gerencia o acesso e manipulação dos dados.

- Complexidade ciclomática: 40

### View (Visão)

## 🔄 RefatoraçãoResponsável pela apresentação dos dados ao usuário. Não contém lógica de negócio.



Este sistema serve como entrada para `../auto-refactor-script/`.### Controller (Controlador)

Intermediário entre Model e View. Processa requisições do usuário e coordena as respostas.

Resultado refatorado: `../clean-architecture-system/`

## 🔧 Requisitos

- Python 3.10+
- Flask (para execução da aplicação web)
- Git instalado para versionamento

## 🚀 Execução

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Execute a aplicação:**
```bash
python main.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📊 Funcionalidades

- ✅ Criar novos usuários
- ✅ Listar usuários cadastrados
- ✅ Visualizar detalhes de usuários
- ✅ Interface simples e direta

## ⚠️ Limitações da Arquitetura MVC

Este sistema apresenta algumas características típicas de sistemas MVC que podem dificultar manutenção:

- **Alto acoplamento** entre camadas
- **Dificuldade de testes** unitários isolados
- **Mistura de responsabilidades** em alguns componentes
- **Dependência direta** de frameworks
- **Escalabilidade limitada** para sistemas complexos

## 🔄 Processo de Refatoração Automatizada

Este sistema serve como entrada (input) para o processo de refatoração automática mediada por IA. O fluxo de transformação inclui:

### Etapas do Processo:
1. **Extração**: Análise da estrutura MVC existente
2. **Identificação**: Mapeamento de entidades, casos de uso e dependências
3. **Transformação**: Geração automática de código pela API do GPT
4. **Reorganização**: Estruturação em camadas da Clean Architecture
5. **Validação**: Verificação da integridade funcional do sistema

### Tecnologias Utilizadas:
- Script automatizador em Python
- API do GPT (OpenAI) como agente de transformação
- Prompts detalhados para guiar a refatoração
- Validação humana para garantir qualidade

O resultado da refatoração está disponível em: `../clean-architecture-system/`

## 📖 Referências

Este sistema faz parte do Trabalho de Conclusão de Curso:

**"Automatização da Refatoração de Sistemas Estruturados em MVC para a Clean Architecture Mediada por Inteligência Artificial"**

O trabalho apresenta um estudo de caso sobre a aplicação prática de modelos de linguagem de grande escala (LLMs) na modernização de sistemas legados, buscando reduzir custos, tempo de execução e a incidência de erros humanos durante o processo de reestruturação de código.
