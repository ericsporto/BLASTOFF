# considerando os dados como letras, coloquei-os entre colchetes
# para o Python aceitá-los mas levei em consideração os dados como números.

n1 = "a"
n2 = "b"
n3 = "c"
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f"O menor valor digitado foi {menor}.")