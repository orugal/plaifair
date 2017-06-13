#-*-coding:utf8;-*-
#qpy:2
#qpy:console
def tablaPlayFaire():
    clave = raw_input("Escriba la clave: ")
    mensaje = raw_input("Escriba el mensaje: ")
    
    claveFinal = procesaClave(clave)
    mensajeFinal = procesaMsg(mensaje.upper())
    tablaCifrado = genTabla(claveFinal)
    encripta = cifrado(claveFinal,mensajeFinal,tablaCifrado)
    print(encripta)
    
#proceso la clave  
def procesaClave(clave):
    #elimino letras repetidas
    nClave = []
    for a in range(len(clave)):
        letra = clave[a].upper()
        if letra != " ":
            if letra not in nClave:
                nClave.append(letra)
    return nClave
#genera la tabla de codificado
def genTabla(clave):
    for a in range(97,123):
        car = chr(a).upper()
        if car not in clave:
            if car != "W":
                clave.append(car)
    #armo el 5 x 5
    '''salida = []
    cuenta = 0
    for b in range(5):
        salida.append([])
        for c in range(5):
            salida[b].append(clave[cuenta])
            cuenta = cuenta + 1'''      
    return clave
#Procesa el mensaje convirtiendolo en bigrama  
def procesaMsg(mensaje):
    nMsg = ""
    msgFinal = ""
    for i in range(len(mensaje)):
        if mensaje[i] != " ":
            nMsg = nMsg+mensaje[i]
    #print(nMsg)
    #analizo si la cantidad de caracteres es par
    lenMsg = len(nMsg)
    if lenMsg % 2 != 0:#no es par
        msgFinal = nMsg+"X"
    else:
        msgFinal = nMsg
    
    #calculo letras repetidas
    letraAnt = ""
    letraSig = ""
    msgResult = ""
    for b in range(len(msgFinal)):
        if letraAnt == "":#primer giro
            letraAnt = msgFinal[b]
            msgResult = msgResult + msgFinal[b]
        else:#otros giros
            if msgFinal[b] == letraAnt:#pongo una x
                    letraAnt = msgFinal[b]
                    letraSig = msgFinal[b]
                    msgResult = msgResult + "X" + msgFinal[b]
            else:
                letraAnt = msgFinal[b]
                msgResult = msgResult + msgFinal[b]
                #letraSig = msgFinal[b]
                    
         
    
    #cada dos letras las agrego a un nuevo array
    cont = 1
    msgParse = []
    temp = []
    for a in range(len(msgResult)):
        if cont == 2:
            cont = 1
            temp.append(msgResult[a])
            msgParse.append(temp)
            temp = []
        else:
            temp.append(msgResult[a])
            cont = cont + 1
                        
    print(msgParse)

#Encripta el mensaje       
def cifrado(clave,mensaje,tabla):
    #print(mensaje)
    for a in mensaje:
        print (mensaje[a])
    #print(tabla.index("X"))
    #print(tabla[0])
       
        
tablaPlayFaire()