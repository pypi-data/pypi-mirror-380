# ArvoresDecisaoGPRL4

Algoritmos de árvore de decisão em Python: **CART**, **C4.5** e **ID3**.

## Instalação

Para instalar a partir do PyPI:

```sh
pip install ArvoresDecisaoGPRL4
```

## Uso

```python
from ArvoresDecisaoGPRL4 import CART, C45, ID3

# Exemplo de uso com pandas DataFrame
import pandas as pd

# Carregue seus dados
df = pd.read_csv('seuarquivo.csv')
X = df[['feature1', 'feature2', ...]]
y = df['target']

# Treine um modelo
cart = CART(max_depth=5)
cart.fit(X, y)

# Preveja
preds = cart.predict(X)
```

## Algoritmos Disponíveis

- **CART**: Árvore binária, critério Gini.
- **C4.5**: Suporte a atributos contínuos e categóricos, critério Gain Ratio.
- **ID3**: Apenas atributos categóricos, critério Information Gain.

## Parâmetros Principais

- `max_depth`: Profundidade máxima da árvore.
- `min_samples_split`: Mínimo de amostras para dividir um nó.
- `min_samples_leaf`: Mínimo de amostras em uma folha.

## Licença

MIT

---

Desenvolvido por Gustavo Rodrigues.