#-------TRIÁNGULO
#a = int(input('Digite el número de altura y ancho: '))
#b = 2
#
#for i in range (a):
#    for k in range(1,b):
#        print('*',end='')
#    b+=1
#    print('\n')
#-------TRIÁNGULO

#-------LENGUAJE HACKER
#abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#hacker = ['4', '8', '(', '|)', '3', '|=', '6', '#', '|', '_|', '|<', '|_', '|\/|', '|\\|', '0', '|o', 'p', 'q', 'r', '5', '7', 'u', '\/', '\/\/', '><', 'y', '2']
#
#nueva = ''
#
#for m in range (5):
#    palabra = input('Ingresa una palabra: ')
#    for i in range (len(palabra)):
#        for k in range (len(abc)):
#            if(palabra[i] == abc[k]):
#                nueva += hacker[k]
#
#    print(nueva)
#    nueva = ''
#-------LENGUAJE HACKER

#--------FIZZ BUZZ
#for i in range (1,101):
#    if(i % 3 == 0 and i % 5 == 0):
#        print('fizz buzz')
#    elif(i % 3 == 0):
#        print('fizz')
#    elif(i % 5 == 0):
#        print('buzz')
#    else:
#        print(i)
#--------FIZZ BUZZ

#--------POSICIÓN DEL ROBOT
#def position(list:list):
#    pos_x   = 0
#    pos_y   = 0
#    rob_dirs = [1,2,3,4]
#    k = 0
#
#    for i in list:
#        match rob_dirs[k]:
#            case 1:
#                pos_y += i
#                k = 1
#            case 2:
#                pos_x -= i
#                k = 2
#            case 3:
#                pos_y -= i
#                k = 3
#            case 4:
#                pos_x += i
#                k = 0
#
#    print("Posición final: (X: ", pos_x , ", Y: ", pos_y , ")")
#
#while True:
#    num = int(input("Número de secuencias de pasos: "))
#    list = [num for _ in range(num)]
#
#    for i in range(len(list)):
#        a = int(input("Ingrese secuencia: "))
#        list[i] = a
#
#    position(list)
#--------POSICIÓN DEL ROBOT.



#def calcular_mayor(list:list):
#    mayor = 0
#
#    for i in list:
#        if i < mayor:
#            continue
#        else:
#            mayor = i
#
#    return mayor
#
#list = [1,3,5,3,46,6]
#mayor = calcular_mayor(list)

#--------EMAIL FOR USERNAME AND DOMAIN
#email = input("Enter email: ")
#
#username = email[:email.index("@")]
#domain = email[email.index("@") + 1:]
#
#print(f"Username: {username} \nDomain: {domain}")
#--------EMAIL FOR USERNAME AND DOMAIN

#--------QR Code
#import pyqrcode
#from PIL import Image
#
#link = input("Enter link: ")
#qrcode = pyqrcode.create(link)
#qrcode.png("QRcode.png", scale=5)
#Image.open("QRcode.png")
#--------QR Code

#--------CALENDAR
#import calendar
#
#for i in range(1,13):
#    print(calendar.month(2012, i))
    #--------CALENDAR

