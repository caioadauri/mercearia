from Models import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from DAO import DaoCategoria, DaoEstoque, DaoVenda, DaoFuncionario, DaoFornecedor, DaoPessoa
from datetime import datetime

class ControllerCategoria:
  def cadastraCategoria(self, novaCategoria):
    existe = False
    x = DaoCategoria.ler()
    for i in x:
      if i.categoria == novaCategoria:
        existe = True
      
    if not existe:
      DaoCategoria.salvar(novaCategoria)
      print('Categoria cadastrada com sucesso!')
    else:
      print('Categoria já cadastrada')

  def removerCategoria(self, categoriaRemover):
    x = DaoCategoria.ler()
    cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

    if len(cat) <= 0:
      print(f'Categoria {x} não existe!')
    else:
      for i in range(len(x)):
        if x[i].categoria == categoriaRemover:
          del x[i]
          break
      print('Cateria removida com sucesso!')

      with open('categoria.txt', 'w') as arq:
        for i in x:
          arq.writelines(i.categoria)
          arq.writelines('\n')

  def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
    x = DaoCategoria.ler()
    cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

    if len(cat) > 0:
      cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
      if len(cat1) == 0:
        x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else(x), x))
        print('Categoria alterada com sucesso!')
      else:
        print('Categoria que dejesa alterar já existe')
    else:
      print('Categoria que deseja alterar não existe')

    with open('categoria.txt', 'w') as arq:
      for i in x:
        arq.writelines(i.categoria)
        arq.writelines('\n')

a = ControllerCategoria()
a.alterarCategoria('Carnes', 'Frutas')