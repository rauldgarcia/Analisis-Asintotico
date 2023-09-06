# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:34:30 2022

@author: pingu
"""
import time
inicio=time.time()
import math
def getExp(n):
    return math.exp(n)

import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np

grafx1=np.empty(())
grafx2=np.empty(())
grafx3=np.empty(())
grafx4=np.empty(())
grafx5=np.empty(())
grafy1=np.empty(())
grafy2=np.empty(())
grafy3=np.empty(())
grafy4=np.empty(())
grafy5=np.empty(())

x1=1.0
x2=0.25
x3=-0.5
output1=1.0
output2=0.5
output3=0

v1=random.random()
v2=random.random()
v3=random.random()
v4=random.random()
v5=random.random()
v6=random.random()

w1=random.random()
w2=random.random()
w3=random.random()
w4=random.random()
w5=random.random()
w6=random.random()

n=0.25

plt.show()
operacion=20
for i in range(250):
    
    '''Entrada capa media'''
    entrada4=(x1*v1)+(x2*v3)+(x3*v5)
    entrada5=(x1*v2)+(x2*v4)+(x3*v6)
    
    '''Salida capa media'''
    salida4=-1+(2/(1+getExp(-2*entrada4)))
    salida5=-1+(2/(1+getExp(-2*entrada5)))
    
    '''Entrada capa salida'''
    entrada6=(salida4*w1)+(salida5*w4)
    entrada7=(salida4*w2)+(salida5*w5)
    entrada8=(salida4*w3)+(salida5*w6)
    
    '''Salida capa salida'''
    salida6=-1+(2/(1+getExp(-2*entrada6)))
    salida7=-1+(2/(1+getExp(-2*entrada7)))
    salida8=-1+(2/(1+getExp(-2*entrada8)))
    
    '''Errores'''
    error6=(salida6-output1)**2
    error7=(salida7-output2)**2
    error8=(salida8-output3)**2
    errortotal=error6+error7+error8
    
    plt.figure(1)
    plt.plot(i,error6,'o',color='r')
    plt.plot(i,error7,'o',color='g')
    plt.plot(i,error8,'o',color='b')
    plt.plot(i,errortotal,'o',color='k')
    plt.plot(i,salida6,'o',color='c')
    plt.plot(i,salida7,'o',color='m')
    plt.plot(i,salida8,'o',color='y')
    plt.xlabel('Iteración',)
    plt.ylabel('Error')
    plt.title('Error')
    plt.grid()
    
    '''BACKPROPAGATION'''
    '''ERROR CAPA DE SALIDA'''
    '''Error dependiente a la salida (6)'''
    errordependientesalida6=2*(salida6-output1)
    errordependientesalida7=2*(salida7-output2)
    errordependientesalida8=2*(salida8-output3)
    
    '''Salida dependiente al peso(7)'''
    salidadepact64=salida6*(1-salida6)*salida4
    salidadepact65=salida6*(1-salida6)*salida5
    salidadepact74=salida7*(1-salida7)*salida4
    salidadepact75=salida7*(1-salida7)*salida5
    salidadepact84=salida8*(1-salida8)*salida4
    salidadepact85=salida8*(1-salida8)*salida5
    
    '''Descenso de gradiente cada peso w(9)'''
    ajustew1=-n*errordependientesalida6*salidadepact64
    ajustew4=-n*errordependientesalida6*salidadepact65
    ajustew2=-n*errordependientesalida7*salidadepact74
    ajustew5=-n*errordependientesalida7*salidadepact75
    ajustew3=-n*errordependientesalida8*salidadepact84
    ajustew6=-n*errordependientesalida8*salidadepact85
    
    '''ERROR CAPA MEDIA'''
    '''Error dependiente a la entrada de la capa previa(11)'''
    salidadepact46=salida6*(1-salida6)*w1
    salidadepact47=salida7*(1-salida7)*w2
    salidadepact48=salida8*(1-salida8)*w3
    salidadepact56=salida6*(1-salida6)*w4
    salidadepact57=salida7*(1-salida7)*w5
    salidadepact58=salida8*(1-salida8)*w6
    
    '''salida dependiente a la entrada(7)'''
    errordepprevia41=salida4*(1-salida4)*v1
    errordepprevia43=salida4*(1-salida4)*v3
    errordepprevia45=salida4*(1-salida4)*v5
    errordepprevia52=salida5*(1-salida4)*v2
    errordepprevia54=salida5*(1-salida4)*v4
    errordepprevia56=salida5*(1-salida4)*v6
    
    '''Descenso de gradiente cada peso v(10)'''
    ajustev1w1=-n*errordependientesalida6*salidadepact46*errordepprevia41
    ajustev3w1=-n*errordependientesalida6*salidadepact46*errordepprevia43
    ajustev5w1=-n*errordependientesalida6*salidadepact46*errordepprevia45
    ajustev2w4=-n*errordependientesalida6*salidadepact56*errordepprevia52
    ajustev4w4=-n*errordependientesalida6*salidadepact56*errordepprevia54
    ajustev6w4=-n*errordependientesalida6*salidadepact56*errordepprevia56
    
    ajustev1w2=-n*errordependientesalida7*salidadepact47*errordepprevia41
    ajustev3w2=-n*errordependientesalida7*salidadepact47*errordepprevia43
    ajustev5w2=-n*errordependientesalida7*salidadepact47*errordepprevia45
    ajustev2w5=-n*errordependientesalida7*salidadepact57*errordepprevia52
    ajustev4w5=-n*errordependientesalida7*salidadepact57*errordepprevia54
    ajustev6w5=-n*errordependientesalida7*salidadepact57*errordepprevia56  
    
    ajustev1w3=-n*errordependientesalida8*salidadepact48*errordepprevia41
    ajustev3w3=-n*errordependientesalida8*salidadepact48*errordepprevia43
    ajustev5w3=-n*errordependientesalida8*salidadepact48*errordepprevia45
    ajustev2w6=-n*errordependientesalida8*salidadepact58*errordepprevia52
    ajustev4w6=-n*errordependientesalida8*salidadepact58*errordepprevia54
    ajustev6w6=-n*errordependientesalida8*salidadepact58*errordepprevia56
    
    '''Ajuste de cada peso v'''
    v1=v1+ajustev1w1+ajustev1w2+ajustev1w3
    v2=v2+ajustev2w4+ajustev2w5+ajustev2w6
    v3=v3+ajustev3w1+ajustev3w2+ajustev3w3
    v4=v4+ajustev4w4+ajustev4w5+ajustev4w6
    v5=v5+ajustev5w1+ajustev5w2+ajustev5w3
    v6=v6+ajustev6w4+ajustev6w5+ajustev6w6
    
    '''Ajuste de cada peso w'''
    w1=w1+ajustew1
    w2=w2+ajustew2
    w3=w3+ajustew3
    w4=w4+ajustew4
    w5=w5+ajustew5
    w6=w6+ajustew6
    plt.figure(2)
    plt.grid()
    t=time.time()
    tiempo=t-inicio
    plt.plot(tiempo,i/10,'o',linewidth=0.8,color='tab:purple',label='Y=n/10')
    plt.plot(tiempo,i,'o',linewidth=0.8,color='tab:orange',label='Y=n')
    plt.plot(tiempo,i*0.5,'o',linewidth=0.8,color='tab:gray',label='Y=0.5n')
    plt.plot(tiempo,i**1.5,'o',linewidth=0.8,color='tab:cyan',label='Y=n1.5')
    plt.plot(tiempo,2**(i/3),'o',color='tab:pink',label='Y=2(n/3)')
    plt.xlabel('Tiempo',)
    plt.ylabel('Iteración')
    plt.title('Analisis Asintotico')
    
    aux1=np.array([i])
    grafx1=np.append(grafx1,aux1)
    auxy1=np.array([tiempo])
    grafy1=np.append(grafy1,auxy1)
    
    aux2=np.array([i])
    grafx2=np.append(grafx2,aux2)
    auxy2=np.array([tiempo/10])
    grafy2=np.append(grafy2,auxy2)
    
    aux3=np.array([i])
    grafx3=np.append(grafx3,aux3)
    auxy3=np.array([tiempo*0.5])
    grafy3=np.append(grafy3,auxy3)
    
    aux4=np.array([i])
    grafx4=np.append(grafx4,aux4)
    auxy4=np.array([tiempo**1.5])
    grafy4=np.append(grafy4,auxy4)

    aux5=np.array([i])
    grafx5=np.append(grafx5,aux5)
    auxy5=np.array([2**(tiempo)])
    grafy5=np.append(grafy5,auxy5)
    time.sleep(0.005)

plt.figure(3)
plt.grid()
plt.plot(grafx1,grafy1,color='tab:orange',label='Y=n')
plt.plot(grafx2,grafy2,color='tab:purple',label='Y=n/10')
plt.plot(grafx3,grafy3,color='tab:gray',label='Y=0.5n')
plt.plot(grafx4,grafy4,color='tab:cyan',label='Y=1**1.5')
plt.plot(grafx5,grafy5,color='tab:pink',label='Y=2**n')
plt.xlabel('Iteración')
plt.ylabel('Tiempo')
plt.title('Tiempo-Iteración')
plt.legend();   
print('Salidas:')    
print(salida6)
print(salida7)
print(salida8)
print('\n')
fin=time.time()
print(fin-inicio)