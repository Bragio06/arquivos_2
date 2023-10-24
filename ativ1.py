def ler_dados():

    nome_do_estudante = input("Digite o nome do estudante: ")
    idade_do_estudante = int(input("Digite a idade do estudante: "))
    curso_do_estudante = input("Digite o curso do estudante: ")

    estudante = {
        "nome": nome_do_estudante,
        "idade": idade_do_estudante,
        "curso": curso_do_estudante,
    }

    return estudante

def ler_varios_alunos():
    quantidade = int (input("Digite a Quantidade: "))
    alunos = []
    for x in range (0,quantidade):
        aluno = ler_dados()
        alunos.append (aluno)
    
    return alunos