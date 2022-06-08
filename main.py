from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


def popup(message, ft_size, x_size):
    pop = Popup(title=message,
                title_size=ft_size,
                title_align='center',
                content=None,
                size_hint=(None, None),
                size=(x_size, 70))
    pop.open()


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.algo_name = None
        self.number = None
        self.duration = None

    def algorithm(self, name):
        self.algo_name = name

    def number_of_elements(self, number):
        self.number = number

    def time_duration(self, duration):
        self.duration = duration

    def start(self):
        if self.algo_name is None:
            popup('Select algorithm', 20, 200)
            return
        if self.number is None:
            popup('Select Number of elements', 20, 290)
            return
        if self.duration is None:
            popup('Select time duration', 20, 230)
            return


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class SAVApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return kv


if __name__ == '__main__':
    SAVApp().run()
