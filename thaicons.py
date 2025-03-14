import tkinter as tk
from tkinter import font

# Thai consonants dictionary
thai_consonants = [
    ("ก", "Ko Kai (Chicken)"), ("ข", "Kho Khai (Egg)"), ("ค", "Kho Khwai (Buffalo)"), ("ง", "Ngo Ngu (Snake)"),
    ("จ", "Cho Chan (Plate)"), ("ฉ", "Cho Ching (Cymbals)"), ("ช", "Cho Chang (Elephant)"), ("ซ", "So So (Chain)"),
    ("ฌ", "Cho Choe (Tree)"), ("ญ", "Yo Ying (Woman)"), ("ฎ", "Do Chada (Headdress)"), ("ฏ", "To Patak (Goad)"),
    ("ฐ", "Tho Than (Base)"), ("ฑ", "Tho Montho (Character Montho)"), ("ฒ", "Tho Phuthao (Elder)"), ("ณ", "No Nen (Novice monk)"),
    ("ด", "Do Dek (Child)"), ("ต", "To Tao (Turtle)"), ("ถ", "Tho Thung (Bag)"), ("ท", "Tho Thahan (Soldier)"),
    ("ธ", "Tho Thong (Flag)"), ("น", "No Nu (Mouse)"), ("บ", "Bo Baimai (Leaf)"), ("ป", "Po Pla (Fish)"),
    ("ผ", "Pho Phueng (Bee)"), ("ฝ", "Fo Fa (Lid)"), ("พ", "Pho Phan (Tray)"), ("ฟ", "Fo Fan (Teeth)"),
    ("ภ", "Pho Samphao (Sailboat)"), ("ม", "Mo Ma (Horse)"), ("ย", "Yo Yak (Giant)"), ("ร", "Ro Ruea (Boat)"),
    ("ล", "Lo Ling (Monkey)"), ("ว", "Wo Waen (Ring)"), ("ศ", "So Sala (Pavilion)"), ("ษ", "So Rue-si (Hermit)"),
    ("ส", "So Suea (Tiger)"), ("ห", "Ho Hip (Chest)"), ("ฬ", "Lo Chula (Kite)"), ("อ", "O Ang (Basin)"),
    ("ฮ", "Ho Nokhuk (Owl)")
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
