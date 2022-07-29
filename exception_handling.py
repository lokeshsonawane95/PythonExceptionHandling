def division_by_zero_exception():
    """
    Function implements divide by zero exception handling
    :return: exception
    """
    try:
        print(5/0)
    except ZeroDivisionError as err:
        print(err)


def invalid_literal_exception():
    """
    Function implements type exception handling
    :return: exception
    """

    try:
        number = int(input("Enter an integer : "))
        print("Entered integer is : ", number)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    division_by_zero_exception()
    invalid_literal_exception()
