def numbers(Number):
    result = ''

    for i in range(Number, 0, -1):
        for j in range(i, 0, -1):
            result = result + str(j) + ''
        result += "\n"

    return result

print(numbers(5))
