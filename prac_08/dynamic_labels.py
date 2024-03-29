from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()