from playlist import Playlist
playlist = Playlist('','', [], [])

class Menu():

    def __init__(self):
        pass

    def menu_funcional(self):
        while True:
            print('BEM VINDO'.center(16, '='))
            print("[1] Criar playlist")
            print("[2] Ver playlist")
            print("[3] Atualizar playlist.")
            print("[4] Apagar música")
            print("[5] Apagar playlist")
            print("[6] Sair")
            escolha = str(input("Escolha uma opção: "))

            if escolha == '1':
                playlist.musicas.clear()
                playlist.add_musica()
                playlist.creat_playlist()
            elif escolha == '2':
                playlist.retornar_playlist()
            elif escolha == '3':
                playlist.atualizar_playlist()
            elif escolha == '4':
                playlist.deletar_musica()
            elif escolha == '5':
                playlist.deletar_playlist()
            elif escolha == '6':
                break
            else:
                print('Escolha uma opção válida')

