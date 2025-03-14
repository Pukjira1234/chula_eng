import tkinter as tk
from tkinter import font

# Thai consonants dictionary
thai_consonants = [
    ("ก", "กอ ไก่"), ("ข", "ขอ ไข่"), ("ค", "คอ ควาย"), ("ง", "งอ งู"),
    ("จ", "จอ จาน"), ("ฉ", "ฉอ ฉิ่ง"), ("ช", "ชอ ช้าง"), ("ซ", "ซอ โซ่"),
    ("ญ", "ญอ หญิง"), ("ฎ", "ฎอ ชฎา"), ("ฏ", "ฏอ ปฏัก"), ("ฐ", "ฐอ ฐาน"),
    ("ท", "ทอ ทหาร"), ("พ", "พอ พาน"), ("ม", "มอ ม้า"), ("ร", "รอ เรือ"),
    ("ล", "ลอ ลิง"), ("ว", "วอ แหวน"), ("ส", "สอ เสือ"), ("ห", "หอ หีบ")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.index = 0
        self.showing_name = False
        
        self.custom_font = font.Font(size=40, weight="bold")
        self.label = tk.Label(root, text=thai_consonants[self.index][0], font=self.custom_font, pady=50)
        self.label.pack()
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()
        
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_card)
        self.prev_button.pack(side=tk.LEFT, padx=20)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=20)
    
    def flip_card(self):
        if self.showing_name:
            self.label.config(text=thai_consonants[self.index][0])
        else:
            self.label.config(text=thai_consonants[self.index][1])
        self.showing_name = not self.showing_name
    
    def next_card(self):
        self.index = (self.index + 1) % len(thai_consonants)
        self.showing_name = False
        self.label.config(text=thai_consonants[self.index][0])
    
    def prev_card(self):
        self.index = (self.index - 1) % len(thai_consonants)
        self.showing_name = False
        self.label.config(text=thai_consonants[self.index][0])

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
