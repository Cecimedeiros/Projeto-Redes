# Documento de Planejamento Inicial

## Tema
Aplicação web simples para monitoramento simulado de serviços de rede.

## Objetivo / Escopo
- Página local mostrando status simulado (UP/DOWN), latência e uptime percentual.
- API `/status` retornando JSON com os estados atuais.
- Simulador em memória (thread) que atualiza a cada 5s.

## Tecnologias
- Python 3.8+
- Flask
- HTML + Bootstrap (CDN)
- Threading para simulação

## Divisão de Tarefas (sugestão)
- Backend: simulador + endpoints
- Frontend: template + polling JS
- Documentação/Entrega: README e arquivos zip

## Critérios de Aceitação
- Página local exibindo serviços simulados e atualizando.
- Instruções e dependências fornecidas.
