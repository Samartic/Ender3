
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField

class EnderCalculator(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        
        global count
        global new 
        global old
        count = 0
        self.greeting = MDLabel(
                        text="Prêt à démarrer?",
                        halign = "center",
                        pos_hint= {"center_x":0.5, "center_y":0.5},
                        font_size= 24,
                        )
        self.remain = MDTextField(
                        multiline=False,
                        padding_y = (10,10),
                        halign = "center",
                        pos_hint= {"center_x":0.5, "center_y":0.4},
                        size_hint = (0.2, 0.3),
                        opacity = 0,
                        )
        self.button = MDFillRoundFlatButton(
                        text="Oui!",
                        pos_hint= {"center_x":0.5, "center_y":0.2},
                        size_hint = (0.15,0.15),
                        )
        self.exit = MDFillRoundFlatButton(
                            text = "Quitter",
                            pos_hint= {"center_x":0.7, "center_y":0.2},
                            opacity = 0,
                            size_hint = (0.15,0.15),
                            )
        # generate windows
        screen = MDScreen()
        
        screen.add_widget(
                Image(source="Logo.png",
                pos_hint = {"center_x":0.5, "center_y":0.7},
                size_hint = (0.5,0.5)
                ))
        screen.add_widget(self.greeting)
        self.button.bind(on_press = self.callback)
        screen.add_widget(self.remain)
        screen.add_widget(self.button)
        self.exit.bind(on_press = self.on_stop)
        screen.add_widget(self.exit)
        
        #add widgets to window

        return screen
    def callback(self, even):
        global count
        global r      
        
        count += 1
        match count:
            case 1:
                self.greeting.text = "Faites une marque a 120mm the la tête d'extrusion"
                self.exit.opacity = 0
                self.button.text = "Ok!"
            case 2:
                self.greeting.text = "Allez dans 'control' \n puis 'temperature' et \najustez tel que recommandé"
                self.button.text = "Suite"  
            case 3:
                self.greeting.text = "Allez à 'control/move axis/extruder/move 10mm' \net ajustez à 100mm"
                self.button.text = "Suite"
            case 4:           
                self.greeting.text = "Combien reste-t-il de milimètre entre l'extrudeur et la marque? "
                self.remain.opacity = 1
                self.button.text = "Soumettre"
                
            case 5:
                try:
                    r = 120 - float(self.remain.text)
                    self.remain.text = ""
                    self.remain.opacity = 0
                    self.greeting.text = "Pour avoir l'ancienne valeur:\n  Allez à 'control/motion/step/Estep' "
                    self.button.text = "Suite"
                except (EOFError, ValueError):
                    count = 100
                
            case 6:
                self.greeting.text = "Quel est la valeur 'E-step'? "
                self.remain.opacity = 1
                self.button.text = "Soumettre"
                
            case 7:
                try:
                    old = float(self.remain.text)
                    self.remain.text = ""
                    self.remain.opacity = 0
                    new = old * 100 / r
                    self.greeting.text = f"La nouvelle valeur est {new:.4f}"
                    self.button.text = "Fin!"
                except (EOFError, ValueError):
                    count = 200
                
            case 8:
                count = 0
                self.greeting.text = "On recommance?"
                self.button.pos_hint = {"center_x":0.3}
                self.exit.opacity = 1
                self.button.text = "Recommencer"
            
            case 101:
                error = self.remain.text
                count = 3
                self.remain.text = ""
                self.greeting.text = f" '{error} ' n'est pas un chiffre\n Error {count}"
                count = 3
                self.button.text = "Ok !"
            case 201:
                self.greeting.text = f" '{error} ' n'est pas un chiffre\n Error {count}"
                count = 5
                self.button.text = "Ok !"

            case _:
                self.greeting.text = "..."
                self.exit.opacity = 0
                self.button.text = "Suite"
                

if __name__ =="__main__":
    EnderCalculator().run()
