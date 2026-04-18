from password_manager import add_login, change_password, encrypt_passwords_in_file

def main() -> None:
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()
        if option == "1":
            print("Enter the website and the new password:")



if __name__ == "__main__":
    main()
