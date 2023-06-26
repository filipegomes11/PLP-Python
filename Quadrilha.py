class Quadrilha:
    def __init__(self, pessoas=None):
        self.pessoas = pessoas if pessoas is not None else []

    def getPessoas(self):
        return self.pessoas

    def setPessoas(self, pessoas):
        self.pessoas = pessoas

    def addPessoa(self, pessoa):
        self.pessoas.append(pessoa)
        print(len(self.pessoas))
        if len(self.pessoas) > 1:
            self.pessoas[-2].setAmor(pessoa)

    def __str__(self):
        result = []
        for i in range(len(self.pessoas)):
            result.append(self.pessoas[i].getNome() + " ")
            if self.pessoas[i].getAmor() is not None:
                result.append("ama " + self.pessoas[i].getAmor().getNome())
                if i < len(self.pessoas) - 1:
                    result.append(", ")
            else:
                result.append("ama toda a quadrilha.")
        return ''.join(result)


class Pessoa:
    def __init__(self, nome, amor=None):
        self.nome = nome
        self.amor = amor

    def getAmor(self):
        return self.amor

    def setAmor(self, amor):
        self.amor = amor

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def __str__(self):
        if self.amor is not None:
            return self.nome + " ama " + self.amor.nome + ", "
        else:
            return self.nome + " ama toda a quadrilha."


fulano = Pessoa("Fulano")
ciclano = Pessoa("Ciclano")
beltrano = Pessoa("Beltrano")

quadrilha = Quadrilha()
quadrilha.addPessoa(fulano)
quadrilha.addPessoa(ciclano)
quadrilha.addPessoa(beltrano)

print(quadrilha)
