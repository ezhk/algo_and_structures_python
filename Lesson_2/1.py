"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

import inspect


def _wrong_sumbol(value):
    """
    Return True if user input not allowed symbol.
    """
    return value not in ('0', '-', '+', '*', '/')


def _is_exit(value):
    """
    Check that user want to exit from program.
    """
    if value == '0':
        return True
    return False


def _is_possible_operation(a, op, b):
    """
    Check that operation is possible,
      e.g. we cannot div to zero.
    """
    if op == '/' and float(b) == 0.0:
        return False
    return True


def process_operation():
    """
    Function run in while cycle
    calculate arithmetic operations.
    """

    while True:
        op = input("Input operation or 0 for exit: ")
        if _is_exit(op):
            print("See you later")
            break
        if _wrong_sumbol(op):
            print("You input wrong symbol, try again...")
            continue

        a = input("Input left operand: ")
        b = input("Input right operand: ")

        if not _is_possible_operation(a, op, b):
            print("Operation is not possible")
            continue
        print(f"{a} {op} {b} = {eval(a + op + b)}")


def process_operation_recursion():
    """
    Function equivalent process_operation,
    but recusrion was used.
    """

    print(f"Current recursion depth: {len(inspect.stack())}")

    op = input("Input operation or 0 for exit: ")
    if _is_exit(op):
        print("See you later")
        return

    if _wrong_sumbol(op):
        print("You input wrong symbol, try again...")
    else:
        a = input("Input left operand: ")
        b = input("Input right operand: ")

        if _is_possible_operation(a, op, b):
            print(f"{a} {op} {b} = {eval(a + op + b)}")
        else:
            print("Operation is not possbile")
    process_operation_recursion()


if __name__ == '__main__':
    process_operation()
    process_operation_recursion()
