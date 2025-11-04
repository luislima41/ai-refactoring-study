# AI-Assisted Refactoring Study

Este repositório contém um estudo de caso sobre refatoração de sistemas MVC para Clean Architecture assistida por inteligência artificial.

## 📋 Visão Geral

O projeto demonstra uma abordagem híbrida (automação via GPT-4 + curadoria humana) para refatoração arquitetural, incluindo:

- **Scripts de automação** para refatoração via API do GPT-4
- **Sistema MVC legado** como baseline de entrada
- **Sistema Clean Architecture** como resultado da refatoração
- **Ferramentas de análise** para métricas comparativas

## 📁 Estrutura do Repositório

```
.
├── auto-refactor-script/       # Scripts de automação e análise
│   ├── main.py                 # Refatoração automatizada via GPT-4
│   ├── analise_comparativa.py  # Analisador de métricas com AST
│   └── requirements.txt        # Dependências Python
│
├── mvc-legacy-system/          # Sistema original (entrada)
│   ├── models/                 # Camada de modelo
│   ├── controllers/            # Camada de controle
│   └── views/                  # Camada de visualização
│
└── clean-architecture-system/  # Sistema refatorado (saída)
    ├── domain/                 # Entidades de domínio
    ├── application/            # Casos de uso
    ├── infrastructure/         # Implementações técnicas
    └── interface/              # Camada de apresentação
```

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.10 ou superior
- Chave de API da OpenAI (para refatoração automatizada)
- Git

### Instalação

```bash
git clone https://github.com/luislima41/ai-refactoring-study.git
cd ai-refactoring-study
```

### Uso

**Executar refatoração automatizada:**

```bash
cd auto-refactor-script
pip install -r requirements.txt
export OPENAI_API_KEY="sua_chave_aqui"
python main.py --input ../mvc-legacy-system --output ./output
```

**Gerar análise comparativa:**

```bash
cd auto-refactor-script
python analise_comparativa.py
```

**Executar smoke test:**

```bash
cd clean-architecture-system
python smoke_test.py
```

## 📊 Resultados

| Métrica | MVC Legacy | Clean Architecture | Variação |
|---------|------------|-------------------|----------|
| Arquivos | 4 | 11 | +175% |
| Linhas de código | 250 | 241 | -3.6% |
| Classes | 1 | 8 | +700% |
| Funções | 26 | 31 | +19.2% |
| Complexidade | 40 | 47 | +17.5% |

## 🔬 Metodologia

O estudo aplica uma abordagem híbrida:

1. **Automação**: GPT-4 realiza refatoração inicial seguindo prompts estruturados
2. **Curadoria**: Revisão humana ajusta o código gerado
3. **Validação**: Testes funcionais garantem equivalência comportamental
4. **Análise**: Métricas quantitativas avaliam impacto arquitetural

## 📝 Licença

Este projeto está disponível como material acadêmico de código aberto para fins educacionais e de pesquisa.

## 📖 Citação

Se você utilizar este trabalho em sua pesquisa, por favor referencie:

```
Lima, L. (2025). AI-Assisted Refactoring Study: MVC to Clean Architecture.
GitHub repository: https://github.com/luislima41/ai-refactoring-study
```

## 🔗 Links Relacionados

- [Documentação do auto-refactor-script](auto-refactor-script/README.md)
- [Documentação do mvc-legacy-system](mvc-legacy-system/README.md)
- [Documentação do clean-architecture-system](clean-architecture-system/README.md)

## 👤 Autor

**Luis Lima**
- GitHub: [@luislima41](https://github.com/luislima41)
