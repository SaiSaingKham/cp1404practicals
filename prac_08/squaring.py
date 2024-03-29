from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Constant for the app background color (in RGBA)
BG_COLOR = (0, 0, 0, 1)

class SquaringApp(App):
    def build(self):
        self.title = "Square Number"
        return Builder.load_file('squaring.kv')

    def handle_calculate(self, number):
        try:
            result = float(number) ** 2
            self.root.ids.output_label.text = f"{result:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "Please enter a valid number"

if __name__ == '__main__':
    SquaringApp().run()

