def main(str):
    try:
        c = cheking(str)
        if c < 1:
            raise ValueError('throws Exception //т.к. строка не является математической операцией')
        elif c > 1:
            raise ValueError('throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')
        lst = str.split()
        if len(lst) != 3:
            raise ValueError("throws Exception")

        try:
            n1 = int(lst[0])
            n2 = int(lst[2])
            if n1 not in range(1, 11) or n2 not in range(1, 11):
                raise ValueError("throws Exception")
        except ValueError:
            raise ValueError("throws Exception")

        operator = lst[1]

        if operator == '-':
            res = n1 - n2
        elif operator == '+':
            res = n1 + n2
        elif operator == '*':
            res = n1 * n2
        elif operator == '/':
            res = n1 // n2
        else:
            raise ValueError("throws Exception")

        print(res)

    except ValueError:
        print("throws Exception")


def cheking(str):
    operator_counter = 0
    for elem in str:
        if elem in ['+', '-', '*', '/']:
            operator_counter += 1
    return operator_counter


s = input()
main(s)