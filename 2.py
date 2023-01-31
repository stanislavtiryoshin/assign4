def forward_difference_table(x, y):
    table = [[] for _ in range(len(x))]
    table[0] = y
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            table[i].append(table[i - 1][j + 1] - table[i - 1][j])
    return table


def print_table(x, table):
    print("x".ljust(7), "y".ljust(7), "d^1".ljust(7), "d^2".ljust(7), "d^3".ljust(7), "d^4".ljust(7))
    for i in range(len(x)):
        for j in range(i + 1):
            if j == 0:
                print(str(x[i]).ljust(5), end="\t")
            print(str(round(table[j][i - j], 2)).ljust(5), end="\t")
        print()


def delta_three_f(x, table, value):
    h = x[1] - x[0]
    n = len(x) - 1
    delta_three_f = table[3][n - 3] / (6 * h ** 3)
    delta_three_f_value = delta_three_f * (value - x[n - 3]) ** 3
    return delta_three_f_value


x = [0, 1, 2, 3, 4]
y = [1.0, 1.5, 2.2, 3.1, 4.6]
table = forward_difference_table(x, y)
print_table(x, table)
print()
print("delta^3f(2) = ", delta_three_f(x, table, 2))