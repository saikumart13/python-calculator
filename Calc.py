import re

print("My calculaor")
print("Enter 'quit' to exit \n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation :")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("Bye")
        run = False
    else:
        equation = re.sub('a-zA-Z', '', equation)

        if previous == 0:
            previous = eval(equation)
            print(previous)
        else:
            previous = eval(str(previous) + equation)
            print(previous)


while run:
    perform_math()