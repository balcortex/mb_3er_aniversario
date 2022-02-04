from typing import Sequence
import random


MUJERES = "lista_mujeres.txt"
HOMBRES = "lista_hombres.txt"


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def sample_winners(filename: str, k: int) -> str:
    lst = read_file(filename).split("\n")
    winners = random.sample(lst, k=k)

    for i, w in enumerate(winners, start=1):
        print(f"{i}. {w}")


if __name__ == "__main__":

    # print("\n * * * LISTA MUJERES * * *")
    # print(read_file(MUJERES))
    # print("\n * * * GANADORES MUJERES * * *")
    # sample_winners(MUJERES, k=2)
    # print()

    print("\n * * * LISTA HOMBRES * * *")
    print(read_file(HOMBRES))
    print("\n * * * GANADORES HOMBRES * * *")
    sample_winners(HOMBRES, k=7)
    print()
