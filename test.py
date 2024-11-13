import customtkinter as ctk
from datetime import datetime
import os

# Set appearance mode to dark
ctk.set_appearance_mode("dark")  # You can also set "light" mode here
# Manually define your custom colors
PRIMARY_COLOR = "#1a1a2e"  # Dark blue
SECONDARY_COLOR = "#e94560"  # Pinkish red
TEXT_COLOR_USER = "#eee"  # White text for user
TEXT_COLOR_AI = "#eee"  # Dark blue text for AI
BACKGROUND_COLOR = "#23272a"  # Dark background
BACKGROUND_COLOR_AI = "#00B096"

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Assistant Chat UI")
        self.geometry("600x500")
        self.resizable(True, True)  # Makes the window resizable

        # Scrollable chat frame
        self.chat_frame = ctk.CTkScrollableFrame(self, fg_color="#658C8B")
        self.chat_frame.pack(fill="both", expand=True, padx=10, pady=(10, 60))

        # Input frame and controls
        self.input_frame = ctk.CTkFrame(self, height=100, corner_radius=8, fg_color="#658C8B")
        self.input_frame.pack(fill="both", expand=True, side="bottom", padx=10, pady=10)

        # Replace CTkEntry with CTkTextbox for multi-line input
        self.input_field = ctk.CTkTextbox(self.input_frame, height=5, width=40, wrap="word", fg_color=BACKGROUND_COLOR, text_color=TEXT_COLOR_USER)
        self.input_field.pack(fill="both" ,side="left", padx=(10, 5), pady=10, expand=True)

        # Bind events for handling Shift+Enter and Enter
        self.input_field.bind("<Return>", lambda event: self.send_message())  # Enter sends the message
        self.input_field.bind("<Shift-Return>", lambda event: self.move_cursor_down())  # Shift+Enter moves the cursor down

        # Clear button
        #self.clear_button = ctk.CTkButton(self.input_frame, text="Clear", command=self.clear_input, fg_color=SECONDARY_COLOR, text_color=TEXT_COLOR_USER)
        #self.clear_button.pack(side="right", padx=(5, 10), pady=10)

        # Send button
        self.send_button = ctk.CTkButton(self.input_frame, text="Send", command=self.send_message, fg_color=SECONDARY_COLOR, text_color=TEXT_COLOR_USER)
        self.send_button.pack(side="right", padx=(5, 10), pady=10)

        # Load chat history (if available)
        self.load_chat_history()

    def send_message(self, event=None):
        message = self.input_field.get("1.0", 'end-1c').strip()  # Get the entire content of the Textbox
        if message:
            self.display_message(message, sender="user")
            self.input_field.delete("1.0", 'end')  # Clear the Textbox
            # Simulating AI response (replace with actual AI interaction)
            self.after(1000, lambda: self.display_message("This is an AI response.", sender="ai"))

    # def clear_input(self):
    #     self.input_field.delete("1.0", 'end')  # Clear the Textbox content

    def move_cursor_down(self):
        # Move the cursor to the next line without sending the message
        self.input_field.insert('insert', '\n')  # Insert a newline at the cursor position

    def display_message(self, message, sender="user"):
        # Determine message alignment and style based on sender
        if sender == "user":
            message_color = SECONDARY_COLOR  # Background color for user
            text_color = TEXT_COLOR_USER  # White text for user messages
            anchor = "e"
            padding = (self.chat_frame.winfo_width() // 2, 10)
        else:
            message_color = BACKGROUND_COLOR_AI  # Background color for AI
            text_color = TEXT_COLOR_AI  # Dark blue text for AI messages
            anchor = "w"
            padding = (10, self.chat_frame.winfo_width() // 2)

        # Message frame setup
        message_frame = ctk.CTkFrame(self.chat_frame, fg_color=message_color, corner_radius=10)
        message_label = ctk.CTkLabel(
            message_frame, text=message, anchor=anchor, wraplength=self.chat_frame.winfo_width() - 60,
            text_color=text_color
        )
        message_label.pack(padx=10, pady=5)

        # Place message in the chat frame with appropriate alignment
        message_frame.pack(pady=5, padx=padding, anchor=anchor)

        # Ensure the latest message is visible
        self.chat_frame.update_idletasks()
        self.chat_frame._parent_canvas.yview_moveto(1.0)

        # Save chat history
        self.save_chat_history(sender, message)

    def load_chat_history(self):
        # Load chat history from a file or database (if available)
        pass

    def save_chat_history(self, sender, message):
        # Save chat history to a file or database
        pass

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
