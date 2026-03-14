# Declaração de classe

class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0
        
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de objetos
    # primeiro objeto
g1 = Gafanhoto() # g1 será o self da classe.

g1.nome = "Maria" # Inserindo atributos
g1.idade = 17 # Inserindo atributos

g1.aniversario() # Aplicando métodos no self g1

print(g1.mensagem())

    # segundo objeto
g2 = Gafanhoto() # g2 será o self da classe.

g2.nome = "Mauro" # Inserindo atributos
g2.idade = 53 # Inserindo atributos

g2.aniversario() # Aplicando métodos no self g2

    # terceiro objeto
g3 = Gafanhoto() # g3 será o self da classe.

g3.nome = "Luzia" # Inserindo atributos
g3.idade = 35 # Inserindo atributos

g3.aniversario() # Aplicando métodos no self g3