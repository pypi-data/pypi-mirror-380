"""Estrutura base para nós das árvores de decisão"""

from typing import Dict, Any, List, Union, Optional
import pandas as pd


class NoArvore:
    """Nó de árvore - pode ser interno (divisão) ou folha (predição)"""

    def __init__(self,
                 classe_predita: Any = None,
                 atributo_split: Optional[str] = None,
                 valor_split: Any = None,
                 profundidade: int = 0):
        self.atributo_split = atributo_split
        self.valor_split = valor_split
        self.filhos = {}
        self.classe_predita = classe_predita
        self.eh_folha = atributo_split is None
        self.profundidade = profundidade
        self.n_amostras = 0
        self.distribuicao_classes = {}

    def adicionar_filho(self, condicao: Any, no_filho: 'NoArvore') -> None:
        """
        Adiciona um nó filho baseado em uma condição.

        Args:
            condicao: Valor ou condição que leva a este filho
                     (ex: 'ensolarado', True, False, '>= 25')
            no_filho: Nó filho a ser adicionado
        """
        self.filhos[condicao] = no_filho
        no_filho.profundidade = self.profundidade + 1

    def eh_no_folha(self) -> bool:
        """
        Verifica se o nó é uma folha.

        Returns:
            bool: True se for folha, False caso contrário
        """
        return self.eh_folha or len(self.filhos) == 0

    def predizer_amostra(self, amostra: Union[Dict, pd.Series]) -> Any:
        """Prediz classe atravessando a árvore"""
        if self.eh_no_folha():
            return self.classe_predita

        if isinstance(amostra, dict):
            valor_atributo = amostra.get(self.atributo_split)
        else:
            valor_atributo = amostra[self.atributo_split] if self.atributo_split in amostra.index else None

        if valor_atributo is None:
            return self.classe_predita

        proximo_no = self._encontrar_proximo_no(valor_atributo)

        if proximo_no is None:
            return self.classe_predita

        return proximo_no.predizer_amostra(amostra)

    def _encontrar_proximo_no(self, valor_atributo: Any) -> Optional['NoArvore']:
        """Encontra próximo nó - busca direta ou condições numéricas/categóricas"""
        if valor_atributo in self.filhos:
            return self.filhos[valor_atributo]

        for condicao, no_filho in self.filhos.items():
            if isinstance(condicao, str):
                # Condições CART categóricas: "in ['valor1', 'valor2']" ou "not in ['valor1']"
                if condicao.startswith('in [') or condicao.startswith('not in ['):
                    try:
                        import ast
                        if condicao.startswith('in ['):
                            # Extrair lista de valores: "in ['valor1', 'valor2']" -> ['valor1', 'valor2']
                            lista_str = condicao[3:]  # Remove "in "
                            valores = ast.literal_eval(lista_str)
                            if valor_atributo in valores:
                                return no_filho
                        elif condicao.startswith('not in ['):
                            # Extrair lista de valores: "not in ['valor1']" -> ['valor1']
                            lista_str = condicao[7:]  # Remove "not in "
                            valores = ast.literal_eval(lista_str)
                            if valor_atributo not in valores:
                                return no_filho
                    except (ValueError, SyntaxError):
                        continue

                # Condições numéricas
                elif condicao.startswith('>=') or condicao.startswith('>'):
                    try:
                        if '>=' in condicao:
                            limiar = float(condicao.split('>=')[1].strip())
                            if valor_atributo >= limiar:
                                return no_filho
                        elif '>' in condicao:
                            limiar = float(condicao.split('>')[1].strip())
                            if valor_atributo > limiar:
                                return no_filho
                    except (ValueError, IndexError):
                        continue

                elif condicao.startswith('<=') or condicao.startswith('<'):
                    try:
                        if '<=' in condicao:
                            limiar = float(condicao.split('<=')[1].strip())
                            if valor_atributo <= limiar:
                                return no_filho
                        elif '<' in condicao:
                            limiar = float(condicao.split('<')[1].strip())
                            if valor_atributo < limiar:
                                return no_filho
                    except (ValueError, IndexError):
                        continue

            # Para condições booleanas diretas
            elif isinstance(condicao, bool):
                if condicao and hasattr(self, 'valor_split') and self.valor_split is not None:
                    if valor_atributo >= self.valor_split:
                        return no_filho
                elif not condicao and hasattr(self, 'valor_split') and self.valor_split is not None:
                    if valor_atributo < self.valor_split:
                        return no_filho

        return None

    def imprimir_arvore(self, prefixo: str = "", eh_ultimo: bool = True) -> str:
        """
        Gera uma representação em texto da árvore a partir deste nó.

        Args:
            prefixo: Prefixo para indentação
            eh_ultimo: Se é o último filho do nó pai

        Returns:
            str: Representação textual da árvore
        """
        resultado = []

        # Símbolo do nó atual
        simbolo = "└── " if eh_ultimo else "├── "

        # Informação do nó atual
        if self.eh_no_folha():
            info_no = f"FOLHA: {self.classe_predita} (n={self.n_amostras})"
        else:
            info_no = f"{self.atributo_split}"
            if self.valor_split is not None:
                info_no += f" (limiar: {self.valor_split})"
            info_no += f" (n={self.n_amostras})"

        resultado.append(f"{prefixo}{simbolo}{info_no}")

        # Adicionar informação sobre distribuição de classes se disponível
        if self.distribuicao_classes:
            dist_str = ", ".join([f"{classe}: {count}"
                                  for classe, count in self.distribuicao_classes.items()])
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")
            resultado.append(f"{novo_prefixo}Classes: [{dist_str}]")

        # Recursivamente imprimir filhos
        if not self.eh_no_folha():
            filhos_lista = list(self.filhos.items())
            novo_prefixo = prefixo + ("    " if eh_ultimo else "│   ")

            for i, (condicao, filho) in enumerate(filhos_lista):
                eh_ultimo_filho = (i == len(filhos_lista) - 1)
                resultado.append(
                    f"{novo_prefixo}{'└── ' if eh_ultimo_filho else '├── '}{condicao}:")
                resultado.append(filho.imprimir_arvore(
                    novo_prefixo + ("    " if eh_ultimo_filho else "│   "),
                    True
                ))

        return "\n".join(resultado)

    def atualizar_estatisticas(self, y: List[Any]) -> None:
        """
        Atualiza as estatísticas do nó baseado nos rótulos.

        Args:
            y: Lista de rótulos das amostras que chegaram a este nó
        """
        from collections import Counter

        self.n_amostras = len(y)
        self.distribuicao_classes = dict(Counter(y))

        # Atualizar classe predita para a mais frequente
        if self.distribuicao_classes:
            self.classe_predita = max(self.distribuicao_classes.items(),
                                      key=lambda x: x[1])[0]

    def calcular_profundidade_maxima(self) -> int:
        """
        Calcula a profundidade máxima da subárvore a partir deste nó.

        Returns:
            int: Profundidade máxima da subárvore
        """
        if self.eh_no_folha():
            return self.profundidade

        profundidade_maxima = self.profundidade
        for filho in self.filhos.values():
            prof_filho = filho.calcular_profundidade_maxima()
            profundidade_maxima = max(profundidade_maxima, prof_filho)

        return profundidade_maxima

    def contar_nos(self) -> Dict[str, int]:
        """
        Conta o número de nós na subárvore.

        Returns:
            Dict: Dicionário com contagem de nós internos, folhas e total
        """
        if self.eh_no_folha():
            return {'internos': 0, 'folhas': 1, 'total': 1}

        contagem = {'internos': 1, 'folhas': 0, 'total': 1}

        for filho in self.filhos.values():
            cont_filho = filho.contar_nos()
            contagem['internos'] += cont_filho['internos']
            contagem['folhas'] += cont_filho['folhas']
            contagem['total'] += cont_filho['total']

        return contagem
