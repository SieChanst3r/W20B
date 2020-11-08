import dbcreds
import mariadb
import functions

while True:
    userSelection = input("Press 1 to Login\nPress 2 to Sign Up ")
    print()

    if userSelection == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print()
        user = functions.userLogin(username, password)
        if user:
            while True:
                menuSelection = input("1. Post new Exploit\n2. Update Exploit\n3. See your own Exploits\n4. See other Hackers' Exploits\n5. EXIT ")
                print()
                if menuSelection == "1":
                    content = input("Please enter Exploit: ")
                    functions.postExploit(content, user)
                elif menuSelection == "2":
                    id = input("Please enter the Exploit Id you wish to update: ")
                    updatedContent = input("Please updated your Exploit: ")
                    functions.updateExploit(updatedContent, id)
                elif menuSelection == "3":
                    functions.myExploits(user)
                elif menuSelection == "4":
                    functions.otherHackerExploits(user)
                elif menuSelection == "5":
                    functions.userLogout(user)
                    break
                else:
                    print("Please make a valid selection...")

    elif userSelection == "2":
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        if len(password) < 6:
            print("Password must be 6 characters or more")
        else:
            functions.userSignup(username,password)
    else:
        print("There was an error")
    break