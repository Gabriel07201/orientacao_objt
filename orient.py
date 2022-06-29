class ControleRemoto: # criando uma classe
    def __init__(self, cor, altura, profundidade, largura): # inicializando a classe, aqui está inicializando as características do objeto  # o self faz referência ao próprio objeto # dentro do parametros acaba sendo obrigatório sempre informar as características do objeto
        self.cor = cor # aqui estamos fazendo a referência que a cor pertence à esse objeto
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    

    def passar_canal(self, botao): # criando um método que irá mudar o canal
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')



controle_remoto = ControleRemoto('cinza', '10cm', '2cm', '2cm') # aqui eu criei uma variável que recebe o objeto, isso acaba recebendo o nome de instancia
print(controle_remoto.cor)

controle_remoto2 = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto2.cor)

controle_remoto.passar_canal('+')