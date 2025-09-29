"""ID3: Ganho de informação, apenas categóricos, divisões multi-ramificadas"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any, Union, Optional
from collections import Counter

from .arvore_base import NoArvore
from .utilidades import calcular_entropia, calcular_ganho_informacao


class ID3:
    """ID3: Ganho de informação, categóricos, decisão de empate = primeiro encontrado"""

    def __init__(self, profundidade_maxima: Optional[int] = None):
        self.arvore_raiz = None
        self.atributos_usados = []
        self.profundidade_maxima = profundidade_maxima

    def fit(self, X: Union[pd.DataFrame, Dict], y: Union[List, np.ndarray, pd.Series]) -> 'ID3':
        """Treina ID3 - assume atributos categóricos"""
        if isinstance(X, dict):
            X = pd.DataFrame([X])
        elif not isinstance(X, pd.DataFrame):
            raise ValueError("X deve ser um DataFrame pandas ou dicionário")

        if len(X) != len(y):
            raise ValueError("X e y devem ter o mesmo número de amostras")

        if len(X) == 0:
            raise ValueError("Conjunto de dados não pode estar vazio")

        self.atributos_usados = []

        self.arvore_raiz = self._construir_arvore(
            X=X,
            y=list(y),
            atributos_disponiveis=list(X.columns),
            profundidade=0
        )

        return self

    def predict(self, X: Union[pd.DataFrame, Dict, List[Dict]]) -> List[Any]:
        """
        Prediz as classes para as amostras fornecidas.

        Args:
            X: Dados para predição. Pode ser:
               - DataFrame pandas
               - Dicionário (única amostra)  
               - Lista de dicionários (múltiplas amostras)

        Returns:
            List: Lista com as classes preditas

        Raises:
            ValueError: Se o modelo não foi treinado
        """
        if self.arvore_raiz is None:
            raise ValueError(
                "Modelo deve ser treinado antes da predição. Use fit() primeiro.")

        # Normalizar entrada
        if isinstance(X, dict):
            amostras = [X]
        elif isinstance(X, pd.DataFrame):
            amostras = [row.to_dict() for _, row in X.iterrows()]
        elif isinstance(X, list):
            amostras = X
        else:
            raise ValueError(
                "X deve ser DataFrame, dicionário ou lista de dicionários")

        # Predizer para cada amostra
        predicoes = []
        for amostra in amostras:
            predicao = self.arvore_raiz.predizer_amostra(amostra)
            predicoes.append(predicao)

        return predicoes

    def _construir_arvore(self,
                          X: pd.DataFrame,
                          y: List[Any],
                          atributos_disponiveis: List[str],
                          profundidade: int) -> NoArvore:
        """
        Constrói a árvore de decisão recursivamente usando o algoritmo ID3.

        Args:
            X: DataFrame com os dados de entrada
            y: Lista com os rótulos
            atributos_disponiveis: Lista de atributos ainda disponíveis para divisão
            profundidade: Profundidade atual na árvore

        Returns:
            NoArvore: Nó construído (pode ser interno ou folha)
        """
        # Criar nó e atualizar estatísticas
        no = NoArvore(profundidade=profundidade)
        no.atualizar_estatisticas(y)

        # Critério de parada 1: Todas as amostras têm a mesma classe
        classes_unicas = set(y)
        if len(classes_unicas) <= 1:
            no.eh_folha = True
            return no

        # Critério de parada 2: Não há mais atributos disponíveis
        if not atributos_disponiveis:
            no.eh_folha = True
            return no

        # Critério de parada 3: Profundidade máxima atingida
        if (self.profundidade_maxima is not None and
                profundidade >= self.profundidade_maxima):
            no.eh_folha = True
            return no

        # Critério de parada 4: Muito poucas amostras
        if len(y) <= 1:
            no.eh_folha = True
            return no

        # Encontrar melhor atributo para divisão
        melhor_atributo = self._encontrar_melhor_atributo(
            X, y, atributos_disponiveis)

        # Se nenhum atributo oferece ganho, criar folha
        if melhor_atributo is None:
            no.eh_folha = True
            return no

        # Configurar nó interno
        no.atributo_split = melhor_atributo
        no.eh_folha = False

        # Obter valores únicos do melhor atributo
        valores_atributo = X[melhor_atributo].unique()

        # Criar nó filho para cada valor do atributo
        novos_atributos = [
            attr for attr in atributos_disponiveis if attr != melhor_atributo]

        for valor in valores_atributo:
            # Filtrar dados para este valor
            mask = X[melhor_atributo] == valor
            X_subset = X[mask].reset_index(drop=True)
            y_subset = [y[i] for i in range(len(y)) if mask.iloc[i]]

            # Se não há amostras para este valor, criar folha com classe mais comum
            if len(y_subset) == 0:
                no_filho = NoArvore(profundidade=profundidade + 1)
                no_filho.classe_predita = no.classe_predita  # Usar classe do pai
                no_filho.eh_folha = True
            else:
                # Construir subárvore recursivamente
                no_filho = self._construir_arvore(
                    X=X_subset,
                    y=y_subset,
                    atributos_disponiveis=novos_atributos,
                    profundidade=profundidade + 1
                )

            no.adicionar_filho(valor, no_filho)

        return no

    def _encontrar_melhor_atributo(self,
                                   X: pd.DataFrame,
                                   y: List[Any],
                                   atributos_disponiveis: List[str]) -> Optional[str]:
        """
        Encontra o atributo com maior ganho de informação.

        Args:
            X: DataFrame com os dados
            y: Lista com os rótulos
            atributos_disponiveis: Lista de atributos candidatos

        Returns:
            str ou None: Nome do melhor atributo ou None se nenhum oferece ganho
        """
        melhor_atributo = None
        melhor_ganho = 0.0

        for atributo in atributos_disponiveis:
            # Calcular ganho de informação para este atributo
            ganho = self._calcular_ganho_atributo(X, y, atributo)

            # Atualizar melhor atributo (em caso de empate, mantém o primeiro)
            if ganho > melhor_ganho:
                melhor_ganho = ganho
                melhor_atributo = atributo

        return melhor_atributo

    def _calcular_ganho_atributo(self,
                                 X: pd.DataFrame,
                                 y: List[Any],
                                 atributo: str) -> float:
        """
        Calcula o ganho de informação para um atributo específico.

        Args:
            X: DataFrame com os dados
            y: Lista com os rótulos
            atributo: Nome do atributo

        Returns:
            float: Ganho de informação do atributo
        """
        # Dividir dados por valores do atributo
        splits = []
        valores_unicos = X[atributo].unique()

        for valor in valores_unicos:
            mask = X[atributo] == valor
            y_subset = [y[i] for i in range(len(y)) if mask.iloc[i]]
            if len(y_subset) > 0:  # Apenas adicionar se não estiver vazio
                splits.append(y_subset)

        # Calcular ganho de informação
        return calcular_ganho_informacao(y, splits)

    def imprimir_arvore(self) -> str:
        """
        Retorna uma representação textual da árvore treinada.

        Returns:
            str: Representação da árvore em formato de texto

        Raises:
            ValueError: Se o modelo não foi treinado
        """
        if self.arvore_raiz is None:
            raise ValueError(
                "Modelo deve ser treinado antes de imprimir a árvore")

        return f"Árvore ID3:\n{self.arvore_raiz.imprimir_arvore()}"

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
            "algoritmo": "ID3",
            "criterio": "Ganho de Informação",
            "profundidade_maxima": prof_maxima,
            "total_nos": contagem_nos["total"],
            "nos_internos": contagem_nos["internos"],
            "nos_folha": contagem_nos["folhas"],
            "atributos_utilizados": len(set(self._obter_atributos_utilizados()))
        }

    def _obter_atributos_utilizados(self) -> List[str]:
        """
        Obtém lista de todos os atributos utilizados na árvore.

        Returns:
            List[str]: Lista de atributos utilizados
        """
        atributos = []

        def percorrer_no(no: NoArvore):
            if not no.eh_no_folha() and no.atributo_split:
                atributos.append(no.atributo_split)
                for filho in no.filhos.values():
                    percorrer_no(filho)

        if self.arvore_raiz:
            percorrer_no(self.arvore_raiz)

        return atributos
