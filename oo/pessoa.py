class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome, idade):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo', idade=35)
    erick = Pessoa(renzo, nome='Erick', idade=18, )
    print(Pessoa.cumprimentar(erick))
    print(erick.cumprimentar())
    print(erick.nome, erick.idade)
    for filho in erick.filhos:
        print(filho.nome)
    erick.sobrenome = "Souza"
    del erick.filhos
    print(erick.__dict__)
    print(renzo.__dict__)
    print(id(erick.olhos))
    print(id(Pessoa.olhos))
    print(erick.__dict__)
    print(renzo.__dict__)
    print('-----------------')
    Pessoa.olhos = 5
    print(erick.olhos)
    renzo.olhos = 2
    print(renzo.olhos)
