# 🏗️ Word Tower# 🏗️ Word Tower

**Jogo de palavras multijogador em tempo real com sistema de eliminação por timeout\*\***Jogo de palavras multijogador em tempo real com sistema de eliminação por timeout\*\*

[![PyPI version](https://badge.fury.io/py/word-tower-game.svg)](https://badge.fury.io/py/word-tower-game)[![PyPI version](https://badge.fury.io/py/word-tower-game.svg)](https://badge.fury.io/py/word-tower-game)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---_Projeto desenvolvido para a disciplina de Programação I (Ciência da Computação - UFCG, Campina Grande)_

## 🚀 Instalação e Uso---

### 📋 Pré-requisitos## 🚀 Instalação Rápida (PyPI)

- **Python 3.8+** ([Download](https://www.python.org/downloads/))### 📋 Pré-requisitos

### ⚡ Instalação- **Python 3.8+** ([Download](https://www.python.org/downloads/))

```````bash### ⚡ Instalação em um comando

pip install word-tower-game

``````bash

pip install word-tower-game

### ▶️ Executar```



```bash### ▶️ Executar

word-tower

``````bash

word-tower

🎉 **Pronto!** O jogo abrirá automaticamente no seu navegador em `http://localhost:8000````



---🎉 **Pronto!** O jogo abrirá automaticamente no seu navegador em `http://localhost:8000`



## 🎮 Como Jogar---



### 🚪 Entrando no Jogo## 🛠️ Instalação para Desenvolvimento



1. **Crie uma sala** ou **entre em uma existente** usando o código### 📋 Pré-requisitos para Desenvolvimento

2. **Aguarde outros jogadores** (mínimo 2 para iniciar)

3. **Host inicia o jogo** quando todos estiverem prontos- **Python 3.8+** ([Download](https://www.python.org/downloads/))

- **Node.js 20+** ([Download](https://nodejs.org/))

### 🎯 Objetivo

### 🔧 Setup de Desenvolvimento

Formar uma "torre de palavras" onde cada palavra deve começar com a **última letra** da palavra anterior.

```bash

### ⏰ Sistema de Tempo# 1. Clone o projeto

git clone https://github.com/KJSS3012/word-tower.git

- **30 segundos** por turno (configurável)cd word-tower

- **Timer visual** mostra tempo restante

- **Eliminação automática** quando tempo esgota# 2. Instalar dependências Python

pip install -r requirements.txt

### 🏆 Vitória

# 3. Instalar dependências Node.js

- **Último jogador ativo** vence a rodadacd front

- **Jogo reinicia** automaticamente para nova partidanpm install



---# 4. Build do frontend

npm run build

## 📝 Regras do Jogo

# 5. Voltar para raiz e executar

### ✅ Palavra Válidacd ..

python -m app.main

- Deve começar com a **letra correta**```

- Deve ser uma **palavra real** (verificada no dicionário)

- **Não pode repetir** palavras já usadas### 🌐 Acessar



### ❌ Palavra InválidaAbra `http://localhost:8000` no navegador e divirta-se!



- **Letra errada**: Eliminação imediata---

- **Palavra inexistente**: Eliminação imediata

- **Palavra repetida**: Eliminação imediata## 🎮 Como Jogar



### 🎲 Dificuldades### 🚪 Entrando no Jogo



| Dificuldade | Dicionário  | Próxima Letra     | Desafio |1. **Crie uma sala** ou **entre em uma existente** usando o código

| ----------- | ----------- | ----------------- | ------- |2. **Aguarde outros jogadores** (mínimo 2 para iniciar)

| **Fácil**   | Sem acentos | Última letra      | ⭐      |3. **Host inicia o jogo** quando todos estiverem prontos

| **Normal**  | Com acentos | Última letra      | ⭐⭐    |

| **Caótico** | Com acentos | Posição aleatória | ⭐⭐⭐  |### 🎯 Objetivo



---Formar uma "torre de palavras" onde cada palavra deve começar com a **última letra** da palavra anterior.



## 💻 Tecnologias### ⏰ Sistema de Tempo



- **Backend**: Python 3.8+ com FastAPI e Socket.IO- **30 segundos** por turno (configurável)

- **Frontend**: Vue 3 + TypeScript- **Timer visual** mostra tempo restante

- **Real-time**: WebSocket para comunicação instantânea- **Eliminação automática** quando tempo esgota

- **Multiplayer**: Suporte para 2-8 jogadores por sala

### 🏆 Vitória

---

- **Último jogador ativo** vence a rodada

## 🎓 Sobre- **Jogo reinicia** automaticamente para nova partida



**Projeto Acadêmico**---



- **Disciplina**: Programação I## 📝 Regras do Jogo

- **Instituição**: Universidade Federal de Campina Grande (UFCG)

- **Curso**: Ciência da Computação### ✅ Palavra Válida



**Word Tower** © 2025 - Licença MIT- Deve começar com a **letra correta**
- Deve ser uma **palavra real** (verificada no dicionário)
- **Não pode repetir** palavras já usadas

### ❌ Palavra Inválida

- **Letra errada**: Eliminação imediata
- **Palavra inexistente**: Eliminação imediata
- **Palavra repetida**: Eliminação imediata

### 🎲 Dificuldades

| Dificuldade | Dicionário  | Próxima Letra     | Desafio |
| ----------- | ----------- | ----------------- | ------- |
| **Fácil**   | Sem acentos | Última letra      | ⭐      |
| **Normal**  | Com acentos | Última letra      | ⭐⭐    |
| **Caótico** | Com acentos | Posição aleatória | ⭐⭐⭐  |

---

## � Distribuição

### PyPI Package

O Word Tower está disponível como um pacote Python no PyPI, facilitando a instalação e distribuição:

- **Package Name**: `word-tower-game`
- **Entry Point**: `word-tower` (comando global após instalação)
- **Inclui**: Backend Python + Frontend Vue.js pré-compilado
- **Auto-start**: Abre automaticamente o navegador
- **Porta**: Detecta automaticamente porta livre (padrão: 8000)

### Como funciona

1. **Instalação**: `pip install word-tower-game`
2. **Execução**: `word-tower`
3. **Backend + Frontend**: Servidor único serve tanto API quanto arquivos estáticos
4. **WebSocket**: Comunicação real-time integrada
5. **Auto-browser**: Abre automaticamente `http://localhost:8000`

---

## �💻 Tecnologias

### Backend

- **Python 3.8+**: Linguagem principal
- **Socket.IO**: Comunicação em tempo real
- **uvicorn**: Servidor ASGI para WebSockets
- **AsyncIO**: Programação assíncrona para timers

### Frontend

- **Vue 3**: Framework reativo moderno
- **TypeScript**: Tipagem estática
- **Pinia**: Gerenciamento de estado
- **Socket.IO Client**: Comunicação real-time

### Comunicação

- **WebSocket**: Tempo real para gameplay
- **JSON**: Formato de troca de dados

---

## 📦 Dependências

### PyPI Package (Automáticas)

```txt
fastapi>=0.104.1              # Framework web moderno
uvicorn[standard]>=0.24.0     # Servidor ASGI
python-socketio>=5.10.0       # Socket.IO real-time
python-multipart>=0.0.6       # Upload de arquivos
jinja2>=3.1.2                 # Template engine
aiofiles>=23.2.1              # Arquivos assíncronos
```````

### Frontend (Pré-compilado no PyPI)

```json
{
  "vue": "^3.5.18", // Framework reativo
  "typescript": "latest", // Tipagem estática
  "pinia": "^3.0.3", // Estado global
  "socket.io-client": "^4.8.1", // WebSocket client
  "vite": "^6.0.3" // Build tool
}
```

---

## 🎓 Créditos

**Projeto Acadêmico**

- **Disciplina**: Programação I
- **Instituição**: Universidade Federal de Campina Grande (UFCG)
- **Curso**: Ciência da Computação

**Word Tower** © 2025
