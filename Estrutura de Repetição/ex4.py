populacaoA = 80000
populacaoB = 200000
anos = 0

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