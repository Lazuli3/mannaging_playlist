#criando sistema principal

from playlist import Playlist
from usuario import Usuarios

users = Usuarios('', '', '', [])
playlist = Playlist('','', [], [])

def menu_login(users):
    while True:
        print("MENU".center(16, '=')) 
        print('[1] CADASTRO')
        print('[2] LOGIN')
        print('[3] SAIR')
          
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            users.cadastro_usuarios()
        elif escolha == '2':
             users.login_usuario()
        elif escolha == '3':
             break
        else:
             print('Escolha uma opção válida.')

menu_login(users)













'''Learnings:

Na linha: if username in self.usuarios and senha in self.usuarios[username]['senha'] == senha:
para fazer a validação precisamos chamar a variavel instituida na função, e não quando criamos a lista.

'''