import customtkinter as ctk

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
    
    decrypt_label2 = ctk.CTkLabel(root2, text= "Decryption")
    decrypt_label2.grid(row = 0, column = 2)
    
    
    
    
    root2.mainloop()

def perform_decryption():
    pass



# Open encryptic window
def encrypt():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    root1 = ctk.CTk()
    root1.title("Encryption Menu")
    root1.geometry('600x400')
    
    
    #Adding padding system
    root1.grid_columnconfigure(0, weight=1)
    root1.grid_columnconfigure(1, weight=1)
    root1.grid_columnconfigure(2, weight=1)
    root1.grid_columnconfigure(3, weight=1)
    root1.grid_columnconfigure(4, weight=1)

    root1.grid_rowconfigure(0, weight=0)
    root1.grid_rowconfigure(1, weight=1)
    root1.grid_rowconfigure(2, weight=1)
    root1.grid_rowconfigure(3, weight=1)
    root1.grid_rowconfigure(4, weight=1)
    
    encrypt_label1 = ctk.CTkLabel(root1, text= "Encryption")
    encrypt_label1.grid(row = 0, column = 2)
    
    
    
    root1.mainloop()
    
    
    
    