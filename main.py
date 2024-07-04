class Main:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, text):
        if text == None:
            self.text = ''
        else:
            self.text = text

class Second(Main):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number


obj_1 = Main("Hello")
print(f"Main text: {obj_1.text}")

obj_1.set_text("Hi")
print(f"Main text after setting new text: {obj_1.text}")

obj_2 = Second("Hello", 42)
print(f"Second text: {obj_2.text}, number: {obj_2.number}")

obj_2.set_text("Sushi")
obj_2.set_number(777)
print(f"Second update text: {obj_2.text}, update number: {obj_2.number}")