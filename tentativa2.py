
##TENTATIVA 2: Buscando mensagens de textos escondidas através de Esteganografia
# Utilizei o código da seguinte referência: https://www.section.io/engineering-education/steganography-in-python/
# Em busca de extrair alguma imagem escondida no arquivo principal. 
# Não foi encontrada nenhuma mensagem escondida na forma de texto utilizando o código. 

import cv2
from tkinter import filedialog, Tk, Button, Label
from pil import Image, ImageTk
import numpy as np

image_display_size = 500, 350


def decrypt():
    # load the image and convert it into a numpy array and display on the GUI.
    load = Image.open("Syngenta.jpg")
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=100, y=50)

    # Algorithm to decrypt the data from the image
    img = cv2.imread("Syngenta.jpg")
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    # join all the bits to form letters (ASCII Representation)
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    # join all the letters to form the message.
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    message_label = Label(app, text=message, bg='lavender', font=("Times New Roman", 10))
    message_label.place(x=30, y=400)

# Defined the TKinter object app with background lavender, title Decrypt, and app size 600*600 pixels.
app = Tk()
app.configure(background='lavender')
app.title("Decrypt")
app.geometry('600x600')
# Add the button to call the function decrypt.
main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
app.mainloop()