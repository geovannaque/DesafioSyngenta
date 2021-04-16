#TENTATIVA 1: Utilizando OpenCV para procurar imagens escondidas através de Esteganografia
# Utilizei o código da seguinte referência: https://www.geeksforgeeks.org/image-steganography-using-opencv-in-python/?ref=rp
# Em busca de extrair alguma imagem escondida no arquivo principal. 
# O resultado foram duas imagens, uma como a original e outra sem os pontos verdes. 
# Dessa forma, não foi encontrada nenhuma mensagem.
import cv2
import numpy as np
import random
def decrypt():
      
    # Encrypted image
    img = cv2.imread('Syngenta.bmp') 
    width = img.shape[0]
    height = img.shape[1]
      
    # img1 and img2 are two blank images
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)
      
    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '8b')
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                  
                # Appending data to img1 and img2
                img1[i][j][l]= int(v2, 2)
                img2[i][j][l]= int(v3, 2)
      
    # These are two images produced from
    # the encrypted image
    cv2.imwrite('imagem1.png', img1)
    cv2.imwrite('imagem2.png', img2)
      
      
# Driver's code
decrypt()