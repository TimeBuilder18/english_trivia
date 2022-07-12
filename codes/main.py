from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from start_screen import start_screen
from quiz import quiz
from username import username
from LeaderBord import Leader_Bord
class etriv(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(start_screen(name="open", manager=sm))
        sm.add_widget(quiz(name='questions_1', manager=sm))
        sm.add_widget(quiz(name='questions_2', manager=sm))
        sm.add_widget(quiz(name='questions_3', manager=sm))
        sm.add_widget(quiz(name='questions_4', manager=sm))
        sm.add_widget(quiz(name='questions_5', manager=sm))
        sm.add_widget(quiz(name='questions_6', manager=sm))
        sm.add_widget(quiz(name='questions_7', manager=sm))
        sm.add_widget(quiz(name='questions_8', manager=sm))
        sm.add_widget(quiz(name='questions_9', manager=sm))
        sm.add_widget(quiz(name='questions_10', manager=sm))
        sm.add_widget(username(name='username', manager=sm))
        sm.add_widget(Leader_Bord(name='leader_Bord', manager=sm))
        return sm

if __name__ == '__main__':
    LayoutsExmp().run()