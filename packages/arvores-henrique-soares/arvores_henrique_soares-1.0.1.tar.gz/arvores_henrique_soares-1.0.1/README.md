# Árvores de Decisão - Henrique Soares

[![PyPI version](https://badge.fury.io/py/arvores-henrique-soares.svg)](https://badge.fury.io/py/arvores-henrique-soares)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Implementação educacional completa dos algoritmos de árvore de decisão **ID3**, **C4.5** e **CART** desenvolvidos do zero em Python.

Esta biblioteca foi criada como material educacional para demonstrar o funcionamento interno dos algoritmos de árvore de decisão, incluindo todas as etapas matemáticas e lógicas de construção das árvores.

## 🚀 Instalação

```bash
pip install arvores-henrique-soares
```

### Dependências

- Python 3.7+
- NumPy >= 1.19.0
- Pandas >= 1.1.0
- Scikit-learn >= 0.24.0

## 📚 Uso Básico

### Exemplo Simples

```python
from minhas_arvores import ID3, C45, CART
import pandas as pd

# Dados de exemplo
dados = pd.DataFrame({
    'Tempo': ['Sol', 'Sol', 'Nublado', 'Chuva', 'Chuva'],
    'Temperatura': ['Quente', 'Quente', 'Quente', 'Frio', 'Frio'],
    'Humidade': ['Alta', 'Alta', 'Alta', 'Normal', 'Normal'],
    'Vento': ['Fraco', 'Forte', 'Fraco', 'Fraco', 'Forte'],
    'Jogar': ['Não', 'Não', 'Sim', 'Sim', 'Não']
})

X = dados[['Tempo', 'Temperatura', 'Humidade', 'Vento']]
y = dados['Jogar']

# Treinar modelo ID3
modelo = ID3()
modelo.fit(X, y)

# Fazer predição
resultado = modelo.predict({'Tempo': 'Sol', 'Temperatura': 'Quente', 
                          'Humidade': 'Normal', 'Vento': 'Fraco'})
print(f"Predição: {resultado}")

# Visualizar árvore
modelo.imprimir_arvore()
```

### Exemplo com Dados Contínuos (C4.5 e CART)

```python
from minhas_arvores import C45, CART
import pandas as pd

# Dados com atributos contínuos
dados = pd.DataFrame({
    'idade': [25, 35, 45, 55, 65],
    'salario': [35000, 45000, 55000, 65000, 75000],
    'aprovado': ['Não', 'Não', 'Sim', 'Sim', 'Sim']
})

X = dados[['idade', 'salario']]
y = dados['aprovado']

# C4.5 - suporta atributos contínuos
c45 = C45()
c45.fit(X, y)
predicao_c45 = c45.predict({'idade': 40, 'salario': 50000})

# CART - divisões binárias
cart = CART()
cart.fit(X, y)
predicao_cart = cart.predict({'idade': 40, 'salario': 50000})
```

## 📊 Algoritmos Implementados

### ID3 (Iterative Dichotomiser 3)

- **Critério**: Ganho de Informação
- **Tipos de Dados**: Apenas categóricos
- **Características**: Algoritmo clássico, simples e eficiente para dados categóricos

### C4.5

- **Critério**: Razão de Ganho (Gain Ratio)
- **Tipos de Dados**: Categóricos e contínuos
- **Características**:
  - Suporta valores ausentes
  - Discretização automática de atributos contínuos
  - Poda de árvore para evitar overfitting

### CART (Classification and Regression Trees)

- **Critério**: Índice de Gini
- **Tipos de Dados**: Categóricos e contínuos
- **Características**:
  - Divisões binárias apenas
  - Robusto e eficiente
  - Base para algoritmos como Random Forest

## 🔧 Exemplo Completo

Execute o script de exemplo incluído:

```bash
git clone https://github.com/HenriqueSoares28/lista4_ia.git
cd lista4_ia
python exemplo_uso.py
```

## 📈 Comparação de Performance

O projeto inclui testes com o dataset Titanic e comparação com scikit-learn:

| Algoritmo | Acurácia | Características |
|-----------|----------|-----------------|
| ID3       | 100%*    | Dados categóricos simples |
| C4.5      | 100%*    | Suporte a contínuos |
| CART      | 85.7%    | Divisões binárias robustas |

*Resultados no dataset Play Tennis (categórico)

## 🏗️ Estrutura do Projeto

```text
minhas_arvores/
├── __init__.py          # Exportações da biblioteca
├── id3.py              # Algoritmo ID3
├── c45.py              # Algoritmo C4.5
├── cart.py             # Algoritmo CART
├── arvore_base.py      # Classe base para nós da árvore
└── utilidades.py       # Funções matemáticas auxiliares
```

## 🤝 Contribuições

Contribuições são bem-vindas! Este projeto tem fins educacionais e pode ser expandido com:

- Novos algoritmos de árvore de decisão
- Métodos de poda mais avançados
- Visualizações gráficas das árvores
- Mais datasets de exemplo

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

### Henrique Soares

- GitHub: [@HenriqueSoares28](https://github.com/HenriqueSoares28)
- Projeto: [lista4_ia](https://github.com/HenriqueSoares28/lista4_ia)

---

*Desenvolvido como projeto educacional para demonstrar a implementação de algoritmos de árvore de decisão do zero.*

