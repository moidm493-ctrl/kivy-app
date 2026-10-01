from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.label = Label(text="Hello! This is a test app.", font_size='20sp')
        btn = Button(text="Click Here", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.label.text = "Success! The APK is working! 🎉"

if __name__ == '__main__':
    TestApp().run()
