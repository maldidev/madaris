import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, parent, title):
        ctk.CTkFrame.__init__(self, parent, fg_color="transparent")
        
        # Title label
        label = ctk.CTkLabel(self, 
                            text=title,
                            font=("Arial", 16, "bold"))
        label.pack(pady=10)
        
        # Separator
        separator = ctk.CTkFrame(self, 
                                height=2, 
                                fg_color=("gray70", "gray30"))
        separator.pack(fill="x")