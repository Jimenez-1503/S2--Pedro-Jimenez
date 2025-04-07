# ============================
# Código Funcional Completo
# ============================

print("=== Verificador de idade ===")
idades = []

for i in range(2):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

for idade in idades:
    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolescente")
    else:
        print("Adulto")