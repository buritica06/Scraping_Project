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
for i in range(1): # Voy a darle click en cargar mas 3 veces
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


'''
# Busco el boton de los carros para darle click
boton_auto = driver.find_element_by_xpath('//li[@data-aut-id="itemBox"]')
for i in range(1): # Voy a darle click en cargar mas 3 veces
    try:
        # le doy click
        boton_auto.click()
        # espero que cargue la informacion dinamica
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton_auto = driver.find_element_by_xpath('//li[@data-aut-id="itemBox"]')
    except:
        # si hay algun error, rompo el lazo. No me complico.
        break
'''
#INICIO DE SESION OLX
boton_login = driver.find_element_by_xpath('//button[@data-aut-id="btnLogin"]')
boton_login.click()
sleep(random.uniform(8.0, 10.0))
boton_email = driver.find_element_by_xpath('//button[@data-aut-id="emailLogin"]')
boton_email.click()
sleep(random.uniform(6.0, 10.0))
e_mail = driver.find_element_by_xpath('//input[@id="email_input_field"]')
e_mail.send_keys("r.buritica@outloook.com")
sleep(random.uniform(6.0, 11.0))
boton_sgte_mail = driver.find_element_by_xpath('//button[@class="rui-3sH3b rui-2yJ_A rui-1zK8h _2_t7-"]')
boton_sgte_mail.click()
sleep(random.uniform(6.0, 11.0))




'''
#DESCOMENTAR PARA SEGUIR CON LA SECUENCIA
autos = driver.find_element_by_xpath('//li[@data-aut-id="itemBox"]')
# Recorro cada uno de los anuncios que he encontrado
for auto in autos:
    # Por cada anuncio hallo el precio
    autos.click()
    sleep(random.uniform(8.0, 10.0))
    precio = driver.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text      
    nombre_vendedor = driver.find_element_by_xpath('.//div[@class="_3oOe9"]').text
    descripcion = driver.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(nombre_vendedor)
    print (precio)
    print (descripcion)
    sleep(random.uniform(8.0, 10.0))
    driver.back()
    # Por cada anuncio hallo la descripcion
'''   
    
