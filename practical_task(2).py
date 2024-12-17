# Дополнительное практическое задание по модулю: "Основные операторы"
def generation(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i)+str(j)
    return result
n = int(input())
print(generation(n))