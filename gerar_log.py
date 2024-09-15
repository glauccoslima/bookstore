import os

# Defina os diretórios e arquivos a serem ignorados
IGNORAR_DIRETORIOS = {'node_modules', '__pycache__', 'venv'}
IGNORAR_ARQUIVOS = {'.pyc', 'package-lock.json'}

# Defina as extensões que você deseja capturar
EXTENSOES = {'.py', '.ts', '.json', '.sql', '.toml', '.txt', '.prisma'}

def listar_arquivos_e_conteudo(diretorio='.'):
    # Define o nome do arquivo de saída como 'geral.txt'
    with open('geral.txt', 'w') as log:
        for root, dirs, files in os.walk(diretorio):
            # Remove diretórios que devem ser ignorados
            dirs[:] = [d for d in dirs if d not in IGNORAR_DIRETORIOS]

            for file in files:
                # Pular arquivos que devem ser ignorados
                if file.endswith(tuple(IGNORAR_ARQUIVOS)):
                    continue

                # Verificar se a extensão do arquivo está na lista de extensões desejadas
                if os.path.splitext(file)[1] in EXTENSOES:
                    caminho_completo = os.path.join(root, file)
                    # Escrever o nome do arquivo no log
                    log.write(f"\n## {file}\n")

                    # Abrir o arquivo e escrever seu conteúdo
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            log.write(f"\n{conteudo}\n")
                    except Exception as e:
                        log.write(f"\n[Erro ao ler o arquivo: {str(e)}]\n")

# Executa a função para listar os arquivos e conteúdo
listar_arquivos_e_conteudo()
