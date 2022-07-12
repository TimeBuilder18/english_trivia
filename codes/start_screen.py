from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, WipeTransition
from kivy.graphics import *


class start_screen(Screen):
    def __init__(self,manager, **kwargs):
        super(start_screen, self).__init__(**kwargs)

        self.layBig = FloatLayout()
        with self.layBig.canvas:
            self.bbb = Rectangle(texture=Image(source="hd.jpg").texture, size=Window.size)

        self.btn1 = Button(text="start quiz", size_hint=(0.5, 0.07), pos_hint=({'x': 0.25, 'y': 0.60}),font_size=(40),
                           on_press=self.start)
        self.btn_l = Button(text="Leader_Bord", size_hint=(0.5, 0.07), pos_hint=({'x': 0.25, 'y': 0.45}),font_size=(40),
                            on_press=self.Leader_Bord)
        self.btn2 = Button(text="exit", size_hint=(0.5, 0.07), pos_hint=({'x': 0.25, 'y': 0.30}),font_size=(40), on_press=self.end)
        self.label2 = Label(text="welcome!", pos_hint=({"x":0.01, "y":0.5}), font_size=(70), color=(7, 4, 6,),size_hint= (1,0.7))
        self.layBig.add_widget(self.btn1)
        self.layBig.add_widget(self.label2)
        self.layBig.add_widget(self.btn2)
        self.layBig.add_widget(self.btn_l)
        Window.bind(on_resize=self.redraw_after_resize)
        self.add_widget(self.layBig)
    def Leader_Bord(self, instance):
        self.manager.transition = WipeTransition()
        self.manager.current = 'leader_Bord'

    def redraw_after_resize(self, window, width, height):
        self.bbb.size = Window.size
    def start(self, instance):
        self.manager.transition = WipeTransition()
        self.manager.current = 'questions_1'

    def end(self, instance):
        exit()

