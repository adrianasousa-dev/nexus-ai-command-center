🚀 Nexus AI Command Center

O Nexus AI Command Center é um motor de orquestração desenvolvido para ambiente Windows, focado na gestão de processos críticos, monitoramento de performance e execução de agentes autônomos.

🧠 Visão Geral

Este sistema atua como o "Cérebro" (Control Plane) de uma infraestrutura de automação local. Ele foi desenhado para inicializar dashboards de performance e núcleos sentinela de forma assíncrona, garantindo que a operação de agentes de IA ocorra em um ambiente estável e monitorado.

🛠️ Funcionalidades Principais

Sentinel Core: Sistema de monitoramento em primeiro plano que verifica a integridade dos processos e a segurança tática.

Performance Dashboard: Execução em background para telemetria de dados e estado térmico/processamento do sistema.

Orquestração Automática: Inicialização inteligente de múltiplos módulos Python através de um único ponto de entrada (Entry Point).

💻 Stack Técnica

Shell Scripting: Batch (Windows CMD) para orquestração de baixo nível e interface de comando.

Backend: Python 3.x para lógica de monitoramento e telemetria.

Interface: CLI (Command Line Interface) tática otimizada para produtividade.

📂 Estrutura do Projeto

INICIAR_NEXUS.bat: O núcleo de inicialização do sistema.

nexus_dashboard.py: Engine de visualização de métricas e performance.

nexus_sentinel.py: Módulo de segurança e integridade de processos.

🚀 Como Executar

Clone este repositório:

git clone [https://github.com/adrianasousa-dev/nexus-ai-command-center.git](https://github.com/adrianasousa-dev/nexus-ai-command-center.git)


Certifique-se de ter o Python 3.x instalado no PATH do sistema.

Execute o arquivo INICIAR_NEXUS.bat como Administrador para garantir todas as permissões de monitoramento.

👩‍💻 Estratégia & Autoria

Adriana Sousa - Product Manager & AI Solutions Architect

"Transformando scripts isolados em centros de comando táticos para automação de larga escala."
