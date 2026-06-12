def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":sub,
    "*":multi,
    "/":div
}


def calculator():

    should_acumulate=True
    num1=float(input("enter the first number?"))

    while should_acumulate:

        for symbol in operations:
            print(symbol)

        operational_symbol=input("pick a operation")
        num2=float(input("what is the next number?:"))

        # Calls the selected function from the dictionary
        answer=operations[operational_symbol](num1,num2)

        print(f"{num1} {operational_symbol} {num2} = {answer}")

        choice=input(f"type 'y' to continue calculating with {answer},or type 'n' to start a new caluculation")

        if choice=='y':
            # Uses the previous answer for the next calculation
            num1=answer
        else:
            should_acumulate=False
            print("\n" * 20)

            # Recursion: calculator() calls itself to start over
            calculator()
            return


# Starts the calculator program
calculator()