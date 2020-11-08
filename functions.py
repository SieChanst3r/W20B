import mariadb
import dbcreds

#User 
def userSignup():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()

        if len(password) < 6:
            print("Password entry must be 6 characters in length or more")
        else:
            cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?), [username, password])"
            conn.commit()

    except mariadb.ProgrammingError:
        print("Sorry, an error occurred to this HACKER")
    except mariadb.OperationalError:
        print("Connection error, Oops!")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

#LOGIN
def userLog(username, password):
    conn = None
    cursor = None 
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [username, password])
        users = cursor.fetchall()

        if cursor.rowcount == 1:
            for user in users:
                print("Login success!")
                print()
            return users[0]
        else:
            print("User Not Valid")
     except mariadb.ProgrammingError:
        print("Sorry hacker, an error occurred :/ ")
    except mariadb.OperationalError:
        print("Connection error, Oops!")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

#CREATE POST
def postExploit(content, user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO exploits(content, user_id) VALUES(?, ?)", [content, user[2]])
        conn.commit()

        if(cursor.rowcount == 1):
            print("Exploit successful!")
            print()
        else:
            print("Exploit failed..")

    except mariadb.ProgrammingError:
        print("There was an issue, hacker made an error..")
    except mariadb.OperationalError:
        print("The connection was lost..")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

#UPDATE
def updateExploit(updatedContent, id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("UPDATE exploits SET content = ?", [updatedContent, id])
        conn.commit()

        if(cursor.rowcount == 1):
            print("Exploit updated!")
            print()
        else:
            print("Oops, what happened?? It didn't work.")

    except mariadb.ProgrammingError:
        print("There was an issue, hacker made an error..")
    except mariadb.OperationalError:
        print("Oops, a connection error occurred.")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

#GET current USER Exploits
def userExploits(user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits e INNER JOIN hackers h ON e.user_id = h.id WHERE user_id = ?", [user[2], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("Alias: " + str(exploit[3]))
            print("Exploit Id: " + str(exploit[1]))
            print("Exploit: " + str(exploit[0]))
            print()

        if(cursor.rowcount == 0):
            print("Awe, something went wrong here :( ")

    except mariadb.ProgrammingError:
        print("There was an issue, hacker made an error..")
    except mariadb.OperationalError:
        print("Oops, a connection error occurred.")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

#AllExploits GET
def AllHackerExploits(user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits e INNER JOIN hackers h ON e.user_id = h.id WHERE user_id != ?", [user[2], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("Alias: " + str(exploit[3]))
            print("Exploit: " + str(exploit[0]))
            print()

    except mariadb.ProgrammingError:
        print("Sorry, a Hacker here made a programming error!")
    except mariadb.OperationalError:
        print("There was a connection error!")
    finally:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()


# USER LOGOUT
def userLogout(user):
    conn = None
    cursor = None
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    cursor.close()
    conn.rollback()
    conn.close()
    print("You're logged out!")

