from re import L #
import random #para datos aleatorios



#Pregunta si se va a jugar en modo desarrollador
def preg_modo():
  p=str(input("¿Jugar en modo desarrollador? (s/n)"))
  if p=="s" or p=="S":
    return True
  else:
    return False

#crea la matriz de las casillas externas
def crear_matr(Matriz):
  Lista=[]
  n=1
  for i in range(0,68):
    Lista.append(n)
    if n==1:
      Lista.append("S1")
    elif n==18:
      Lista.append("S2")
    elif n==35:
      Lista.append("S3")
    elif n==52:
      Lista.append("S4")
    elif n==64:
      Lista.append("E1")
    elif n==13:
      Lista.append("E2")
    elif n==30:
      Lista.append("E3")
    elif n==47:
      Lista.append("E4")
    elif n==8 or n==25 or n==42 or n==59:
      Lista.append("SE")
    else:
      Lista.append("")
    n+=1
    Lista.append([])
    Matriz.append(Lista)
    Lista=[]

#crea las fichas y sus respectivos datos
def crear_ficha(matriz,numj,abc):
  n=1
  for i in range(0,numj):
    f=1
    for i in range(0,4):
      Lista=[]
      pos=0
      nomf=str(n)+str(abc[f-1])
      posi=0
      cmov=0
      Lista.append(n);Lista.append(f);Lista.append(pos);Lista.append(nomf);Lista.append(posi);Lista.append(cmov)
      matriz.append(Lista)
      f+=1
    n+=1

#Crea matriz de casillas internas(camino de llegada)
def crear_intes(Inte,numj):
  n=1
  Lista=[]
  for i in range(0,numj):
    Lista.append(n)
    Lista2=[]
    for i in range(0,8):
      Lista2=[]
      Lista2.append(i+1)
      Lista2.append([])
      f=1
     
      Lista.append(Lista2)
    n+=1
    Inte.append(Lista)

#calcula los números de dos dados entre uno y seis
def dados():
  d1=random.randint(1,6)
  return (d1)

#Quita la ficha de una posición en la matriz
def quitar_ficha(ficha,matriz):
  for i in matriz:
    for e in i[2]:
      if e==ficha:
        i[2].remove(ficha)
      break

#Pone la ficha en una posición en la matriz
def poner_ficha(posicion,ficha,matriz):
  for i in matriz:
    if i[0]==posicion:
      i[2].append(ficha)
      break

#Quita la ficha que después pone en otra posición en la matriz
def mover_ficha(posicion,ficha,matriz):
  quitar_ficha(ficha,matriz)
  poner_ficha(posicion,ficha,matriz)

#Busca la ficha y cambia su número de posición en matriz fichas
def cambiar_posicion(jugador,ficha,Fichas):
  n=0
  for i in Fichas:
      if i[0]==jugador and i[1]==ficha:
        i[2]=n
        nom=i[3]
        break

#Quita la ficha de una posición de la matriz de internas
def quitar_inte(ficha,Inte):
  for i in Inte:
    for e in i[int(ficha[0])]:
      if e==ficha:
        i[int(ficha[0])].remove(ficha)
      break

#Pone la ficha en una posición de la matriz de internas
def poner_inte(posi,ficha,Inte):
  for i in Inte:
    if i[0]==posi:
      i[int(ficha[0])].append(ficha)
      break

#Busca la ficha y cambia su número de posi(posición de internas)
def mover_inte(posi,ficha,Inte):
  quitar_inte(ficha,Inte)
  poner_inte(posi,ficha,Inte)

#Busca la ficha y cambia su número de posición
def cambiar_inte(jugador,ficha,Fichas,Inte):
  n=0
  for i in Fichas:
      if i[0]==jugador and i[1]==ficha:
        i[2]=n
        nom=i[3]
        break

#Hace aparecer ficha en las casillas externas (ficha es número de ficha)
def sacar_ficha(jugador,ficha,Fichas,Matriz,carcel):
    n=0
    nom=""
    if jugador ==1:
          n=1
    elif jugador ==2:
          n=18
    elif jugador ==3:
          n=35
    elif jugador ==4:
          n=52
    for i in Fichas:
      if i[0]==jugador and i[1]==ficha:
        i[2]=n
        nom=i[3]
        break
    for i in Matriz:
      if i[0]==n:
        i[2].append(nom)
        break

    for i in carcel[jugador-1][1]:
      if i==nom:
        carcel[jugador-1][1].remove(i)
        break

