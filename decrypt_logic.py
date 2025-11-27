import customtkinter as ctk
from cryptography.fernet import Fernet
import main_window

# Function to use the key and ciphertext
def decrypt(entry_password_widget, entry_decrypt_widget):
    # Get the values from the widgets passed to this function
    key = entry_password_widget.get()
    ciphertext = entry_decrypt_widget.get()

    try:
        # Use the values ciphertext and key for decryption
        f = Fernet(key.encode())
        decrypted_bytes = f.decrypt(ciphertext.encode())
        decrypted_plaintext = decrypted_bytes.decode()
    except Exception as e:
        decrypted_plaintext = f"Error: Decryption failed. Check key and message. ({e})"
    
    # Create the results window
    root4 = ctk.CTk()
    root4.title = "Decrypted message"
    root4.geometry('200x200')
    
    # Configure grid
    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root4.grid_columnconfigure(i, weight=1)
        root4.grid_rowconfigure(i, weight=1)
    
    final_decrypted_message = ctk.CTkLabel(root4, text=f'Decrypted message: {decrypted_plaintext}')
    final_decrypted_message.grid(row=0, column=1)
    
    root4.mainloop()

# Open decryptic window
def decrypt_window(previous_root):
    # Destroy previous window
    previous_root.destroy()
    
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
    
    # Back button ( soft restart)
    back_button= ctk.CTkButton(root2, text="◀ Back",command=lambda: main_window.reset_and_go_to_main_menu(root2), width=100, fg_color="gray", hover_color="darkgray")
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    # Reset button (full soft restart)
    reset_button = ctk.CTkButton(root2, text="⟲ Reset App",command=lambda: main_window.reset_and_go_to_main_menu(root2), width=120, fg_color="red", hover_color="#b30000")
    reset_button.grid(row=0, column=4, padx=10, pady=10, sticky="ne")
    
    # Create buttons using TUPLE
    header_font_style = ("Helvetica", 20) 
    decrypt_label2 = ctk.CTkLabel(root2, text= "Encryption", font=header_font_style)
    decrypt_label2.grid(row = 1, column = 2, pady=(10, 20))
   
    label_message = ctk.CTkLabel(root2, text="Enter text to decrypt:")
    label_message.grid(row=2, column=1)
    
    entry_decrypt = ctk.CTkEntry(root2, placeholder_text="Enter message")
    entry_decrypt.grid(row = 2, column=3)
    
    label_password = ctk.CTkLabel(root2, text="Enter key:")
    label_password.grid(row=3, column=1)
    
    entry_password = ctk.CTkEntry(root2, placeholder_text="Enter key")
    entry_password.grid(row=3, column=3)
    
    submit_button = ctk.CTkButton(root2, text="Submit", command=lambda: decrypt(entry_password, entry_decrypt))
    submit_button.grid(row=4, column=2, pady=(30, 0))

    root2.mainloop()