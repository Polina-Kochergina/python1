from scipy.fft import fft, ifft
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np
import random as r


def mapping(values_x, a, b): 
    y = []
    for i in range(len(values_x)):
        y.append(a*values_x[i] + b)
    return y

def correlogram(N3):
    c = (ifft(np.abs(X)**2).real/N)[0:N3]
    return c

def smoothed_periodogram(N3, c, k):    
    Cm = []
    Wm = []

    for j in range(N3):
        Wm = np.append(Wm, (1 -2*a) + 2*a*np.cos(np.pi*j/N3))
        Cm = np.append(Cm, c[j]*Wm[j])

    for i in range(N2-len(c)):
        Cm = np.append(Cm, 0)

    Cm_fft = fft(Cm)
    Dj = (2*Cm_fft.real/N3 - Cm_fft[0]/N3)[:N1+1]

    axes[k][1].plot(nu, Dj, color = "crimson", linewidth = 1.3,)
    axes[k][1].set_title(f"Сглаженная периодограмма (N* = N/{int(N/N3)}, a = 0.25)")


# дано:
dt = 1; N = 230; q = 0.01
X1 = 9.0; A1 = 1; nu1 = 0.1
phi1 = 0; gamma = 0.50
alpha = 0.1; beta = 0.05
sigma_n = np.sqrt((A1**2)/(2*gamma))

t = [ k*dt for k in range(N) ]

eps = [r.normalvariate(0,1) for i in range(N)]

# модельный ряд 
x = [alpha + beta*t[k] + A1*np.cos(2*np.pi*nu1*t[k]-phi1) + sigma_n*eps[k] for k in range(N)]


# исключение тренда и центрирование ряда
popt, _ = curve_fit(mapping, t, x)
a, b = popt

y = mapping(t, a, b)
x_new = [x[i] - y[i] for i in range(N)]

#5 оценивание дисперсии
sigma2 = 0
for i in range(len(x_new)):
    sigma2 = sigma2 + x_new[i]**2
sigma2 = sigma2/(N-1)

print(sigma2)



# 4 вычисление периодограммы
N1 = 512
N2 = 2*N1

for i in range(N2-N):
    x_new = np.append(x_new, 0)

X = fft(x_new)
print(len(X))

D = []
nu = []
dnu = 1/(N2*dt)
for j in range(N1 + 1):
    D = np.append(D, (np.abs(X[j])/N)**2)
    nu = np.append(nu, j*dnu)

q = sigma2*X1/N


# 7 коррелограмма
N3 = int(N/10)
N4 = int(N/2)
a = 0.25
c1 = correlogram(N3)
c2 = correlogram(N4)

# строим графики:

fig, axes = plt.subplots(ncols=2, nrows=3, figsize=(25, 12))
axes[0][0].plot(t, x, color = "crimson", linewidth = 1.3)
axes[0][0].set_title("График модельного ряда")
axes[1][0].plot(t, x_new[0:230], color = "crimson", linewidth = 1.3,)
axes[1][0].set_title("График центрированного ряда")
axes[2][0].plot(t[:N4], c2, color = "crimson", linewidth = 1.3,)
axes[2][0].set_title("График смещенной функции коррелограммы")
axes[2][0].set_xlabel("Time, s")

axes[0][1].set_title("Периодограмма Шустера модельного ряда и 99%-й порог обнаружения сигнала в шумах")
axes[0][1].plot(nu, D, color = "crimson", linewidth = 1.3,)
axes[0][1].axhline(y = q)
axes[2][1].set_xlabel("Frequency, 1/s")

# 9-11 взвешенная коррелограмма и сглаженная периодограмма
smoothed_periodogram(N3, c1, 1)
smoothed_periodogram(N4, c2, 2)


plt.savefig("image1.png")
plt.show()