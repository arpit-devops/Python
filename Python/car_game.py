command = ""

while True:
    command = input (">  ")
    if (command.lower() == "start"):
        print("you car is running")
    elif (command.lower() == "help"):
        print("""
        start - to start car
        stop - to stop car
        help 
        exit - to exit game
        """)
    elif (command.lower() == "stop"):
        print ("car is stopped")
    elif (command.lower() == "exit"):
        print("we are going to exit , thanks ")
        exit()
    else:
        print("wrong input please see help")

