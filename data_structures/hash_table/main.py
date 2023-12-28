# add checks for corner cases
from data_structures.hash_table.hash_table import HashTable


def main():
    hash_table = HashTable(10)

    hash_table.set('aidar', 27)
    hash_table.set('barys', 25)
    hash_table.set('kairat', 29)
    hash_table.set('kanat', 23)
    hash_table.set('aidos', 24)

    hash_table.set('aidos', 28)
    hash_table.set('aidar', 22)

    print(hash_table)


if __name__ == "__main__":
    main()
