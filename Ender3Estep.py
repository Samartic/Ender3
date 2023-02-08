from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class EnderCalculator(App):
    def build(self):
        global count
        global new 
        global old
        count = 0
        self.greeting = Label(
                        text="Prêt à démarrer?",
                        font_size= 24,
                        color = 'c5c5c5'
                        )
        self.remain = TextInput(
                        multiline=False,
                        padding_y = (10,10),
                        size_hint = (0.2, 0.3),
                        background_color = 'adadad'
                        )
        self.button = Button(
                        text="Oui!",
                        size_hint = (0.2,0.3),
                        background_color = '2b18ff'
                        )
        # generate windows
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.8)
        self.window.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="Logo.png"))
        self.window.add_widget(self.greeting)
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.remain)
        self.window.add_widget(self.button)
        
        #add widgets to window

        return self.window
    def callback(self, even):
        global count
        global r      
        
        count += 1
        match count:
            case 1:
                self.greeting.text = "Faites une marque a 120mm the la tête d'extrusion"
                self.button.text = "Ok!"
            case 2:
                self.greeting.text = "Allez dans 'control' \n puis 'temperature' et \najustez tel que recommandé"
                self.button.text = "Suite"  
            case 3:
                self.greeting.text = "Allez à control/move axis/extruder/move 10mm \net ajustez à 100mm"
                self.button.text = "Suite"
            case 4:           
                self.greeting.text = "Combien reste-t-il de milimètre entre l'extrudeur et la marque? "
                self.button.text = "Soumettre"
            case 5:
                try:
                    r = 120 - float(self.remain.text)
                    self.remain.text = ""
                    self.greeting.text = "Pour avoir l'ancienne valeur \naller à Pour avoir l'ancienne valeur:\n  ► Allez à 'control/motion/step/Estep' "
                    self.button.text = "Suite"
                except ValueError:
                    count = 100
                
            case 6:
                self.greeting.text = "Quel est la valeur 'E-step'? "
                self.button.text = "Soumettre"
                
            case 7:
                try:
                    old = float(self.remain.text)
                    self.remain.text = ""
                    new = old * 100 / r
                    self.greeting.text = f"La nouvelle valeur est {new:.4f}"
                    self.button.text = "Fin!"
                except ValueError:
                    count = 200
                
            case 8:
                count = 0
                self.greeting.text = "On recommance?"
                self.button.text = "Recommencer"
            
            case 100:
                self.greeting.text = "Ce n'est pas un chiffre"
                self.button.text = "Ok !"
            case 101:
                count = 4
            case 200:
                self.greeting.text = "Ce n'est pas un chiffre"
                self.button.text = "Ok !"
            case 201:
                count = 6
            case _:
                self.greeting.text = "Prêt à démarré ?"
                self.button.text = "Oui!"
                

if __name__ =="__main__":
    EnderCalculator().run()
