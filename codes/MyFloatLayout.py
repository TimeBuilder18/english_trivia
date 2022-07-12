from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import *




class MyFloatLayout(FloatLayout):
    def __init__(self,what_image, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(texture=Image(source=what_image).texture, size=Window.size)