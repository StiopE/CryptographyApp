import customtkinter as ctk
from cryptography.fernet import Fernet
import encrypt_logic  as enc
import decrypt_logic as dec

def reset_and_go_to_main_menu(current_window):
    # Destroys the current window, and restart the main menu.
    if current_window:
        current_window.destroy()
    init_app()

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
    menu_text.grid(row=0, column =2, pady=(50, 5))
    menu_text2 = ctk.CTkLabel(root, text="Would you like to Encrypt or Decrypt?", font=("Helvetica", 14))
    menu_text2.grid(row=1, column =2, pady=(0, 20))
        
    # 2 Options, Encrypt of Decrypt
    encryptOption = ctk.CTkButton(root, text="Encrypt", command=lambda: enc.encrypt_window(root))
    encryptOption.grid(row=2, column=2, pady=10)
    decryptOption = ctk.CTkButton(root, text="Decrypt", command=lambda: dec.decrypt_window(root))
    decryptOption.grid(row=3, column=2, pady=10)
    
    exit_button = ctk.CTkButton(root, text="Exit", command=root.destroy,fg_color="red")
    exit_button.grid(row=4, column=2, pady=(20, 10))

    # user_string_input = ctk.CTkEntry(root, placeholder_text="Enter message to encrypt", height=50, width=200)
    # user_string_input.pack(pady=10)

    root.mainloop()