#Elimina la ficha de matriz y la pone en la cárcel
def capturar_ficha(vtur,ficha,Fichas,Matriz,carcel):
  quitar_ficha(ficha,Matriz)
  carcel[vtur-1][1].append(ficha)
  for i in Fichas:
    if i[3]==ficha:
      i[2]=0
      break

#Crear matriz tabla posiciones
def crear_posiciones(numj,posiciones):
  n=1
  Lista=[]
  for i in range(0,numj):
    Lista=[]
    Lista.append(n);Lista.append(0);Lista.append(0);Lista.append("")
    n+=1
    posiciones.append(Lista)

#Crea matirz de cárcel
def crear_carcel(numj,carcel,abc):
  n=1
  Lista=[]
  Lista2=[]
  f=1
  for i in range(0,numj):
    Lista=[]
    Lista2=[]
    for i in range(0,4):
      nomf=str(n)+str(abc[f-1])
      Lista2.append(nomf)
      f+=1
    f=1
    Lista.append(n);Lista.append(Lista2)
    carcel.append(Lista)
    n+=1

#Letra a número
def letra_a_num(nomf,abc):
  f=0
  for i in abc:
    if nomf[1]==i:
      f=(abc.index(i))+1
      break
  return(f)

#función letra a número pero recibiendo solo una letra
def solo_letra(let,abc):
  f=0
  for i in abc:
    if let==i:
      f=(abc.index(i))+1
      break
  return(f)

#Verifica si se puede sacar una ficha
def ver_salida(vtur,Fichas,Matr,Carcel,dado):
  if len(Carcel[vtur-1][1]) !=0:
      for i in Matr[salidat][2]:
        if len(i) !=0:
          if i[0] != vtur:
            capturar_ficha(vtur,i,Fichas,Matr,Carcel)
            print("Se capturó ficha"+str(i))
      if vtur ==1:
            if len(Matr[0][2])<2:
              sacar_ficha(vtur,letra_a_num(Carcel[vtur-1][1][0],abc),Fichas,Matr,Carcel)
              print("Se sacó ficha de la carcel")
              fsacadas=True
              if dado==1:
                d1u=True
              elif dado==2:
                d2u=True
              else:
                d1u=True
                d2u=True
      elif vtur ==2:
            if len(Matr[17][2])<2:
              sacar_ficha(vtur,letra_a_num(Carcel[vtur-1][1][0],abc),Fichas,Matr,Carcel)
              print("Se sacó ficha de la carcel")
              fsacadas=True
              if dado==1:
                d1u=True
              elif dado==2:
                d2u=True
              else:
                d1u=True
                d2u=True
      elif vtur ==3:
            if len(Matr[34][2])<2:
              sacar_ficha(vtur,letra_a_num(Carcel[vtur-1][1][0],abc),Fichas,Matr,Carcel)
              print("Se sacó ficha de la carcel")
              fsacadas=True
              if dado==1:
                d1u=True
              elif dado==2:
                d2u=True
              else:
                d1u=True
                d2u=True
      elif vtur ==4:
            if len(Matr[51][2])<2:
              sacar_ficha(vtur,letra_a_num(Carcel[vtur-1][1][0],abc),Fichas,Matr,Carcel)
              print("Se sacó ficha de la carcel")
              fsacadas=True
              if dado==1:
                d1u=True
              elif dado==2:
                d2u=True
              else:
                d1u=True
                d2u=True

#Detecta si hay un bloqueo entre la posición en la que está y en la que quedaría se usa ese dado
def detectar_bloqueo(posicion,Matr,pasos,movf):
    posp=posicion+pasos
    if 68<posp:
      posp-=68
      print
      for i in range(posicion-1,68):
        print(len(Matr[i][2]))
        if len(Matr[i][2])>1:
          return True
          break
      for i in range(0,posp-1):
        if len(Matr[i][2])>1:
          return True
          break
    else:
      for i in range(posicion-1,posp-1):
        if len(Matr[i][2])>1:
          return True
          break
    return False

