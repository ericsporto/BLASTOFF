num = int(input("Digite um número: "))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")