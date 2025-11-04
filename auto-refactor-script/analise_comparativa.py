"""
Script de Análise Comparativa: MVC vs Clean Architecture
Gera métricas detalhadas para comparação entre os sistemas
"""

import os
import ast
import json
from pathlib import Path
from datetime import datetime

def analisar_arquivo_python(caminho):
    """Analisa um arquivo Python e extrai métricas"""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        tree = ast.parse(codigo)
        
        metricas = {
            "linhas_totais": len(codigo.split('\n')),
            "linhas_codigo": len([l for l in codigo.split('\n') if l.strip() and not l.strip().startswith('#')]),
            "classes": len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]),
            "funcoes": len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]),
            "imports": len([n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]),
            "atribuicoes": len([n for n in ast.walk(tree) if isinstance(n, ast.Assign)]),
            "chamadas_funcao": len([n for n in ast.walk(tree) if isinstance(n, ast.Call)]),
            "complexidade_ciclomatica": calcular_complexidade(tree)
        }
        
        # Análise de dependências
        dependencias = extrair_dependencias(tree)
        metricas["dependencias_externas"] = len(dependencias["externas"])
        metricas["dependencias_internas"] = len(dependencias["internas"])
        metricas["lista_dependencias"] = dependencias
        
        return metricas
        
    except Exception as e:
        print(f"Erro ao analisar {caminho}: {str(e)}")
        return None

def calcular_complexidade(tree):
    """Calcula complexidade ciclomática simplificada"""
    complexidade = 1  # Base
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
            complexidade += 1
        elif isinstance(node, ast.BoolOp):
            complexidade += len(node.values) - 1
    
    return complexidade

def extrair_dependencias(tree):
    """Extrai dependências do código"""
    externas = set()
    internas = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split('.')[0] in ['os', 'sys', 'json', 'time', 'datetime', 'openai']:
                    externas.add(alias.name)
                else:
                    internas.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                if node.module.split('.')[0] in ['os', 'sys', 'json', 'time', 'datetime', 'openai']:
                    externas.add(node.module)
                else:
                    internas.add(node.module)
    
    return {
        "externas": list(externas),
        "internas": list(internas)
    }

def analisar_diretorio(base_path, nome_sistema):
    """Analisa todos os arquivos Python de um diretório"""
    metricas_sistema = {
        "nome": nome_sistema,
        "caminho": base_path,
        "arquivos": [],
        "total_arquivos": 0,
        "total_linhas": 0,
        "total_classes": 0,
        "total_funcoes": 0,
        "total_imports": 0,
        "complexidade_total": 0
    }
    
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                caminho = os.path.join(root, file)
                print(f"Analisando {file}...")
                
                metricas = analisar_arquivo_python(caminho)
                if metricas:
                    metricas["nome_arquivo"] = file
                    metricas["caminho_relativo"] = os.path.relpath(caminho, base_path)
                    metricas_sistema["arquivos"].append(metricas)
                    
                    # Acumula totais
                    metricas_sistema["total_arquivos"] += 1
                    metricas_sistema["total_linhas"] += metricas["linhas_codigo"]
                    metricas_sistema["total_classes"] += metricas["classes"]
                    metricas_sistema["total_funcoes"] += metricas["funcoes"]
                    metricas_sistema["total_imports"] += metricas["imports"]
                    metricas_sistema["complexidade_total"] += metricas["complexidade_ciclomatica"]
    
    return metricas_sistema

def gerar_tabela_comparativa(mvc_metrics, clean_metrics):
    """Gera tabela comparativa em formato LaTeX"""
    
    latex = r"""
\begin{table}[h]
\centering
\caption{Comparação Quantitativa: MVC vs Clean Architecture}
\label{tab:comparacao}
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Métrica} & \textbf{MVC} & \textbf{Clean Arch} & \textbf{Variação} \\
\hline
"""
    
    metricas = [
        ("Arquivos Python", mvc_metrics["total_arquivos"], clean_metrics["total_arquivos"]),
        ("Linhas de Código", mvc_metrics["total_linhas"], clean_metrics["total_linhas"]),
        ("Classes", mvc_metrics["total_classes"], clean_metrics["total_classes"]),
        ("Funções/Métodos", mvc_metrics["total_funcoes"], clean_metrics["total_funcoes"]),
        ("Imports", mvc_metrics["total_imports"], clean_metrics["total_imports"]),
        ("Complexidade Ciclomática", mvc_metrics["complexidade_total"], clean_metrics["complexidade_total"])
    ]
    
    for metrica, valor_mvc, valor_clean in metricas:
        variacao = valor_clean - valor_mvc
        if valor_mvc > 0:
            percentual = (variacao / valor_mvc) * 100
            variacao_str = f"{variacao:+d} ({percentual:+.1f}\\%)"
        else:
            variacao_str = f"{variacao:+d}"
        
        latex += f"{metrica} & {valor_mvc} & {valor_clean} & {variacao_str} \\\\\n\\hline\n"
    
    latex += r"""\end{tabular}
\end{table}
"""
    
    return latex

