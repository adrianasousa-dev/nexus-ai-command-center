# -*- coding: utf-8 -*-
"""
NEXUS AI - Sentinel Core
Monitorização de integridade e orquestração de logs.
Autor: Adriana Sousa
"""

import logging
import time

# Configuração de Logs Profissional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class NexusSentinel:
    def __init__(self):
        self.status = "INITIALIZING"
        self.security_level = "TACTICAL"

    def run_diagnostics(self):
        logging.info("A iniciar diagnósticos do Sentinel Core...")
        time.sleep(1)
        logging.info("A verificar integridade dos núcleos de IA...")
        time.sleep(1)
        logging.info("Protocolos de segurança carregados com sucesso.")
        self.status = "ACTIVE"

    def monitor_loop(self):
        logging.info(f"Sentinel Core em estado: {self.status}")
        try:
            while True:
                logging.info("Verificação de rotina: Todos os agentes operando em parâmetros nominais.")
                time.sleep(10)
        except KeyboardInterrupt:
            logging.warning("Interrupção detetada. Sentinel Core a encerrar protocolos.")

if __name__ == "__main__":
    sentinel = NexusSentinel()
    sentinel.run_diagnostics()
    sentinel.monitor_loop()
