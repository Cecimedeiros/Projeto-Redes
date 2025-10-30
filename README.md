# 💻 **Simulator**
> *Monitoramento simulado de serviços de rede em nuvem*

O **Simulator** é um projeto desenvolvido para aplicação dos conceitos estudados na disciplina **Infraestrutura de Comunicação**.  
A proposta é criar uma aplicação web simples que **simula o monitoramento de serviços de rede**, apresentando dados de status, latência e uptime.

---

## 🚀 **Objetivo**
Simular o comportamento de serviços de rede em uma aplicação local, com atualização periódica dos dados e disponibilização via API.

---

## ⚙️ **Tecnologias Utilizadas**
- 🐍 **Python 3.8+**
- 🌐 **Flask** (HTML + Bootstrap via CDN)
- 🧵 **Threading** para simulação periódica

---

## 🧩 **Escopo do Projeto**
- Página web local exibindo:
  - Status simulado: **UP / DOWN**
  - Latência (ms)
  - Uptime percentual  
- Endpoint `/status` retornando **JSON** com os estados atuais  
- Thread de atualização automática a cada **5 segundos**

---

## 🧠 **Divisão de Tarefas**
| Área | Responsabilidade |
|------|------------------|
| **Backend** | Implementação do simulador e endpoints Flask |
| **Frontend** | Criação do template e script de polling (JS) |
| **Documentação / Entrega** | Criação do README e pacote ZIP final |

---

## ✅ **Critérios de Aceitação**
- [x] Página local exibindo corretamente os serviços simulados  
- [x] Atualização automática dos dados  
- [x] API funcional com endpoint `/status`  
- [x] Instruções e dependências documentadas  

---

## 👩‍💻 **Equipe**
| Integrante | Perfil |
|------------|--------|
| <img src="https://github.com/user-attachments/assets/ab3d5f4b-1a84-4660-b6ec-bae496e9dc1a" width="80" style="border-radius:10px;"> | **Beatriz Paredes**<br>[LinkedIn](https://www.linkedin.com/in/beatriz-paredes-do-nascimento-91664a182/) |
| <img src="https://github.com/user-attachments/assets/c3b643ec-ebe1-4c73-991f-b7b60d6045bb" width="80" style="border-radius:10px;"> | **Catarina Loureiro**<br>[LinkedIn](https://www.linkedin.com/in/catarina-virginia-lima-loureiro-xavier-439731338/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) |
| <img src="https://github.com/user-attachments/assets/5c5ebd9a-bd8d-4600-bf45-ae54c9ccd5bc" width="80" style="border-radius:10px;"> | **Cecília Medeiro**