def gerar_relatorio_completo(mvc_metrics, clean_metrics, output_path):
    """Gera relatório completo em múltiplos formatos"""
    
    relatorio = {
        "data_analise": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mvc": mvc_metrics,
        "clean_architecture": clean_metrics,
        "comparacao": {
            "reducao_acoplamento": {
                "dependencias_mvc": sum(a["dependencias_internas"] for a in mvc_metrics["arquivos"]),
                "dependencias_clean": sum(a["dependencias_internas"] for a in clean_metrics["arquivos"])
            },
            "aumento_modularizacao": {
                "arquivos_mvc": mvc_metrics["total_arquivos"],
                "arquivos_clean": clean_metrics["total_arquivos"],
                "diferenca": clean_metrics["total_arquivos"] - mvc_metrics["total_arquivos"]
            }
        }
    }
    
    # Salva JSON completo
    json_path = os.path.join(output_path, "analise_completa.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Relatório JSON salvo em: {json_path}")
    
    # Gera tabela LaTeX
    latex_table = gerar_tabela_comparativa(mvc_metrics, clean_metrics)
    latex_path = os.path.join(output_path, "tabela_comparacao.tex")
    with open(latex_path, 'w', encoding='utf-8') as f:
        f.write(latex_table)
    
    print(f"✅ Tabela LaTeX salva em: {latex_path}")
    
    # Gera relatório texto
    gerar_relatorio_texto(mvc_metrics, clean_metrics, output_path)

