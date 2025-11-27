import customtkinter as ctk
from cryptography.fernet import Fernet
import main_window
import json
import logging


# This creates or appends to the file "app.log"
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Core logic for pytest
def core_encrypt_logic(plain_text):
    # Pure function, that takes string input and returns key and ciphertext.
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(plain_text.encode())
    return key, encrypted_message

# Function  to copy the outputs
def copy_info(data_to_copy, root3_window):
    # Clear clipboard and add the new text (decoded to string)
    try:
        root3_window.clipboard_clear()
        text_data = data_to_copy if isinstance(data_to_copy, str) else data_to_copy.decode('utf-8')
        root3_window.clipboard_append(text_data) 
        root3_window.update()
        logging.info("User copied data to clipboard.")
    except Exception as e:
        logging.error(f"Clipboard copy failed: {e}")

# Function to encrypt the plaintext
def encrypt(entry_encrypt):
    # Generate key and ciphertext
    message_to_encrypt = entry_encrypt.get()
    key, encrypted_message = core_encrypt_logic(message_to_encrypt)
        
    # Store the result, Key and Ciphertext, using DICTIONARIES
    secure_data = {
        "ciphertext": encrypted_message.decode(),
        "key": key.decode()
    }   
    
    # Store it in a JSON file.
    try:
        with open('encryption_data.json', 'w') as json_file:
            json.dump(secure_data, json_file, indent=4)
        logging.info("Encryption successful: Data saved to encryption_data.json")
    except IOError as e:
        # Log the specific error
        logging.error(f"File I/O Error during encryption save: {e}")
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
    encrypted_message_label = ctk.CTkEntry(root3, placeholder_text=f'{encrypted_message}', state="readonly", width=1000)
    encrypted_message_label.grid(row=0, column=0, sticky='ew')
    encrypted_message_label.configure(state="normal")
    encrypted_message_label.insert(0, f'Encrypted Message: {encrypted_message}')
    encrypted_message_label.configure(state="readonly")
    
    # Buttons to copy outputs
    button_copy_msg = ctk.CTkButton(root3, text="Copy Ciphertext", command=lambda: copy_info(secure_data["ciphertext"], root3))
    button_copy_msg.grid(row=1, column=0, pady=5)
    
    # Buttons key settings
    encrypted_key_label = ctk.CTkEntry(root3, placeholder_text = f'{key}', state='readonly', width=1000)
    encrypted_key_label.grid(row=2, column=0, sticky='ew')
    encrypted_key_label.configure(state="normal")
    encrypted_key_label.insert(0, f'Key used to encrypt: {key}')
    encrypted_key_label.configure(state="readonly")
    
    # Buttons to copy key
    button_copy_key = ctk.CTkButton(root3, text="Copy Key", command=lambda: copy_info(secure_data["key"], root3))
    button_copy_key.grid(row=3, column=0, pady=5)
    
    root3.mainloop()

# Open encryptic window
def encrypt_window(previous_root):
    # Destroy previous window
    previous_root.destroy()            
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
    
    # Back Button (soft restart)
    back_button = ctk.CTkButton(root1, text="◀ Back", command=lambda: main_window.reset_and_go_to_main_menu(root1), width=100, fg_color="gray", hover_color="darkgray")
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    
    # Reset Button (full soft restart)
    reset_button = ctk.CTkButton(root1, text="⟲ Reset App", command=lambda: main_window.reset_and_go_to_main_menu(root1), width=120, fg_color="red", hover_color="#b30000")
    reset_button.grid(row=0, column=4, padx=10, pady=10, sticky="ne")
    
    # Store font setting in a TUPLE
    header_font_style = ("Helvetica", 20) 
    encrypt_label1 = ctk.CTkLabel(root1, text= "Encryption", font=header_font_style)
    encrypt_label1.grid(row = 1, column = 2, pady=(10, 20))
    
    label_message = ctk.CTkLabel(root1, text="Enter text to encrypt:")
    label_message.grid(row=2, column=1)
    
    entry_encrypt = ctk.CTkEntry(root1, placeholder_text="Enter message")
    entry_encrypt.grid(row = 2, column=3)
    
    submit_button = ctk.CTkButton(root1, text="Submit", command=lambda: encrypt(entry_encrypt))
    submit_button.grid(row=4, column=2, pady=(30, 0))
    
    root1.mainloop()