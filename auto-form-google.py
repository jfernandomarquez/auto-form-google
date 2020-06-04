import time
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#valores en texto

name = 'mi nombre'
fecha = '10/10/10'
motivo = 'motivo'

#Xpath url

inputName = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input' 

inputFecha = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'

inputmotivo = '//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[1]/div[2]/textarea'

#botones

uno = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'

dos = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div'


###################
user = '//*[@id="identifierId"]' 
siguiente = '//*[@id="identifierNext"]/span'

contra = '//*[@id="password"]/div[1]/div/div[1]/input'
siguiente2 = '//*[@id="passwordNext"]/span' 

code = "cOntraensesentaycuatro=="
micontra = base64.b64decode(code)
newcode = str(micontra, 'utf-8')

##################

#enviar

enviar='//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span'

browser = webdriver.Chrome('/home/juan.marquez/Downloads/chromedriver_linux64/chromedriver')

browser.get('https://docs.google.com/forms/d/e/1FAIpQLSciQI7GT1sGe0-rF4fZ1sVAU5XSXfHcANmeuSVU7Rbx1HallA/viewform?vc=0&c=0&w=1')

#login
browser.find_element_by_xpath(user).send_keys('micorreo@gmail.com')
browser.find_element_by_xpath(siguiente).click()
time.sleep(3)
browser.find_element_by_xpath(contra).send_keys(newcode)
browser.find_element_by_xpath(siguiente2).click()
time.sleep(20)
# accion

browser.find_element_by_xpath(inputName).send_keys(name)
browser.find_element_by_xpath(inputFecha).send_keys(fecha)
browser.find_element_by_xpath(inputmotivo).send_keys(motivo)
browser.find_element_by_xpath(uno).click()
browser.find_element_by_xpath(dos).click()
browser.find_element_by_xpath(enviar).click()
browser.back()
browser.quit()
