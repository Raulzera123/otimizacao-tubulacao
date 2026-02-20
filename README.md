# Otimização de Custos de Tubagem (Pipeline Cost Optimization) 🚀

Este projeto é uma aplicação de **Otimização Matemática** utilizando Python para resolver um problema clássico de mecânica dos fluidos: encontrar o diâmetro ótimo de uma tubagem que minimize o custo total do projeto, equilibrando os custos de instalação e os custos operacionais de bombagem.

Este algoritmo utiliza o método de otimização escalar da biblioteca `SciPy` para encontrar o ponto de mínimo global da função de custo total.

## 🧮 Modelação Matemática

A função objetivo a ser minimizada é o Custo Total ($C_T$), dependente do diâmetro ($D$):

$$C_T(D) = C_{amor}+ C_{op}$$

Onde:
* $C_{inv}$ é o custo amortizado do material instalado (proporcional ao diâmetro e comprimento).
* $C_{op}$ é o custo operacional (proporcional à potência da bomba requerida para vencer a perda de carga).

O algoritmo calcula a potência requerida ($Pot$) considerando a vazão ($Q$), a densidade ($\rho$), a viscosidade dinâmica ($\mu$), a eficiência do sistema ($\eta$) e a queda de pressão ($\delta$ $P$).

## 🛠️ Tecnologias Utilizadas

O projeto foi estruturado utilizando os princípios de **Programação Orientada a Objetos (POO)** para facilitar a reutilização e manutenção do código.

* **Python 3.12.6**
* **SciPy (`minimize_scalar`):** Algoritmo para encontrar o mínimo da função de custo.
* **NumPy:** Manipulação de arrays e cálculos numéricos.
* **Matplotlib & Seaborn:** Visualização de dados e plotagem da curva de custos.

## 📊 Visualização dos Resultados

O script gera automaticamente um gráfico de linha que ilustra a variação do custo total em função do diâmetro. O ponto ótimo de custo mínimo é destacado no gráfico, providenciando uma validação visual clara do resultado matemático.
