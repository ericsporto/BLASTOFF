listaA = [1,2,3,4]
listaB = [1,2,5,8]
rep = 0
for num in listaA:
    if num in listaB:
        rep += 1
print(rep)