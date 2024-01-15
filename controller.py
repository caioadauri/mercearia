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


a = ControllerCategoria()
a.cadastraCategoria('Frios')