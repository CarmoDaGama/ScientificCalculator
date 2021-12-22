operators = '^*/+-'


def get_list_expression(expression):
    global operators
    expression_list = []
    member = ''
    for character in expression:
        if character in operators:
            if member.isnumeric():
                expression_list.append(member)
                expression_list.append(character)
            member = ''
        else:
            if character.isnumeric():
                member += character

    if member.isnumeric():
        expression_list.append(member)

    return expression_list


def calc(number1, number2, operator):
    if operator == '^':
        return number1**number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    elif operator == '+':
        return number1 + number2


def calculate_expression(expression):
    expressions = get_list_expression(expression)
    for operator in operators:
        count = len(expressions) - 1
       # print(type(operator))
        while operator in expressions:
            if operator == expressions[count] and expressions[count - 1].isnumeric() and expressions[count + 1].isnumeric():
                number1 = float(expressions[count - 1])
                number2 = float(expressions[count + 1])
                result = calc(number1, number2, operator)
                expressions.pop(count - 1)
                expressions.pop(count)
                if len(expressions) > count + 1:
                    expressions.pop(count + 1)
                expressions.insert(0, result)
                count -= 2
            else:
                count -= 1


expression = str(input('Type it Expression: '))

print(get_list_expression(expression))
print(f'Rseult: {calculate_expression(expression)}')