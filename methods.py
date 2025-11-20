import customtkinter as ctk
from cryptography.fernet import Fernet

# Main menu function
def init_app():
    # System settings
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Root window
    root = ctk.CTk()
    root.title("Cryptography App")
    root.geometry("600x400")

    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root.grid_columnconfigure(i, weight=1)
        root.grid_rowconfigure(i, weight=1)

    menu_text = ctk.CTkLabel(root, text="Welcome to the Encryption App", font=("Helvetica", 20) )
    menu_text.grid(row=0, column =2)
    menu_text2 = ctk.CTkLabel(root, text="Would you like to Encrypt or Decrypt?", font=("Helvetica", 14))
    menu_text2.grid(row=1, column =2)
        
    # 2 Options, Encrypt of Decrypt
    encryptOption = ctk.CTkButton(root, text="Encrypt", command=encrypt_window)
    encryptOption.grid(row=2, column=2)
    decryptOption = ctk.CTkButton(root, text="Decrypt", command=decrypt_window)
    decryptOption.grid(row=3, column=2)

    # user_string_input = ctk.CTkEntry(root, placeholder_text="Enter message to encrypt", height=50, width=200)
    # user_string_input.pack(pady=10)

    root.mainloop()

# Open decryptic window
def decrypt_window():
    # Function to decrypt the ciphertext using the key
    def decrypt():
        # Making new window for decrypt
        root4 = ctk.CTk()
        root4.title="Decrypted message"
        root4.geometry('200x200')
        
        # Root window using LIST
        indices = [0, 1, 2, 3, 4] 
        for i in indices:
            root4.grid_columnconfigure(i, weight=1)
            root4.grid_rowconfigure(i, weight=1)
        
        # Make the key into bytes
        key = entry_password.get()
        ciphertext = entry_decrypt.get()
        
        f = Fernet(key.encode())
        
        # Decrypt ciphertext into bytes
        decrypted_bytes = f.decrypt(ciphertext.encode())
        
        # Plaintext decrypted_bytes
        decrypted_plaintext = decrypted_bytes.decode()
        
        final_decrypted_message = ctk.CTkLabel(root4, text=f'Decrypted message: {decrypted_plaintext}')
        final_decrypted_message.grid(row=0, column=1)
        
        root4.mainloop()
    
    # System settings 
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    # First window configuration
    root2 = ctk.CTk()
    root2.title("Decryption Menu")
    root2.geometry('600x400')
    
    # Adding padding system LIST
    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root2.grid_columnconfigure(i, weight=1)
        root2.grid_rowconfigure(i, weight=1)
    
    # Create buttons using TUPLE
    header_font_style = ("Helvetica", 20) 
    decrypt_label2 = ctk.CTkLabel(root2, text= "Encryption", font=header_font_style)
    decrypt_label2.grid(row = 0, column = 2)
   
    label_message = ctk.CTkLabel(root2, text="Enter text to decrypt:")
    label_message.grid(row=1, column=1)
    
    entry_decrypt = ctk.CTkEntry(root2, placeholder_text="Enter message")
    entry_decrypt.grid(row = 1, column=3)
    
    label_password = ctk.CTkLabel(root2, text="Enter key:")
    label_password.grid(row=2, column=1)
    
    entry_password = ctk.CTkEntry(root2, placeholder_text="Enter key")
    entry_password.grid(row=2, column=3)
    
    submit_button = ctk.CTkButton(root2, text="Submit", command=decrypt)
    submit_button.grid(row=4, column=2)
    
    root2.mainloop()


# Open encryptic window
def encrypt_window():
    # Function to encrypt the plaintext
    def encrypt():
        # Generate key and ciphertext
        message_to_encrypt = entry_encrypt.get()
        key = Fernet.generate_key()
        f = Fernet(key)
        
        encrypted_message = f.encrypt(message_to_encrypt.encode())      
        
        # Make a new window to not break the encrypt window
        root3 = ctk.CTk()
        root3.title("Ciphertext and Key")
        root3.geometry('1000x200')
        
        # Root window using LIST
        indices = [0, 1, 2, 3, 4] 
        for i in indices:
            root3.grid_columnconfigure(i, weight=1)
            root3.grid_rowconfigure(i, weight=1)
        
        # Buttons setting
        encrypted_message_label = ctk.CTkEntry(root3, placeholder_text=f'Encrypted Message: {encrypted_message}', state="readonly", width=1000)
        encrypted_message_label.grid(row=0, column=0, sticky='ew')
        
        encrypted_message_label.configure(state="normal")
        encrypted_message_label.insert(0, f'Encrypted Message: {encrypted_message}')
        encrypted_message_label.configure(state="readonly")
        
        encrypted_key_label = ctk.CTkEntry(root3, placeholder_text = f'Key used to encrypt: {key}', state='readonly', width=1000)
        encrypted_key_label.grid(row=2, column=0, sticky='ew')
        
        encrypted_key_label.configure(state="normal")
        encrypted_key_label.insert(0, f'Key used to encrypt: {key}')
        encrypted_key_label.configure(state="readonly")
        
        warning_message_label = ctk.CTkLabel(root3, text="Copy the key to ensure decryption")
        warning_message_label.grid(row=3, column=0)
        
        root3.mainloop()
    
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
    
    submit_button = ctk.CTkButton(root1, text="Submit", command = encrypt)
    submit_button.grid(row=3, column=2)
    
    root1.mainloop()