sexo = str(input("Digite seu sexo [M/F] ")).upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, tente novamente ")).upper()[0]
print(f"Certo seu sexo é {sexo}, aguarde que entraremos em contato.")