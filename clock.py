from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
import time

class B(Label):

    def met(self,text):
        self.text=time.ctime()


class A(App):

    def build(self):
        t=B()
        Clock.schedule_interval(t.met,1)
        return t

Window.clearcolor = (0, 1, 1, 1)

A().run()
