def print_operation_table(operation, num_rows:int=6, num_columns:int=6) -> list:
    return list([[operation(x, y) for y in range(1, num_columns + 1)] for x in range(1, num_rows + 1)])

func = lambda x, y: x * y
res = print_operation_table(func)
for i in range(len(res)):
    [print(str(res[i][j]).ljust(3), end='') for j in range(len(res[i]))]
    print()