# -*- coding: utf-8 -*-
"""
NEXUS AI - Dashboard Engine
Visualização de métricas e telemetria de processos em tempo real.
Autor: Adriana Sousa
"""

import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_telemetry():
    """Simula a captura de dados de performance do sistema"""
    metrics = {
        "CPU_LOAD": f"{random.randint(15, 45)}%",
        "RAM_USAGE": f"{random.randint(2, 8)}GB",
        "AI_CORE_TEMP": f"{random.randint(40, 65)}°C",
        "ACTIVE_AGENTS": random.randint(3, 12)
    }
    return metrics

def display_dashboard():
    print("="*50)
    print("      NEXUS AI - PERFORMANCE MONITORING")
    print("="*50)
    
    try:
        while True:
            data = generate_telemetry()
            clear_screen()
            print(f"\n[SISTEMA OPERACIONAL: ONLINE]")
            print(f"Horário de Brasília: {time.strftime('%H:%M:%S')}\n")
            
            for key, value in data.items():
                print(f" > {key.ljust(15)}: {value}")
                
            print("\n" + "-"*50)
            print("Pressione CTRL+C para encerrar a monitorização.")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[INFO] Dashboard encerrado pela operadora.")

if __name__ == "__main__":
    display_dashboard()
