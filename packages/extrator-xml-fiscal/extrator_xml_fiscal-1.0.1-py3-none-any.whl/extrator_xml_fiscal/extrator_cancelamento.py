from typing import Dict, Any
from .extrator_evento_base import ExtratorEventoBase
from . import utils


class ExtratorCancelamento(ExtratorEventoBase):
    """
    Extrator específico para Cancelamento de NFe.

    Processa arquivos XML de eventos de cancelamento e extrai dados estruturados.
    """

    def _extrair_dados(self, dados_xml: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extrai dados do Cancelamento com validação de tipo ANTES do processamento.

        Args:
            dados_xml (Dict[str, Any]): XML do evento convertido para dicionário

        Returns:
            Dict[str, Any]: Dados estruturados do evento

        Raises:
            ValueError: Se não for um evento de cancelamento
        """
        # VALIDA TIPO PRIMEIRO - antes de processar qualquer coisa
        raiz_evento = self._encontrar_raiz_evento(dados_xml)
        tipo_evento = raiz_evento.get('tpEvento')

        if tipo_evento != '110111':
            raise ValueError(f'Tipo de evento {tipo_evento} não é um Cancelamento (esperado: 110111)')

        # Se chegou até aqui, é realmente um cancelamento - processa normalmente
        return {
            'dados_evento': self._extrair_dados_evento(raiz_evento),
            'dados_protocolo': self._extrair_protocolo(dados_xml),
            'dados_especificos': self._extrair_dados_especificos(raiz_evento)
        }

    def _extrair_dados_especificos(self, raiz_evento: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extrai dados específicos do Cancelamento.

        Args:
            raiz_evento (Dict[str, Any]): Dados do infEvento

        Returns:
            Dict[str, Any]: Dados específicos do cancelamento
        """
        det_evento = raiz_evento.get('detEvento', {})

        return {
            'descricao_evento': det_evento.get('descEvento'),
            'numero_protocolo_nfe': det_evento.get('nProt'),
            'justificativa': utils.limpar_texto(det_evento.get('xJust')),
            'versao_layout': det_evento.get('@versao')
        }
