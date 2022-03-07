# File: main.py
from kivy.app import App
class ClockApp(App):
    pass
if __name__ == '__main__':
    ClockApp().run()
    
# File: clock.kv
BoxLayout:
    orientation: 'vertical'
    Label:
        text: '00:00:00'
rom kivy.core.text import LabelBase
LabelBase.register(name='Roboto',
    fn_regular='Roboto-Thin.ttf',
    fn_bold='Roboto-Medium.ttf')

# In clock.kv
Label:
    text: '00:00:00'
    font_name: 'Roboto'
    font_size: 60
      
      
Label:
    text: '[b]00[/b]:00:00'
    markup: True
      
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex('#101216')

#make the clock tick
Label:
    id: time
      
def on_start(self):
    Clock.schedule_interval(self.update_time, 1)
    
# In main.py
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
class ClockLayout(BoxLayout):
   time_prop = ObjectProperty(None)
    
ClockLayout:
    time_prop: time
    Label:
        id: time
          
BoxLayout:
    orientation: 'vertical'
    Label:
        id: time
        text: '[b]00[/b]:00:00'
        font_name: 'Roboto'
        font_size: 60
        markup: True
    BoxLayout:
        height: 90
        orientation: 'horizontal'
        padding: 20
        spacing: 20
        size_hint: (1, None)
        Button:
            text: 'Start'
            font_name: 'Roboto'
            font_size: 25
            bold: True
        Button:
            text: 'Reset'
            font_name: 'Roboto'
            font_size: 25
            bold: True
    Label:
        id: stopwatch
        text: '00:00.[size=40]00[/size]'
        font_name: 'Roboto'
        font_size: 60
        markup: True
          
RobotoButton:
    text: 'Start'
