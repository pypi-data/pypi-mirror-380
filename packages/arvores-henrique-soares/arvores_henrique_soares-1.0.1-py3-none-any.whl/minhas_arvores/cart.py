"""CART: Gini, sempre binário, binarização por combinações (limitada)"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any, Union, Optional, Tuple, Set
from collections import Counter
from itertools import combinations

from .arvore_base import NoArvore
from .utilidades import (
    calcular_gini,
    calcular_impureza_ponderada_gini,
    encontrar_melhor_limiar
)


class CART:
    """CART: Binarização categórica = testa combinações (max 100 por eficiência)"""

    def __init__(self,
                 profundidade_maxima: Optional[int] = None,
                 min_amostras_divisao: int = 4,
                 min_amostras_folha: int = 2):
        self.arvore_raiz = None
        self.profundidade_maxima = profundidade_maxima
        self.min_amostras_divisao = min_amostras_divisao
        self.min_amostras_folha = min_amostras_folha
        self.atributos_continuos = set()

    def fit(self, X: Union[pd.DataFrame, Dict], y: Union[List, np.ndarray, pd.Series]) -> 'CART':
        """
        Treina a árvore de decisão CART com os dados fornecidos.

        Args:
            X: Dados de entrada (features). DataFrame pandas ou dict
            y: Rótulos de saída (target)

        Returns:
            self: Instância treinada do classificador
        """
        # Validar e normalizar entrada
        if isinstance(X, dict):
            X = pd.DataFrame([X])
        elif not isinstance(X, pd.DataFrame):
            raise ValueError("X deve ser um DataFrame pandas ou dicionário")

        if len(X) != len(y):
            raise ValueError("X e y devem ter o mesmo número de amostras")

        if len(X) == 0:
            raise ValueError("Conjunto de dados não pode estar vazio")

        # Identificar atributos contínuos
        self._identificar_tipos_atributos(X)

        # Construir árvore recursivamente
        self.arvore_raiz = self._construir_arvore(
            X=X.copy(),
            y=list(y),
            profundidade=0
        )

        return self

    def predict(self, X: Union[pd.DataFrame, Dict, List[Dict]]) -> List[Any]:
        """
        Prediz as classes para as amostras fornecidas.

        Args:
            X: Dados para predição

        Returns:
            List: Lista com as classes preditas
        """
        if self.arvore_raiz is None:
            raise ValueError("Modelo deve ser treinado antes da predição")

        # Normalizar entrada
        if isinstance(X, dict):
            X_df = pd.DataFrame([X])
        elif isinstance(X, pd.DataFrame):
            X_df = X.copy()
        elif isinstance(X, list):
            X_df = pd.DataFrame(X)
        else:
            raise ValueError(
                "X deve ser DataFrame, dicionário ou lista de dicionários")

        # Predizer para cada amostra
        predicoes = []
        for _, row in X_df.iterrows():
            predicao = self.arvore_raiz.predizer_amostra(row.to_dict())
            predicoes.append(predicao)

        return predicoes

    def _identificar_tipos_atributos(self, X: pd.DataFrame) -> None:
        """
        Identifica quais atributos são contínuos (numéricos) ou categóricos.

        Args:
            X: DataFrame com os dados
        """
        self.atributos_continuos = set()

        for coluna in X.columns:
            if (pd.api.types.is_numeric_dtype(X[coluna]) and
                    not pd.api.types.is_bool_dtype(X[coluna])):
                # Considerar contínuo se tem muitos valores únicos ou é float
                valores_unicos = X[coluna].nunique()
                if valores_unicos > 10 or X[coluna].dtype == 'float64':
                    self.atributos_continuos.add(coluna)

    def _construir_arvore(self,
                          X: pd.DataFrame,
                          y: List[Any],
                          profundidade: int) -> NoArvore:
        """
        Constrói a árvore de decisão recursivamente usando o algoritmo CART.

        Args:
            X: DataFrame com os dados de entrada
            y: Lista com os rótulos
            profundidade: Profundidade atual na árvore

        Returns:
            NoArvore: Nó construído (interno ou folha)
        """
        # Criar nó e atualizar estatísticas
        no = NoArvore(profundidade=profundidade)
        no.atualizar_estatisticas(y)

        # Critérios de parada
        if (len(set(y)) <= 1 or  # Uma classe apenas
            # Poucas amostras para divisão
            len(y) < self.min_amostras_divisao or
            len(X.columns) == 0 or  # Sem atributos
            (self.profundidade_maxima is not None and
             profundidade >= self.profundidade_maxima)):  # Profundidade máxima
            no.eh_folha = True
            return no

        # Encontrar melhor divisão binária
        melhor_resultado = self._encontrar_melhor_divisao(X, y)

        # Se não encontrou divisão válida ou ganho é insignificante, criar folha
        if melhor_resultado is None:
            no.eh_folha = True
            return no

        atributo, valor_split, condicao_esquerda, condicao_direita = melhor_resultado

        # Aplicar divisão
        mask_esquerda, mask_direita = self._aplicar_divisao(
            X, atributo, valor_split, condicao_esquerda
        )

        # Verificar se divisão é válida (ambos os lados devem ter amostras)
        if (mask_esquerda.sum() < self.min_amostras_folha or
                mask_direita.sum() < self.min_amostras_folha):
            no.eh_folha = True
            return no

        # Configurar nó interno
        no.atributo_split = atributo
        no.valor_split = valor_split
        no.eh_folha = False

        # Criar subconjuntos
        X_esquerda = X[mask_esquerda].reset_index(drop=True)
        y_esquerda = [y[i] for i in range(len(y)) if mask_esquerda.iloc[i]]

        X_direita = X[mask_direita].reset_index(drop=True)
        y_direita = [y[i] for i in range(len(y)) if mask_direita.iloc[i]]

        # Construir subárvores recursivamente
        no_esquerda = self._construir_arvore(
            X_esquerda, y_esquerda, profundidade + 1)
        no_direita = self._construir_arvore(
            X_direita, y_direita, profundidade + 1)

        # Adicionar filhos com as condições apropriadas
        no.adicionar_filho(condicao_esquerda, no_esquerda)
        no.adicionar_filho(condicao_direita, no_direita)

        return no

    def _encontrar_melhor_divisao(self,
                                  X: pd.DataFrame,
                                  y: List[Any]) -> Optional[Tuple[str, Any, str, str]]:
        """
        Encontra a melhor divisão binária considerando todos os atributos.

        Args:
            X: DataFrame com os dados
            y: Lista com os rótulos

        Returns:
            Tuple ou None: (atributo, valor_split, condicao_esq, condicao_dir) ou None
        """
        melhor_atributo = None
        melhor_valor_split = None
        melhor_reducao_gini = 0.0
        melhor_condicao_esquerda = None
        melhor_condicao_direita = None

        gini_atual = calcular_gini(y)

        for atributo in X.columns:
            if atributo in self.atributos_continuos:
                # Atributo contínuo: buscar melhor limiar
                resultado = self._melhor_divisao_continua(X[atributo], y)
                if resultado is not None:
                    limiar, reducao_gini = resultado
                    if reducao_gini > melhor_reducao_gini:
                        melhor_reducao_gini = reducao_gini
                        melhor_atributo = atributo
                        melhor_valor_split = limiar
                        melhor_condicao_esquerda = f"<= {limiar}"
                        melhor_condicao_direita = f"> {limiar}"
            else:
                # Atributo categórico: buscar melhor binarização
                resultado = self._melhor_divisao_categorica(X[atributo], y)
                if resultado is not None:
                    grupos_esquerda, reducao_gini = resultado
                    if reducao_gini > melhor_reducao_gini:
                        melhor_reducao_gini = reducao_gini
                        melhor_atributo = atributo
                        melhor_valor_split = grupos_esquerda
                        melhor_condicao_esquerda = f"in {list(grupos_esquerda)}"
                        melhor_condicao_direita = f"not in {list(grupos_esquerda)}"

        if melhor_atributo is None:
            return None

        return (melhor_atributo, melhor_valor_split,
                melhor_condicao_esquerda, melhor_condicao_direita)

    def _melhor_divisao_continua(self,
                                 valores: pd.Series,
                                 y: List[Any]) -> Optional[Tuple[float, float]]:
        """
        Encontra a melhor divisão para um atributo contínuo.

        Args:
            valores: Series com valores do atributo contínuo
            y: Lista com os rótulos

        Returns:
            Tuple ou None: (limiar, redução_gini) ou None se não há melhoria
        """
        limiar, ganho = encontrar_melhor_limiar(valores, y, criterio='gini')

        # Só aceita divisão se ganho é significativo (> 0.01)
        if ganho > 0.01:
            return limiar, ganho
        return None

    def _melhor_divisao_categorica(self,
                                   valores: pd.Series,
                                   y: List[Any]) -> Optional[Tuple[Set, float]]:
        """
        Encontra a melhor binarização para um atributo categórico.

        Para atributos categóricos, o CART testa todas as possíveis formas
        de dividir os valores em dois grupos e escolhe a que minimiza o Gini.

        Args:
            valores: Series com valores do atributo categórico
            y: Lista com os rótulos

        Returns:
            Tuple ou None: (conjunto_valores_esquerda, redução_gini) ou None
        """
        valores_unicos = list(valores.unique())

        # Se só há um valor único, não podemos dividir
        if len(valores_unicos) <= 1:
            return None

        melhor_grupo_esquerda = None
        melhor_reducao_gini = 0.0
        gini_atual = calcular_gini(y)

        # Testar todas as possíveis divisões binárias
        # Para N valores únicos, temos 2^(N-1) - 1 divisões possíveis
        # Limitamos a busca para evitar explosão combinatória
        max_combinacoes = min(2**(len(valores_unicos)-1) - 1, 100)

        for tamanho_grupo in range(1, len(valores_unicos)):
            # Testar combinações de diferentes tamanhos
            combinacoes = list(combinations(valores_unicos, tamanho_grupo))

            # Limitar número de combinações para eficiência
            if len(combinacoes) > max_combinacoes // tamanho_grupo:
                combinacoes = combinacoes[:max_combinacoes // tamanho_grupo]

            for grupo_esquerda in combinacoes:
                grupo_esquerda_set = set(grupo_esquerda)

                # Dividir dados
                mask_esquerda = valores.isin(grupo_esquerda_set)

                y_esquerda = [y[i]
                              for i in range(len(y)) if mask_esquerda.iloc[i]]
                y_direita = [y[i]
                             for i in range(len(y)) if not mask_esquerda.iloc[i]]

                # Verificar se divisão é válida
                if len(y_esquerda) == 0 or len(y_direita) == 0:
                    continue

                # Calcular Gini ponderado após divisão
                n_total = len(y)
                gini_depois = (len(y_esquerda) / n_total * calcular_gini(y_esquerda) +
                               len(y_direita) / n_total * calcular_gini(y_direita))

                # Calcular redução no Gini
                reducao_gini = gini_atual - gini_depois

                # Atualizar melhor divisão se ganho é significativo
                if reducao_gini > melhor_reducao_gini and reducao_gini > 0.01:
                    melhor_reducao_gini = reducao_gini
                    melhor_grupo_esquerda = grupo_esquerda_set

        # Só retorna se encontrou divisão com ganho significativo
        if melhor_grupo_esquerda is None or melhor_reducao_gini <= 0.01:
            return None

        return melhor_grupo_esquerda, melhor_reducao_gini

    def _aplicar_divisao(self,
                         X: pd.DataFrame,
                         atributo: str,
                         valor_split: Any,
                         condicao_esquerda: str) -> Tuple[pd.Series, pd.Series]:
        """
        Aplica a divisão aos dados baseada no atributo e valor de split.

        Args:
            X: DataFrame com os dados
            atributo: Nome do atributo para divisão
            valor_split: Valor ou conjunto de valores para divisão
            condicao_esquerda: String descrevendo a condição da esquerda

        Returns:
            Tuple[pd.Series, pd.Series]: (mask_esquerda, mask_direita)
        """
        if atributo in self.atributos_continuos:
            # Divisão contínua
            mask_esquerda = X[atributo] <= valor_split
        else:
            # Divisão categórica
            if isinstance(valor_split, set):
                mask_esquerda = X[atributo].isin(valor_split)
            else:
                # Fallback para outros tipos
                mask_esquerda = X[atributo] == valor_split

        mask_direita = ~mask_esquerda
        return mask_esquerda, mask_direita

    def imprimir_arvore(self) -> str:
        """
        Retorna uma representação textual da árvore treinada.

        Returns:
            str: Representação da árvore em formato de texto
        """
        if self.arvore_raiz is None:
            raise ValueError(
                "Modelo deve ser treinado antes de imprimir a árvore")

        return f"Árvore CART:\n{self.arvore_raiz.imprimir_arvore()}"

    def obter_estatisticas(self) -> Dict[str, Any]:
        """
        Retorna estatísticas sobre a árvore construída.

        Returns:
            Dict: Dicionário com estatísticas da árvore
        """
        if self.arvore_raiz is None:
            return {"erro": "Modelo não treinado"}

        contagem_nos = self.arvore_raiz.contar_nos()
        prof_maxima = self.arvore_raiz.calcular_profundidade_maxima()

        return {
            "algoritmo": "CART",
            "criterio": "Índice Gini",
            "tipo_divisao": "Binária",
            "profundidade_maxima": prof_maxima,
            "total_nos": contagem_nos["total"],
            "nos_internos": contagem_nos["internos"],
            "nos_folha": contagem_nos["folhas"],
            "atributos_continuos": list(self.atributos_continuos),
            "min_amostras_divisao": self.min_amostras_divisao,
            "min_amostras_folha": self.min_amostras_folha
        }

    def calcular_importancia_atributos(self) -> Dict[str, float]:
        """
        Calcula a importância de cada atributo baseada na redução de impureza.

        Returns:
            Dict[str, float]: Dicionário com importância de cada atributo
        """
        if self.arvore_raiz is None:
            return {}

        importancias = {}

        def calcular_importancia_no(no: NoArvore, n_amostras_total: int):
            if not no.eh_no_folha() and no.atributo_split:
                # Calcular redução de impureza neste nó
                reducao_impureza = 0.0

                # Gini antes da divisão
                gini_antes = calcular_gini([no.classe_predita] * no.n_amostras)

                # Gini após divisão (ponderado)
                gini_depois = 0.0
                for filho in no.filhos.values():
                    peso = filho.n_amostras / no.n_amostras
                    gini_filho = calcular_gini(
                        [filho.classe_predita] * filho.n_amostras)
                    gini_depois += peso * gini_filho

                reducao_impureza = gini_antes - gini_depois

                # Ponderar pela proporção de amostras
                peso_no = no.n_amostras / n_amostras_total
                importancia = peso_no * reducao_impureza

                # Adicionar à importância do atributo
                if no.atributo_split not in importancias:
                    importancias[no.atributo_split] = 0.0
                importancias[no.atributo_split] += importancia

                # Recursivamente calcular para filhos
                for filho in no.filhos.values():
                    calcular_importancia_no(filho, n_amostras_total)

        calcular_importancia_no(self.arvore_raiz, self.arvore_raiz.n_amostras)

        # Normalizar importâncias (somar 1.0)
        total_importancia = sum(importancias.values())
        if total_importancia > 0:
            for atributo in importancias:
                importancias[atributo] /= total_importancia

        return importancias
