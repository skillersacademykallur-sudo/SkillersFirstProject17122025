
import auth_ash

def main():
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if auth_ash.check_username(user) and auth_ash.check_password(pwd):
        print("Login Successful")
    else:
        print("Login Failed")

if __name__ == "__main__":
    main()
