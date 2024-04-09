import tkinter as tk

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(self.root, text="Phone:")
        self.label_phone.grid(row=1, column=0, sticky="e")
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.grid(row=6, column=0, columnspan=2, pady=5)

    def insert_text(self, text):
        self.result_text.insert("1.0", text + "\n")

    def clear_text(self):
        self.result_text.delete("1.0", tk.END)

    def validate_phone(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            return False
        return True

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone and self.validate_phone(phone):
            contact = Contact(name, phone)
            self.contacts.append(contact)
            self.insert_text("Contact added successfully.")
        elif not name:
            self.insert_text("Name is required.")
        elif not phone:
            self.insert_text("Phone number is required.")
        else:
            self.insert_text("Invalid phone number. Please enter 10 digits only.")

        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

    def search_contact(self):
        self.clear_text()
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if not name and not phone:
            self.insert_text("Enter name or phone number to search.")
            return

        found_contacts = []
        for contact in self.contacts:
            if name.lower() == contact.name.lower() or phone == contact.phone:
                found_contacts.append(contact)

        if found_contacts:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone}" for contact in found_contacts])
            self.insert_text(f"Search Results:\n{contact_list}")
        else:
            self.insert_text("No matching contacts found.")

    def update_contact(self):
        self.clear_text()
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if not name:
            self.insert_text("Enter name of contact to update.")
            return

        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                if phone and self.validate_phone(phone):
                    contact.phone = phone
                    self.insert_text("Contact updated successfully.")
                    self.entry_name.delete(0, tk.END)
                    self.entry_phone.delete(0, tk.END)
                    return
                elif not phone:
                    self.insert_text("Phone number is required.")
                    return
                else:
                    self.insert_text("Invalid phone number. Please enter 10 digits only.")
                    return

        self.insert_text("Contact not found.")

    def view_contacts(self):
        self.clear_text()
        if self.contacts:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone}" for contact in self.contacts])
            self.insert_text(f"Contact List:\n{contact_list}")
        else:
            self.insert_text("Contact list is empty.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
