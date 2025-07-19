import customtkinter as ctk
from components.header import Header
from components.footer import Footer

class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        Header(self, "Installation Settings").pack(fill="x", padx=20, pady=(10,5))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)

        settings_frame = ctk.CTkFrame(content)
        settings_frame.pack(fill="both", expand=True, pady=10)

        self.var1 = ctk.IntVar(value=1)
        cb1 = ctk.CTkCheckBox(settings_frame, 
                             text="Enable Basic Features",
                             variable=self.var1)
        cb1.pack(anchor="w", pady=5)
        
        self.var2 = ctk.IntVar()
        cb2 = ctk.CTkCheckBox(settings_frame, 
                             text="Enable Advanced Features",
                             variable=self.var2)
        cb2.pack(anchor="w", pady=5)
        
        self.var3 = ctk.IntVar(value=1)
        cb3 = ctk.CTkCheckBox(settings_frame, 
                             text="Create Desktop Shortcut",
                             variable=self.var3)
        cb3.pack(anchor="w", pady=5)

        btn_frame = ctk.CTkFrame(content, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        back_btn = ctk.CTkButton(btn_frame, 
                                text="← Back", 
                                command=lambda: controller.show_frame("WelcomePage"),
                                width=120)
        back_btn.pack(side="left", padx=10)
        
        next_btn = ctk.CTkButton(btn_frame, 
                                text="Next →", 
                                command=lambda: controller.show_frame("FunctionPage"),
                                width=120)
        next_btn.pack(side="left", padx=10)

        Footer(self, controller).pack(fill="x", padx=20, pady=(5,10))