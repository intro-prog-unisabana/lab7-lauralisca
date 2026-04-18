import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    
    with open(filename, "r") as f:
        password = f.read().strip()

    encrypted_password = caesar_encrypt(password)

    with open(filename, "w") as f:
        f.write(encrypted_password)

if __name__ == "__main__":
    encrypt_single_pass("examples/example1.txt")
    


def encrypt_passwords_in_file(filename: str) -> None:
    with open (filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print (row)

def encrypt_passwords_in_file(filename: str) -> None:
    rows = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                rows.append(row)
    for i in range(1, len(rows)):
        rows[i][2] = caesar_encrypt(rows[i][2])
    with open (filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
def change_password(filename: str, website: str, password: str) -> bool:
    rows = []
    found = False 
    with open(filename, "r") as file:
        reader = csv.reader(file)
        



def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
