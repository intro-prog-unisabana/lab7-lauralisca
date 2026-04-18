from password_manager import add_login, change_password, encrypt_passwords_in_file

def main() -> None:
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()
        if option == "1":
            print("Enter the website and the new password:")
            data = input().split()
            if len(data)< 2:
                print("Input is in the wrong format!")
                continue
            website, password = data
            if len(password) <12 :
                print("Password is too short!")
                continue
            result = change_password(filename, website, password)
            if not result:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")
        elif option == "2":
            print("Enter the website, username, and password:")
            data = input().split()
            if len(data) < 3:
                print("Input is in the wrong format!")
                continue
            





if __name__ == "__main__":
    main()