#Busca otras fichas en la casilla a la que se va 
def prueba_comer(Matr):
  if len(Matr[posp][2])<0:
    for i in Matr[posp][2]:
      Matr[posp][2].remove(i)
      return True

#Comprueba si la ficha continua su camino en la matriz inte y la deja en inte
def pasa_inte(Fichas,ficha,Matr,movf):
  if Fichas[ficha[0]][2]>=entradat and posp < entradat:
    Fichas[ficha[0]][4]-=entradat
    Fichas[ficha[0]][2]=0
    dato=4
    movf=False
  else:
    return None


#Comprueba si tiene la posibilidad de moverse a esa casilla en inte y si entró. Si entró la añade a posiciones
def pruebs_inte(Fichas,ficha,Inte,movf):
  if posp>8:
    movf=False
  if posp==8:
    for i in Inte[ficha[0]][1][1]:
      if i==ficha:
        Inte[ficha[0]][1][1].remove(i)
        break
    Posiciones[ficha[0]][2]+=1

#crea matriz de opciones
def crear_opc(Opc):
  Listaabcd=[]
  Lista=[]
  Listaabcd.append("A")
  Listaabcd.append("B")
  Listaabcd.append("C")
  Listaabcd.append("D")
  Opc.append(Listaabcd)
  for i in range(0,3):
    for i in range(0,4):
      Lista.append("-")
  Opc.append(Lista)

#Llena la matriz de opciones
def llenar_Opc(Ficha):
  for i in Fichas:
    if i[0]==vtur and (i[2]!=0 or i[4]!=0):
        d=d1
        if mps==1:
            movf=False
        if d1u==True:
           movf=False
        detectar_bloqueo(Ficha[dato],Matr,d1)
        pasa_inte()
        pruebs_inte()
        if movf==True:
            Opc[i[1]-1]=d
        d=d2
        if mps==2:
          movf=False
        if d2u==True:
           movf=False
        detectar_bloqueo(Ficha[dato],Matr,d1)
        pasa_inte()
        pruebs_inte()
        if movf==True:
            Opc[i[1]-1]=d
        d=d1+d2
        if mps==3:
            movf==False
        if d1u==True or d2u==True:
           movf=False
        detectar_bloqueo(Ficha[dato],Matr,d1)
        pasa_inte()
        pruebs_inte()
        if movf==True:
            Opcpc[i[1]-1]=d
  else:
    Opcpc[i[1]-1]=("-")

#crea un matriz carta de opciones para mostrar al jugador
def crear_carta():
    carta=Opc
    carta[0].insert("opc")
    carta[1].insert("d1")
    carta[2].insert("d2")
    carta[3].insert("d1+d2")
#Matr:matriz casillas externas; Inte:matriz casillas internas
#Fichas:Matriz de datos de fichas #Posiciones Matriz tabla posiciones
Matr=[];Inte=[];Fichas=[];Posiciones=[];Carcel=[];Opc=[];carta=[]
abc="ABCD" #Usado en funciones
tj=True #¿terminójuego?

#datos de inicio
numj=(int(input("Insertar número de jugadores (Entre 2 y 4): ")))#número jugadores
desarrollador= preg_modo()#Modo desarollador
tj=False #¿termino juego?
vtur=1 #variable de turno
d1=0;d2=0 #dados 1 y 2
ld="" #¿Lanzar dados? En modo desarrollador en cada turno se escoge si se lanza o se inserta el valor de los dados, esta variable es s si se decidió lanzar.
d1u=False;d2u=False #Indica en cada turno si ya se usó dato de cada dado
fsacadas=False#fichas sacadas en el turno
salidat=0 #Salida del jugador de turno
entradat=0 #Entrada del jugador de turno
posp=0 #posición posible
movf=True #¿Se puede mover la ficha con los números de esos dados?
cd=0 #contador de dobles
mps=0 #¿mover para sacar?
dato=0 #dato temporal usado en unas funciones
fs=0 #ficha seleccionada
ds=0 #dado seleccionado
pc=False #Prueba comer

#Creación de matrices
crear_matr(Matr)
crear_ficha(Fichas,numj,abc)
crear_intes(Inte,numj)
crear_posiciones(numj,Posiciones)
crear_carcel(numj,Carcel,abc)


