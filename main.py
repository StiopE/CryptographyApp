import customtkinter as ctk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import methods

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Root window
root = ctk.CTk()
root.title("Cryptography App")
root.geometry("600x400")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

menu_text = ctk.CTkLabel(root, text="Welcome to the Encryption App", font=("Helvetica", 20) )
menu_text.grid(row=0, column =2)
menu_text2 = ctk.CTkLabel(root, text="Would you like to Encrypt or Decrypt?", font=("Helvetica", 14))
menu_text2.grid(row=1, column =2)
    
# 2 Options, Encrypt of Decrypt
encryptOption = ctk.CTkButton(root, text="Encrypt", command=methods.encrypt)
encryptOption.grid(row=2, column=2)
decryptOption = ctk.CTkButton(root, text="Decrypt", command=methods.encrypt)
decryptOption.grid(row=3, column=2)



# user_string_input = ctk.CTkEntry(root, placeholder_text="Enter message to encrypt", height=50, width=200)
# user_string_input.pack(pady=10)


root.mainloop()