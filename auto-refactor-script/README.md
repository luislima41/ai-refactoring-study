# 🤖 Script de Refatoração Automática MVC → Clean Architecture# 🤖 Script de Refatoração Automática MVC → Clean Architecture# 🤖 Script de Refatoração Automática MVC → Clean Architecture# 🤖 Script de Refatoração Automática MVC → Clean Architecture



Scripts para refatoração automatizada de sistemas MVC para Clean Architecture usando GPT-4 e análise de métricas.



## 📁 ArquivosScripts para refatoração automatizada de sistemas MVC para Clean Architecture usando GPT-4 e análise de métricas.



- **`main.py`**: Script de refatoração usando API do GPT-4

- **`analise_comparativa.py`**: Analisador de métricas (AST-based)

- **`requirements.txt`**: Dependências Python## 📁 ArquivosScripts para refatoração automatizada de sistemas MVC para Clean Architecture usando GPT-4 e análise de métricas.Este script realiza a refatoração automatizada de sistemas baseados no padrão Model-View-Controller (MVC) para a Clean Architecture, utilizando técnicas de Inteligência Artificial por meio da API do GPT.



## 🔧 Requisitos



- Python 3.10+- **`main.py`**: Script de refatoração usando API do GPT-4

- Chave de API da OpenAI

- Dependências: `openai==0.28.0`, `python-dotenv==1.0.0`- **`analise_comparativa.py`**: Analisador de métricas (AST-based)



## 🚀 Uso- **`requirements.txt`**: Dependências Python## 📁 Arquivos## 📋 Descrição



### 1. Refatoração Automatizada



```bash## 🔧 Requisitos

# Configure a API key

export OPENAI_API_KEY="sua_chave_aqui"



# Execute a refatoração- Python 3.10+- **`main.py`**: Script de refatoração usando API do GPT-4Ferramenta desenvolvida como parte do estudo de caso "Automatização da Refatoração de Sistemas Estruturados em MVC para a Clean Architecture Mediada por Inteligência Artificial". O script foi projetado para extrair, analisar e transformar componentes do sistema MVC, reorganizando-os conforme os princípios da Clean Architecture.

python main.py --input ../mvc-legacy-system --output ./clean_architecture_output

```- Chave de API da OpenAI



**Saída**: Código refatorado + `metricas_refatoracao.json`- Dependências: `openai==0.28.0`, `python-dotenv==1.0.0`- **`analise_comparativa.py`**: Analisador de métricas (AST-based)



### 2. Análise Comparativa



```bash## 🚀 Uso- **`requirements.txt`**: Dependências PythonA API do GPT desempenha o papel de agente automatizador, encarregado de compreender os padrões arquiteturais e propor transformações estruturais no código-fonte.

# Analisa MVC vs Clean Architecture e gera métricas

python analise_comparativa.py

```

### 1. Refatoração Automatizada

**Saída**:

- `analise_completa.json` - Métricas detalhadas

- `relatorio_analise.txt` - Relatório textual

```bash## 🔧 Requisitos## 🎯 Objetivos

## ⚠️ Limitações

# Configure a API key

- Script refatora arquivo por arquivo (não cria estrutura de diretórios automática)

- Requer refinamento manual para estrutura completa de Clean Architectureexport OPENAI_API_KEY="sua_chave_aqui"

- Validações e divisão em casos de uso devem ser feitas manualmente



# Execute a refatoração- Python 3.10+- Demonstrar a viabilidade técnica da aplicação de LLMs na modernização de sistemas legados

python main.py --input ../mvc-legacy-system --output ./clean_architecture_output

```- Chave de API da OpenAI- Reduzir custos, tempo de execução e incidência de erros humanos no processo de refatoração



**Saída**: Código refatorado + `metricas_refatoracao.json`- Dependências: `openai==0.28.0`, `python-dotenv==1.0.0`- Automatizar a reestruturação de código seguindo princípios da Clean Architecture:



