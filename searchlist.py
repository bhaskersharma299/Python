import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        self.expression = ""
        self.create_ui()
    
    def create_ui(self):
        # Display
        display_font = font.Font(family="Arial", size=20, weight="bold")
        self.display = tk.Entry(self.root, font=display_font, borderwidth=2, 
                                relief=tk.SOLID, justify=tk.RIGHT)
        self.display.pack(pady=20, padx=20, fill=tk.BOTH, ipady=10)
        
        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        button_font = font.Font(family="Arial", size=14, weight="bold")
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]
        
        colors = {
            "=": "#51B455",
            "C": "#f44336",
            "/": "#FF9800",
            "*": "#FF9800",
            "-": "#FF9800",
            "+": "#FF9800"
        }
        
        for row in buttons:
            row_frame = tk.Frame(buttons_frame, bg="#F6F4F4")
            row_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            for btn_text in row:
                btn_color = colors.get(btn_text, "#e0e0e0")
                btn = tk.Button(row_frame, text=btn_text, font=button_font, 
                               bg=btn_color, fg="white" if btn_color != "#e0e0e0" else "black",
                               command=lambda x=btn_text: self.on_button_click(x))
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
