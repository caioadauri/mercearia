from Models import *

class DaoCategoria:
  @classmethod
  def salvar(cls, categoria):
    with open('categoria.txt', 'a') as arq:
      arq.writelines(categoria)
      arq.writelines('\n')
  
  @classmethod
  def ler(cls):
    with open('categoria.txt', 'r') as arq:
      cls.categoria = arq.readlines()
    
    cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

    print(cls.categoria)

# DaoCategoria.salvar('Frutas')
# DaoCategoria.salvar('Legumes')
# DaoCategoria.salvar('Verduras')
DaoCategoria.ler()
