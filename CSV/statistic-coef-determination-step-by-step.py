import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pl = pd.read_csv(
    "https://www.dropbox.com/s/lp2xto2f9p424ku/fake-classrooms-correl08.csv?dl=1")
colunay = input()
colunax = pl["Nota Final"]
if(colunay == "Faltas" or colunay == "Horas Estudo"):
    # obtendo coeficientes da curva
    (a, b) = np.polyfit(x=colunax, y=pl[colunay], deg=1)

    # passo a passo
    predicao = a*colunax + b
    # obtendo a relacao entre a predicao e a colunay
    dif = (pl[colunay]-predicao)**2
    media = pl[colunay].mean()
    dif_media = (pl[colunay]-media)**2
    # coef de determinação
    cdet = 1 - dif.sum() / dif_media.sum()
    print('%.2f' % cdet)
else:
    print("Coluna inválida")
