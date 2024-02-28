class Restaurante:
    restaurantes = []

    #init = construtor - onde ficam os parâmetros que a gente quer que a adição de itens siga (atributos, por exemplo)
    #usar o SELF para indicar que aqueles atributos pertencem ao objeto que vai entrar

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} < {'Categoria do restaurante'.ljust(25)} < {'Status do restaurante'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} > {restaurante.categoria.ljust(25)} > {restaurante.ativo}')

    #PROPERTY = usado para modificar o atributo. Para fazer operações matemáticas, pegar vários valores e agrupar em um só, etc

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()