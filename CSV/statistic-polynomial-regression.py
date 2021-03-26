# lendo a planilha
df7 = pd.read_csv(
    "https://drive.google.com/u/1/uc?id=1ZNKsK1dGsDiGDU3841yA-MdK1H3QSdxc&export=download")
nota1 = df7["Exame 1"]
nota2 = df7["Exame 2"]

# obtendo coeficientes da curva
(a, b, c, d) = np.polyfit(x=nota1, y=nota2, deg=3)  # especificando o grau 3

# coef de determinação
predicao = a*nota1**3 + b*nota1**2 + c*nota1 + d  # usar o X
# obtendo a relacao entre a predicao e a nota 2
dif = (nota2-predicao)**2
media = nota2.mean()
dif_media = (nota2-media)**2
# coef de determinação
cdet = 1 - dif.sum() / dif_media.sum()
print(cdet)
