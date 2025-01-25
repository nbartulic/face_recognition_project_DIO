import os
import subprocess

# Configuração do repositório
repo_url = "https://github.com/nbartulic/face_recognition_project_DIO/tree/dda3b5fc9d1654d866d54004a690a0d1b76ae432"
commit_message = "First commit - Face Recognition Project"

def run_command(command):
    """Executa um comando do sistema e retorna a saída."""
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Erro ao executar: {command}\n{process.stderr}")
    else:
        print(process.stdout)

def git_push():
    try:
        # Inicializa o repositório Git localmente
        run_command("git init")
        
        # Adiciona todos os arquivos ao commit
        run_command("git add .")

        # Faz o commit com uma mensagem
        run_command(f'git commit -m "{commit_message}"')

        # Adiciona o repositório remoto
        run_command(f"git remote add origin {repo_url}")

        # Faz o push para o repositório remoto
        run_command("git branch -M main")
        run_command("git push -u origin main")

        print("Projeto enviado para o GitHub com sucesso!")

    except Exception as e:
        print(f"Erro durante o processo de upload: {e}")

if __name__ == "__main__":
    git_push()
