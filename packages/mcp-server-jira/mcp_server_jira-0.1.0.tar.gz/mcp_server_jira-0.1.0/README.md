# Jira Um servidor Model Context Protocol (MCP) que fornece integração com Jira, permitindo que LLMs interajam com issues, executem transições, adicionem worklogs e realizem buscas usando a API REST do Jira.

## 📦 Instalação

### Via PyPI (Recomendado)
```bash
pip install mcp-server-jira
```

### Via GitHub
```bash
pip install git+https://github.com/your-username/mcp-jira-v3.git
```

### Desenvolvimento
```bash
git clone https://github.com/your-username/mcp-jira-v3.git
cd mcp-jira-v3
pip install -e .
```

## 🚀 Uso Rápido

```bash
# Executar com token padrão
mcp-server-jira --jira-token "SEU_TOKEN_AQUI"

# Executar com URL customizada
mcp-server-jira --jira-base-url "https://jira.sua-empresa.com" --jira-token "SEU_TOKEN"

# Ajuda
mcp-server-jira --help
```

## 📋 O que é o Projeto Server

[![PyPI version](https://badge.fury.io/py/mcp-server-jira.svg)](https://badge.fury.io/py/mcp-server-jira)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/mcp-server-jira)](https://pepy.tech/project/mcp-server-jira)

Um servidor Model Context Protocol (MCP) que fornece integração com Jira, permitindo que LLMs interajam com issues, executem transições, adicionem worklogs e realizem buscas usando a API REST do Jira.

## � O que é o Projeto

Este é um servidor MCP que atua como ponte entre Large Language Models (LLMs) e o Jira, oferecendo automação de tarefas e consultas através de comandos em linguagem natural.

## ⚡ Funcionalidades

O servidor oferece 5 ferramentas principais:

### 1. `get_issue` - Consultar Issue
- **Ação**: Obtém informações detalhadas de uma issue do Jira
- **Parâmetros**: `issue_key` (ex: "PROJ-123"), `token` (opcional)

### 2. `get_transitions` - Listar Transições
- **Ação**: Lista transições disponíveis para uma issue
- **Parâmetros**: `issue_key`, `token` (opcional)

### 3. `transition_issue` - Executar Transição
- **Ação**: Executa uma transição na issue (muda status)
- **Parâmetros**: `issue_key`, `transition_id`, `token` (opcional)

### 4. `add_worklog` - Adicionar Worklog
- **Ação**: Adiciona registro de trabalho à issue
- **Parâmetros**: `issue_key`, `time_spent` (ex: "2h 30m"), `description`, `token` (opcional)

### 5. `search_issues` - Buscar Issues
- **Ação**: Busca issues usando JQL (Jira Query Language)
- **Parâmetros**: `jql` (ex: "assignee = currentUser()"), `token` (opcional)

## 🏗️ Arquitetura do Programa

```
mcp-jira-v3/
├── src/mcp_server_jira/
│   ├── __init__.py          # Entry point com função main()
│   └── server.py            # JiraServer class com 5 ferramentas MCP
├── test/
│   └── jira_server_test.py  # Testes unitários completos
├── pyproject.toml           # Configuração do projeto e dependências
└── dist/
    └── mcp_server_jira-0.1.0.tar.gz  # Pacote de distribuição (12.9 KB)
```

**Arquitetura Interna:**
- **JiraServer**: Classe principal que implementa o servidor MCP
- **Modelos Pydantic**: JiraIssue, JiraTransition, WorklogResult, etc.
- **Cliente HTTP**: httpx com SSL bypass para ambientes corporativos
- **Autenticação Flexível**: Token padrão configurável + token por requisição

## 🛠️ Bibliotecas e Frameworks

### Dependências Principais
- **`mcp>=1.0.0`** - Model Context Protocol framework
- **`pydantic>=2.0.0`** - Validação de dados e modelos
- **`httpx>=0.25.0`** - Cliente HTTP assíncrono

### Dependências de Desenvolvimento
- **`pytest>=8.3.3`** - Framework de testes

### Características Técnicas
- **Python 3.10+** - Versão mínima suportada
- **Async/Await** - Programação assíncrona
- **Type Hints** - Tipagem completa
- **SSL Bypass** - Para ambientes corporativos

## 🔧 Como Configurar Ambiente de DEV

### 1. Preparar Ambiente
```bash
# Clone o repositório
git clone <repo-url>
cd mcp-jira-v3

# Instalar Python 3.10+
# Verificar versão
python --version
```

### 2. Instalar Dependências
```bash
# Instalar em modo de desenvolvimento
pip install -e .

# Instalar dependências de teste
pip install pytest
```

### 3. Obter Token Jira
1. Acesse sua conta Jira
2. Vá em **Configurações** → **Segurança** → **Tokens de API**
3. Crie um novo token
4. Copie o token gerado

## 📦 Como Instalar a Aplicação

### Instalação via Pacote Distribuído
```bash
# Instalar do arquivo .tar.gz
pip install mcp_server_jira-0.1.0.tar.gz

# Verificar instalação
mcp-server-jira --help
```

### Verificar Instalação
```bash
# Testar comando básico
mcp-server-jira --jira-base-url "https://jira.exemplo.com" --jira-token "SEU_TOKEN"
```

## ▶️ Como Executar a Aplicação

### Execução Básica
```bash
# Com URL padrão (https://jira.telefonica.com.br)
mcp-server-jira --jira-token "SEU_TOKEN_AQUI"

# Com URL customizada
mcp-server-jira --jira-base-url "https://jira.sua-empresa.com" --jira-token "SEU_TOKEN"

# Sem token padrão (fornecido por requisição)
mcp-server-jira --jira-base-url "https://jira.sua-empresa.com"
```

### Parâmetros Disponíveis
- `--jira-base-url`: URL base do Jira (padrão: https://jira.telefonica.com.br)
- `--jira-token`: Token de autenticação (opcional, pode ser fornecido por requisição)

## 🧪 Como Testar a Aplicação

### Executar Testes Unitários
```bash
# Rodar todos os testes
pytest test/ -v

# Rodar testes específicos
pytest test/jira_server_test.py::TestValidationFunctions -v
```

### Testar Funcionalidade Manualmente
```bash
# Testar ajuda
mcp-server-jira --help

# Testar conexão (substitua pelo seu token)
mcp-server-jira --jira-token "SEU_TOKEN_REAL"
```

## ⚙️ Configuração MCP no VS Code

### Configuração Local (Projeto Específico)

1. **Criar arquivo de configuração local:**
```bash
mkdir .vscode
nano .vscode/mcp.json
```

2. **Adicionar configuração no `.vscode/settings.json`:**
```json
{
	"servers": {
		"mcp-jira-dev":  {
           "command": "py",
             "args": ["-m", "mcp_server_jira", "--jira-token", "SEU TOKEN"]

    }
	},
	"inputs": []
}
```

### Configuração Global (Todos os Projetos)

1. **Abrir configurações globais do VS Code:**
   - Pressione `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (Mac)
   - Digite "Preferences: Open User Settings (JSON)"
   - Selecione para abrir o `settings.json` ou `mcp.json` global

2. **Adicionar configuração no settings.json global:**
```json
{
	"servers": {
		"mcp-jira-dev":  {
           "command": "py",
             "args": ["-m", "mcp_server_jira", "--jira-token", "SEU TOKEN"]

    }
	},
	"inputs": []
}
```

### Configuração Sem Token Padrão (Mais Seguro)
```json
{
	"servers": {
		"mcp-jira-dev":  {
           "command": "py",
             "args": ["-m", "mcp_server_jira"]

    }
	},
	"inputs": []
}
```
*Com esta configuração, você fornecerá o token a cada uso das ferramentas.*

## 📋 Informações do Projeto

- **Versão**: 0.1.0
- **Tamanho**: 12.9 KB
- **Licença**: MIT
- **Python**: 3.10+