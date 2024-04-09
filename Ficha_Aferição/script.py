import json

def corrigir_dataset(dataset):
    pessoas_corrigidas = []
    for pessoa in dataset['pessoas']:
        pessoa_corrigida = {
            '_id': pessoa.get('BI') or pessoa.get('CC') or None,  # Usar BI ou CC como identificador, ou None se nenhum estiver presente
            'nome': pessoa['nome'],
            'idade': int(pessoa['idade']),
            'sexo': pessoa['sexo'],
            'morada': pessoa['morada'],
            'descricao': pessoa['descrição'],  # Corrigido para 'descricao'
            'profissao': pessoa['profissao'],
            'partido_politico': pessoa['partido_politico'],
            'religiao': pessoa.get('religiao'),  # Adicionar religião se presente
            'desportos': pessoa['desportos'],
            'animais': pessoa['animais'],
            'figura_publica_pt': pessoa['figura_publica_pt'],
            'marca_carro': pessoa['marca_carro'],
            'destinos_favoritos': pessoa['destinos_favoritos'],
            'atributos': pessoa['atributos']
        }
        pessoas_corrigidas.append(pessoa_corrigida)
    return pessoas_corrigidas

with open('datasets/dataset.json', 'r') as file:
    dataset = json.load(file)

pessoas_corrigidas = corrigir_dataset(dataset)

# Salvar as pessoas corrigidas em um novo arquivo JSON
with open('dataset_corrigido.json', 'w') as file:
    json.dump(pessoas_corrigidas, file, indent=2)

print("Dataset corrigido e salvo como 'dataset_corrigido.json'.")