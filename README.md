# 🧠 Simulador de Máquina de Mealy — LFA 2025/2

Projeto desenvolvido para a disciplina de **Linguagens Formais e Autômatos (LFA)**.  
Implementa a simulação de uma **Máquina de Mealy** que lê a descrição formal de um autômato e uma palavra de entrada, gerando como saída uma **imagem PPM (formato P1)**.  

Autor: **Uriel Pacheco de Souza**
Docente: **Karina Girardi Roggia**
Período: **2025/2**

---

## ⚙️ Funcionalidades

- Lê arquivos `.txt` com a especificação de uma Máquina de Mealy (estado inicial, transições e saídas).
- Lê uma palavra de entrada (arquivo `.txt`) com símbolos `{1,2,3,4,. ,N}`.
- Simula a execução da máquina, gerando uma sequência de saídas (`0`, `1` e `\n`).
- Constrói automaticamente uma **imagem PPM (P1)** com base na saída.
- Permite visualizar a imagem diretamente no **Google Colab** ou convertê-la para `.png`.

---

## 📁 Estrutura do projeto

├── mealy.py # Script principal da simulação
├── MM.txt # Arquivo de especificação da Máquina de Mealy
├── w16.txt # Palavra de entrada de exemplo
├── saida.ppm # Saída gerada (imagem em formato PPM)
└── README.md # Este arquivo
