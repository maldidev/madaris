import customtkinter as ctk
from components.header import Header
from components.footer import Footer

class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        Header(self, "Welcome to Installer").pack(fill="x", padx=20, pady=(10,5))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)

        welcome_msg = """
        This installer will guide you through the installation process.
        
        Please click 'Next' to continue with the setup.
        """
        label = ctk.CTkLabel(content, 
                            text=welcome_msg,
                            font=("Arial", 12),
                            justify="left")
        label.pack(pady=20)

        next_btn = ctk.CTkButton(content, 
                               text="Next →", 
                               command=lambda: controller.show_frame("SettingsPage"),
                               width=120)
        next_btn.pack(pady=20)

        Footer(self, controller).pack(fill="x", padx=20, pady=(5,10))