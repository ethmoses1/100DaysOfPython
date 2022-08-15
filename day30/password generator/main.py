from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_list =[]
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# -------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", "r") as data_files:
            #Reading old data
            data = json.load(data_files)
    except FileNotFoundError:
        messagebox.showinfo(title=f"{website.capitalize()}", message=f"File doesn't exist")
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website.capitalize()}", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title=f"{website.capitalize()}", message=f"Website: {website} does not exist")
    finally:
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password= password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    
    if not website or not password:
        messagebox.showwarning(title="Details error", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite: {website} \nEmail: {email} \nPassword: {password}")
        
        if is_ok:
            try:
                with open("data.json", "r") as data_files:
                    #Reading old data
                    data = json.load(data_files)

                    #updating old data with new data
            except FileNotFoundError:
                with open("data.json", "w") as data_files:
                    json.dump(new_data, data_files, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_files:
                    #saving updated data
                    json.dump(data, data_files, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)
window.mainloop()

