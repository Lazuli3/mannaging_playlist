class Usuarios:
    def __init__(self, user:str, senha:str, plano:str, usuarios:list(dict[str, str, str])):
        self.usuarios = {}
        self.user = user
        self.senha = senha 
        self.plano = plano

    def cadastro_usuarios(self):
        user = input('Insira o user do usuario:')
        if user in self.usuarios:
            print('usuario já existente')
        if user == '':
            print('O user não pode ser vazio.')
            return
        
        senha = input('Insira a sua senha: ')
        plano = input('Escolha um plano (premium/normal): ')
        self.usuarios[user] = {'senha':senha, 'plano':plano}
        print(self.usuarios)

    def login_usuario(self):
        username = input('Insira o seu nome de usuário: ')
        senha = input('Insira a sua senha: ')

        if username in self.usuarios and senha in self.usuarios[username]['senha'] == senha:
            print('vai chamar o menu.')
        else:
            print('Login inválido, tente novamente.')

sistema = Usuarios('', '', '', [])

sistema.cadastro_usuarios()
sistema.login_usuario()


'''Learnings:

Na linha: if username in self.usuarios and senha in self.usuarios[username]['senha'] == senha:
para fazer a validação precisamos chamar a variavel instituida na função, e não quando criamos a lista.

'''
