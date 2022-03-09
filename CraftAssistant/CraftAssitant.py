# my take on a smart assistant
import time
import webbrowser
import datetime
import random

print("=====CraftAssistant=====")

# user name log in
name = str(input("What is your name?"))
if name == "will":
    print("Checking if that's your name")
    time.sleep(0.5)
    print("Welcome Back ")
else:
    print("Access Denied!")

while True:
    # a calculator
    if name == "will":
        Quest = input("What do you need " + name)

        if Quest == "help":
            print("====Help====\n"
                  "keepword = a word or sentence you can keep and come back to later\n"
                  " >what is my keepword = tells you your keep word(only works if you have a keep word)\n"
                  "how are you = a emotional response from craftyassistiant\n"
                  "money = places fake money into a fake account\n"
                  "jacob = tells you about jacob\n"
                  "jamie = tells you about jamie\n"
                  "stop = stops the program\n"
                  "random number = picks a random number between 1 and 100\n"
                  "calculator = a built in calculator (that can do multiplication,divide,subtract,addition\n"
                  "Web = use the set websites to access them\n"
                  " >whatweb = what you can look up on the web\n"
                  "Heads or Tails = plays a game of heads or tails\n"
                  "time = tells you the time\n"
                  "date = tells you the date\n"
                  )

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
                    num1 = float(input("Enter first number" + name, " :"))
                    num2 = float(input("Enter second number" + name, " :"))

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
        random_word_list = ["I'm felling ok " + name, "I'm having a strong connection to your wifi Sir " + name,
                            "I'm waiting for you to ask a question Sir " + name, "i'm felling nice today Sir " + name,
                            "i'm doing good Sir " + name]
        random_word = random.choice(random_word_list)
        print(random_word)

    # jacob who is Jacob.H
    if Quest == "jacob":
        print("Jacob.H is a ALPHA MALE,Air Cadet (CORPORAL) Gamer Boyfriend"
              "and a rubbish reborn police officer")

    # money and cash
    if Quest == "money":
        random_word_listM = ["£100 has been put into your account", "YOU HAVE WON £100,000!!",
                             "A shiny one pound sterling as been placed into account"]
        random_Monword = random.choice(random_word_listM)
        print(random_Monword)

    # keep word system saves a word or sentence if you want
    if Quest == "keepword":
        keepword = str(input("What word(s) do you want to keep " + name))
        print("Your keep word is " + keepword)
    if Quest == "what is my keepword":
        print("Your keep word is " + keepword, +name)

    # random number generator
    if Quest == "random number":
        import random

        x = random.randint(1, 100)
        print(x)

    if Quest == "whatweb":
        print("===WhatWeb===\n"
              "--USE THE COMMAND 'type' TO USE YOUR OWN WEBSITE URL (eg: youtube.com)--\n"
              "(then uses 'stop' to stop the command and return to main text bar.)\n"
              "==USE THE COMMAND 'presets' to look at the presets within CraftAssistant==\n"
              "-You can use\n"
              "google\n"
              "youtube\n"
              "wikipedia\n"
              "bing\n"
              "github\n")

    if Quest == "web":
        while True:
            web = input("What do you want to look up " +name)
            if web == "type":
                website = input("What website do you want to search " +name)
                print("searching")
                time.sleep(1.5)
                webbrowser.open_new_tab(website)
            if web == "help":
                print("Use the command 'stop' then use 'whatweb'")

            if web == "stop":
                break

            if web == "presets":
                print("google = google.com\n"
                      "youtube = youtube.com\n"
                      "wiki = wikiipedia.org\n"
                      "bing = bing.com\n"
                      "github = github.com\n")
                pre = input("What preset do you want")
                if pre == "google":
                    webbrowser.open_new_tab("google.com")
                if pre == "youtube":
                    webbrowser.open_new_tab("youtube.com")
                if pre == "wiki":
                    webbrowser.open_new_tab("wikipedia.org")
                if pre == "bing":
                    webbrowser.open_new_tab("bing.com")
                if pre == "github":
                    webbrowser.open_new_tab("github.com")
            if web == "stop":
                break

    if Quest == "jamie":
        print("He is")
        time.sleep(1)
        print("Seening what he is doing")
        time.sleep(1)
        print("-He is still trying to learn python-")

    if Quest == "egg":
        print("This is a easter egg. Nice Find!")

    if Quest == "heads or tails":
        random_coin_flip = ["Heads", "Tails"]
        random_Coin = random.choice(random_coin_flip)
        print(random_Coin)

    if Quest == "survival game":
        print("IN PROGRESS")

    if Quest == "date":
        tday = datetime.date.today()
        print(tday)

    if Quest == "time":
        t = datetime.datetime.now()
        print(t)

    if Quest == "stop":
        print("Ok sir have a good day " +name)
        break

