import kivy
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
import socket


class MySocket:
    def get_data(self, prefix):
        x = requests.get('http://127.0.0.1:5000/'+prefix)
        print(x.text)

class functions:
    def up(self):
        MySocket.get_data(MySocket, prefix="up")
        print("up")

    def down(self):
        MySocket.get_data(MySocket, prefix="down")
        print("down")

    def mute(self):
        MySocket.get_data(MySocket, prefix="mute")
        print("volumemute")

    def disconnect(self):
        MySocket.get_data(MySocket, prefix="disconnect")
        print("disconnect")


class TestApp(App):

    def build(self):
        up = Button(text='UP', background_color=[0.3, 0.3, 0.3, 1])
        down = Button(text='DOWN', background_color=[0.3, 0.3, 0.3, 1])
        mute = Button(text='MUTE TOGGLE', background_color=[0.3, 0.3, 0.3, 1])
        disconnect = Button(text='DISCONNECT', background_color=[0.3, 0.3, 0.3, 1])
        blayout = GridLayout(orientation='tb-lr', spacing=10, rows=2, cols=2, padding=10)
        up.bind(on_press=functions.up)
        down.bind(on_press=functions.down)
        mute.bind(on_press=functions.mute)
        disconnect.bind(on_press=functions.disconnect)
        blayout.add_widget(mute)
        blayout.add_widget(disconnect)
        blayout.add_widget(up)
        blayout.add_widget(down)
        return blayout


if __name__ == '__main__':
    TestApp().run()
