import random
from time import sleep
from selenium import webdriver

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(r"C:\Users\rburi\AppData\Local\Programs\Python\Python39\Proyectos\Scraping_Project\chromedriver.exe")

# Voy a la pagina que requiero
driver.get('https://www.olx.com.co/atlantico_g2007003/carros_c378?sorting=desc-creation')

'''
# Busco el boton para cargar mas informacion
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(): # Voy a darle click en cargar mas 3 veces
    try:
        # le doy click
        boton.click()
        # espero que cargue la informacion dinamica
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        # si hay algun error, rompo el lazo. No me complico.
        break

# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
'''

autos = driver.find_element_by_xpath('//li[@data-aut-id="itemBox"]')


# Recorro cada uno de los anuncios que he encontrado

# Por cada anuncio hallo el preico
autos.click()
sleep(random.uniform(8.0, 10.0))
precio = driver.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
descripcion = driver.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
nombre_vendedor = driver.find_element_by_xpath('.//div[@class="_3oOe9"]').text
numero_click = driver.find_element_by_xpath('.//div[@class="_2b6xv"]')
numero_click.click()
sleep(random.uniform(8.0, 10.0))
boton_contestar = driver.find_element_by_xpath('//button[@data-aut-id="rui-3sH3b rui-2yJ_A rui-1zK8h _1G5N6"]')
boton_contestar.click()
sleep(random.uniform(8.0, 10.0))
numero_c = driver.find_element_by_xpath('.//div[@class="_1uXYV"]').text
print (precio)
print(nombre_vendedor)
# Por cada anuncio hallo la descripcion
print (descripcion)
print(numero_c)
sleep(random.uniform(8.0, 10.0))
driver.back()
