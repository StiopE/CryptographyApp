import customtkinter as ctk

# function to decrypt
def decrypt():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    root2 = ctk.CTk()
    root2.title("Decrypt Menu")
    
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
    
    #
    decrypt_label2() = ctk.CTkLabel(root2, text="Decryption")
    
    
    method.decrypt()
    
    root2.mainloop()

    