#superclasse para criar duas playlists menores


'''
adicionar musica - done
criar playlist - done
deletar música - done
deletar playlist - done
retornar musica - done 
'''

class Playlist:
    
    def __init__(self, nome:str, dono:str, musicas:list(dict[str, str]), playlist: list(dict[str, str, str])):
        self.nome = nome
        self.dono = dono
        self.musicas = []
        self.playlist  = []

    def add_musica(self):
        while True:
            nome = input('Insira o nome da música: ')
            if nome == '':
                print('O nome da música não pode ser um espaço em branco.')
                break
            
            autor = input('Insira o autor(a) da música: ')
            self.musicas.append({"nome": nome, "autor": autor})
            
            continuar = input('Quer adicionar outra música? S/N').upper()
            if continuar != 'S':
                break

    def creat_playlist(self):
        if self.musicas == []:
            print('É necessário que tenhamos músicas adicionadas.')
        else:
            nome_playlist = input('Insira o nome da sua playlist: ')
            self.playlist.append({'playlist': nome_playlist, 'musicas': self.musicas.copy()})
            print('Playlist criada com sucesso')

    def deletar_musica(self):
        nome = input('Insira o nome da música que você quer deletar: ')
        for v in self.playlist:
            for musica in v['musicas']:
                if musica['nome'].lower() == nome.lower():
                    v['musicas'].remove(musica)
                    print('Musica deletada com sucesso!!')
                print('Música não encontrada.')

    def deletar_playlist(self):
        nome = input('Insira o nome da playlist que você quer deletar: ')
        for v in self.playlist:
            if v['playlist'].lower() == nome.lower():
                self.playlist.remove(v)
                print('Playlist deletada!')

    def retornar_playlist(self):
        nome = input('Insira o nome da playlist que você quer ver: ')
        encontrada = False
        for v in self.playlist:
            if v['playlist'].lower() == nome.lower():
                print(v)
                break
        if not encontrada:
            print('Essa playlist não existe.')

    def atualizar_playlist(self):
        nome = input('Insira o nome da playlist que você quer atualizar: ')
        for v in self.playlist:
            if v['playlist'].lower() == nome.lower():
                self.add_musica()
                v['musicas'] = self.musicas.copy()
                print(f"Playlist '{nome}' atualizada com sucesso.")


'''LEARNINGS

- o método de deletar musicas precisa que nós percorramos todo a lista de dicionarios, por isso é necessário que façamos dois loopings;

- o método de atualizar a playlist funciona diferente pq é só uma string, ela não é uma lista então pra ser acessada é muito mais simples;
'''