from matplotlib import pyplot as plt
from matplotlib import  numpy  as  np
import random

#------------------Función inicial---------------
#Retorna el valor de la funcion 

def f1(x):
    return (10*x)-20


#----------------Función población----------------
#Retorna una lista de la poblacion dependiendo de los datos 

def generarPoblacion(n,maximo,minimo):
    return [random.sample(list(range(minimo,maximo)),n),[]]


#------------Función Calcular Fitnnes-------------
#Retorna la lista con la población inicial ordenada 
def calcularFitnnes(poblacionInicial,maximo):
    i=0
    while(i<maximo):
        j=0
        while(j<maximo):
            if((abs(poblacionInicial[1][i]))<(abs(poblacionInicial[1][j]))):
                aux=poblacionInicial[1][j]
                poblacionInicial[1][j]=poblacionInicial[1][i]
                poblacionInicial[1][i]=aux
                aux=poblacionInicial[0][j]
                poblacionInicial[0][j]=poblacionInicial[0][i]
                poblacionInicial[0][i]=aux
            j+=1
        i+=1
    return poblacionInicial

#Variables usadas 
mutacion=25
rangoSupervivencia=4;
poblacionInicial= generarPoblacion(8,20,-10)
i=1
d=-1
#-----------------Función reproducir-----------------
#Retorna la lista con los 4 mejores genotipos
def funcion_reproducir(poblacionInicial,maximo,mutacion):
    supervivientes=poblacionInicial[0][:4]
    otraGeneracion=[]
    i=0
    j=0
    print("Genotipo supervivientes")
    print(supervivientes)
    while(i<maximo):
        r1=random.randint(0,3)
        r2=random.randint(0,3)
    return otraGeneracion

def f(x):
    return (-50*x*x)+500*x

def f_dev(x):
    return (-100*x)+500

sample= np.linspace(-50,100,num=30)
mutacion=25
rangoSupervivencia=4;
poblacionInicial= generarPoblacion(8,20,-10)
i=1
index=-1
while(i<50):
    j=0
    r=0
    print("Generacion "+str(i))
    print(poblacionInicial[0])
    
    for x in poblacionInicial[0]:
        res=f_dev(x)
        poblacionInicial[1].append(res)

    if(0 in poblacionInicial[1]):
        print ("Cero encontrado")
        index= poblacionInicial[1].index(0)
        break

    calcularFitnnes(poblacionInicial,8)
    poblacionInicial[0]=funcion_reproducir(poblacionInicial,8,mutacion)
    del poblacionInicial[1][:]
    i+=1
    
    
if(index!=-1):
    print("Maximo Relativo "+ str(poblacionInicial[0][index]))
    print("El valor maximo de R es ", f(poblacionInicial[0][index]))
    plt.scatter(poblacionInicial[0][index], f(poblacionInicial[0][index]), s=30)
    y=f(sample)
    plt.plot(sample,y)
    plt.show()
    


print("Ultima poblacion",poblacionInicial)



