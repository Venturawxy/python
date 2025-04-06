import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Cadastrar")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("-----------------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", ENCODING="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivos:
            return json.load(arquivos)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def cadastrar_pessoa (cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    turma = input("Turma:")
    curso = input("Curso:")
    cadastros.append({"Nome": nome,"Idade": idade,"Turma": turma,"Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")