from tkinter import *
from bs4 import BeautifulSoup
import requests
import random
from PIL import Image, ImageTk

# webscrapping quotes
def get_quotes():
    response= requests.get(url="https://www.goodreads.com/quotes/tag/inspirational?page=0")
    data= response.text
    soup= BeautifulSoup(data, 'html.parser')

    quotes_list= [q.getText() for q in soup.select("div.quoteText")]

    all_quotes=[]
    all_authors=[]
    for quotes in quotes_list:
        all_quotes.append(quotes.split("\n")[1].lstrip())
        all_authors.append(quotes.split("\n")[-3].lstrip())

    random_quote_num= random.randint(0,len(all_quotes)-1)

    quote_to_display= all_quotes[random_quote_num]+'\n'+"by "+all_authors[random_quote_num]

    canvas.itemconfig(quote_text, text= quote_to_display)

# tkinter window
window= Tk()
window.title("Quotes Teller")
window.config(bg='#f8f6f0')

# for quotes to be displayed
canvas= Canvas(width=540, height=360, bg='#ffbf00')
background_img=PhotoImage(file="APIs/quotes_teller/background.png")
background_img= background_img.zoom(2)
canvas.create_image(270,180, image=background_img)
quote_text = canvas.create_text(230,100, text="Click the button to get motivation", width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

# for button to change quotes
image = Image.open("APIs/quotes_teller/btn_image.jpg")
resized_image= image.resize((120,120), Image.ANTIALIAS)
btn_image = ImageTk.PhotoImage(resized_image)
btn= Button(image=btn_image, highlightthickness=0, command=get_quotes)
btn.grid(row=1, column=0, pady=10)

window.mainloop()
