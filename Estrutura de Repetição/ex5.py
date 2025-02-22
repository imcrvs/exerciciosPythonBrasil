populacaoA = int(input("Digite a população da cidade A: "))
populacaoB = int(input("Digite a população da cidade B: "))
anos = 0

if populacaoA > populacaoB:
    print("A população da cidade A já é maior que da cidade B!")
elif populacaoA < populacaoB:
    while True:
        anos += 1
        populacaoA *= 1 + (3 / 100)
        populacaoB *= 1 + (1.5 / 100)
        if populacaoA >= populacaoB:
            print(
                f"\nDemorou {anos} anos para que a população de A ultrapassar ou igualar a de B.",
                f"\nA tem {populacaoA:.0f} habitantes e B tem {populacaoB:.0f}."
            )
            break