# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print("-" * 40)
print("VOGAIS NAS PALAVRAS".center(40))
print("-" * 40)

palavras = ("Python",
            "Java",
            "JavaScript",
            "Ruby",
            "Kotlin",
            "Typescript",
            "Dotnet",
            "Django",
            "SpringBoot",
            "Laravel")
for p in palavras:
    print(f"> Na palavra {p}: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=" ")
    print()
