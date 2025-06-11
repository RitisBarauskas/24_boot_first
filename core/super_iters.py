from random import shuffle


def magic_printer(count=10):
    for item in range(count):
        print(f'Magic #{item}')


def print_hello(
        names: list = None,
        exclude_names: list = None,
        is_random: bool = False,
):
    if names is None:
        names = ['24 bootcamp']

    if exclude_names is None:
        exclude_names = []

    if is_random:
        shuffle(names)

    for name in names:
        if name in exclude_names:
            print(f'Name {name} was excluded')
            continue

        print(f'Hello, {name}!')
