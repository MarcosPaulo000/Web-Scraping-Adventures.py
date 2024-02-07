import requests
from bs4 import BeautifulSoup

item = str(input('Qual produto deseja buscar? '))
req = requests.get(f'https://lista.mercadolivre.com.br/{item}')
cont = req.content
site = BeautifulSoup(cont, 'html.parser')
produtos = site.findAll('div', attrs={'class', 'andes-card ui-search-result ui-search-result--core andes-card--flat '
                                               'andes-card--padding-16'})

for produto in produtos:
    
    # Nome do produto
    name = produto.find('h2', attrs={'class', 'ui-search-item__title'})

    # Link do produto
    link = produto.find('a',
                        attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

    print(name.text)
    print(link['href'])
    # Preço do produto
    price = produto.find('span', attrs={'aria-label', 'andes-money-amount ui-search-price__part '
                                                      'ui-search-price__part--medium '
                                                      'andes-money-amount--cents-superscript'})
    # Desconto do produto
    discount = produto.find('span', attrs={'class', 'ui-search-price__discount'})

    print(f'{price.text}', end=' ')
    if discount:
        print(discount.text)

    # Comparador de preços
    reference = price.text
    valor = reference.replace('R$', '')
    if ',' in valor:
        valor = valor.replace(',', '.')
    comp = float(valor)
    if produto == produtos[0]:
        cheapest = comp
        cheapname = name.text
        cheaplink = link['href']
    else:
        if comp < cheapest:
            cheapest = comp
            cheapname = name.text
            cheaplink = link['href']
    print('')
    print('-' * 30)
    print('')
print('O produto mais barato é: ')
print(cheapname)
print(f'Preço: R${cheapest}')
print(cheaplink)
