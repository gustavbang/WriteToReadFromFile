def print_menu(columnName):
    print("you are inspecting column: " + columnName + ", what would you like to examine?")
    print("1: Amount of observations")
    print("2: Amount of unique occurences")

keepRunning = True;

def action1():
    pass # put a function here

def action2():
    pass # blah blah

def action3():
    pass # and so on

def no_such_action():
    pass # print a message indicating there's no such action

def main():
    actions = {"1": action1, "2": action2, "3": action3}
    while True:
        print("What column name would you like to inspect?")
        column_name = input("Your selection: ")

        print_menu(column_name)
        selection = input("Your selection: ")
        if "quit" == selection:
            return
        toDo = actions.get(selection, no_such_action)
        toDo()

    if __name__ == "__main__":
        main()




fileReader = open("FL_insurance_sample.csv", "r")

thisList = fileReader.read().split(",")


main()

