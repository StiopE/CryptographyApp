import customtkinter as ctk
from cryptography.fernet import Fernet
import json

# Function  to copy the outputs
def copy_info(data_to_copy, root3_window):
    # Clear clipboard and add the new text (decoded to string)
    root3_window.clipboard_clear()
    root3_window.clipboard_append(data_to_copy.decode('utf-8')) 
    root3_window.update()

# Function to encrypt the plaintext
def encrypt(entry_encrypt):
    # Generate key and ciphertext
    message_to_encrypt = entry_encrypt.get()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message_to_encrypt.encode())  
        
    # Store the result, Key and Ciphertext, using DICTIONARIES
    secure_data = {
        "ciphertext": encrypted_message.decode(),
        "key": key.decode()
    }   
    
    # Store it in a JSON file.
    # Using 'w' mode will overwrite the file each time, which is what you wanted.
    try:
        with open('encryption_data.json', 'w') as json_file:
            json.dump(secure_data, json_file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
    
    # Make a new window to not break the encrypt window
    root3 = ctk.CTk()
    root3.title("Ciphertext and Key")
    root3.geometry('1000x200')
    
    # Root window using LIST
    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root3.grid_columnconfigure(i, weight=1)
        root3.grid_rowconfigure(i, weight=1)
    
    # Buttons message settings
    encrypted_message_label = ctk.CTkEntry(root3, placeholder_text=f'Encrypted Message: {encrypted_message}', state="readonly", width=1000)
    encrypted_message_label.grid(row=0, column=0, sticky='ew')

    encrypted_message_label.configure(state="normal")
    encrypted_message_label.insert(0, f'Encrypted Message: {encrypted_message}')
    encrypted_message_label.configure(state="readonly")
    
    # Buttons to copy outputs
    button_copy_msg = ctk.CTkButton(root3, text="Copy Ciphertext", command=lambda: copy_info(secure_data["ciphertext"], root3))
    button_copy_msg.grid(row=1, column=0, pady=5)
    
    # Buttons key settings
    encrypted_key_label = ctk.CTkEntry(root3, placeholder_text = f'Key used to encrypt: {key}', state='readonly', width=1000)
    encrypted_key_label.grid(row=2, column=0, sticky='ew')
    
    encrypted_key_label.configure(state="normal")
    encrypted_key_label.insert(0, f'Key used to encrypt: {key}')
    encrypted_key_label.configure(state="readonly")
    
    # Buttons to copy key
    button_copy_key = ctk.CTkButton(root3, text="Copy Key", command=lambda: copy_info(secure_data["key"], root3))
    button_copy_key.grid(row=3, column=0, pady=5)
    
    root3.mainloop()

# Open encryptic window
def encrypt_window():            
    # System settings
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    # First encryption window
    root1 = ctk.CTk()
    root1.title("Encryption Menu")
    root1.geometry('600x400')
    
    # Adding padding system with LIST
    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root1.grid_columnconfigure(i, weight=1)
        root1.grid_rowconfigure(i, weight=1)
    
    # Store font setting in a TUPLE
    header_font_style = ("Helvetica", 20) 
    encrypt_label1 = ctk.CTkLabel(root1, text= "Encryption", font=header_font_style)
    encrypt_label1.grid(row = 0, column = 2)
    
    label_message = ctk.CTkLabel(root1, text="Enter text to encrypt:")
    label_message.grid(row=1, column=1)
    
    entry_encrypt = ctk.CTkEntry(root1, placeholder_text="Enter message")
    entry_encrypt.grid(row = 1, column=3)
    
    submit_button = ctk.CTkButton(root1, text="Submit", command=lambda: encrypt(entry_encrypt))
    submit_button.grid(row=3, column=2)
    
    root1.mainloop()