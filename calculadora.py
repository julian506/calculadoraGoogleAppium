def main():
    from appium import webdriver

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "ginkgo"
    caps["automationName"] = "UiAutomator1"
    caps["appPackage"] = "com.google.android.calculator"
    caps["appActivity"] = "com.android.calculator2.Calculator"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    num0 = driver.find_element_by_id("com.google.android.calculator:id/digit_0")
    num1 = driver.find_element_by_id("com.google.android.calculator:id/digit_1")
    num2 = driver.find_element_by_id("com.google.android.calculator:id/digit_2")
    num3 = driver.find_element_by_id("com.google.android.calculator:id/digit_3")
    num4 = driver.find_element_by_id("com.google.android.calculator:id/digit_4")
    num5 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
    num6 = driver.find_element_by_id("com.google.android.calculator:id/digit_6")
    num7 = driver.find_element_by_id("com.google.android.calculator:id/digit_7")
    num8 = driver.find_element_by_id("com.google.android.calculator:id/digit_8")
    num9 = driver.find_element_by_id("com.google.android.calculator:id/digit_9")
    
    suma = driver.find_element_by_id("com.google.android.calculator:id/op_add")
    resta = driver.find_element_by_id("com.google.android.calculator:id/op_sub")
    multiplica = driver.find_element_by_id("com.google.android.calculator:id/op_mul")
    divide = driver.find_element_by_id("com.google.android.calculator:id/op_div")

    igual = driver.find_element_by_id("com.google.android.calculator:id/eq")
    borrar = driver.find_element_by_id("com.google.android.calculator:id/del")

    while True:
        
        expresion = input("Ingrese la expresion a calcular sin espacios: ")
        resultadoPython = eval(expresion) #La función eval permite obtener el resultado de una operación matemática entrada via cadena

        lista = list(expresion)
        for i in range(len(lista)): #Convierto los numeros a enteros
            try:
                lista[i] = int(lista[i])
            except:
                lista[i] = lista[i]
        print("Expresion: ", lista)
        
        lista2=[]
        for i in range (len(lista)):
            if lista[i] == 1:
                num1.click()
                lista2.append(num1.text)
            elif lista[i] == 2:
                num2.click()
                lista2.append(num2.text)
            elif lista[i] == 3:
                num3.click()
                lista2.append(num3.text)
            elif lista[i] == 4:
                num4.click()
                lista2.append(num4.text)
            elif lista[i] == 5:
                num5.click()
                lista2.append(num5.text)
            elif lista[i] == 6:
                num6.click()
                lista2.append(num6.text)
            elif lista[i] == 7:
                num7.click()
                lista2.append(num7.text)
            elif lista[i] == 8:
                num8.click()
                lista2.append(num8.text)
            elif lista[i] == 9:
                num9.click()
                lista2.append(num9.text)
            elif lista[i] == 0:
                num0.click()
                lista2.append(num0.text)
            elif lista[i] == "+":
                suma.click()
                lista2.append(suma.text)
            elif lista[i] == "-":
                resta.click()
                lista2.append(resta.text)
            elif lista[i] == "*":
                multiplica.click()
                lista2.append("*")
            elif lista[i] == "/":
                divide.click()
                lista2.append("/")
        igual.click()
        clear = driver.find_element_by_id("com.google.android.calculator:id/clr") #Se define después de darle click al igual porque es en ese momento que aparece el boton, de lo contrario saca error
        resultadoAppium = eval("".join(lista2))

        print("Resultado de la calculadora esperado:", resultadoAppium) #Esperado porque es lo que se le está pidiendo por código que haga. Toca verificar el resultado como tal en la app
        print("Resultado de Python:", resultadoPython)
        cosa = input("Presione ENTER para ingresar una nueva operacion")
        #Borro la operación ya existente
        clear.click()

main()