### 2. Análise Comparativa  - Separação de responsabilidades



```bash## 🚀 Uso  - Inversão de dependências

# Analisa MVC vs Clean Architecture e gera métricas

python analise_comparativa.py  - Isolamento das regras de negócio

```

### 1. Refatoração Automatizada

**Saída**:

- `analise_completa.json` - Métricas detalhadas## 🎯 Funcionalidades

- `relatorio_analise.txt` - Relatório textual

```bash

## ⚠️ Limitações

# Configure a API key- **Análise automática** da estrutura MVC existente

- Script refatora arquivo por arquivo (não cria estrutura de diretórios automática)

- Requer refinamento manual para estrutura completa de Clean Architectureexport OPENAI_API_KEY="sua_chave_aqui"- **Identificação inteligente** de entidades, casos de uso e repositórios

- Validações e divisão em casos de uso devem ser feitas manualmente

- **Geração de código** seguindo princípios da Clean Architecture

# Execute a refatoração- **Separação em camadas**: Domain, Application, Infrastructure, Interface

python main.py --input ../mvc-legacy-system --output ./clean_architecture_output- **Preservação** da lógica de negócio original

```- **Transformação assistida por IA** através da API do GPT



**Saída**: Código refatorado + `metricas_refatoracao.json`## 📁 Estrutura



### 2. Análise Comparativa```

auto-refactor-script/

```bash├── main.py          # Script principal de refatoração

# Analisa MVC vs Clean Architecture e gera métricas└── README.md        # Este arquivo

python analise_comparativa.py

```tcc-latex/           # (novo) Todos os arquivos LaTeX (.tex) do TCC foram movidos para cá

```

**Saída**:

- `analise_completa.json` - Métricas detalhadasObservação: todos os arquivos .tex (capítulos, listas e pré-textuais) foram movidos para `tcc-latex/` para manter este diretório focado apenas no código. Se o seu documento principal inclui caminhos como `\input{auto-refactor-script/...}`, atualize para `\input{tcc-latex/...}`.

- `relatorio_analise.txt` - Relatório textual

## 🔧 Requisitos

## ⚠️ Limitações

- Python 3.10+

- Script refatora arquivo por arquivo (não cria estrutura de diretórios automática)- Acesso à API do GPT (OpenAI)

- Requer refinamento manual para estrutura completa de Clean Architecture- Chave de API válida da OpenAI

- Validações e divisão em casos de uso devem ser feitas manualmente- Dependências Python: `openai`, `python-dotenv`



## 📖 Contexto## 🚀 Como Usar



Parte do TCC: "Refatoração de Sistemas MVC para Clean Architecture Assistida por Inteligência Artificial"1. **Instale as dependências:**

```bash

Ver também: `../mvc-legacy-system/` (entrada) e `../clean-architecture-system/` (saída refinada)pip install -r requirements.txt

