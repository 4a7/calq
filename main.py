
import kivy
import webbrowser
kivy.require('1.1.3')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
posiciones_en_alfa={'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}
letras={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",18:"I",19:"J",20:"K",21:"L",22:"M",23:"N",24:"O",25:"P",26:"Q",27:"R",28:"S",29:"T",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}
numeroletra={'V': 22, 'L': 12, 'U': 21, 'P': 16, 'B': 2, 'H': 8, 'S': 19, 'N': 14, 'A': 1, 'Y': 25, 'W': 23, 'X': 24, 'I': 9, 'M': 13, 'K': 11, 'D': 4, 'C': 3, 'G': 7, 'F': 6, 'Z': 26, 'T': 20, 'O': 15, 'R': 18, 'Q': 17, 'E': 5, 'J': 10}
letrasformato={1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
#funciones para convertir de otra a 10




def deotraa10(tira,fuente):
    tira=tira.upper()
    lista=[]
    check=1
    tira=tira+"$"
    for i in range(len(tira)-1):
        
        if  tira[i+1]=="(" and tira[i].isalpha():
            num=""
            for j in range(i+2,len(tira)-1):
            
                if tira[j].isdigit():
                    num=num+tira[j]
                else:
                    break
            num=int(num)
            lista.append([tira[i],num])
            check=0
        elif tira[i]==")":
            check=1
        elif tira[i+1]==")" or tira[i]=="(" or check==0:
            pass
        elif tira[i]=="$":
            pass
        
        else:
            lista.append([tira[i],0])
    
    resultado=0
    
    lista.reverse()
    for i in range(len(lista)):
        if lista[i][0].isalpha():
            j=lista[i][0]
            
            w=((lista[i][1])*26)+9+posiciones_en_alfa[j]
            w=w*(int(fuente)**i)
        else:
            w=(int(lista[i][0]))*(int(fuente)**i)
        resultado=resultado+w
    resultado=str(resultado)
    
    return resultado  
        
    

            
        







#funciones para convertir de 10 a otra
def formato(num):#convierte a formato con techitos
    techitos=(num-9)//26
    digito=(num-9)-techitos*26
    if digito==0:
        digito=26
        techitos-=1
    
    retorno=letrasformato[digito]+"("+str(techitos)+")"#-foramto
    
    
    return retorno

def de10aotro(num,destino):#convierte de 10 a otras bases
    num=int(num)
    destino=int(destino)
    
    digitos=[]
    division=0
    while num>0:
        division=num%destino
        division=str(division)
        
        digitos.append(division)
        num=num//destino
    
    digitos.reverse()
    retorno=""
    
    for i in digitos:#une los valores de la lista, si el valor >9 entonces lo reemplaza por su letra
        
        if int(i)>9 and int(i)<=35:
            
            retorno=retorno+letras[int(i)]
            
        elif int(i)>35:
            
            retorno=retorno+formato(int(i))
            
        else:
            
            retorno=retorno+i
        
    return retorno
        
        

class MyApp(App):
# layout
    def build(self):
        --orientation 
        layout = BoxLayout(padding=10, orientation='vertical')
        
        btnayuda=Button(text="Ayuda",background_color=(0,0,1,1))
        layout.add_widget(btnayuda)
        btnconvertir = Button(text="Convertir")
        btnconvertir.bind(on_press=self.buttonClicked)
        btnayuda.bind(on_press=self.buttonURL)
        
        self.lblresultado = Label(text="...")
        #basefuente
        self.lblfuente = Label(text="Base fuente")
        layout.add_widget(self.lblfuente)
        self.basefuente = TextInput(text='', multiline=False)
        layout.add_widget(self.basefuente)
        #basedestino
        self.lbldestino = Label(text="Base destino")
        layout.add_widget(self.lbldestino)
        self.basedestino = TextInput(text='', multiline=False)
        layout.add_widget(self.basedestino)
        #numero
        self.lblnumero = Label(text="Numero")
        layout.add_widget(self.lblnumero)
        self.numero = TextInput(text='', multiline=False)
        layout.add_widget(self.numero)

        #convertir y resultado
        layout.add_widget(btnconvertir)
        
        layout.add_widget(self.lblresultado)
        return layout

# button click function
#si se pueden poner funciones de afuera dentro de buttonclicked, esas funciones estan fuera de la clase
    def buttonClicked(self,btn):
        fuente=self.basefuente.text#basefuente
        destino=self.basedestino.text#basedestino
        num=self.numero.text#el numero
        try:
            numres=deotraa10(num,fuente)
            
            numres2=de10aotro(numres,destino)
            
            self.lblresultado.text =numres2
            """
            if int(fuente)==10 and:#si la base fuente es 10
                
                self.lblresultado.text = de10aotro(num,destino)
            
                
            else:
                self.lblresultado.text=deotraa10(num,fuente)"""
        except:
            self.lblresultado.text = "error"#cuando se tienen numeros muy grades el error esta en la asignacion en el diccionario letras
            
    def buttonURL(self,btn):
        webbrowser.open("http://www.youtube.com/watch?v=7ZYpIRjzNBg/")
        
#en p.py esta el codigo para corregir  de la aprte de otraa10            
        
        
            
            
        
        

# run app
if __name__ == "__main__":
    MyApp().run()

