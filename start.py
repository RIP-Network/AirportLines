import smtplib, ssl
import os
import time
import getpass
from selenium import webdriver

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

print(blanco+"Creado por RIP-Network"+cierre)

web = webdriver.Firefox()
web.get('https://www.flightradar24.com/43.73,1.68/8')
time.sleep(5)