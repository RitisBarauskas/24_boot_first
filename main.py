from core.super_iters import print_hello


def main():
    names = ['Alexandra', 'Nikita', 'Julya', 'Kristina', 'Ritis']
    print_hello(names=names, exclude_names=['Ritis'], is_random=True)


if __name__ == '__main__':
    main()
