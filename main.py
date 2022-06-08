from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from random import shuffle
from time import sleep
from threading import Thread


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
        self.state = 0
        self.algo_name = None
        self.number = None
        self.duration = None
        self.array = []
        self.canvases = []
        self.positions = []
        self.sizes = []

    def render(self):
        if self.ids.algo_name.text == 'Choose Algorithm':
            return
        if self.ids.number_of_elements.text == 'Number of elements':
            return
        if self.ids.duration.text == 'Time Duration':
            return

        self.algo_name = self.ids.algo_name.text
        self.number = int(self.ids.number_of_elements.text)
        self.duration = float(self.ids.duration.text)
        self.array = [x+1 for x in range(self.number)]
        shuffle(self.array)

        width, height = Window.width - 50, Window.height - 120
        length = len(self.array)
        maximum = max(self.array)
        w, h = width / length, height / maximum
        for n, i in enumerate(self.array):
            with self.canvas:
                Color(1, 1, 1)
                self.canvases.append(Rectangle(size=(w, h*i),
                                               pos=(25 + (w * n), 25)))
                self.positions.append((25 + (w * n), 25))
                self.sizes.append((w, h*i))
        self.bind(pos=self.update_pos,
                  size=self.update_pos)

    def start(self):
        if self.ids.algo_name.text == 'Choose Algorithm':
            popup('Select algorithm', 20, 200)
            return
        if self.ids.number_of_elements.text == 'Number of elements':
            popup('Select Number of elements', 20, 290)
            return
        if self.ids.duration.text == 'Number of elements':
            popup('Select time duration', 20, 230)
            return
        if self.state == 1:
            popup('Reset before Starting again', 20, 300)
            return

        self.state = 1
        Thread(target=self.start_thread).start()

    def start_thread(self):
        print("Cool")

    def update_pos(self, t1=None, t2=None, t3=None):
        try:
            width, height = Window.width - 50, Window.height - 120
            length = len(self.array)
            maximum = max(self.array)
            w, h = width / length, height / maximum
            for n, i in enumerate(self.canvases):
                i.pos = (25 + (w * n), 25)
                i.size = (w, h*self.array[n])
        except ValueError:
            pass

    def reset(self):
        for i in self.canvases:
            i.pos = -10000, -10000
        self.state = 0
        self.algo_name = None
        self.number = None
        self.duration = None
        self.array = []
        self.canvases = []
        self.positions = []
        self.sizes = []
        self.ids.algo_name.text = 'Choose Algorithm'
        self.ids.number_of_elements.text = 'Number of elements'
        self.ids.duration.text = 'Time Duration'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class SAVApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return kv


if __name__ == '__main__':
    SAVApp().run()
