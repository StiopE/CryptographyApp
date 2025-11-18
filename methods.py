import customtkinter as ctk
from cryptography.fernet import Fernet

# Open decryptic window
def decrypt_window():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    root2 = ctk.CTk()
    root2.title("Decryption Menu")
    root2.geometry('600x400')
    
    # Adding padding system
    root2.grid_columnconfigure(0, weight=1)
    root2.grid_columnconfigure(1, weight=1)
    root2.grid_columnconfigure(2, weight=1)
    root2.grid_columnconfigure(3, weight=1)
    root2.grid_columnconfigure(4, weight=1)
    
    root2.grid_rowconfigure(0, weight=0)
    root2.grid_rowconfigure(1, weight=1)
    root2.grid_rowconfigure(2, weight=1)
    root2.grid_rowconfigure(3, weight=1)
    root2.grid_rowconfigure(4, weight=1)
    
    decrypt_label2 = ctk.CTkLabel(root2, text= "Decryption", font=("Helvetica", 20))
    decrypt_label2.grid(row = 0, column = 2)
   
    
    label_message = ctk.CTkLabel(root2, text="Enter text to decrypt:")
    label_message.grid(row=1, column=1)
    
    entry_decrypt = ctk.CTkEntry(root2, placeholder_text="Enter message")
    entry_decrypt.grid(row = 1, column=3)
    
    label_password = ctk.CTkLabel(root2, text="Enter password:")
    label_password.grid(row=2, column=1)
    
    entry_password = ctk.CTkEntry(root2, placeholder_text="Enter password")
    entry_password.grid(row=2, column=3)
    
    submit_button = ctk.CTkButton(root2, text="Submit")
    submit_button.grid(row=4, column=2)
    
    root2.mainloop()

# Do the decryption process
def perform_decryption(key, password):
    pass



# Open encryptic window
def encrypt_window():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    root1 = ctk.CTk()
    root1.title("Encryption Menu")
    root1.geometry('600x400')
    
    
    #Adding padding system
    root1.grid_columnconfigure(0, weight=1)
    root1.grid_columnconfigure(1, weight=0)
    root1.grid_columnconfigure(2, weight=0)
    root1.grid_columnconfigure(3, weight=1)
    root1.grid_columnconfigure(4, weight=1)

    root1.grid_rowconfigure(0, weight=1)
    root1.grid_rowconfigure(1, weight=1)
    root1.grid_rowconfigure(2, weight=1)
    root1.grid_rowconfigure(3, weight=1)
    root1.grid_rowconfigure(4, weight=1)
    
    encrypt_label1 = ctk.CTkLabel(root1, text= "Encryption", font=("Helvetica", 20))
    encrypt_label1.grid(row = 0, column = 2)
    
    
    label_message = ctk.CTkLabel(root1, text="Enter text to encrypt:")
    label_message.grid(row=1, column=1)
    
    entry_encrypt = ctk.CTkEntry(root1, placeholder_text="Enter message")
    entry_encrypt.grid(row = 1, column=3)
    
    
        
    
    
    
    
    submit_button = ctk.CTkButton(root1, text="Submit", command = encrypt)
    submit_button.grid(row=4, column=2)
    message_to_encrypt = entry_encrypt.get()
    
    
    
    
    root1.mainloop()

#Encrypt
def encrypt(message):
    f = Fernet.generate_key()
    
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message




    
    
    
    
    
    
    
    
    
    