# Minhas Árvores

Implementação educacional dos algoritmos ID3, C4.5 e CART em Python.

## Instalação

```bash
pip install numpy pandas scikit-learn
```

## Uso

```python
from minhas_arvores import ID3, C45, CART
import pandas as pd

dados = pd.DataFrame({
    'Tempo': ['Sol', 'Nublado', 'Chuva'],
    'Jogar': ['Não', 'Sim', 'Sim']
})

X = dados[['Tempo']]
y = dados['Jogar']

# Treinar
id3 = ID3()
id3.fit(X, y)

# Predizer
resultado = id3.predict({'Tempo': 'Sol'})
print(resultado)
```

## Exemplo Completo

```bash
python exemplo_uso.py
```

## Algoritmos

- **ID3**: Ganho de informação, categóricos apenas
- **C4.5**: Razão de ganho, suporta contínuos e missing values  
- **CART**: Gini index, divisões binárias

## Licença

MIT

