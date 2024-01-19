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

  def mostrarCategoria(self):
    categorias = DaoCategoria.ler()
    if len(categorias) == 0:
      print('Nenhuma categoria cadastrada')
    else:
      for i in categorias:
        print(i.categoria)

class ControllerEstoque:

  def cadastrarProduto(self, nome, preco, categoria, quantidade):
    x = DaoEstoque.ler()
    y = DaoCategoria.ler()
    h = list(filter(lambda x: x.categoria == categoria, y))
    est = list(filter(lambda x: x.produto.nome == nome, x))

    if len(h) > 0:
      if len(est) == 0:
        produto = Produtos(nome, preco, categoria)
        DaoEstoque.salvar(produto, quantidade)
        print('Produto cadastrado com sucesso!')
      else:
        print('Produto já cadastrado')
    else:
      print('Categoria não cadastrada')

  def removerProduto(nome):
    x = DaoEstoque.ler()
    est = list(filter(lambda x: x.produto.nome == nome, x))

    if len(est) <= 0:
      print('Produto não encontrado!')
    else:
      for i in range(len(x)):
        if x[i].produto.nome == nome:
          del x[i]
          break
      print('Produto removido com sucesso!')
    
    with open('estoque.txt', 'w') as arq:
      for i in x:
        arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + i.quantidade)
        arq.writelines('\n')

  def alterarProduto(self, nome, nomeNovo, precoNovo, categoriaNova, quantidadeNova):
    x = DaoEstoque.ler()
    y = DaoCategoria.ler()
    h = list(filter(lambda x: x.categoria == categoriaNova, y))

    if len(h) > 0:
      est = list(filter(lambda x: x.produto.nome == nome, x))
      if len(est) > 0:
        est = list(filter(lambda x: x.produto.nome == nomeNovo, x))
        if len(est) == 0:
          x = list(map(lambda x: Estoque(Produtos(nomeNovo, precoNovo, categoriaNova), quantidadeNova) if(x.produto.nome == nome) else(x), x))
          print('Produto alterado com sucesso!')
        else:
          print('Produto já está cadastrado, tento outro nome')
      else:
        print('Produto não existente')
      
      with open('estoque.txt', 'w') as arq:
        for i in x:
          arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + i.quantidade)
          arq.writelines('\n')
    else:
      print('Nova categoria não existente')

  def mostrarEstoque(self):
    estoque = DaoEstoque.ler()
    if len(estoque) > 0:
      for i in estoque:
        print('=====================')
        print(f'Nome: {i.produto.nome}  R$ {i.produto.preco},00  Categoria: {i.produto.categoria}  Quantidade: {i.quantidade}')
    else:
      print('Não existe produtos cadastrados')


class ControllerVenda:
  def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
    x = DaoEstoque.ler()
    temp = []
    existe = False
    quantidade = False
    
    for i in x:
      if existe == False:
        if i.produto.nome == nomeProduto:
          existe = True
          if i.quantidade >= quantidadeVendida:
            quantidade = True
            i.quantidade = int(i.quantidade) - int(quantidadeVendida)

            vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

            valorCompra = int(i.produto.preco) * int(quantidadeVendida)

            DaoVenda.salvar(vendido)
      temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

    arq = open('estoque.txt', 'w')
    arq.write('')

    for i in temp:
      with open('estoque.txt', 'a') as arq:
        arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria + '|' + str(i[1]))
        arq.writelines('\n')
      
    if existe == False:
      print('O produto não existe')
      return None
    elif not quantidade:
      print('A quantidade vendida não contém em estoque')
      return None
    else:
      print('Compra efetivada com sucesso')
      return valorCompra

  def relatorioProdutos(self):
    vendas = DaoVenda.ler()
    produtos = []
    if len(vendas) > 0:
      for i in vendas:
        nome = i.itensVendido.nome
        quantidade = i.quantidadeVendida
        tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
        if len(tamanho) > 0:
          produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade) } if (x['produto'] == nome) else(x), produtos))
        else:
          produtos.append({'produto': nome, 'quantidade': int(quantidade)})
    else:
      print('não existe vendas')

    ordenado = sorted(produtos, key = lambda k: k['quantidade'], reverse = True )

    print('Esse é o relatório ordenado por quantidade')
    a = 1
    for i in ordenado:
      print(f'=====Produto [{a}]=====')
      print(f'produto: {i["produto"]}')
      print(f'quantidade: {i["quantidade"]}\n')
      a += 1

  def mostrarVenda(self, dataInicio, dataFim):
    vendas = DaoVenda.ler()
    dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
    dataFim1 = datetime.strptime(dataFim, '%d/%m/%Y')

    vendasSelecionadas = filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataFim1, vendas)
    
    cont = 1
    total = 0
    for i in vendasSelecionadas:
      print(f'=========={cont}==========')
      print(f'Nome: {i.itensVendido.nome} \n'
            f'Categoria: {i.itensVendido.categoria} \n'
            f'Data: {i.data}'
            f'Quantidade: {i.quantidadeVendida}'
            f'Comprador: {i.comprador}'
            f'Vendedor: {i.vendedor}')
      total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
      cont += 1
    print(f'Total vendido: {total}')

