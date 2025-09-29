"""C4.5: Razão de ganho, categóricos + contínuos, trata missing values"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any, Union, Optional, Tuple
from collections import Counter

from .arvore_base import NoArvore
from .utilidades import (
    calcular_entropia,
    calcular_razao_ganho,
    encontrar_melhor_limiar,
    calcular_ganho_informacao
)


class C45:
    """C4.5: Missing values = média/moda, contínuos = >10 valores únicos"""

    def __init__(self,
                 profundidade_maxima: Optional[int] = None,
                 min_amostras_divisao: int = 2):
        self.arvore_raiz = None
        self.profundidade_maxima = profundidade_maxima
        self.min_amostras_divisao = min_amostras_divisao
        self.atributos_continuos = set()
        self._valores_preenchimento = {}  # Para tratar missing values

    def fit(self, X: Union[pd.DataFrame, Dict], y: Union[List, np.ndarray, pd.Series]) -> 'C45':
        """
        Treina a árvore de decisão C4.5 com os dados fornecidos.

        Args:
            X: Dados de entrada (features). DataFrame pandas ou dict
            y: Rótulos de saída (target)

        Returns:
            self: Instância treinada do classificador

        Note:
            O C4.5 detecta automaticamente atributos contínuos (numéricos) e
            categóricos (object/string). Missing values são tratados durante o fit.
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

        # Fazer cópia para não modificar dados originais
        X = X.copy()

        # Identificar atributos contínuos e categóricos
        self._identificar_tipos_atributos(X)

        # Tratar valores ausentes
        X = self._tratar_valores_ausentes(X)

        # Construir árvore recursivamente
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

        # Tratar valores ausentes usando valores aprendidos no treino
        X_df = self._aplicar_preenchimento_valores(X_df)

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
            # Considerar contínuo se for numérico e não booleano
            if (pd.api.types.is_numeric_dtype(X[coluna]) and
                    not pd.api.types.is_bool_dtype(X[coluna])):
                # Verificar se não é um categórico disfarçado (poucos valores únicos)
                valores_unicos = X[coluna].nunique()
                # Se tem muitos valores únicos, provavelmente é contínuo
                if valores_unicos > 10 or X[coluna].dtype == 'float64':
                    self.atributos_continuos.add(coluna)

    def _tratar_valores_ausentes(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Trata valores ausentes substituindo por moda (categóricos) ou média (contínuos).

        Args:
            X: DataFrame com possíveis valores ausentes

        Returns:
            pd.DataFrame: DataFrame com valores ausentes preenchidos
        """
        X_tratado = X.copy()
        self._valores_preenchimento = {}

        for coluna in X.columns:
            if X[coluna].isnull().any():
                if coluna in self.atributos_continuos:
                    # Para contínuos: usar média
                    valor_preenchimento = X[coluna].mean()
                else:
                    # Para categóricos: usar moda
                    valor_preenchimento = X[coluna].mode(
                    )[0] if not X[coluna].mode().empty else X[coluna].iloc[0]

                self._valores_preenchimento[coluna] = valor_preenchimento
                X_tratado[coluna].fillna(valor_preenchimento, inplace=True)

        return X_tratado

    def _aplicar_preenchimento_valores(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Aplica o preenchimento de valores ausentes usando valores aprendidos no treino.

        Args:
            X: DataFrame com dados de teste

        Returns:
            pd.DataFrame: DataFrame com valores preenchidos
        """
        X_tratado = X.copy()

        for coluna, valor in self._valores_preenchimento.items():
            if coluna in X_tratado.columns and X_tratado[coluna].isnull().any():
                X_tratado[coluna].fillna(valor, inplace=True)

        return X_tratado

    def _construir_arvore(self,
                          X: pd.DataFrame,
                          y: List[Any],
                          atributos_disponiveis: List[str],
                          profundidade: int) -> NoArvore:
        """
        Constrói a árvore de decisão recursivamente usando o algoritmo C4.5.

        Args:
            X: DataFrame com os dados de entrada
            y: Lista com os rótulos
            atributos_disponiveis: Lista de atributos disponíveis para divisão
            profundidade: Profundidade atual na árvore

        Returns:
            NoArvore: Nó construído (interno ou folha)
        """
        # Criar nó e atualizar estatísticas
        no = NoArvore(profundidade=profundidade)
        no.atualizar_estatisticas(y)

        # Critérios de parada
        if (len(set(y)) <= 1 or  # Uma classe apenas
            not atributos_disponiveis or  # Sem atributos
            len(y) < self.min_amostras_divisao or  # Poucas amostras
            (self.profundidade_maxima is not None and
             profundidade >= self.profundidade_maxima)):  # Profundidade máxima
            no.eh_folha = True
            return no

        # Encontrar melhor atributo para divisão
        melhor_resultado = self._encontrar_melhor_atributo(
            X, y, atributos_disponiveis)

        if melhor_resultado is None:
            no.eh_folha = True
            return no

        melhor_atributo, valor_split, eh_continuo = melhor_resultado

        # Configurar nó interno
        no.atributo_split = melhor_atributo
        no.valor_split = valor_split if eh_continuo else None
        no.eh_folha = False

        if eh_continuo:
            # Divisão binária para atributo contínuo
            self._criar_divisao_binaria(no, X, y, melhor_atributo, valor_split,
                                        atributos_disponiveis, profundidade)
        else:
            # Divisão multi-ramificada para atributo categórico
            self._criar_divisao_categorica(no, X, y, melhor_atributo,
                                           atributos_disponiveis, profundidade)

        return no

    def _encontrar_melhor_atributo(self,
                                   X: pd.DataFrame,
                                   y: List[Any],
                                   atributos_disponiveis: List[str]) -> Optional[Tuple[str, Any, bool]]:
        """
        Encontra o atributo com maior razão de ganho.

        Args:
            X: DataFrame com os dados
            y: Lista com os rótulos
            atributos_disponiveis: Lista de atributos candidatos

        Returns:
            Tuple ou None: (atributo, valor_split, eh_continuo) ou None se nenhum ganho
        """
        melhor_atributo = None
        melhor_valor_split = None
        melhor_razao_ganho = 0.0
        melhor_eh_continuo = False

        for atributo in atributos_disponiveis:
            if atributo in self.atributos_continuos:
                # Atributo contínuo: buscar melhor limiar
                limiar, ganho = encontrar_melhor_limiar(
                    X[atributo], y, criterio='razao_ganho'
                )

                if ganho > melhor_razao_ganho:
                    melhor_razao_ganho = ganho
                    melhor_atributo = atributo
                    melhor_valor_split = limiar
                    melhor_eh_continuo = True
            else:
                # Atributo categórico: calcular razão de ganho
                razao_ganho = self._calcular_razao_ganho_categorico(
                    X, y, atributo)

                if razao_ganho > melhor_razao_ganho:
                    melhor_razao_ganho = razao_ganho
                    melhor_atributo = atributo
                    melhor_valor_split = None
                    melhor_eh_continuo = False

        if melhor_atributo is None:
            return None

        return melhor_atributo, melhor_valor_split, melhor_eh_continuo

    def _calcular_razao_ganho_categorico(self,
                                         X: pd.DataFrame,
                                         y: List[Any],
                                         atributo: str) -> float:
        """
        Calcula a razão de ganho para um atributo categórico.

        Args:
            X: DataFrame com os dados
            y: Lista com os rótulos
            atributo: Nome do atributo categórico

        Returns:
            float: Razão de ganho do atributo
        """
        # Dividir dados por valores do atributo
        splits = []
        valores_unicos = X[atributo].unique()

        for valor in valores_unicos:
            mask = X[atributo] == valor
            y_subset = [y[i] for i in range(len(y)) if mask.iloc[i]]
            if len(y_subset) > 0:
                splits.append(y_subset)

        # Calcular razão de ganho
        return calcular_razao_ganho(y, splits)

    def _criar_divisao_binaria(self,
                               no: NoArvore,
                               X: pd.DataFrame,
                               y: List[Any],
                               atributo: str,
                               limiar: float,
                               atributos_disponiveis: List[str],
                               profundidade: int) -> None:
        """
        Cria divisão binária para atributo contínuo.

        Args:
            no: Nó pai que receberá os filhos
            X: DataFrame com dados
            y: Lista de rótulos
            atributo: Nome do atributo contínuo
            limiar: Valor do limiar para divisão
            atributos_disponiveis: Atributos disponíveis para próximas divisões
            profundidade: Profundidade atual
        """
        # Dividir dados baseado no limiar
        mask_esquerda = X[atributo] <= limiar
        mask_direita = X[atributo] > limiar

        # Dados do lado esquerdo (<= limiar)
        X_esquerda = X[mask_esquerda].reset_index(drop=True)
        y_esquerda = [y[i] for i in range(len(y)) if mask_esquerda.iloc[i]]

        # Dados do lado direito (> limiar)
        X_direita = X[mask_direita].reset_index(drop=True)
        y_direita = [y[i] for i in range(len(y)) if mask_direita.iloc[i]]

        # Criar nós filhos
        if len(y_esquerda) > 0:
            no_esquerda = self._construir_arvore(
                X_esquerda, y_esquerda, atributos_disponiveis, profundidade + 1
            )
            no.adicionar_filho(f"<= {limiar}", no_esquerda)

        if len(y_direita) > 0:
            no_direita = self._construir_arvore(
                X_direita, y_direita, atributos_disponiveis, profundidade + 1
            )
            no.adicionar_filho(f"> {limiar}", no_direita)

    def _criar_divisao_categorica(self,
                                  no: NoArvore,
                                  X: pd.DataFrame,
                                  y: List[Any],
                                  atributo: str,
                                  atributos_disponiveis: List[str],
                                  profundidade: int) -> None:
        """
        Cria divisão multi-ramificada para atributo categórico.

        Args:
            no: Nó pai que receberá os filhos
            X: DataFrame com dados
            y: Lista de rótulos
            atributo: Nome do atributo categórico
            atributos_disponiveis: Atributos disponíveis (menos o atual)
            profundidade: Profundidade atual
        """
        valores_unicos = X[atributo].unique()
        novos_atributos = [
            attr for attr in atributos_disponiveis if attr != atributo]

        for valor in valores_unicos:
            # Filtrar dados para este valor
            mask = X[atributo] == valor
            X_subset = X[mask].reset_index(drop=True)
            y_subset = [y[i] for i in range(len(y)) if mask.iloc[i]]

            if len(y_subset) > 0:
                no_filho = self._construir_arvore(
                    X_subset, y_subset, novos_atributos, profundidade + 1
                )
            else:
                # Criar folha com classe mais comum do pai
                no_filho = NoArvore(profundidade=profundidade + 1)
                no_filho.classe_predita = no.classe_predita
                no_filho.eh_folha = True

            no.adicionar_filho(valor, no_filho)

    def imprimir_arvore(self) -> str:
        """
        Retorna uma representação textual da árvore treinada.

        Returns:
            str: Representação da árvore em formato de texto
        """
        if self.arvore_raiz is None:
            raise ValueError(
                "Modelo deve ser treinado antes de imprimir a árvore")

        return f"Árvore C4.5:\n{self.arvore_raiz.imprimir_arvore()}"

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
            "algoritmo": "C4.5",
            "criterio": "Razão de Ganho",
            "profundidade_maxima": prof_maxima,
            "total_nos": contagem_nos["total"],
            "nos_internos": contagem_nos["internos"],
            "nos_folha": contagem_nos["folhas"],
            "atributos_continuos": list(self.atributos_continuos),
            "missing_values_tratados": bool(self._valores_preenchimento)
        }
