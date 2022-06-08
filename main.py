from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    def algorithm(self, name):
        print(name)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class SAVApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return kv


if __name__ == '__main__':
    SAVApp().run()