class ControllerFornecedor:
  def cadastrarFornecedor(nome, cnpj, telefone, categoria):
    x = DaoFornecedor.ler()
    listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
    listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
    if len(listaCnpj) > 0:
      print('CNPJ já cadastrado')
    elif len(listaTelefone) > 0:
      print('Telefone já cadastrado')
    else:
      if len(cnpj) == 14 and len(telefone) >= 11:
        DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
        print('Fornecedor Cadastrado com Sucesso!')
      else:
        print('Digite um CNPJ ou telefone válido')
    
  def removerFornecedor(nomeRemover):
    x = DaoFornecedor.ler()
    forn = list(filter(lambda x: x.nome == nomeRemover, x))

    if len(forn) <= 0:
      print(f'Fornecedor {x} não existe!')
    else:
      for i in range(len(x)):
        if x[i].nome == nomeRemover:
          del x[i]
          break
      print('Fornecedor removido com sucesso!')

      with open('fornecedor.txt', 'w') as arq:
        for i in x:
          arq.writelines(i.nome + '|' + i.cnpj +'|' + i.telefone + '|' + i.categoria) 
          arq.writelines('\n')
  
  def alterarFornecedor( nomeAlterar, nomeAlterado, cnpjAlterado, telefoneAlterado, categoriaAlterado):
    x = DaoFornecedor.ler()
    forn = list(filter(lambda x: x.nome == nomeAlterar, x))

    if len(forn) > 0:
      forn1 = list(filter(lambda x: x.nome == nomeAlterado, x))
      if len(forn1) == 0:
        x = list(map(lambda x: Fornecedor(nomeAlterado, cnpjAlterado, telefoneAlterado, categoriaAlterado) if (x.nome == nomeAlterar) else(x), x))
        print('Fornecedor alterado com Sucesso!')
      else:
        print('Fornecedor que dejesa alterar já existe')
    else:
      print('Fornecedor que deseja alterar não existe')

    with open('fornecedor.txt', 'w') as arq:
      for i in x:
        arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.telefone + '|' + i.categoria)
        arq.writelines('\n')

a = ControllerFornecedor
# a.alterarFornecedor('Caio Adauri', 'Caio Haritov', '12345678987654', '98765432112', 'Carnes')
# a.removerFornecedor('Caio')
# a.cadastrarFornecedor('Caio', '12345678912347', '12345678908', 'Frutas')


# a = ControllerEstoque()
# a.cadastrarProduto('Maça', '15', 'Frutas', 30)
      
# a = ControllerVenda()
# a.cadastrarVenda('Maça', 'Caio', 'Caio Adauri', 6)

# a = ControllerVenda()
# a.relatorioProdutos()
# a.mostrarVenda('17/01/2024', '18/01/2024')




