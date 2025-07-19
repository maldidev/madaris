import customtkinter as ctk

class Footer(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color="transparent")
        
        # Separator
        separator = ctk.CTkFrame(self, 
                                height=2, 
                                fg_color=("gray70", "gray30"))
        separator.pack(fill="x", pady=5)
        
        # Footer text
        label = ctk.CTkLabel(self, 
                            text="Madaris v1.0 • 2025",
                            font=("Arial", 10),
                            text_color=("gray50", "gray60"))
        label.pack(pady=5)