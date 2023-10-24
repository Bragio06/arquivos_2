from lerDados import ler_varios_alunos
from procurarAluno import procurarAluno
from atualizarAluno import atualizarAluno
from removerEstudante import removerEstudante
from ler_arquivo import ler_arquivo
from criarArquivo import criar_arquivo_lista
from idadeMedia import calcularIdadeMedia
from contagemCursos import contarCursos

if __name__ == '__main__':
    dados_alunos = ler_varios_alunos()

    criar_arquivo_lista(lista=dados_alunos, nome_arquivo="manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt")

    aluno_escolhido = procurarAluno()

    print(atualizarAluno(aluno_escolhido=aluno_escolhido))

    print(removerEstudante())

    print(ler_arquivo("manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt"))

    print(calcularIdadeMedia())

    print(f"Total de cursos: {contarCursos()}")