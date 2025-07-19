import customtkinter as ctk
from components.header import Header
from components.footer import Footer

class FunctionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        Header(self, "Custom Function").pack(fill="x", padx=20, pady=(10,5))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)

        label = ctk.CTkLabel(content, 
                            text="Enter your custom installation function below:",
                            font=("Arial", 12))
        label.pack(pady=(0,10))

        self.function_entry = ctk.CTkTextbox(content, 
                                           width=400, 
                                           height=150,
                                           font=("Consolas", 11))
        self.function_entry.pack(pady=10)
        self.function_entry.insert("1.0", "def install():\n    # Your installation code here")

        btn_frame = ctk.CTkFrame(content, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        back_btn = ctk.CTkButton(btn_frame, 
                                text="← Back", 
                                command=lambda: controller.show_frame("SettingsPage"),
                                width=120)
        back_btn.pack(side="left", padx=10)
        
        install_btn = ctk.CTkButton(btn_frame, 
                                   text="Install Now →", 
                                   command=lambda: controller.show_frame("InstallPage"),
                                   width=120)
        install_btn.pack(side="left", padx=10)

        Footer(self, controller).pack(fill="x", padx=20, pady=(5,10))