def forward_difference_table(x):
    y = [i ** 3 + 5 * i - 7 for i in x]
    table = [[] for _ in range(len(x))]
    table[0] = y
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            table[i].append(table[i - 1][j + 1] - table[i - 1][j])
    return table


def print_table(x, table):
    print("x".ljust(7), "y".ljust(7), "d^1".ljust(7), "d^2".ljust(7), "d^3".ljust(7), "d^4".ljust(7), "d^5".ljust(7),
          "d^6".ljust(7))
    for i in range(len(x)):
        for j in range(i + 1):
            if j == 0:
                print(str(x[i]).ljust(5), end="\t")
            print(str(table[j][i - j]).ljust(5), end="\t")
        print()


x = [-1, 0, 1, 2, 3, 4, 5]
table = forward_difference_table(x)
print_table(x, table)
print()
f_x_6 = table[0][6] + table[1][5] + table[2][4] + table[3][3] + table[4][2] + table[5][1] + table[6][0]
print("f(6):", f_x_6)
