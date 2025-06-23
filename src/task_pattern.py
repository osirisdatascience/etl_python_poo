class ETLPattern:
    def __init__(self, nome):
        self.nome = nome

    def executar(self):
        """Se tentar usar o metodo executar com um objeto dessa classe: erro"""
        raise NotImplementedError("Você precisa implementar o método executar().")
