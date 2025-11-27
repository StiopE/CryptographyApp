import customtkinter as ctk
from cryptography.fernet import Fernet, InvalidToken
import main_window
import re
import logging

# Logging configurations
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Core logic
def core_decrypt_logic(key_str, ciphertext_str):
    # 1. DATA VALIDATION WITH REGEX
    fernet_pattern = r'^[A-Za-z0-9\-_=]+$'
    
    if not key_str or not ciphertext_str:
        logging.warning("Decryption failed: Empty input fields.")
        return False, "Error: Empty input fields."

    if not re.match(fernet_pattern, key_str):
        logging.warning(f"Decryption failed: Invalid Key Format. Input: {key_str[:5]}...") # Log only first 5 chars for safety
        return False, "Error: Key format is invalid (must be Base64)."

    # Error handling with try
    try:
        key_bytes = key_str.encode()
        cipher_bytes = ciphertext_str.encode()
        
        f = Fernet(key_bytes)
        decrypted_bytes = f.decrypt(cipher_bytes)
        
        logging.info("Decryption successful.")
        return True, decrypted_bytes.decode()
        
    except InvalidToken:
        logging.error("Decryption error: Invalid Token (Key does not match Ciphertext).")
        return False, "Error: Invalid Token (Wrong Key or Corrupted Data)."
    except ValueError as e:
        logging.error(f"Decryption error: Value Error - {e}")
        return False, "Error: Value Error (Encoding issue)."
    except Exception as e:
        logging.critical(f"Decryption error: Unexpected Exception - {e}")
        return False, f"Unknown Error: {str(e)}"

# Function to use the key and ciphertext
def decrypt(entry_password_widget, entry_decrypt_widget):
    # Get the values from the widgets passed to this function
    key = entry_password_widget.get().strip()
    ciphertext = entry_decrypt_widget.get().strip()

    success, result_text = core_decrypt_logic(key, ciphertext)
    
    # Create the results window
    root4 = ctk.CTk()
    root4.title = "Decryption Result"
    root4.geometry('400x200')
    
    # Configure grid
    indices = [0, 1, 2, 3, 4] 
    for i in indices:
        root4.grid_columnconfigure(i, weight=1)
        root4.grid_rowconfigure(i, weight=1)
    
    text_color = "black" if success else "red"
    
    final_decrypted_message = ctk.CTkLabel(root4, text=f'{result_text}', text_color=text_color, wraplength=350)
    final_decrypted_message.grid(row=0, column=2, pady=20)
    
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
    decrypt_label2 = ctk.CTkLabel(root2, text= "Decryption", font=header_font_style)
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