#El juego está contenido en el while y cada vez que se reinicia empieza un nuevo turno
while tj==False:

    print("turno del jugador: "+str(vtur))
    input("Enter para lanzar dados")
  
    if vtur ==1:
        salidat=0
        entradat=63
    elif vtur ==2:
        salidat=17
        entradat=12
    elif vtur ==3:
        salidat=34
        entradat=29
    elif vtur ==4:
        salidat=51
        entradat=46
    
    crear_opc[Opc]
  
    if desarrollador ==True:
        ld=str(input("Insertar los valores de los dados (s/n)"))
        if ld=="s" or "S":
            d1=int(input("Insertar valor del dado 1: "))
            d2=int(input("Insertar valor del dado 2: "))
        else:
            d1=dados()
            d2=dados()
  
    print("dado 1:"+str(d1)+"| dado 2:"+str(d2))

    if d1==5:
        ver_salida(vtur,Fichas,Matr,Carcel,1)

    if d2==5:
        ver_salida(vtur,Fichas,Matr,Carcel,2)

    if d1+d2==5:
        ver_salida(vtur,Fichas,Matr,Carcel,3)

    if len(Carcel[vtur-1][1]) !=0:
        if (d1==5 and d2==5) and (d1u==False and d2u==False):
            mps=3
        else:
            if d1==5 and (d1u==False and d2u==False):
                mps=1
            if d2==5 or d2==5 and (d1u==False and d2u==False):
                mps=2

    print("estas son las opciones y cuánto se puede mover cada ficha")

    llenar_opc(Fichas)

    for i in Opc:
       print(i)
    
    fs=solo_letra(input("Cuál ficha mover(A/B/C/D): "))
    ds=input("Qué dado(s) usar (d1→1/d2→2/d1+d2→3): ")

    if ds==1:
       d1u=True
    if ds==2:
       d2u=True
    if ds==3:
       d1u=True;d2u=True

    for i in Fichas:
        if i[0]==vtur:
            if i[fs]:
                if i[2]!=0:
                    pc=prueba_comer(posp,Matr)
                    mover_ficha(posp,i[3],Matr)
                if i[4]!=0:
                    mover_inte(posp,i[3],Matr)
    
    movf=True
    fs=0
    ds=0
    pc=False

    if d1==5:
        ver_salida(vtur,Fichas,Matr,Carcel,1)

    if d2==5:
        ver_salida(vtur,Fichas,Matr,Carcel,2)

    if d1+d2==5:
        ver_salida(vtur,Fichas,Matr,Carcel,3)

    if len(Carcel[vtur-1][1]) !=0:
        if (d1==5 and d2==5) and (d1u==False and d2u==False):
            mps=3
        else:
            if d1==5 and (d1u==False and d2u==False):
                mps=1
            if d2==5 or d2==5 and (d1u==False and d2u==False):
                mps=2

    print("estas son las opciones y cuánto se puede mover cada ficha")

    Opc=[]
    llenar_opc(Fichas)

    if vtur == numj:
        vtur=1
    else:
        vtur+=1
    d1u=False;d2u=False;fsacadas=False
    if cd<3:
        if d1!=d2:
            d1=0;d2=0 #dados 1 y 2
            ld="" #¿Lanzar dados? En modo desarrollador en cada turno se escoge si se lanza o se inserta el valor de los dados, esta variable es s si se decidió lanzar.
            d1u=False;d2u=False #Indica en cada turno si ya se usó dato de cada dado
            fsacadas=False#fichas sacadas en el turno
            salidat=0 #Salida del jugador de turno
            entradat=0 #Entrada del jugador de turno
            posp=0 #posición posible
            movf=True #¿Se puede mover la ficha con los números de esos dados?
            cd=0 #contador de dobles
            mps=0#¿mover para sacar?
            dato=0
            fs=0#ficha seleccionada
            ds=0#dado seleccionado
            pc=False#Prueba comer
            if vtur == numj:
                vtur=1
            else:
                vtur+=1
        else:
            vtur=vtur

    for i in Posiciones:
        if i[1]<3:
            tj=True
            print("juego terminó, jugador  "+str(i)+" gana")
        else:
            tj=True

