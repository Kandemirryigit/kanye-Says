# Tkinter is a library for creating user interfaces.
from tkinter import *  # From tkinter import everything
import requests  # To send HTTP requests to web services and APIs


def get_quote():
    response=requests.get(url="https://api.kanye.rest")  # To send HTTP get to specify url
    response.raise_for_status()  # If we have an error like 400,500 it raises an error 
    data=response.json()  # to convert json format
    quote=data["quote"]  # for get details inside that title
    canvas.itemconfig(quote_text,text=quote) 


window = Tk()  # To define tkinter
window.title("Kanye Says...")  # To determine window's title
window.config(padx=50, pady=50)  # To determine user interface
window.config(bg="black")  # To determine background color black

# To creat image in the screen
canvas = Canvas(width=300, height=414,bg="black",highlightthickness=0)   # Highlightthickness is for clear borders
# This path is not gonna work in your computer you should write your own path
background_img = PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/Kanye Says/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

# To creat a button with an image
# This path is not gonna work in your computer you should write your own path
kanye_img = PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/Kanye Says/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,bg="gray")
kanye_button.grid(row=1, column=0)


window.mainloop()  # If I don't click exit button the screen won't close