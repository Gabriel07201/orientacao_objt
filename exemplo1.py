# criando uma classe para clientes da netflix
class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ['basico', 'premium'] # aqui está sendo criando informações que serão fixas para todos os objetos
        if plano in self.planos:
            self.plano = plano
        else:
            print('Erro')


    def mudar_plano(self, novo_plano): # como lá em cima eu usei o self para fazer referência ao objeto, eu posso usar as características em outras funções e também alterar as características do objeto
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')


cliente = Cliente('Gabriel', 'meuemails@gmail.com', 'basico')

