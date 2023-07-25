def fact(x):
    if x < 0:
        return None
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

if __name__ == '__main__':
    print(fact(8))
    print(fact(5))
    print(fact(4))
    print(fact(0))
    print(fact(-1))