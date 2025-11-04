# ✨ Sistema Refatorado (Clean Architecture)# Sistema Refatorado (Clean Architecture)# ✨ Sistema Refatorado (Clean Architecture)



Sistema de gerenciamento de usuários refatorado para Clean Architecture, resultado do processo híbrido (IA + curadoria humana).



## 📁 EstruturaSistema de gerenciamento de usuários refatorado para Clean Architecture, resultado do processo híbrido (IA + curadoria humana).Este repositório contém a versão refatorada do sistema legado originalmente desenvolvido em MVC, transformada para o padrão Clean Architecture com suporte de um modelo de linguagem (LLM) e técnicas de Inteligência Artificial.



```

clean-architecture-system/

├── domain/entities/user.py              # Entidade pura de domínio## 📁 Estrutura## 📖 Contexto

├── application/use_cases/               # 6 casos de uso especializados

│   ├── create_user.py

│   ├── update_user.py

│   ├── delete_user.py```O sistema foi gerado automaticamente a partir do repositório `mvc-legacy-system` utilizando o script de refatoração disponível em `auto-refactor-script`, com auxílio da API do GPT.

│   ├── get_user.py

│   ├── list_users.pyclean-architecture-system/

│   └── list_active_users.py

├── infrastructure/repositories/user_repository.py   # Persistência├── domain/entities/user.py              # Entidade pura de domínioEste sistema representa o resultado prático do estudo de caso sobre **automatização da refatoração mediada por IA**, demonstrando a viabilidade técnica da aplicação de modelos de linguagem de grande escala (LLMs) na modernização de sistemas legados.

├── interface/user_interface.py          # Apresentação

└── main.py                              # Ponto de entrada├── application/use_cases/               # 6 casos de uso especializados

```

│   ├── create_user.py### Objetivos da Transformação:

## 🚀 Execução

│   ├── update_user.py- ✅ Melhorar modularidade e testabilidade do código

```bash

pip install -r requirements.txt│   ├── delete_user.py- ✅ Isolar regras de negócio da infraestrutura

python main.py

```│   ├── get_user.py- ✅ Promover arquitetura independente de frameworks



## 🧪 Testes│   ├── list_users.py- ✅ Facilitar manutenção e evolução do código



```bash│   └── list_active_users.py- ✅ Reduzir custos e tempo de refatoração manual

python smoke_test.py

```├── infrastructure/repositories/user_repository.py   # Persistência- ✅ Minimizar erros humanos no processo de reestruturação



## 📊 Métricas├── interface/user_interface.py          # Apresentação



- 11 arquivos Python (+175%)└── main.py                              # Ponto de entrada## 📁 Estrutura do Projeto

- 241 linhas de código (-3.6%)

- 8 classes (+700%), 31 funções (+19%)```

- Complexidade ciclomática: 47 (+17.5%)

```

## 🎯 Melhorias vs MVC

## 🚀 Execuçãoclean-architecture-system/

✅ Separação de responsabilidades  

✅ Inversão de dependências  ├── domain/                    # Camada de Domínio

✅ Testabilidade isolada  

✅ Independência de frameworks  ```bash│   └── entities/

✅ Regras de negócio no domínio

pip install -r requirements.txt│       └── user.py           # Entidade User

Sistema original: `../mvc-legacy-system/`

python main.py├── application/              # Camada de Aplicação

```│   └── use_cases/

│       ├── create_user.py    # Caso de uso: Criar usuário

## 🧪 Testes│       └── list_users.py     # Caso de uso: Listar usuários

├── infrastructure/           # Camada de Infraestrutura

```bash│   └── repositories/

python smoke_test.py│       └── user_repository.py # Implementação do repositório

```├── interface/                # Camada de Interface

│   └── user_interface.py     # Interface com usuário

## 📊 Métricas├── main.py                   # Ponto de entrada da aplicação

└── README.md                 # Este arquivo

- 11 arquivos Python (+175%)```

- 241 linhas de código (-3.6%)

- 8 classes (+700%), 31 funções (+19%)## 🎯 Princípios da Clean Architecture

- Complexidade ciclomática: 47 (+17.5%)

1. **Independência de Frameworks**: A arquitetura não depende de bibliotecas específicas

## 🎯 Melhorias vs MVC2. **Testabilidade**: Regras de negócio podem ser testadas isoladamente

3. **Independência de UI**: A interface pode ser alterada sem modificar o core

✅ Separação de responsabilidades  4. **Independência de Banco de Dados**: Regras de negócio não conhecem o BD

✅ Inversão de dependências  5. **Separação de Responsabilidades**: Cada camada tem sua responsabilidade bem definida

✅ Testabilidade isolada  

✅ Independência de frameworks  ## 🔧 Requisitos

✅ Regras de negócio no domínio

- Python 3.10+

Sistema original: `../mvc-legacy-system/`- Dependências listadas em `requirements.txt`


## 🚀 Execução

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Rodar aplicação:**
```bash
python main.py
```

## 🧪 Testes

Para executar os testes unitários:
```bash
pytest
```

Para executar com cobertura:
```bash
pytest --cov=. --cov-report=html
```

## 📚 Camadas da Arquitetura

### Domain (Domínio)
Contém as entidades e regras de negócio fundamentais. Não depende de nenhuma outra camada.

### Application (Aplicação)
Contém os casos de uso que orquestram o fluxo de dados entre as camadas.

### Infrastructure (Infraestrutura)
Implementações concretas de repositórios, acesso a banco de dados, APIs externas, etc.

### Interface
Controladores, views, APIs REST, CLI - tudo que interage com o mundo externo.

## 🔄 Comparação com MVC

| Aspecto | MVC | Clean Architecture |
|---------|-----|-------------------|
| Separação | 3 camadas | 4+ camadas bem definidas |
| Testabilidade | Média | Alta (testes unitários isolados) |
| Acoplamento | Alto | Baixo (inversão de dependências) |
| Manutenção | Complexa | Facilitada (responsabilidades claras) |
| Escalabilidade | Limitada | Flexível e escalável |
| Independência | Framework-dependente | Framework-independente |
| Regras de Negócio | Misturadas | Isoladas no domínio |

### Avanços Significativos Alcançados
A comparação evidenciou melhorias substanciais na:
- **Separação das camadas**: Cada camada tem responsabilidades bem definidas
- **Flexibilidade de manutenção**: Mudanças localizadas sem impacto sistêmico
- **Independência tecnológica**: Possibilidade de trocar frameworks sem reescrever regras de negócio
- **Sustentabilidade**: Arquitetura mais sustentável para ambientes de maior complexidade

## 📖 Referências

Este sistema faz parte do Trabalho de Conclusão de Curso:

**"Automatização da Refatoração de Sistemas Estruturados em MVC para a Clean Architecture Mediada por Inteligência Artificial"**

O trabalho demonstra que a refatoração automatizada mediada por IA é um método promissor para a modernização de software, desde que integrada a processos consistentes de validação, curadoria e aprendizado contínuo. 
