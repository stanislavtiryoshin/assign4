def forward_difference_table(x, y):
    table = [[] for _ in range(len(x))]
    table[0] = y
    for i in range(1, len(x)):
        for j in range(len(x) - i):
            table[i].append(table[i-1][j+1] - table[i-1][j])
    return table


def print_table(x, table):
    print("x\t\ty\t\t\tdifference")
    for i in range(len(x)):
        for j in range(i+1):
            if j == 0:
                print(x[i], end="\t\t")
            print(round(table[j][i-j], 2), end="\t\t")
        print()


x = [10, 20, 30, 40]
y = [1.1, 2.0, 4.4, 7.9]
table = forward_difference_table(x, y)
print_table(x, table)
