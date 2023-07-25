def times_tables(n):
    grid = ""
    for i in range(1, n + 1):
        grid += '\t'.join([str(x * i) for x in range(1, n + 1)]) + '\n'
    return grid

if __name__ == '__main__':
    print(times_tables(4))
    print(times_tables(7))