"""
30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.
"""

import copy

dict={"Bruno": 13, "Marco": 20, "Gustavo": 17, "Tales": 15, "Joao": 12}

dict2 = {}

dict2 = copy.deepcopy(dict)

print(dict2)
