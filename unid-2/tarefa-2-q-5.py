# 5) Crie uma classe chamada Livro que tenha um método construtor com os seguintes atributos:
# titulo: o título do livro.
# autor: o nome do autor.
# ano_publicacao: o ano de publicação do livro.
# preco: o preço do livro.
# Crie dois objetos dessa classe, cada um com atributos diferentes, e imprima as informações de cada livro no formato: "Título: {titulo}, Autor: {autor}, Ano: {ano_publicacao}, Preço: R${preco}"

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor  = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco  
    
    def exibir_informacoes(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Preço: R${self.preco}')


livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 39.90)
livro2 = Livro('Dom Casmurro', 'Machado de Assis', 1899, 19.90)

livro1.exibir_informacoes()
livro2.exibir_informacoes()