def gerar_relatorio_texto(mvc_metrics, clean_metrics, output_path):
    """Gera relatório em formato texto para inclusão no TCC"""
    
    texto = f"""
ANÁLISE COMPARATIVA: MVC vs CLEAN ARCHITECTURE
{'='*70}

1. CONTEXTUALIZAÇÃO DO MÓDULO ANALISADO
{'='*70}

Módulo: Sistema de Gerenciamento de Usuários

Sistema MVC Original:
- Total de arquivos: {mvc_metrics['total_arquivos']}
- Linhas de código: {mvc_metrics['total_linhas']}
- Classes definidas: {mvc_metrics['total_classes']}
- Funções/métodos: {mvc_metrics['total_funcoes']}
- Imports (dependências): {mvc_metrics['total_imports']}
- Complexidade ciclomática total: {mvc_metrics['complexidade_total']}

Estrutura do sistema MVC:
"""
    
    for arquivo in mvc_metrics['arquivos']:
        texto += f"\n  • {arquivo['nome_arquivo']}:\n"
        texto += f"    - Linhas: {arquivo['linhas_codigo']}\n"
        texto += f"    - Classes: {arquivo['classes']}\n"
        texto += f"    - Funções: {arquivo['funcoes']}\n"
        texto += f"    - Complexidade: {arquivo['complexidade_ciclomatica']}\n"
    
    texto += f"""

2. RESULTADOS DA REFATORAÇÃO
{'='*70}

Sistema Clean Architecture Resultante:
- Total de arquivos: {clean_metrics['total_arquivos']}
- Linhas de código: {clean_metrics['total_linhas']}
- Classes definidas: {clean_metrics['total_classes']}
- Funções/métodos: {clean_metrics['total_funcoes']}
- Imports (dependências): {clean_metrics['total_imports']}
- Complexidade ciclomática total: {clean_metrics['complexidade_total']}

Estrutura do sistema Clean Architecture:
"""
    
    for arquivo in clean_metrics['arquivos']:
        texto += f"\n  • {arquivo['nome_arquivo']}:\n"
        texto += f"    - Linhas: {arquivo['linhas_codigo']}\n"
        texto += f"    - Classes: {arquivo['classes']}\n"
        texto += f"    - Funções: {arquivo['funcoes']}\n"
        texto += f"    - Complexidade: {arquivo['complexidade_ciclomatica']}\n"
    
    # Cálculos de variação
    var_arquivos = clean_metrics['total_arquivos'] - mvc_metrics['total_arquivos']
    var_linhas = clean_metrics['total_linhas'] - mvc_metrics['total_linhas']
    var_classes = clean_metrics['total_classes'] - mvc_metrics['total_classes']
    var_funcoes = clean_metrics['total_funcoes'] - mvc_metrics['total_funcoes']
    var_complexidade = clean_metrics['complexidade_total'] - mvc_metrics['complexidade_total']
    
    texto += f"""

3. MÉTRICAS COMPARATIVAS
{'='*70}

Variações observadas após a refatoração:

• Arquivos: {var_arquivos:+d} ({(var_arquivos/mvc_metrics['total_arquivos']*100):+.1f}%)
  Interpretação: {"Aumento na modularização" if var_arquivos > 0 else "Redução de arquivos"}

• Linhas de código: {var_linhas:+d} ({(var_linhas/mvc_metrics['total_linhas']*100):+.1f}%)
  Interpretação: {"Expansão devido à separação de responsabilidades" if var_linhas > 0 else "Redução de código"}

• Classes: {var_classes:+d} ({(var_classes/mvc_metrics['total_classes']*100 if mvc_metrics['total_classes'] > 0 else 0):+.1f}%)
  Interpretação: {"Maior granularidade e separação de conceitos" if var_classes > 0 else "Simplificação"}

• Funções: {var_funcoes:+d} ({(var_funcoes/mvc_metrics['total_funcoes']*100):+.1f}%)
  Interpretação: {"Métodos mais específicos e coesos" if var_funcoes > 0 else "Consolidação"}

• Complexidade: {var_complexidade:+d} ({(var_complexidade/mvc_metrics['complexidade_total']*100):+.1f}%)
  Interpretação: {"Aumento pontual" if var_complexidade > 0 else "Redução da complexidade"}

4. ANÁLISE QUALITATIVA
{'='*70}

Melhorias Estruturais Identificadas:

✓ Separação de Responsabilidades:
  - Entidades de domínio isoladas (domain/entities/)
  - Casos de uso independentes (application/use_cases/)
  - Infraestrutura separada (infrastructure/)
  
✓ Inversão de Dependências:
  - Casos de uso recebem repositórios via injeção
  - Domínio não conhece infraestrutura
  
✓ Testabilidade:
  - Componentes podem ser testados isoladamente
  - Mocks e stubs facilitados pela arquitetura

✓ Manutenibilidade:
  - Mudanças localizadas por camada
  - Menor propagação de impacto
"""
    
    txt_path = os.path.join(output_path, "relatorio_analise.txt")
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(texto)
    
    print(f"✅ Relatório TXT salvo em: {txt_path}")

def main():
    print("🔍 Iniciando Análise Comparativa\n")
    
    # Define caminhos
    base_dir = Path(__file__).parent.parent
    mvc_path = base_dir / "mvc-legacy-system"
    clean_path = base_dir / "clean-architecture-system"
    output_path = base_dir / "auto-refactor-script"
    
    # Analisa sistemas
    print("\n📊 Analisando sistema MVC...")
    mvc_metrics = analisar_diretorio(str(mvc_path), "MVC Legacy System")
    
    print("\n📊 Analisando sistema Clean Architecture...")
    clean_metrics = analisar_diretorio(str(clean_path), "Clean Architecture System")
    
    # Gera relatórios
    print("\n📝 Gerando relatórios comparativos...")
    gerar_relatorio_completo(mvc_metrics, clean_metrics, str(output_path))
    
    print("\n" + "="*70)
    print("✅ Análise Comparativa Concluída!")
    print("="*70)
    print("\nArquivos gerados:")
    print("  • analise_completa.json - Dados completos em JSON")
    print("  • tabela_comparacao.tex - Tabela para LaTeX")
    print("  • relatorio_analise.txt - Relatório detalhado")
    print("="*70)

if __name__ == "__main__":
    main()
