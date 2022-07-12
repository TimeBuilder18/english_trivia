from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, WipeTransition
from MyFloatLayout import FloatLayout
from quiz import points
from kivy.uix.label import Label
from firebase import F_DB
from kivy.graphics import *
from kivy.uix.image import Image
from kivy.core.window import Window
game_ended = False
class username(Screen):
    def __init__(self, manager, **kwargs):
        super(username, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        with self.layBig.canvas:
            self.bbb = Rectangle(texture=Image(source="hd.jpg").texture, size=Window.size)


        self.confirm_username_btn = Button(text="submit", size_hint=(0.5, 0.07),pos_hint=({"x":0.25,"y":0.2}), on_press=self.leaderbord,font_size=(40))
        self.back_to_home_btn = Button(text="home", size_hint=(0.3, 0.07), pos_hint=({"x": 0.6755, "y": 0.8955}),
                                           on_press=self.returen_home,font_size=(35))
        self.textinput_username = TextInput(text="",hint_text="enter user name here", multiline=False,pos_hint=({"x":0.25,"y":0.6}), size_hint=(0.5, 0.07),font_size=(20))
        self.layBig.add_widget(self.confirm_username_btn)
        self.layBig.add_widget(self.textinput_username)
        Window.bind(on_resize=self.redraw_after_resize)
        self.layBig.add_widget(self.back_to_home_btn)

        self.add_widget(self.layBig)

    def redraw_after_resize(self, window, width, height):
        self.bbb.size = Window.size
    def leaderbord(self, instance):
        users = []
        score = len(points)
        list_of_username = F_DB.child("users_score").get()
        for i in list_of_username.each():
            users.append(i.key())
        if self.textinput_username.text not in users:
            user_to_add = {self.textinput_username.text: score}
            F_DB.child("users_score").update(user_to_add)
            points.clear()

        else:
            fire_base_old_score = F_DB.child("users_score").child(self.textinput_username.text).get()
            old_score = fire_base_old_score.val()
            new_score = old_score + score
            data = {self.textinput_username.text:new_score}
            F_DB.child("users_score").update(data)
            points.clear()
        self.manager.transition = WipeTransition()
        self.manager.current = 'open'
    def returen_home(self,instance):
        self.manager.transition = WipeTransition()
        self.manager.current = 'open'