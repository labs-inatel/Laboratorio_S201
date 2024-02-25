class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

pessoa01 = Pessoa("Iza",20)
pessoa02 = Pessoa("Izo",20)

print(pessoa01.nome,pessoa01.idade)
print(pessoa02.nome,pessoa02.idade)