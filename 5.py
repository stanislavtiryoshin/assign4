def forward_difference_table(x, y):
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
            print(str(round(table[j][i - j], 3)).ljust(5), end="\t")
        print()


x = [-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y = [2.6, 3.0, 3.4, 4.28, 7.08, 14.2, 29.0]
table = forward_difference_table(x, y)
print_table(x, table)

f_x_value1 = table[0][0] + table[1][0] * -0.4 + table[2][0] * (-0.4) ** 2 / 2 + table[3][0] * (-0.4) ** 3 / 6
f_x_value2 = table[0][6] + table[1][5] * 1.2 + table[2][4] * 1.2 ** 2 / 2 + table[3][3] * 1.2 ** 3 / 6

print()
print("f(-0.4):", f_x_value1)
print("f(1.2):", f_x_value2)