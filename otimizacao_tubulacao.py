import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

"""
Aqui a ideia é otimizar o custo total de uma tubulação com base nas suas equações. Foram dados a vazão, viscosidade, 
a densidade do líquido que irá percorrer na tubulação, o comprimento do tubo, eficiência do motor e algumas constantes
arbitrárias. Com isso chega-se numa função objetivo para que seja minimizada, a fim de verificar qual o diâmetro ótimo
para a tubulação e verificar seu custo mínimo.

"""
# Iniciamos criando uma classe chamada tubulação (aqui podemos alterar as variáveis caso necessário)
class Tubulacao:
    def __init__(self):
        """
        Aqui foram usadas as variáveis propostas e já transformadas para o SI

        """
        self.vazao = 7.00/3600
        self.viscosidade = 2.1/1000
        self.rho = 880
        self.comprimento = 400
        self.n = 1.5
        self.c1 = 320
        self.c2 = 0.5
        self.efic = 0.6
    
    def calcular_custo(self, D):
        """
        Calcula o custo total para um dado diâmetro D (em metros).

        """
        # Diâmetro fisicamente tem que ser positivo e maior que zero
        if D <= 0:
            return np.inf
        
        # a) Geometria e Velocidade
        area = (np.pi * D**2) / 4
        v = self.vazao / area
        
        # b) Número de Reynolds (Re)
        Re = (D * v * self.rho) / self.viscosidade
        
        # c)  Fator de atrito - 10^3 < Re < 10^5
        f = 0.079 * (Re**-0.25)
        
        # d) Queda de pressão na tubulação e Potência
        Delta_P = 2 * f * self.rho * (v**2) * (self.comprimento / D)
        Potencia_W = (self.vazao * Delta_P) / self.efic
        
        # e) Custos
        # Custo de Investimento (Tubulação)
        custo_inv = self.c1 * self.comprimento * (D**self.n)
        
        # Custo Operacional (Bombeamento)
        custo_op = self.c2 * Potencia_W
        
        return custo_inv + custo_op
    
    def otimizacao(self):
        resultado = minimize_scalar(self.calcular_custo)
        return resultado.x, resultado.fun

# Criação de um objeto para realizar a análise
tubo = Tubulacao()
D_otimo, Custo_minimo = tubo.otimizacao() # -> Armazenamos o resultado da otimização em duas variáveis

"""
Plotando o gráfico dos custos com base nos diâmetros de uma tubulação qualquer
"""

# Definir o eixo x de variação do diâmetro
x_axis = np.linspace(0.01, 0.2, 100)

# Definir o eixo y de variação dos valores
y_axis = []

# Loop for para verificar para cada diâmetro no intervalo
for values in x_axis:
    custo = tubo.calcular_custo(values)
    y_axis.append(custo)
print(y_axis)

# Criando o gráfico
plt.figure(figsize=(10,6))

# Destacar o ponto ótimo
plt.scatter([D_otimo*1000], [Custo_minimo], color='black', zorder=5)
plt.annotate(f'Mínimo: {D_otimo*1000:.1f} mm', 
             xy=(D_otimo*1000, Custo_minimo), 
             xytext=(D_otimo*1000 + 5, Custo_minimo + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.plot(x_axis * 1000, y_axis, color='purple', label='Custo Total') # Multipliquei por 1000 para deixar em mm que é o comercial
plt.title('Otimização do Diâmetro')
plt.xlabel('Diâmetro Interno (mm)')
plt.ylabel('Custo Total')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()