class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Erick', 18)
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome, p.idade)