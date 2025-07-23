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

