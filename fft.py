import numpy
import matplotlib.pyplot as plt

n=1000 #discretização do sinal em n valores
tx=500 #tamanho do intervalo (x) funciona como o período de análise
w=2*numpy.pi/tx #wraping frequency: mantem o sinal todo dentro de apenas uma volta 
t=numpy.linspace(0, tx, n) #retorna o tempos em que as funções serão avaliadas: n vezes entre 0 e tx

#exemplo
signal1=5*numpy.cos(5*w*t)
signal2=2*numpy.cos(30*w*t)
s=signal1+signal2

freq=numpy.fft.fftfreq(n) #mesmo que t, porém em frequência
mascara=freq>0 #limita o gráfico da transformada apenas para "freqências positivas"

fft_calculo=numpy.fft.fft(s) #transformada propriamente dita: 
fft_modulo=2*numpy.abs(fft_calculo/n) #trabalhando com os valores em modulo da função

#Gráfico do sinal
plt.figure(1)
plt.title("Sinal Original")
plt.plot(t,s)

#Gráfico do sinal transformado
plt.figure(2)
plt.title("Transformada de Fourier")
plt.plot(freq[mascara],fft_modulo[mascara])

#Mostra Grafico
plt.show()






