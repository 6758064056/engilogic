import tkinter as tk
import random


thai_consonants = [
    ("ก", "Gor Kai"),
    ("ข", "Kor Khai"),
    ("ฃ", "Kor Khuat"),
    ("ค", "Kor Khwai"),
    ("ฅ", "Kor Khon"),
    ("ฆ", "Kor Rakhang"),
    ("ง", "Ngor Ngu"),
    ("จ", "Jor Jan"),
    ("ฉ", "Chor Ching"),
    ("ช", "Chor Chang"),
    ("ซ", "Sor So"),
    ("ฌ", "Chor Cher"),
    ("ญ", "Yor Ying"),
    ("ฎ", "Dor Chada"),
    ("ฏ", "Tor Patak"),
    ("ฐ", "Thor Than"),
    ("ฑ", "Thor Montho"),
    ("ฒ", "Thor Phu-Thao"),
    ("ณ", "Nor Nen"),
    ("ด", "Dor Dek"),
    ("ต", "Tor Tao"),
    ("ถ", "Thor Thung"),
    ("ท", "Thor Thahan"),
    ("ธ", "Thor Thong"),
    ("น", "Nor Nu"),
    ("บ", "Bor Baimai"),
    ("ป", "Por Pla"),
    ("ผ", "Phor Phueng"),
    ("ฝ", "For Fa"),
    ("พ", "Phor Phan"),
    ("ฟ", "For Fan"),
    ("ภ", "Phor Samphao"),
    ("ม", "Mor Ma"),
    ("ย", "Yor Yak"),
    ("ร", "Ror Rua"),
    ("ล", "Lor Ling"),
    ("ว", "Wor Waen"),
    ("ศ", "Sor Sala"),
    ("ษ", "Sor Rue-Si"),
    ("ส", "Sor Suea"),
    ("ห", "Hor Hip"),
    ("ฬ", "Lor Chu-La"),
    ("อ", "Or Ang"),
    ("ฮ", "Hor Nok-Huk")
]



class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, borderwidth=3)
        self.card_frame.pack(expand=True)

        self.label = tk.Label(self.card_frame, text="", font=("Arial", 48), bg="white")
        self.label.pack(expand=True)

        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)

        self.current_card = None
        self.showing_name = False

        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.showing_name = False

    def flip_card(self, event):
        if self.showing_name:
            self.label.config(text=self.current_card[0])
        else:
            self.label.config(text=self.current_card[1])
        self.showing_name = not self.showing_name

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()