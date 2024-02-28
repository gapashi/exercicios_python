class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = float(duracao)
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} , {self.artista} , {self.duracao}'
            
    def listar_musicas():
        for musica in Musica.musicas:    
            print(f'{musica.nome} > {musica.artista} > {musica.duracao}')

musica_1 = Musica('As It Was', 'Harry Styles', 3.00)
musica_2 = Musica('Baepsae', 'BTS', 3.53)

Musica.listar_musicas()
