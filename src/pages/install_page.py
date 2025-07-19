import customtkinter as ctk
import time
from components.header import Header
from components.footer import Footer
from utils.installer import run_installation

class InstallPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        
        # Header
        Header(self, "Installation Progress").pack(fill="x", padx=20, pady=(10,5))
        
        # Content
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Status label
        self.status_label = ctk.CTkLabel(content, 
                                       text="Ready to begin installation...",
                                       font=("Arial", 12))
        self.status_label.pack(pady=20)
        
        # Progress bar
        self.progress = ctk.CTkProgressBar(content, 
                                         width=400,
                                         mode="determinate")
        self.progress.pack(pady=10)
        self.progress.set(0)
        
        # Install button
        self.install_btn = ctk.CTkButton(content, 
                                       text="Start Installation", 
                                       command=self.start_installation)
        self.install_btn.pack(pady=20)
        
        # Footer
        Footer(self, controller).pack(fill="x", padx=20, pady=(5,10))
    
    def start_installation(self):
        self.install_btn.configure(state="disabled")
        self.status_label.configure(text="Installing... Please wait")
        
        # Simulate installation progress
        for i in range(101):
            self.progress.set(i/100)
            self.update_idletasks()
            time.sleep(0.05)  # Simulate work
        
        self.status_label.configure(text="Installation completed successfully!")
        self.install_btn.configure(text="Finish", 
                                 command=self.master.quit,
                                 state="normal")