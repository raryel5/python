# Declaração de classe

class Gafanhoto:
    """
Essa classe cria um aluno do curso do Guanabara, que ele carinhosamente chama de gafanhotos.
    
Para criar uma nova pessoa, use:
variavel = Gafanhoto(nome, idade)
    
Este é um exemplo documentação sobre classe Gafanhoto, que poderá ser lido com o método DUNDER DOC.

O underline duplo é chamado de Dunder.
    """

    def __init__(self, nome = "", idade=0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade
        
    # Métodos de instância
    def aniversario(self):
        self.idade += 1        

    def __str__(self): # vai exibir uma mensagem quando a objeto for chamado sem nenhum método.
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}."

# Declaração de objetos
g1 = Gafanhoto("Maria", 17) # g1 será o self da classe.
g1.aniversario() # Aplicando métodos no self g1
print(g1)

g2 = Gafanhoto("Mauro", 53) # g1 será o self da classe.
g2.aniversario() # Aplicando métodos no self g1
print(g2)

print(g1.__doc__) # Exibe a documentação da classe à que pertence o objeto g1, se houver.

print(g1.__dict__) # Retorna os atributos do objeto em formato de lista.
print(g1.__getstate__()) # Método que retorna o estado dos atributos do objeto g1.
print(g1.__class__) # Retorna a classe do objeto g1.

