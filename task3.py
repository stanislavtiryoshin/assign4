def forward_difference_table(x):
    y = [i ** 3 + i ** 2 - 2 * i + 1 for i in x]
    table = [[] for _ in range(len(x))]
    table[0] = y
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            table[i].append(table[i - 1][j + 1] - table[i - 1][j])
    return table


def print_table(x, table):
    print("x".ljust(7), "y".ljust(7), "d^1".ljust(7), "d^2".ljust(7), "d^3".ljust(7), "d^4".ljust(7), "d^5".ljust(7))
    for i in range(len(x)):
        for j in range(i + 1):
            if j == 0:
                print(str(x[i]).ljust(5), end="\t")
            print(str(table[j][i - j]).ljust(5), end="\t")
        print()


x = [0, 1, 2, 3, 4, 5]
table = forward_difference_table(x)
print_table(x, table)

print()
y_6 = table[0][5] + table[1][4] + table[2][3] + table[3][2] + table[4][1] + table[5][0]
print("y at x = 6:", y_6)
y_6_substitution = 6 ** 3 + 6 ** 2 - 2 * 6 + 1
print("y at x = 6 by substitution:", y_6_substitution)
