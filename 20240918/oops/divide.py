class MyException(ZeroDivisionError):
    pass

def find_quotient(d, n):
    if n == 0:
        raise MyException()
    return d/ n

def find_quotient(d, n):
    if n == 0:
        raise ZeroDivisionError()
    return d / n
try:
    number = int(input("Enter a number: "))
    result = find_quotient(10,number)
except (ValueError):
    print("Invalid input! Please enter valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print(result)
finally:
    print('Cleaning up')
print('End of program')