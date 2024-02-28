class Restaurante:
    restaurantes = []

    #init = construtor - onde ficam os parâmetros que a gente quer que a adição de itens siga (atributos, por exemplo)
    #usar o SELF para indicar que aqueles atributos pertencem ao objeto que vai entrar

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} > {restaurante.categoria} > {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()