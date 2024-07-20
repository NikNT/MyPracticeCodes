# Exception - Interrupts the flow of program 


try:
    number = int(input("Enter a number: "))
    print((1/number))
except ZeroDivisionError:
    print("You cannot divide by ZERO!")
except ValueError:
    print("Enter only numbers!")
except Exception as e:
    print("Something went wrong!", e)
finally:
    print("Execution completed!")