# 🏗️ Word Tower

Jogo de palavras multijogador em tempo real com sistema de eliminação por timeout

[![PyPI version](https://badge.fury.io/py/word-tower-game.svg)](https://badge.fury.io/py/word-tower-game)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Sobre

**Word Tower** é um jogo de palavras multijogador em tempo real onde os jogadores devem formar uma torre de palavras conectadas. Cada palavra deve começar com a última letra da palavra anterior, criando uma cadeia contínua de palavras.

### ✨ Características

- 🌐 **Multijogador em tempo real** via WebSocket
- ⏱️ **Sistema de timeout** - seja rápido ou seja eliminado!
- 🎯 **Validação de palavras** automática
- 📱 **Interface web responsiva** 
- 🎮 **Fácil de jogar**, difícil de dominar

---

## 🚀 Instalação

**Pré-requisitos:**
- Python 3.8+ ([download aqui](https://www.python.org/downloads/))

**Instalação via PyPI:**

```bash
pip install word-tower-game
```

**Executar o jogo:**

```bash
word-tower
```

O servidor será iniciado em `http://localhost:8000`

---

## 🎮 Como Jogar

1. **Acesse** o jogo no navegador
2. **Crie ou entre** em uma sala
3. **Aguarde** outros jogadores se conectarem
4. **Digite palavras** que começem com a última letra da palavra anterior
5. **Seja rápido** - você tem tempo limitado para responder!
6. **Último jogador** restante vence!

---

## 🛠️ Tecnologias

### Backend
- **Python 3.8+** - Linguagem principal
- **FastAPI** - Framework web moderno
- **Socket.IO** - Comunicação em tempo real
- **Uvicorn** - Servidor ASGI

### Frontend
- **Vue.js 3** - Framework reativo
- **TypeScript** - Tipagem estática
- **Pinia** - Gerenciamento de estado
- **Vite** - Build tool

---

## 📚 Projeto Acadêmico

Este projeto foi desenvolvido como parte da disciplina **Programação I** do curso de **Ciência da Computação** da **Universidade Federal de Campina Grande (UFCG)**.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

**Word Tower** © 2025
