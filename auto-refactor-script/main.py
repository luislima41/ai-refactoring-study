import os
import openai
import time
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY não definida.")
    print("Configure no PowerShell: $env:OPENAI_API_KEY=\"sua_chave\"")
    print("Ou crie arquivo .env com: OPENAI_API_KEY=...")
openai.api_key = OPENAI_API_KEY

BASE_PATH = r"c:\\Users\\Luis\\Documents\\TCC\\mvc-legacy-system"
OUTPUT_PATH = r"c:\\Users\\Luis\\Documents\\TCC\\auto-refactor-script\\clean_architecture_output"
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Estrutura para armazenar métricas
metricas = {
    "data_execucao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "tempo_total_segundos": 0,
    "arquivos_processados": 0,
    "linhas_codigo_originais": 0,
    "linhas_codigo_refatoradas": 0,
    "tokens_consumidos": 0,
    "erros": 0,
    "detalhes_arquivos": []
}

def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def salvar_arquivo(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def contar_linhas(codigo):
    return len([linha for linha in codigo.split('\n') if linha.strip()])

def contar_classes(codigo):
    return codigo.count('class ')

def contar_funcoes(codigo):
    return codigo.count('def ')

def contar_imports(codigo):
    linhas = codigo.split('\n')
    return len([l for l in linhas if l.strip().startswith(('import ', 'from '))])

def refatorar_codigo(codigo, nome_arquivo):
    prompt = f'''
Você é um engenheiro de software especializado em Clean Architecture.
Analise o seguinte código MVC e reorganize-o conforme os princípios da Clean Architecture,
preservando a lógica de negócio e separando responsabilidades.

Código original ({nome_arquivo}):
{codigo}

Retorne APENAS o código Python refatorado, sem explicações adicionais.
Organize o código seguindo:
- Entidades de domínio puras (sem dependências externas)
- Casos de uso com injeção de dependências
- Repositórios com interfaces abstratas
- Separação clara de responsabilidades
'''
    tempo_inicio = time.time()
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1800,
        temperature=0.0
    )
    tempo_decorrido = time.time() - tempo_inicio
    
    # Registra métricas da chamada da API
    metricas["tokens_consumidos"] += resposta.usage.total_tokens
    
    return resposta.choices[0].message["content"], tempo_decorrido

def processar_diretorio(base_dir):
    tempo_inicio_total = time.time()
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                try:
                    caminho_entrada = os.path.join(root, file)
                    codigo_original = ler_arquivo(caminho_entrada)
                    
                    # Métricas do código original
                    linhas_originais = contar_linhas(codigo_original)
                    classes_originais = contar_classes(codigo_original)
                    funcoes_originais = contar_funcoes(codigo_original)
                    imports_originais = contar_imports(codigo_original)
                    
                    print(f"Refatorando {file} ...")
                    novo_codigo, tempo_arquivo = refatorar_codigo(codigo_original, file)
                    
                    if novo_codigo.startswith("```python"):
                        novo_codigo = novo_codigo.split("```python")[1].split("```")[0].strip()
                    elif novo_codigo.startswith("```"):
                        novo_codigo = novo_codigo.split("```")[1].split("```")[0].strip()
                    
                    linhas_refatoradas = contar_linhas(novo_codigo)
                    classes_refatoradas = contar_classes(novo_codigo)
                    funcoes_refatoradas = contar_funcoes(novo_codigo)
                    imports_refatorados = contar_imports(novo_codigo)
                    
                    linhas_refatoradas = contar_linhas(novo_codigo)
                    classes_refatoradas = contar_classes(novo_codigo)
                    funcoes_refatoradas = contar_funcoes(novo_codigo)
                    imports_refatorados = contar_imports(novo_codigo)
                    
                    caminho_saida = caminho_entrada.replace(BASE_PATH, OUTPUT_PATH)
                    salvar_arquivo(caminho_saida, novo_codigo)
                    
                    metricas["arquivos_processados"] += 1
                    metricas["linhas_codigo_originais"] += linhas_originais
                    metricas["linhas_codigo_refatoradas"] += linhas_refatoradas
                    
                    metricas["detalhes_arquivos"].append({
                        "nome": file,
                        "caminho": caminho_entrada,
                        "tempo_processamento_segundos": round(tempo_arquivo, 2),
                        "linhas_originais": linhas_originais,
                        "linhas_refatoradas": linhas_refatoradas,
                        "classes_originais": classes_originais,
                        "classes_refatoradas": classes_refatoradas,
                        "funcoes_originais": funcoes_originais,
                        "funcoes_refatoradas": funcoes_refatoradas,
                        "imports_originais": imports_originais,
                        "imports_refatorados": imports_refatorados
                    })
                    
                    print(f"  ✓ Concluído em {tempo_arquivo:.2f}s")
                    
                except Exception as e:
                    print(f"  ✗ Erro ao processar {file}: {str(e)}")
                    metricas["erros"] += 1
    
    metricas["tempo_total_segundos"] = round(time.time() - tempo_inicio_total, 2)

def salvar_metricas():
    caminho_metricas = os.path.join(OUTPUT_PATH, "metricas_refatoracao.json")
    with open(caminho_metricas, 'w', encoding='utf-8') as f:
        json.dump(metricas, f, indent=2, ensure_ascii=False)
    print(f"\n📊 Métricas salvas em: {caminho_metricas}")

def exibir_relatorio():
    """Exibe relatório resumido no console"""
    print("\n" + "="*60)
    print("RELATÓRIO DE REFATORAÇÃO AUTOMATIZADA")
    print("="*60)
    print(f"Data/Hora: {metricas['data_execucao']}")
    print(f"Tempo Total: {metricas['tempo_total_segundos']}s")
    print(f"Arquivos Processados: {metricas['arquivos_processados']}")
    print(f"Erros: {metricas['erros']}")
    print(f"Tokens Consumidos (API): {metricas['tokens_consumidos']}")
    print(f"\nLinhas de Código:")
    print(f"  Original: {metricas['linhas_codigo_originais']}")
    print(f"  Refatorado: {metricas['linhas_codigo_refatoradas']}")
    print(f"  Diferença: {metricas['linhas_codigo_refatoradas'] - metricas['linhas_codigo_originais']:+d}")
    
    if metricas['arquivos_processados'] > 0:
        tempo_medio = metricas['tempo_total_segundos'] / metricas['arquivos_processados']
        print(f"\nTempo Médio por Arquivo: {tempo_medio:.2f}s")
    
    print("="*60)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Refatoração automatizada MVC → Clean Architecture")
    parser.add_argument("--input", "-i", dest="input_dir", default=BASE_PATH, help="Diretório de entrada (sistema MVC)")
    parser.add_argument("--output", "-o", dest="output_dir", default=OUTPUT_PATH, help="Diretório de saída (código refatorado)")
    args = parser.parse_args()

    # Resolve caminhos absolutos e atualiza variáveis globais
    BASE_PATH = os.path.abspath(args.input_dir)
    OUTPUT_PATH = os.path.abspath(args.output_dir)
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    print("🚀 Iniciando refatoração automatizada MVC → Clean Architecture")
    print(f"Diretório de entrada: {BASE_PATH}")
    print(f"Diretório de saída: {OUTPUT_PATH}\n")

    if not OPENAI_API_KEY:
        print("⚠️ Encerrando: a variável OPENAI_API_KEY não está definida.")
    else:
        processar_diretorio(BASE_PATH)
        salvar_metricas()
        exibir_relatorio()
        print("\n✅ Refatoração automatizada concluída com sucesso!")
