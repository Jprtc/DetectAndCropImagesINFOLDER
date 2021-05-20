import cv2;
import sys;
import os;

pasta = sys.argv[1]
pastaDestino = sys.argv[2]
caminhoCasc = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(caminhoCasc)

counter = 1

imagens = []
def carregarImagensPasta(pasta):
    for filename in os.listdir(pasta):
        imagem = cv2.imread(os.path.join(pasta, filename))
        if imagem is not None:
            imagens.append(imagem)
    return imagens

#Funcao coloca todas as imagens da pasta em uma lista
carregarImagensPasta(pasta)

for imagem in imagens:

    imagem 
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Alterar os valores aqui para resultados diferentes na detecção facial
#Principalmente o scaleFactor e minSize
    faces = faceCascade.detectMultiScale(
        cinza,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (50,50),
    )

    print("{0} Faces encontradas!".format(len(faces)))

    for (x,y,w,h) in faces: 
        cv2.rectangle(imagem,(x,y), (x+w,y+h), (0,255,0), 2)
        cropImg = imagem[y:(y+h) ,x:(x+w)]

        #cropImg = imagem[0:400, 0:350]
    
        status = cv2.imwrite(os.path.join(pastaDestino,'Imagem') + "_Cortada_" + str(counter) + '.jpg' ,cropImg)
        counter +=1

    #cv2.imshow("Faces Cortadas",imagem)
    #cv2.waitKey(0)
        #print("Imagens salvas no sistema?",status)
        
print('Total de faces encontradas:',counter-1)