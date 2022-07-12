import random
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.graphics import *
from questions import update_dq

quiz_dq = update_dq
points = []
growing_number = [1,]
class quiz(Screen):
    def __init__(self,manager, **kwargs):
        super(quiz, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        with self.layBig.canvas:
            self.bbb = Rectangle(texture=Image(source="hd.jpg").texture, size=Window.size)
        question, answers = random.choice(list(quiz_dq.items()))
        quiz_dq.pop(question)
        self.answers_list = answers.split("*")
        self.correct_answer = self.answers_list[0]
        len_of_q = len(question)
        if len_of_q >= 20:
            len_of_q = len_of_q//2
            half_question =question[0:len_of_q]
            second_half_question = question[len_of_q::]
            self.label_first_row = Label(text=half_question, pos_hint=({"x": 0.2, "y": 0.6}), font_size=(34), size_hint=(0.6, 0.6),color=(3, 9, 7,))
            self.label_second_row = Label(text=second_half_question, pos_hint=({"x": 0.2, "y": 0.47}), font_size=(34),size_hint=(0.6, 0.6), color=(3, 9, 7,))
            self.layBig.add_widget(self.label_first_row)
            self.layBig.add_widget(self.label_second_row)
        elif len_of_q < 20:
            self.label = Label(text=question, pos_hint=({"x": 0.2, "y": 0.5}), font_size=(38), size_hint=(0.6, 0.6),color=(3, 9, 7,))
            self.layBig.add_widget(self.label)
        self.option1 = random.choice(self.answers_list)
        self.answers_list.remove(self.option1)
        self.option2 = random.choice(self.answers_list)
        self.answers_list.remove(self.option2)
        self.option3 = random.choice(self.answers_list)
        self.answers_list.remove(self.option3)
        self.option4 = random.choice(self.answers_list)
        self.answers_list.remove(self.option4)
        self.option1_btn = Button(text=self.option1, size_hint=(0.5, 0.07), pos_hint=({'x':0.25, 'y':0.60}),font_size=(40), on_press=self.switch_screen1)
        self.option2_btn = Button(text=self.option2, size_hint=(0.5, 0.07), pos_hint=({'x':0.25, 'y':0.45}),font_size=(40), on_press=self.switch_screen2)
        self.option3_btn = Button(text=self.option3, size_hint=(0.5, 0.07), pos_hint=({'x':0.25, 'y':0.30}),font_size=(40), on_press=self.switch_screen3)
        self.option4_btn = Button(text=self.option4, size_hint=(0.5, 0.07), pos_hint=({'x':0.25, 'y':0.15}),font_size=(40), on_press=self.switch_screen4)
        self.layBig.add_widget(self.option1_btn)
        self.layBig.add_widget(self.option2_btn)
        self.layBig.add_widget(self.option3_btn)
        self.layBig.add_widget(self.option4_btn)
        Window.bind(on_resize=self.redraw_after_resize)
        self.add_widget(self.layBig)

    def switch_screen1(self, instance):
        self.num_of_btn = 1
        self.switch_screen(self)
    def switch_screen2(self, instance):
        self.num_of_btn = 2
        self.switch_screen(self)
    def switch_screen3(self, instance):
        self.num_of_btn = 3
        self.switch_screen(self)
    def switch_screen4(self, instance):
        self.num_of_btn = 4
        self.switch_screen(self)

    def redraw_after_resize(self, window, width, height):
        self.bbb.size = Window.size
    def switch_screen(self, instance):
        u = 0
        growing_number.append(1)

        growing_number_str = str(len(growing_number))
        if self.num_of_btn == 1:
            if self.option1_btn.text == self.correct_answer:
                u = 1
        elif self.num_of_btn == 2:
            if self.option2_btn.text == self.correct_answer:
                u = 1
        elif self.num_of_btn == 3:
            if self.option3_btn.text == self.correct_answer:
                u = 1
        elif self.num_of_btn == 4:
            if self.option4_btn.text == self.correct_answer:
                u = 1
        if u == 1:
            points.append(1)
        if len(growing_number) == 11:
            growing_number.clear()
            growing_number.append(1)
            self.manager.current = 'username'
        else:
            self.manager.current = 'questions_'+ growing_number_str