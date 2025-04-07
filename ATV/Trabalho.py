# ============================
# Código Funcional Completo
# ============================

print("=== Verificador de idade ===")
idades = []

for i in range(2):
    idade = int(input("Digite um número: "))
    idades.append(idade)

for idade in idades:
    if idade < 12:
        print("Adulto")
    elif idade < 18:
        print("Adolescente")
    else:
        print("Criança")