```

2. **Configure suas credenciais da API do GPT** (arquivo `.env`):
```env
OPENAI_API_KEY=sua_chave_api_aqui
```

3. **Execute o script** apontando para o sistema MVC de origem:
```bash
python main.py --input ../mvc-legacy-system --output ../clean-architecture-system
```

## 📊 Metodologia

O processo de refatoração automatizada segue duas etapas principais:

### 1. Desenvolvimento do Script Automatizador
- Extração de componentes do sistema MVC
- Análise da estrutura e dependências
- Mapeamento para padrões da Clean Architecture

### 2. Execução da Refatoração Assistida por IA
- Envio de prompts detalhados para a API do GPT
- Geração de código estruturado por camadas
- Validação e ajustes estruturais

## 📊 Resultados e Expectativas

### O Que o Script Gera

O script atual processa cada arquivo MVC individualmente e aplica princípios de Clean Architecture ao código. **A saída preserva a estrutura de arquivos original** com melhorias arquiteturais aplicadas ao conteúdo de cada arquivo:

- **Separação de responsabilidades** dentro dos arquivos existentes
- **Aplicação de princípios SOLID** ao código refatorado
- **Remoção de acoplamentos** diretos entre componentes
- **Introdução de abstrações** e interfaces onde apropriado

### Refinamento Manual Necessário

Para alcançar uma **estrutura completa de Clean Architecture** com múltiplos arquivos organizados em camadas (`domain/`, `application/use_cases/`, `infrastructure/`, `interface/`), é necessário:

1. **Reestruturação de diretórios**: Criar manualmente a hierarquia de pastas da Clean Architecture
2. **Divisão em múltiplos arquivos**: Separar casos de uso individuais (create, update, delete, list, etc.)
3. **Refinamento de interfaces**: Definir contratos claros entre camadas
4. **Validações específicas**: Implementar regras de negócio detalhadas (validação de email, campos obrigatórios, etc.)
5. **Testes e validação**: Garantir que a funcionalidade foi preservada

### Benefícios do Processo Híbrido (IA + Humano)

✅ **Aceleração inicial**: O script reduz significativamente o esforço de refatoração básica  
✅ **Sugestões arquiteturais**: A IA identifica separações de responsabilidades não óbvias  
✅ **Redução de erros mecânicos**: Automatiza transformações repetitivas com consistência  
✅ **Base sólida**: Fornece código já melhorado como ponto de partida para refinamento manual  
✅ **Documentação implícita**: As transformações sugeridas servem como guia educacional

### Sistema Demonstrado no TCC

O sistema `clean-architecture-system` presente neste repositório representa o **resultado final após refinamento manual**, demonstrando:
- 11 arquivos bem separados (vs. 4 originais do MVC)
- 8 classes especializadas com responsabilidades únicas
- 31 funções com granularidade apropriada
- 47 pontos de complexidade ciclomática distribuídos
- Estrutura completa de camadas independentes

**Este sistema final não é gerado automaticamente pelo script**, mas sim resultado da aplicação dos princípios sugeridos pela IA combinados com decisões arquiteturais humanas.

## ⚠️ Limitações Identificadas

Durante o desenvolvimento e aplicação do script, foram identificadas as seguintes limitações:

### Limitações Técnicas
- **Granularidade de saída**: O script refatora arquivo por arquivo, não cria automaticamente a estrutura multi-arquivo da Clean Architecture
- **Estrutura de diretórios**: Não reorganiza automaticamente os arquivos em camadas (`domain/`, `application/`, etc.)
- **Determinismo limitado**: Mesmo com `temperature=0.0`, pequenas variações podem ocorrer entre execuções

### Limitações do Processo com IA
- **Compreensão contextual dos LLMs**: Necessidade de contexto detalhado para transformações complexas
- **Elaboração de prompts**: Requer prompts bem estruturados e específicos para resultados consistentes
- **Validação humana**: Essencial para assegurar a integridade funcional do sistema refatorado
- **Aprendizado contínuo**: Processo iterativo que demanda ajustes e refinamentos nos prompts

### Recomendações de Uso
Para obter os melhores resultados:
1. Use o script como **primeira etapa** da refatoração
2. Revise e teste o código gerado antes de prosseguir
3. Aplique **refinamentos manuais** para estruturação completa
4. Documente as decisões arquiteturais tomadas durante o refinamento
5. Itere sobre os prompts com base nos resultados obtidos

## 🔍 Trabalho Acadêmico

Este script faz parte do Trabalho de Conclusão de Curso:

**"Automatização da Refatoração de Sistemas Estruturados em MVC para a Clean Architecture Mediada por Inteligência Artificial"**

### Conclusão do Estudo
A refatoração automatizada mediada por IA configura-se como um método promissor para a modernização de software, desde que esteja integrada a processos consistentes de validação, curadoria e aprendizado contínuo. A comparação entre MVC e Clean Architecture evidenciou avanços significativos na separação das camadas, consolidando a Clean Architecture como uma alternativa mais sustentável e escalável para ambientes de maior complexidade.
