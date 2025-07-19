import customtkinter as ctk
from PIL import Image
from pages.welcome_page import WelcomePage
from pages.settings_page import SettingsPage
from pages.function_page import FunctionPage
from pages.install_page import InstallPage

class InstallerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App configuration
        self.title("Madaris Installer")
        self.geometry("700x550")  # Slightly taller for logo
        
        # Load and display logo
        try:
            logo_image = ctk.CTkImage(
                light_image=Image.open("assets/logo.png"),
                size=(200, 60)  # Adjust size as needed
            )
            logo_label = ctk.CTkLabel(self, image=logo_image, text="")
            logo_label.pack(pady=(10, 0))
        except Exception as e:
            print(f"Couldn't load logo: {e}")
            # Fallback text logo
            logo_label = ctk.CTkLabel(self, text="Madaris", 
                                    font=("Arial", 24, "bold"))
            logo_label.pack(pady=(10, 0))
        
        # Container frame
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Page frames
        self.frames = {}
        
        for F in (WelcomePage, SettingsPage, FunctionPage, InstallPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("WelcomePage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = InstallerApp()
    app.mainloop()