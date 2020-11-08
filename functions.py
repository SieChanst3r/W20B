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
