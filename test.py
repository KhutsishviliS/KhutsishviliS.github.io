import customtkinter as ctk
from tkinter import *

class StyledApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure the window
        self.title("Styled CustomTkinter App")
        self.geometry("400x500")
        
        # Create a container frame with padding (similar to CSS padding)
        self.container = ctk.CTkFrame(
            self,
            fg_color="#f0f0f0",  # Similar to CSS background-color
            corner_radius=10     # Similar to CSS border-radius
        )
        self.container.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Create a heading (similar to CSS text styling)
        self.heading = ctk.CTkLabel(
            self.container,
            text="Welcome Back",
            font=("Helvetica", 24, "bold"),  # Similar to CSS font properties
            text_color="#333333"             # Similar to CSS color
        )
        self.heading.pack(pady=20)
        
        # Create a styled input field (similar to CSS input styling)
        self.username = ctk.CTkEntry(
            self.container,
            width=300,
            height=40,
            placeholder_text="Username",
            corner_radius=5,
            border_width=2,
            border_color="#e1e1e1"
        )
        self.username.pack(pady=10)
        
        # Create a styled button (similar to CSS button styling)
        self.login_button = ctk.CTkButton(
            self.container,
            text="Login",
            width=300,
            height=40,
            corner_radius=5,
            fg_color="#007bff",     # Similar to CSS background-color
            hover_color="#0056b3",  # Similar to CSS :hover
            font=("Helvetica", 14)
        )
        self.login_button.pack(pady=10)
        
        # Create a styled link (similar to CSS <a> styling)
        self.forgot_password = ctk.CTkLabel(
            self.container,
            text="Forgot Password?",
            text_color="#007bff",
            font=("Helvetica", 12),
            cursor="hand2"  # Similar to CSS cursor: pointer
        )
        self.forgot_password.pack(pady=10)
        
        # Create a card-like frame (similar to CSS card components)
        self.card = ctk.CTkFrame(
            self.container,
            fg_color="white",
            corner_radius=10,
            border_width=1,
            border_color="#e1e1e1"
        )
        self.card.pack(pady=20, padx=20, fill="x")
        
        # Add content to the card
        self.card_title = ctk.CTkLabel(
            self.card,
            text="Need Help?",
            font=("Helvetica", 16, "bold"),
            text_color="#333333"
        )
        self.card_title.pack(pady=(15,5), padx=15)
        
        self.card_text = ctk.CTkLabel(
            self.card,
            text="Contact our support team\nfor assistance",
            font=("Helvetica", 12),
            text_color="#666666"
        )
        self.card_text.pack(pady=(0,15), padx=15)

if __name__ == "__main__":
    app = StyledApp()
    app.mainloop()