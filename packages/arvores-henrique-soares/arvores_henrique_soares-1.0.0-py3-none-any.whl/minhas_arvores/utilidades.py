"""Funções matemáticas para ID3, C4.5 e CART"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Union
from collections import Counter


def calcular_entropia(y: Union[List, np.ndarray, pd.Series]) -> float:
    """Calcula entropia: E(S) = -Σ(p_i * log2(p_i))"""
    if len(y) == 0:
        return 0.0

    contadores = Counter(y)
    n_total = len(y)

    entropia = 0.0
    for count in contadores.values():
        if count > 0:
            p = count / n_total
            entropia -= p * np.log2(p)

    return entropia


def calcular_gini(y: Union[List, np.ndarray, pd.Series]) -> float:
    """Calcula índice Gini: Gini(S) = 1 - Σ(p_i²) - usado pelo CART"""
    if len(y) == 0:
        return 0.0

    contadores = Counter(y)
    n_total = len(y)

    gini = 1.0
    for count in contadores.values():
        p = count / n_total
        gini -= p ** 2

    return gini


def calcular_ganho_informacao(y_antes: Union[List, np.ndarray, pd.Series],
                              splits: List[Union[List, np.ndarray, pd.Series]]) -> float:
    """Ganho de informação: E(antes) - Σ(peso * E(split)) - usado por ID3 e C4.5"""
    entropia_antes = calcular_entropia(y_antes)
    n_total = len(y_antes)

    if n_total == 0:
        return 0.0

    entropia_depois = 0.0
    for split in splits:
        if len(split) > 0:
            peso = len(split) / n_total
            entropia_depois += peso * calcular_entropia(split)

    return entropia_antes - entropia_depois


def calcular_razao_ganho(y_antes: Union[List, np.ndarray, pd.Series],
                         splits: List[Union[List, np.ndarray, pd.Series]]) -> float:
    """Razão de ganho = Ganho(S,A) / InfoDivisao(S,A) - evita viés do ID3"""
    ganho_info = calcular_ganho_informacao(y_antes, splits)
    n_total = len(y_antes)

    if n_total == 0 or ganho_info == 0:
        return 0.0

    # Calcular informação de divisão (split information)
    info_divisao = 0.0
    for split in splits:
        if len(split) > 0:
            p = len(split) / n_total
            info_divisao -= p * np.log2(p)

    # Evitar divisão por zero
    if info_divisao == 0:
        return 0.0

    return ganho_info / info_divisao


def encontrar_melhor_limiar(X: Union[List, np.ndarray, pd.Series],
                            y: Union[List, np.ndarray, pd.Series],
                            criterio: str = 'gini') -> Tuple[float, float]:
    """Busca melhor limiar para atributos contínuos testando pontos médios"""
    if len(X) != len(y):
        raise ValueError("X e y devem ter o mesmo comprimento")

    # Converter para arrays numpy para facilitar manipulação
    X_array = np.array(X)
    y_array = np.array(y)

    # Ordenar por valores de X
    indices_ordenados = np.argsort(X_array)
    X_ordenado = X_array[indices_ordenados]
    y_ordenado = y_array[indices_ordenados]

    # Encontrar valores únicos e calcular pontos médios
    valores_unicos = np.unique(X_ordenado)

    if len(valores_unicos) < 2:
        return valores_unicos[0] if len(valores_unicos) == 1 else 0.0, 0.0

    melhor_limiar = 0.0
    melhor_ganho = -float('inf')

    # Testar cada ponto médio entre valores únicos adjacentes
    for i in range(len(valores_unicos) - 1):
        limiar = (valores_unicos[i] + valores_unicos[i + 1]) / 2

        # Dividir dados baseado no limiar
        mask_esquerda = X_ordenado <= limiar
        mask_direita = X_ordenado > limiar

        y_esquerda = y_ordenado[mask_esquerda]
        y_direita = y_ordenado[mask_direita]

        # Pular se uma das divisões estiver vazia
        if len(y_esquerda) == 0 or len(y_direita) == 0:
            continue

        # Calcular ganho baseado no critério escolhido
        if criterio == 'gini':
            # Para Gini, calculamos a redução na impureza
            gini_antes = calcular_gini(y_ordenado)
            n_total = len(y_ordenado)
            gini_depois = (len(y_esquerda) / n_total * calcular_gini(y_esquerda) +
                           len(y_direita) / n_total * calcular_gini(y_direita))
            ganho = gini_antes - gini_depois

        elif criterio == 'entropia':
            ganho = calcular_ganho_informacao(
                y_ordenado, [y_esquerda, y_direita])

        elif criterio == 'razao_ganho':
            ganho = calcular_razao_ganho(y_ordenado, [y_esquerda, y_direita])

        else:
            raise ValueError(f"Critério '{criterio}' não reconhecido. "
                             "Use 'gini', 'entropia' ou 'razao_ganho'.")

        # Atualizar melhor limiar se necessário
        if ganho > melhor_ganho:
            melhor_ganho = ganho
            melhor_limiar = limiar

    return melhor_limiar, melhor_ganho


def calcular_impureza_ponderada_gini(grupos: List[Union[List, np.ndarray, pd.Series]]) -> float:
    """Gini ponderado: Σ(peso_grupo * Gini(grupo)) - usado pelo CART"""
    n_total = sum(len(grupo) for grupo in grupos)

    if n_total == 0:
        return 0.0

    impureza_ponderada = 0.0
    for grupo in grupos:
        if len(grupo) > 0:
            peso = len(grupo) / n_total
            impureza_ponderada += peso * calcular_gini(grupo)

    return impureza_ponderada
