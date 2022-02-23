# my take on a smart assistant

print("=====CraftAssistant=====")

# user name log in
name = str(input("What is your name?"))
if name == "will":
    print("Welcome Back Sir!")
else:
    print("Access Denied!")

while True:
    # a calculator
    if name == "will":
        Quest = input("What do you need Sir?")

        if Quest == "help":
            print("====Help====\n"
                  "keepword = a word or sentence you can keep and come back to later\n"
                  " >what is my keepword = tells you your keep word(only works if you have a keep word)\n"
                  "how are you = a emotional response from craftyassistiant\n"
                  "money = places fake money into a fake account\n"
                  "jacob = tells you about jacob\n"
                  "stop = stops the program\n"
                  "random number = picks a random number between 1 and 100\n"
                  "calculator = a built in calculator (that can do multiplication,divide,subtract,addition\n"
                  "google = opens a new tab in google")

        if Quest == "calculator":

            def add(x, y):
                return x + y


            def subtract(x, y):
                return x - y


            def multiply(x, y):
                return x * y


            def divide(x, y):
                return x / y


            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                # take input from the user
                choice = input("Enter choice(1/2/3/4): ")

                # check if choice is one of the four options
                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    # check if user wants another calculation
                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                        break

                else:
                    print("Invalid Input")

    # random emotional response
    if Quest == "how are you":
        import random

        random_word_list = ["I'm felling ok Sir", "I'm having a strong connection to your wifi Sir",
                            "I'm waiting for you to ask a question Sir", "i'm felling nice today Sir",
                            "i'm doing good Sir"]
        random_word = random.choice(random_word_list)
        print(random_word)

    # jacob who is Jacob.H
    if Quest == "jacob":
        print("Jacob.H is a ALPHA MALE,Air Cadet (CORPORAL) Gamer Boyfriend"
              "and a rubbish reborn police officer")

    # money and cash
    if Quest == "money":
        import random

        random_word_listM = ["£100 has been put into your account", "YOU HAVE WON £100,000!!",
                             "A shiny one pound sterling as been placed into account"]
        random_Monword = random.choice(random_word_listM)
        print(random_Monword)

    # keep word system saves a word or sentence if you want
    if Quest == "keepword":
        keepword = str(input("What word(s) do you want to keep Sir?"))
        print("Your keep word is " + keepword)
    if Quest == "what is my keepword":
        print("Your keep word is " + keepword, "Sir")
    # random number generator
    if Quest == "random number":
        import random

        x = random.randint(1, 100)
        print(x)

    if Quest == "google":
        import webbrowser
        webbrowser.open_new_tab("google.com")

    if Quest == "stop":
        print("Ok sir have a good day")
        break
