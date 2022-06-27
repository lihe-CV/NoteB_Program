for i in range(1, 10):
    for j in range(1, i+1):
        result = i * j
        if i > j:
            print(i, '*', j, '=', result, ' ', end='')
        else:
            print(i, '*', j, '=', result, ' ')

print(pow(2, 2))