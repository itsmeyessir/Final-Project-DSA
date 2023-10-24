import pandas as pd
import os

# File paths
excel_file = 'books.xlsx'
csv_file = 'books.csv'
usercreds_csv_file = 'usercreds.csv'
usercreds_xlsx_file = 'usercreds.xlsx'

# Hash table to store username and password
user_credentials = {}

# Load existing user credentials from CSV
if os.path.exists(usercreds_csv_file):
    dfff = pd.read_csv(usercreds_csv_file)
    for index, row in dfff.iterrows():
        user_credentials[row['Username']] = row['Password']
        
# Load existing data from Excel and CSV
df = pd.read_excel(excel_file)
dff = pd.read_csv(csv_file)
dfff = pd.read_csv(usercreds_csv_file)
dffff = pd.read_excel(usercreds_xlsx_file)

def save_user_credentials():
    dfff = pd.DataFrame(user_credentials.items(), columns=['Username', 'Password'])
    dfff.to_csv(usercreds_csv_file, index=False)

def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_credentials[username] = password
    save_user_credentials()
    print("Sign-up successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    dff = dff.append({'Title': title, 'Author': author}, ignore_index=True)
    dff.to_csv(csv_file, index=False)
    print("Book added successfully!")
    
def select_book():
    title = input("Enter the title or ID of the book you want to select: ")
    
    # Try to convert the input to an integer (assuming it's an ID)
    try:
        book_id = int(title)
        if book_id < 1 or book_id > len(df):
            print("Invalid book ID.")
            return
        book_info = df.iloc[book_id - 1]
    except ValueError:
        # If it's not a valid integer, search by title
        book_info = df[df['Title'] == title]

    if book_info.empty:
        print("Book not found in the database.")
    else:
        print("Book Details:")
        print(book_info)

def delete_book():
    title = input("Enter the title of the book to delete: ")
    dff = dff[dff['Title'] != title]
    dff.to_csv(csv_file, index=False)
    print("Book deleted successfully!")

def save_to_excel():
    df.to_excel(excel_file, index=False)
    save_user_credentials()
    print("Data saved to Excel and user credentials saved to CSV successfully!")

def main():
    while True:
        print("\nOptions:")
        print("1. Sign up")
        print("2. Login")
        print("3. Add a book")
        print("4. Delete a book")
        print("5. Save data to Excel")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            if login():
                while True:
                    print("\nUser Options:")
                    print("1. Add a book")
                    print("2. Select a book")
                    print("3. Delete a book")
                    print("4. Save data to Excel")
                    print("5. Log out")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        add_book()
                    elif user_choice == '2':
                        select_book()
                    elif user_choice == '3':
                        delete_book()
                    elif user_choice == '4':
                        save_to_excel()
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("You need to login first.")
        elif choice == '4':
            print("You need to login first.")
        elif choice == '5':
            print("You need to login first.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()