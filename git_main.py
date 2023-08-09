from random import randint as rnd

degree = int(input('Введите максимальную степень многочлена: '))

equation_pattern = {}
for key in range(degree, -1, -1):
    value = rnd(-100, 100)
    equation_pattern[key] = value

print(equation_pattern)

def decode_equation(equation: dict) -> str: # подсказка, какой тип данных возвращает метод
    new_equation = ''
    first = True
    for key, value in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'- {value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value} '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1 '
                    else:
                        new_equation += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        new_equation += f'- {abs(value)}*x '
                    elif key == 0:
                        new_equation += f'- {abs(value)} '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '




    return new_equation


equation = decode_equation(equation_pattern)


