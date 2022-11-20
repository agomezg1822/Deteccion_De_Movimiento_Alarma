import cv2
import numpy as np
import imutils
import winsound
import requests

#https://api.telegram.org/
#https://core.telegram.org/bots/api


video = cv2.VideoCapture('http://192.168.20.110:81/stream')#la url de la esp32

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
        requests.post('https://api.telegram.org/bot"aca pone el token de su bot"/sendMessage',
         data = {'chat_id': "aca pone el @ de su canal publico", 'text': "texto que quiere enviar"}) #envia al api de telgram
        winsound.PlaySound("C:/datos disco/CURSOS/PROYECTOS/grabar/alarma2.wav",  winsound.SND_ASYNC ) #reproducir el sonido
       
  
  cv2.imshow('Frame',frame)
  i = i+1
  if cv2.waitKey(30) & 0xFF == 27: #cuando presione 'Esc' se va a cerrar el programa
    break
video.release()