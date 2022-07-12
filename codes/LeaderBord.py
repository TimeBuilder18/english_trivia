from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,WipeTransition
from kivy.graphics import *
from kivy.uix.button import Button
from firebase import F_DB



class Leader_Bord(Screen):
    def __init__(self, manager, **kwargs):
        super(Leader_Bord, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        with self.layBig.canvas:
            self.bbb = Rectangle(texture=Image(source="ld.jpg").texture, size=Window.size)
        self.labels = []
        self.labels_score2 = []
        l_pos_X = 0.2
        l_pos_y = 0.5
        self.btn_exit = Button(text="exit", size_hint=(0.2, 0.07), pos_hint=({'x': 0.8, 'y': 0.001}),
                            on_press=self.exit_from_Leader_bord)

        Leader_Bord_lst = F_DB.child("users_score").get()
        d = dict()
        lst_k=[]
        lst_v=[]
        lst_k_2 = []
        i=0
        for user in Leader_Bord_lst.each():
            lst_k.append(user.key())
            lst_v.append(user.val())
        for vals in range(len(lst_v)):
            index_max=lst_v.index(max(lst_v))
            val = lst_v.pop(index_max)
            key=lst_k[index_max]
            lst_k.remove(lst_k[index_max])
            lst_k_2.append(key)
            d.update({key:val})

        for l_num in range(0,5):
            number = str(l_num+1)
            key_text = list(d)[l_num]
            val_te = list(d.values())[l_num]
            val_text = str(val_te)
            if l_num == 0:
                l_pos_X = 0.25
                l_pos_y = 0.45
            elif l_num == 1:
                l_pos_X = 0.47
                l_pos_y = 0.32
            elif l_num == 2:
                l_pos_X = 0
                l_pos_y = 0.32
            elif l_num == 3:
                l_pos_X = 0.6
                l_pos_y = 0.18
            elif l_num == 4:
                l_pos_X = -0.1
                l_pos_y = 0.18
            self.labels.append(Label(text = "#"+number +" "+ key_text+"  "+val_text,pos_hint = ({"x":l_pos_X,"y":l_pos_y}),font_size=(45),size_hint = (0.5,0.5)))
            self.layBig.add_widget(self.labels[l_num])
        Window.bind(on_resize=self.redraw_after_resize)
        self.layBig.add_widget(self.btn_exit)
        self.leader_bord_label = Label(text= "LeaderBord",pos_hint = ({"x":0.25,"y":0.8}),font_size=(60),size_hint=(0.5,0.2))
        self.layBig.add_widget(self.leader_bord_label)
        self.add_widget(self.layBig)

    def redraw_after_resize(self, window, width, height):
        self.bbb.size = Window.size
    def exit_from_Leader_bord(self,instance):
        self.manager.transition = WipeTransition()
        self.manager.current = 'open'