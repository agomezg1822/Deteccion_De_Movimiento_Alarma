import cv2
import numpy as np
import imutils
import winsound
import requests
import telegram
import time


#https://api.telegram.org/
#https://core.telegram.org/bots/api

#telegram
bot_token = 'token'
chat_id='el @ de su canal publico'
bot = telegram.Bot(token=bot_token)

video = cv2.VideoCapture('direccion ip de la camara')#la url de la esp32

i = 0
while True:
  ret, frame = video.read()
  if ret == False: break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if i == 20:
    bgGray = gray
  if i > 20:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
      area = cv2.contourArea(c)
      if area > 10000:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        winsound.PlaySound("C:/datos disco/CURSOS/PROYECTOS/grabar/alarma2.wav",  winsound.SND_ASYNC ) #reproducir el sonidO
       #enviar foto 
        with open ('C:/datos disco/CURSOS/PROYECTOS/grabar/fotos/imagen.jpg','rb') as photo_file: 
          bot.sendPhoto(chat_id=chat_id,photo=photo_file, caption='ALERTA INTRUSO DETECTADO') #mensaje que aparecera con la foto

        
       
  cv2.imwrite('C:/datos disco/CURSOS/PROYECTOS/grabar/fotos/imagen.jpg',frame)
  cv2.imshow('Frame',frame)
  i = i+1
  if cv2.waitKey(30) & 0xFF == 27: #cuando presione 'Esc' se va a cerrar el programa
    break
video.release()

