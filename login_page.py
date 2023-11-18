def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login Successful")
    else:
        print("Invalid username or password. Try again.")

users = {"user1": "password1", "user2": "password2", "user3": "password3"}
if __name__ == "__main__":
    login()

    