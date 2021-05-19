import cv2;
import sys;
import os;

pasta = sys.argv[1]
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
#print(imagens)

for imagem in imagens:

    imagem 
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        cinza,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (50,50),
    )

    print("{0} Faces encontradas!".format(len(faces)))

    for (x,y,w,h) in faces: 
        cv2.rectangle(imagem,(x,y), (x+w,y+h), (0,255,0), 1)
        cropImg = imagem[y:y+h ,x:x+w]
        #imagem[y:(y+h), x:(x+w)]
        status = cv2.imwrite('C:/Users/joao.calazans/Desktop/faceDetection/PastaDestino/Imagem' + "_Cortada_" + str(counter) + '.jpg' ,cropImg)
        counter +=1
        #cv2.imshow("Faces Cortadas",cropImg)
        #cv2.waitKey(0)
        #print("Imagens salvas no sistema?",status)
        

    cv2.imshow("Faces Detectadas",imagem)
    cv2.waitKey(0)

        