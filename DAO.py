from Models import *

class DaoCategoria:
  @classmethod
  def salvar(cls, categoria: Categoria):
    with open('categoria.txt', 'a') as arq:
      arq.writelines(categoria)
      arq.writelines('\n')
  
  @classmethod
  def ler(cls):
    with open('categoria.txt', 'r') as arq:
      cls.categoria = arq.readlines()
    
    cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

    cat = []
    for i in cls.categoria:
      cat.append(Categoria(i))
    return cat


class DaoVenda:
  @classmethod
  def salvar(cls, venda: Venda):
    with open('venda.txt', 'a') as arq:
      arq.writelines(venda.itensVendido.nome + '|' + venda.itensVendido.preco + '|' + venda.itensVendido.categoria + '|' 
                     + venda.vendedor + '|' + venda.comprador + '|' + str(venda.quantidadeVendida) + '|' + venda.data)
      arq.writelines('\n')
    
  @classmethod
  def ler(cls):
    with open('venda.txt', 'r') as arq:
      cls.venda = arq.readlines()
      
    cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
    cls.venda = list(map(lambda x: x.split('|'), cls.venda))
    vend = []
    for i in cls.venda:
      vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
    return vend


class DaoEstoque:
  @classmethod
  def salvar(cls, produto: Produtos, quantidade):
    with open('estoque.txt', 'a') as arq:
      arq.writelines(produto.nome + '|' + produto.preco + '|' + produto.categoria + '|' + str(quantidade))
      arq.writelines('\n')
  
  @classmethod
  def ler(cls):
    with open('estoque.txt', 'r') as arq:
      cls.estoque = arq.readlines()
    
    cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
    cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
    estoq = []
    for i in cls.estoque:
      estoq.append(Estoque(Produtos(i[0], i[1], i[2], i[3])))
    return estoq
  

class DaoFornecedor:
  @classmethod
  def salvar(cls, fornecedor: Fornecedor):
    with open('fornecedor.txt', 'a') as arq:
      arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' + fornecedor.telefone + '|' + fornecedor.categoria)
      arq.writelines('\n')
  
  @classmethod
  def ler(cls):
    with open('fornecedor.txt', 'r') as arq:
      cls.fornecedores = arq.readlines()

    cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
    cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
    forn = []
    for i in cls.fornecedores:
      forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
    return forn


class DaoPessoa:
  @classmethod
  def salvar(cls, pessoa: Pessoa):
    with open('pessoa.txt', 'a') as arq:
      arq.writelines(pessoa.nome + '|' + pessoa.telefone + '|' + pessoa.cpf + '|' + pessoa.email + '|' + pessoa.endereco)
      arq.writelines('\n')

  @classmethod
  def ler(cls):
    with open('pessoa.txt', 'r') as arq:
      cls.pessoas = arq.readlines()

    cls.pessoas = list(map(lambda x: x.replace('\n', ''), cls.pessoas))
    cls.pessoas = list(map(lambda x: x.split('|'), cls.pessoas))

    pess = []
    for i in cls.pessoas:
      pess.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
    
    return pess


class DaoFuncionario:
  @classmethod
  def salvar(cls, funcionario: Funcionario):
    with open('funcionario.txt', 'a') as arq:
      arq.wtritelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + 
                      '|' + funcionario.email + '|' + funcionario.endereco)
      arq.writelines('\n')

  @classmethod
  def ler(cls):
    with open('funcionario.txt', 'r') as arq:
      cls.funcionarios = arq.readlines()
    
    cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
    cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

    func = []
    for i in cls.funcionarios:
      func.append(Funcionario(i[0],i[1], i[2], i[3], i[4], i[5]))
    return func

