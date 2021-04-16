#Importando as bibliotecas Numpy e OpenCV
import numpy as np
import cv2

#Lendo a Imagem
img = cv2.imread('Syngenta.bmp', cv2.IMREAD_COLOR)

#Definindo o valor do pixel verde, a OpenCV utiliza por padrão "BGR"
#Para descobrir esse valor, utilizei o código "rgb_green.py"
green_pixel = [0,192,96] 

#Utlizando a função count_nozero para contar o número de vezes que o gree_pixel ocorre. 
result = np.count_nonzero(np.all(img==green_pixel,axis=2))

#Imprimindo resultado
print("Pixels verdes encontrados: ", result)


