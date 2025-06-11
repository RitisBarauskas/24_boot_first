def magic_printer(count=10):
    for item in range(count):
        print(f'Magic #{item}')


def print_hello(names: list = None):
    if names is None:
        names = ['24 bootcamp']

    for name in names:
        print(f'Hello, {name}!')
