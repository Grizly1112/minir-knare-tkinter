"""""
Filip Prössel Te2b - Miniräknare GUI
[Länkar]
- https://www.youtube.com/watch?v=Q56J736uWPA
- https://stackoverflow.com/questions/49232866/how-to-delete-last-character-in-text-widget-tkinter
- https://realpython.com/python-eval-function/#:~:text=Python%E2%80%99s%20eval%20%28%29%20allows%20you%20to%20evaluate%20arbitrary,as%20a%20string%20or%20a%20compiled%20code%20object.
"""

# importerar Tkinter.
from tkinter import *

# sätter upp fönstret.
window = Tk()
window.geometry("405x240")
window.title("Miniräknare")

#  Skapar dictionaryt för de senaste beräkningen
senaste = {"seanste": ""}

def input(inmatningen):
    """
    Skriver ut alla tecken i textfältet som användaren angivit.
    :param inmatningen:
    :return: none
    """
    textfalt.insert("end", str(inmatningen))

def hamta_data():
    """
    Hämtar alla karaktärer från textfältet.
    :return: inmatningen
    """
    inmatningen = textfalt.get("1.0",END)
    return inmatningen


def berakna():
    """
    Använder inmatningen från textfäletet för att senare med hälp av -
    eval beräkna denna, för att senare updatera textfältet. Senaste -
    beräkningar uppdaters även i samband med detta.
    """
    result=eval(hamta_data())
    senaste.update({"senaste": result})
    textfalt.delete(1.0,"end")
    textfalt.insert(1.0,str(result))
def rensa():
    """
    Rensar textfältet på dess innehåll.
    :return: None
    """
    textfalt.delete(1.0,"end")

def radera():
    """
    Först hämtas textfältet innehåll varav et urklipp fr¨ån första -
    till näst sista tecknet görs,
    sedan updateras textfältet utan den sista tecknet.
    :return: None
    """
    ta_bort = textfalt.get(1.0, "end")
    ta_bort = ta_bort[:-2]
    textfalt.delete(1.0,"end")
    textfalt.insert(1.0,ta_bort)

def ans():
    """
    Hämtar det senaste resultet från dicotionaryt,
    varav senare lägger till denna i textfältet.
    :return: None
    """
    textfalt.insert("end", senaste.get("senaste"))

def procent():
    """
    Hämar allt i textfälet i följd av tömma detta och skriver -
    ut inmatningen i procent.
    :return: None
    """
    inmatning = textfalt.get(1.0, END)
    textfalt.delete(1.0, END)
    textfalt.insert(1.0, int(inmatning) *0.01)


def shutdown():
    """
    Avslutar fönstret.
    :return: None
    """
    exit()

# Sätter upp textfältet.
textfalt=Text(window, height=1, width=19, font=("Arial", 20))
textfalt.grid(columnspan=4)

# Sätter upp och placerar alla knappar i fönstret.
kanpp_1=Button(window,text="1",command=lambda:input(1),height=1,width=5,font=("Arial",18))
kanpp_1.grid(row=3,column=0)
kanpp_2=Button(window,text="2",command=lambda:input(2),height=1,width=5,font=("Arial",18))
kanpp_2.grid(row=3,column=1)
kanpp_3= Button(window,text="3",command=lambda:input(3),height=1,width=5,font=("Arial",18))
kanpp_3.grid(row=3,column=2)
kanpp_4= Button(window,text="4",command=lambda:input(4),height=1,width=5,font=("Arial",18))
kanpp_4.grid(row=2,column=0)
kanpp_5= Button(window,text="5",command=lambda:input(5),height=1,width=5,font=("Arial",18))
kanpp_5.grid(row=2,column=1)
kanpp_6= Button(window,text="6",command=lambda:input(6),height=1,width=5,font=("Arial",18))
kanpp_6.grid(row=2,column=2)
kanpp_7= Button(window,text="7",command=lambda:input(7),height=1,width=5,font=("Arial",18))
kanpp_7.grid(row=1,column=0)
kanpp_8= Button(window,text="8",command=lambda:input(8),height=1,width=5,font=("Arial",18))
kanpp_8.grid(row=1,column=1)
kanpp_9= Button(window,text="9",command=lambda:input(9),height=1,width=5,font=("Arial",18))
kanpp_9.grid(row=1,column=2)
kanpp_0= Button(window,text="0",command=lambda:input(0),height=1,width=5,font=("Arial",18))
kanpp_0.grid(row=4,column=0)
kanpp_plus= Button(window,text="➕",command=lambda:input("+"),height=1,width=5,font=("Arial",18), bg='#696969', fg='White')
kanpp_plus.grid(row=3,column=3)
kanpp_minus= Button(window,text="➖",command=lambda:input("-"),height=1,width=5,font=("Arial",18), bg='#696969', fg='White')
kanpp_minus.grid(row=3,column=4)
kanpp_result= Button(window,text="=",command=lambda:berakna(),height=1,width=5,font=("Arial",18), bg='#545454', fg='White')
kanpp_result.grid(row=4,column=4)
kanpp_divide= Button(window,text="➗",command=lambda:input("/"),height=1,width=5,font=("Arial",18), bg='#696969', fg='White')
kanpp_divide.grid(row=2,column=4)
kanpp_multiply= Button(window,text="✖",command=lambda:input("*"),height=1,width=5,font=("Arial",18), bg='#696969', fg='White')
kanpp_multiply.grid(row=2,column=3)
kanpp_result= Button(window,text="AC",command=rensa,height=1,width=5,font=("Arial",18),bg='#0066b8',fg='white')
kanpp_result.grid(row=1,column=4)
kanpp_radera = Button(window,text="DEL",command=radera,height=1,width=5,font=("Arial",18),bg='#0066b8',fg='white')
kanpp_radera.grid(row=1,column=3)
knapp_ans = Button(window,text="ANS",command=ans,height=1,width=5,font=("Arial",18), bg='#545454', fg='White')
knapp_ans.grid(row=4, column=3)
knapp_power = Button(window,text="🔘",command=shutdown,height=1,width=5,font=("Arial",18),bg='#545454',fg='white')
knapp_power.grid(row=0, column=4)
knapp_power = Button(window,text="%",command=procent,height=1,width=5,font=("Arial",18))
knapp_power.grid(row=4, column=2)
kanpp_decimal = Button(window,text=",",command=lambda:input("."),height=1,width=5,font=("Arial",18))
kanpp_decimal.grid(row=4,column=1)

# Loopar fönstret.
window.mainloop()
