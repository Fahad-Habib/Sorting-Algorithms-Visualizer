from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
from random import shuffle
from time import sleep
from threading import Thread


def popup(message, ft_size, x_size):
    Popup(title=message,
          title_size=ft_size,
          title_align='center',
          content=None,
          size_hint=(None, None),
          size=(x_size, 70)).open()


class MainWindow(Screen):
    def mergeSort(self):
        def merge(a, b):
            c = []
            n = len(a) + len(b)
            while len(c) != n:
                if len(a) == 0 and len(b) != 0:
                    c += b
                elif len(b) == 0 and len(a) != 0:
                    c += a
                else:
                    if b[0] < a[0]:
                        c.append(b[0])
                        b.remove(b[0])
                    else:
                        c.append(a[0])
                        a.remove(a[0])
            return c

        def sort(A):
            if len(A) == 1:
                return A
            else:
                return merge(sort(A[:len(A) // 2]), sort(A[len(A) // 2:]))

        self.array = sort(self.array)

    def quickSort(self):
        def sort(data_list, first, last):
            if first < last:
                split_point = partition(data_list, first, last)

                sort(data_list, first, split_point - 1)
                sort(data_list, split_point + 1, last)

        def partition(data_list, first, last):
            pivot_value = data_list[first]

            left_mark = first + 1
            right_mark = last

            done = False
            while not done:

                while left_mark <= right_mark and data_list[left_mark] <= pivot_value:
                    left_mark += 1

                while data_list[right_mark] >= pivot_value and right_mark >= left_mark:
                    right_mark -= 1

                if right_mark < left_mark:
                    done = True
                else:
                    data_list[left_mark], data_list[right_mark] = data_list[right_mark], data_list[left_mark]

            data_list[first], data_list[right_mark] = data_list[right_mark], data_list[first]

            return right_mark

        sort(self.array, 0, len(self.array) - 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def spinner(text, pos, values):
            return Spinner(text=text,
                           text_size=(self.width, None),
                           font_size=20,
                           halign='center',
                           background_normal='Assets/Photos/black.png',
                           background_down='Assets/Photos/white.png',
                           background_color=(1, 1, 1, 0.5),
                           size_hint=(None, None),
                           size=(Window.width / 4 - 20, 60),
                           pos=pos,
                           values=values)

        self.state = False
        self.in_progress = False
        self.done = False
        self.algo_name = None
        self.number = None
        self.duration = None
        self.array = []
        self.canvases = []
        self.positions = []
        self.sizes = []

        self.index_1 = None
        self.index_2 = None

        with self.canvas:
            Color(0, 0, 1)
            self.top_bar = Rectangle(size=(Window.width + 20, 70),
                                     pos=(-10, Window.height - 70))

        self.algo_spinner = spinner('Choose Algorithm', (5, Window.height - 65),
                                    ('Bubble Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort'))
        self.number_spinner = spinner('Number of elements', (Window.width / 4 + 5, Window.height - 65),
                                     ('50', '100', '1000'))
        self.time_spinner = spinner('Time Duration', (2 * (Window.width / 4) + 5, Window.height - 65),
                                    ('1ms', '10ms', '100ms', '0.25s', '0.5s', '0.75s', '1s'))

        self.start_btn = Button(text='Start',
                                text_size=(self.width, None),
                                font_size=20,
                                halign='center',
                                size_hint=(None, None),
                                background_normal='Assets/Photos/black.png',
                                background_down='Assets/Photos/white.png',
                                background_color=(1, 1, 1, 0.5),
                                size=(Window.width / 4 - 20, 60),
                                pos=(3 * (Window.width / 4) + 5, Window.height - 65))
        self.reset_btn = Button(text='Reset',
                                text_size=(self.width, None),
                                font_size=20,
                                halign='center',
                                size_hint=(None, None),
                                background_normal='Assets/Photos/black.png',
                                background_down='Assets/Photos/white.png',
                                background_color=(1, 1, 1, 0.5),
                                size=(Window.width / 4 - 20, 60),
                                pos=(-1000, -1000))

        self.start_btn.bind(on_release=self.start)
        self.reset_btn.bind(on_release=self.reset)
        self.algo_spinner.bind(text=self.render)
        self.number_spinner.bind(text=self.render)
        self.time_spinner.bind(text=self.render)

        self.add_widget(self.algo_spinner)
        self.add_widget(self.number_spinner)
        self.add_widget(self.time_spinner)
        self.add_widget(self.start_btn)
        self.add_widget(self.reset_btn)
        self.bind(pos=self.update_btns,
                  size=self.update_btns)

    def render(self, *args):
        if self.algo_spinner.text == 'Choose Algorithm' or self.number_spinner.text == 'Number of elements' or self.time_spinner.text == 'Time Duration':
            return
        if self.state:
            if self.number != int(self.number_spinner.text):
                for i in self.canvases:
                    self.canvas.remove(i)
                self.canvases = []
                self.positions = []
                self.sizes = []
            else:
                return

        times = {'1ms': 0.001, '10ms': 0.01, '100ms': 0.1, '0.25s': 0.25, '0.5s': 0.5}

        self.algo_name = self.algo_spinner.text
        self.number = int(self.number_spinner.text)
        self.duration = times[self.time_spinner.text]
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
        self.state = True
        self.bind(pos=self.update_bars,
                  size=self.update_bars)

    def start(self, *args):
        if self.algo_spinner.text == 'Choose Algorithm':
            popup('Select algorithm', 20, 200)
            return
        if self.number_spinner.text == 'Number of elements':
            popup('Select Number of elements', 20, 290)
            return
        if self.time_spinner.text == 'Number of elements':
            popup('Select time duration', 20, 230)
            return

        self.in_progress = True

        self.algo_spinner.pos = -1000, -1000
        self.number_spinner.pos = -1000, -1000
        self.time_spinner.pos = -1000, -1000
        self.start_btn.pos = -1000, -1000

        Thread(target=self.start_thread).start()

    def start_thread(self):
        if self.algo_name == 'Merge Sort':
            self.mergeSort()
        elif self.algo_name == 'Quick Sort':
            self.quickSort()
        self.update_bars()
        temp_rects = []
        for i in range(self.number):
            with self.canvas:
                Color(0, 1, 0)
                temp_rects.append(Rectangle(size=self.canvases[i].size, pos=self.canvases[i].pos))
            if self.number == 1000:
                if i % 10 == 0:
                    sleep(0.01)
            else:
                sleep(1 / self.number)
        for i in temp_rects:
            self.canvas.remove(i)
        self.update_bars()
        self.done = True
        self.update_btns()

    def update_bars(self, *args):
        if self.state:
            width, height = Window.width - 50, Window.height - 120
            length = len(self.array)
            maximum = max(self.array)
            w, h = width / length, height / maximum
            for n, i in enumerate(self.canvases):
                i.pos = (25 + (w * n), 25)
                i.size = (w, h*self.array[n])

    def update_btns(self, *args):
        w, h = Window.width, Window.height
        self.top_bar.size = (w + 20, 70)
        self.top_bar.pos = (-10, h - 70)

        if not self.in_progress:
            self.algo_spinner.pos = 5, h - 65
            self.algo_spinner.size = (w / 4 - 20, 60)
            self.algo_spinner.text_size = (w / 4 - 20, None)

            self.number_spinner.pos = (w / 4) + 5, h - 65
            self.number_spinner.size = (w / 4 - 20, 60)
            self.number_spinner.text_size = (w / 4 - 20, None)

            self.time_spinner.pos = 2 * (w / 4) + 5, h - 65
            self.time_spinner.size = (w / 4 - 20, 60)
            self.time_spinner.text_size = (w / 4 - 20, None)

            self.start_btn.pos = 3 * (w / 4) + 5, h - 65
            self.start_btn.size = (w / 4 - 20, 60)
            self.start_btn.text_size = (w / 4 - 20, None)

        if self.done:
            self.reset_btn.pos = (3 * (w / 8) + 10, h - 65)
            self.reset_btn.size = (w / 4 - 20, 60)
            self.reset_btn.text_size = (w / 4 - 20, None)
        else:
            self.reset_btn.pos = (-1000, -1000)

    def reset(self, *args):
        for i in self.canvases:
            self.canvas.remove(i)
        self.state = False
        self.in_progress = False
        self.done = False
        self.algo_name = None
        self.number = None
        self.duration = None
        self.array = []
        self.canvases = []
        self.positions = []
        self.sizes = []
        self.algo_spinner.text = 'Choose Algorithm'
        self.number_spinner.text = 'Number of elements'
        self.time_spinner.text = 'Time Duration'
        self.update_btns()


class WindowManager(ScreenManager):
    pass


class SAVApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(MainWindow(name="main"))
        return sm


if __name__ == '__main__':
    SAVApp().run()
