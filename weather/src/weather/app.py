"""
This is a Hackathon app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Weather(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'How is the weather: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        output_box = toga.Box(style = Pack(direction=ROW, padding = 5))
        output = toga.TextInput(style = Pack(flex=1))
        output_label = toga.Label(
            'This is the weather: ',
            style = Pack(padding = (0, 5))
        )

        output_box.add(output_label)
        output_box.add(output)

        def say_weather(widget):
            output.value = 'The weather is ' + self.name_input.value
            

        button = toga.Button(
            'Show',
            on_press=say_weather,
            style=Pack(padding=5)
        )
        
        main_box.add(name_box)
        main_box.add(button)
        main_box.add(output_box)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    
        

def main():
    return Weather()
