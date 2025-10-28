# 🎬 Sistema de Vendas de Ingressos de Cinema

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Sistema completo de gerenciamento de vendas de ingressos de cinema com painel administrativo e design responsivo**

[Demo ao Vivo](https://cinema-ingressos.onrender.com) • [Reportar Bug](https://github.com/CostaCodesFullStack/cinema-ingressos/issues) • [Solicitar Feature](https://github.com/CostaCodesFullStack/cinema-ingressos/issues)

</div>

---

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Arquitetura](#-arquitetura)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [API Endpoints](#-api-endpoints)
- [Capturas de Tela](#-capturas-de-tela)
- [Roadmap](#-roadmap)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🎯 Sobre o Projeto

O **Sistema de Vendas de Ingressos de Cinema** é uma aplicação web moderna desenvolvida com Flask que simula um sistema completo de bilheteria de cinema. O projeto foi criado para demonstrar boas práticas de desenvolvimento web, incluindo arquitetura MVC, persistência de dados e design responsivo.

### 🌟 Destaques

- ✅ Interface moderna e responsiva
- ✅ Sistema de meia-entrada automático
- ✅ Controle de estoque em tempo real
- ✅ Painel administrativo completo
- ✅ Validações robustas (frontend e backend)
- ✅ Persistência de dados em JSON
- ✅ Deploy pronto para produção

### 🎭 Problema Resolvido

Este sistema resolve a necessidade de:
- **Automatizar** o processo de venda de ingressos
- **Controlar** estoque de forma eficiente
- **Calcular** automaticamente descontos de meia-entrada
- **Acompanhar** vendas e arrecadação em tempo real
- **Proporcionar** uma experiência de usuário fluida e moderna

---

## ✨ Funcionalidades

### 👥 Para Usuários

#### 🎫 Sistema de Compras
- Listagem de filmes em cartaz com cards visuais
- Visualização de preços (inteira e meia)
- Sistema de busca por título de filme
- Cálculo automático de meia-entrada para:
  - Menores de 18 anos
  - Estudantes com carteira
- Validação em tempo real de estoque
- Comprovante detalhado de compra

#### 🔍 Busca e Navegação
- Busca inteligente por nome do filme
- Feedback visual quando nenhum resultado é encontrado
- Badge "NOVO" para filmes de 2024 em diante
- Contador de ingressos vendidos por filme

### 👨‍💼 Painel Administrativo

#### 📊 Dashboard
- Total de vendas realizadas
- Valor total arrecadado
- Estatísticas em tempo real

#### 📦 Gestão de Estoque
- Monitoramento de estoque por filme
- Sistema de alertas visuais:
  - 🔴 Crítico: < 20 ingressos
  - 🟡 Atenção: < 50 ingressos
  - 🟢 Normal: ≥ 50 ingressos

#### 🏆 Análise de Vendas
- Ranking de filmes mais vendidos
- Histórico completo de transações
- Data e hora de cada venda
- Detalhamento de tipo de ingresso

### 🎬 Integração TMDB (NOVO v2.0)

#### 🔄 Atualização Automática
- Busca filmes em cartaz no Brasil
- Busca filmes populares do momento
- Atualização com 8 filmes por vez (configurável)
- Mantém estoque de filmes existentes
- Atualização com um clique no painel admin

#### 🔍 Busca Inteligente
- Adicione qualquer filme da base TMDB
- Busca por título em português ou inglês
- Dados completos: sinopse, nota, gêneros
- Imagens oficiais em alta qualidade

#### 📊 Dados Enriquecidos
- **Sinopse completa** do filme
- **Nota de avaliação** (0-10) da comunidade TMDB
- **ID único** para futuras integrações
- **Gêneros atualizados** automaticamente
- **Ano de lançamento** preciso

---

## 🛠️ Tecnologias

### Backend
```
Python 3.8+          - Linguagem de programação
Flask 3.0+           - Framework web
Gunicorn 23.0        - Servidor WSGI para produção
Requests 2.31.0      - Cliente HTTP para APIs       ⭐ NOVO
Python-dotenv 1.0.0  - Variáveis de ambiente       ⭐ NOVO
```

### Frontend
```
HTML5           - Estruturação semântica
CSS3            - Estilização moderna
Jinja2          - Template engine
```

### APIs & Integrações
```
TMDB API        - The Movie Database (catálogo de filmes)  ⭐ NOVO
JSON            - Persistência de dados
```

### Ferramentas
```
Git             - Controle de versão
Render          - Plataforma de deploy
dotenv          - Gerenciamento de configurações            ⭐ NOVO
```

### Padrões e Práticas
- 🏗️ **Arquitetura MVC** - Separação de responsabilidades
- 🔄 **RESTful Routes** - URLs semânticas
- 📱 **Responsive Design** - Mobile-first approach
- ✅ **Validação Dupla** - Frontend e Backend
- 📝 **Clean Code** - Código limpo e documentado

---

## 🏗️ Arquitetura

### Estrutura MVC

```
┌─────────────┐
│   VIEW      │  Templates HTML (Jinja2)
│  (Frontend) │  
└─────┬───────┘
      │
┌─────▼───────┐
│ CONTROLLER  │  Rotas Flask (@app.route)
│  (Routes)   │  Lógica de negócio
└─────┬───────┘
      │
┌─────▼───────┐
│   MODEL     │  Dados (JSON)
│   (Data)    │  Funções de persistência
└─────────────┘
```

### Fluxo de Dados

```
Usuário → Rota → Validação → Processamento → Persistência → Resposta
```

### Sistema de Persistência

```python
dados/
├── filmes.json      # Catálogo de filmes e estoque
└── historico.json   # Registro de todas as vendas
```

---

## 📥 Instalação

### Pré-requisitos

Certifique-se de ter instalado:
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- **Conta no TMDB (gratuita)** ⭐ NOVO

### Passo a Passo

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/CostaCodesFullStack/cinema-flask.git
cd cinema-flask
```

2️⃣ **Crie um ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Instale as dependências**
```bash
pip install -r requirements.txt
```

4️⃣ **⭐ NOVO: Configure a API do TMDB**

**a) Obtenha sua API Key:**
1. Acesse: https://www.themoviedb.org/signup
2. Crie uma conta gratuita
3. Vá em: **Configurações → API**
4. Clique em **"Criar"** ou **"Solicitar uma chave de API"**
5. Selecione **"Developer"**
6. Aceite os termos
7. Copie sua **API Key (v3 auth)**

**b) Crie o arquivo `.env`:**
```bash
# Crie o arquivo .env na raiz do projeto
touch .env  # Linux/Mac
type nul > .env  # Windows
```

**c) Adicione a configuração:**
```env
TMDB_API_KEY=sua_chave_aqui
SECRET_KEY=dev-secret-key-mude-isso-em-producao
DEBUG=True
FLASK_ENV=development
```

5️⃣ **Teste a configuração** ⭐ NOVO
```bash
python teste_config.py
```

Você deve ver:
```
🔍 Testando configurações...
✅ API Key: c06e7ccd90...41c83
✅ Base URL: https://api.themoviedb.org/3
✅ Debug: True
✅ Estoque padrão: 100
✅ Preço padrão: R$ 20.0

🎉 Configuração carregada com sucesso!
```

6️⃣ **Execute a aplicação**
```bash
# Modo desenvolvimento
python app.py

# Modo produção
gunicorn app:app
```

7️⃣ **Acesse no navegador**
```
http://localhost:5000
```

---

## 🚀 Uso

### 💳 Comprando Ingressos

1. **Acesse a página inicial** e navegue pelos filmes disponíveis
2. **Clique em "🎟️ Comprar"** no filme desejado
3. **Preencha o formulário:**
   - Idade do comprador
   - Possui carteira de estudante? (Sim/Não)
   - Quantidade de ingressos
4. **Clique em "Finalizar Compra"**
5. **Receba o comprovante** com os detalhes da transação

### 📊 Acessando o Painel Admin

1. **Clique em "⚙️ Admin"** no menu de navegação
2. **Visualize as estatísticas:**
   - Total de vendas
   - Valor arrecadado
   - Estoque atual
   - Filmes mais vendidos

### 📝 Consultando o Histórico

1. **Clique em "📊 Histórico"** no menu
2. **Veja todas as vendas realizadas** com detalhes:
   - Data e hora
   - Filme
   - Tipo de ingresso
   - Quantidade
   - Valor total

---

## 📁 Estrutura do Projeto
```
cinema-flask/
│
├── 📄 app.py                    # Aplicação principal Flask
├── 📄 config.py                 # Configurações centralizadas      ⭐ NOVO
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 .env                      # Variáveis de ambiente (gitignored) ⭐ NOVO
├── 📄 .gitignore               # Arquivos ignorados pelo Git
├── 📄 teste_config.py          # Script de teste de configuração  ⭐ NOVO
├── 📄 README.md                # Documentação
│
├── 📁 services/                # Serviços externos                 ⭐ NOVO
│   ├── __init__.py
│   └── tmdb_service.py         # Integração com API TMDB          ⭐ NOVO
│
├── 📁 utils/                   # Funções auxiliares                ⭐ NOVO
│   ├── __init__.py
│   └── helpers.py              # Helpers para JSON e data          ⭐ NOVO
│
├── 📁 templates/               # Templates HTML (Jinja2)
│   ├── index.html              # Página inicial
│   ├── compra.html             # Formulário de compra
│   ├── sucesso.html            # Confirmação de compra
│   ├── historico.html          # Histórico de vendas
│   └── admin.html              # Painel administrativo (atualizado) ⭐
│
├── 📁 static/                  # Arquivos estáticos
│   └── style.css               # Estilos CSS globais
│
└── 📁 dados/                   # Persistência de dados
    ├── filmes.json             # Catálogo de filmes (enriquecido)  ⭐
    └── historico.json          # Registro de vendas
```

### Detalhamento dos Novos Arquivos

#### `config.py` - Configurações Centralizadas ⭐ NOVO
```python
# Configurações do sistema:
- TMDB_API_KEY          # Chave da API
- TMDB_BASE_URL         # URL base da API
- TMDB_IMAGE_BASE_URL   # URL das imagens
- ESTOQUE_PADRAO        # Estoque inicial (100)
- PRECO_PADRAO          # Preço padrão (R$ 20)
- QUANTIDADE_FILMES     # Filmes por atualização (8)
```

#### `services/tmdb_service.py` - API Service ⭐ NOVO
```python
class TMDBService:
    - filmes_em_cartaz()        # Busca filmes em cartaz
    - filmes_populares()        # Busca filmes populares
    - buscar_filme(titulo)      # Busca por título
    - detalhes_filme(id)        # Detalhes completos
    - formatar_para_sistema()   # Converte para formato interno
    - atualizar_catalogo()      # Atualiza catálogo completo
```

#### `utils/helpers.py` - Funções Auxiliares ⭐ NOVO
```python
- criar_diretorios()         # Cria estrutura de pastas
- carregar_json()            # Carrega arquivo JSON
- salvar_json()              # Salva arquivo JSON
- mesclar_filmes()           # Mescla catálogos mantendo estoque
```

### Detalhamento de Arquivos

#### `app.py` - Aplicação Principal
```python
# 6 Rotas principais:
@app.route('/')                    # Página inicial
@app.route('/comprar/<filme>')     # Processo de compra
@app.route('/sucesso')             # Confirmação
@app.route('/historico')           # Histórico
@app.route('/admin')               # Painel admin
@app.route('/buscar')              # Busca de filmes
```

#### `filmes.json` - Estrutura de Dados
```json
{
  "Nome do Filme": {
    "estoque": 100,
    "preco": 20.0,
    "imagem": "url_da_imagem",
    "ano": 2024,
    "genero": "Categoria"
  }
}
```

#### `historico.json` - Registro de Vendas
```json
[
  {
    "filme": "Nome do Filme",
    "tipo": "Inteira/Meia",
    "quantidade": 2,
    "total": 40.0,
    "data": "26/10/2025 15:30"
  }
]
```

---

## 🔌 API Endpoints

### Rotas Públicas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Página inicial com listagem de filmes |
| GET | `/comprar/<filme>` | Formulário de compra |
| POST | `/comprar/<filme>` | Processar compra |
| GET | `/sucesso` | Confirmação de compra |
| GET | `/buscar?q=termo` | Buscar filmes |

### Rotas Administrativas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/admin` | Painel administrativo |
| GET | `/historico` | Histórico de vendas |

---

## 🎨 Capturas de Tela

### 🏠 Página Inicial
![Página Inicial](https://cinema-ingressos.onrender.com)
- Cards de filmes com design moderno
- Informações de preço e disponibilidade
- Sistema de busca integrado

### 🎫 Página de Compra
![Compra](https://cinema-ingressos.onrender.com/comprar/Titanic)
- Tabela de preços clara
- Validações em tempo real
- Feedback visual de erros

### ⚙️ Painel Admin
![Admin](https://cinema-ingressos.onrender.com/admin)
- Dashboard com estatísticas
- Controle de estoque visual
- Ranking de vendas

---

## 🎯 Validações Implementadas

### Frontend (HTML5)
```html
✅ Campos obrigatórios (required)
✅ Tipos de input apropriados (number, select)
✅ Valores mínimos (min="0", min="1")
```

### Backend (Python)
```python
✅ Idade entre 0 e 120 anos
✅ Quantidade maior que zero
✅ Estoque disponível suficiente
✅ Filme existente no catálogo
✅ Todos os campos preenchidos
✅ Valores numéricos válidos
✅ Conversão segura de tipos
```

---

## 💰 Regras de Negócio

### Cálculo de Meia-Entrada

```python
if idade < 18 OR possui_carteira_estudante:
    preco_final = preco_inteira / 2
    tipo = "Meia"
else:
    preco_final = preco_inteira
    tipo = "Inteira"
```

### Controle de Estoque

```python
if estoque_disponivel >= quantidade_solicitada:
    # Processar venda
    estoque -= quantidade_solicitada
    registrar_venda()
else:
    # Retornar erro
    exibir_mensagem("Estoque insuficiente")
```

---

## 🗺️ Roadmap

### 🚀 Versão 2.0 (Planejado)

#### Banco de Dados
- [ ] Migração para SQLite/PostgreSQL
- [ ] Sistema de migrations
- [ ] Backup automático

#### Autenticação & Segurança
- [x] Sistema de login/registro ✅ **IMPLEMENTADO v2.1.0**
- [x] Níveis de acesso (admin, operador, cliente) ✅ **IMPLEMENTADO v2.1.0**
- [x] Proteção de rotas com decorators ✅ **IMPLEMENTADO v2.1.0**
- [ ] Tokens JWT para API

#### Funcionalidades Avançadas
- [ ] Sistema de sessões de cinema (horários)
- [ ] Escolha de assentos interativa
- [x] Integração com API TMDB (sinopses, trailers) ✅ **IMPLEMENTADO v2.0.0**
- [ ] Geração de QR Code nos ingressos
- [ ] Sistema de reservas (pagar depois)

#### Pagamentos
- [ ] Integração com Stripe/Mercado Pago
- [ ] Múltiplas formas de pagamento
- [ ] Confirmação por email
- [ ] Nota fiscal eletrônica

#### Análise & Relatórios
- [ ] Gráficos interativos (Chart.js/Plotly)
- [ ] Exportação para PDF/Excel
- [ ] Dashboard de analytics
- [ ] Previsão de vendas (ML)

#### UX/UI
- [ ] Modo escuro/claro
- [ ] Temas personalizáveis
- [ ] Animações avançadas
- [ ] PWA (Progressive Web App)
- [ ] App mobile (Flutter/React Native)

#### DevOps
- [ ] CI/CD com GitHub Actions
- [ ] Testes automatizados (pytest)
- [ ] Docker containerization
- [ ] Monitoramento com Sentry
- [ ] Cache com Redis

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Siga estas etapas:

### 1️⃣ Fork o Projeto
```bash
# Clique no botão "Fork" no GitHub
```

### 2️⃣ Crie uma Branch
```bash
git checkout -b feature/MinhaNovaFeature
```

### 3️⃣ Commit suas Mudanças
```bash
git commit -m 'Add: Nova funcionalidade incrível'
```

### 4️⃣ Push para a Branch
```bash
git push origin feature/MinhaNovaFeature
```

### 5️⃣ Abra um Pull Request
```bash
# No GitHub, clique em "New Pull Request"
```

### 📝 Padrão de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: Adiciona nova funcionalidade
fix: Corrige um bug
docs: Atualiza documentação
style: Mudanças de formatação/estilo
refactor: Refatoração de código
test: Adiciona ou modifica testes
chore: Tarefas de manutenção
```

---

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

```
MIT License - Copyright (c) 2025 Cauã Costa
```

---

## 👤 Autor

**Cauã Costa**

- 🌐 Website: [https://portfolio-one-gold-6xch6vskv8.vercel.app](https://portfolio-one-gold-6xch6vskv8.vercel.app)
- 💼 LinkedIn: [@Caua Costa](www.linkedin.com/in/caua-costa-222900278)
- 🐙 GitHub: [@CostaCodesFullStack](https://github.com/CostaCodesFullStack)
- 📧 Email: cauadevcosta@gmail.com

---

## 🙏 Agradecimentos

- [Flask](https://flask.palletsprojects.com/) - Framework web incrível
- [TMDB](https://www.themoviedb.org/) - Imagens dos filmes
- [Render](https://render.com/) - Hospedagem gratuita
- Comunidade Python - Pelo suporte constante
- Você - Por usar e contribuir com este projeto! 💙

---

## 📊 Status do Projeto
```
⚡ Versão Atual: 2.1.0  ⭐ ATUALIZADO
🚀 Status: Em Produção com API TMDB + Autenticação
🛠️ Última Atualização: 28 de Outubro de 2025
🔥 Features Novas: Sistema de Login/Registro, Proteção de Rotas
✅ Bugs Conhecidos: 0
📦 Dependências: 8 (Flask, Requests, Dotenv, Gunicorn, Jinja2, Werkzeug, Flask-Login)
```

---

## 📅 Histórico de Atualizações

### 🔐 Versão 2.1.0 (28/10/2025)
**🚀 ATUALIZAÇÃO MAJOR - Sistema de Autenticação Completo**

**✨ Novas Funcionalidades:**
- ✅ **Sistema de Login/Registro** - Autenticação completa de usuários
- ✅ **Flask-Login integrado** - Gerenciamento de sessões seguras
- ✅ **Hash de senhas com bcrypt** - Segurança via Werkzeug
- ✅ **Dois níveis de acesso:**
  - **User** - Usuário comum (pode comprar ingressos)
  - **Admin** - Administrador (acesso total ao sistema)
- ✅ **Proteção de rotas administrativas** - Decorator `@admin_required`
- ✅ **Página de perfil do usuário** - Visualizar informações da conta
- ✅ **Usuário admin padrão** - Criado automaticamente (admin/admin123)

**🎨 Novos Templates:**
- ✅ `base.html` - Template base com menu de usuário dinâmico
- ✅ `login.html` - Página de login responsiva
- ✅ `registro.html` - Página de registro com validações
- ✅ `perfil.html` - Página de perfil do usuário

**🏗️ Arquitetura:**
- ✅ Criado `services/auth_service.py` - Serviço de autenticação
- ✅ Classe `User` compatível com Flask-Login
- ✅ Classe `AuthService` para gerenciamento de usuários
- ✅ Persistência em `dados/usuarios.json` (protegido no .gitignore)

**🔐 Segurança:**
- ✅ Senhas com hash bcrypt (nunca armazenadas em texto plano)
- ✅ Validações de entrada (username mín. 3 chars, senha mín. 6 chars)
- ✅ Proteção CSRF automática do Flask
- ✅ Sessões seguras com Flask-Login
- ✅ Arquivo de usuários no .gitignore

**⚙️ Novas Rotas:**
```python
GET/POST /login              # Página de login
GET/POST /registro           # Página de registro
GET      /logout             # Fazer logout (protegida)
GET      /perfil             # Ver perfil (protegida)
```

**🛡️ Rotas Protegidas:**
- ✅ `/admin` - Apenas administradores
- ✅ `/admin/atualizar-catalogo` - Apenas administradores
- ✅ `/admin/adicionar-filme` - Apenas administradores
- ✅ `/perfil` - Apenas usuários logados
- ✅ `/logout` - Apenas usuários logados

**📦 Dependências Adicionadas:**
- `Flask-Login==0.6.3` - Gerenciamento de autenticação
- `Werkzeug==3.0.3` - Hash de senhas (bcrypt)

**📚 Documentação:**
- ✅ Criado `AUTH_DOCS.md` - Documentação completa do sistema de autenticação
- ✅ Exemplos de uso da API do AuthService
- ✅ Guia de segurança e boas práticas
- ✅ Instruções de credenciais padrão

**🎯 Validações Implementadas:**
- ✅ Username único (case-insensitive)
- ✅ Email único e formato válido
- ✅ Confirmação de senha no registro
- ✅ Proteção contra último admin ser deletado
- ✅ Mensagens de erro amigáveis

**🔄 Melhorias no Deploy:**
- ✅ Correção de porta e host para Render (erro 502 resolvido)
- ✅ Configuração dinâmica de PORT via variável de ambiente
- ✅ Host configurado como 0.0.0.0 para aceitar conexões externas
- ✅ Debug desativado por padrão em produção
- ✅ Criado `DEPLOY.md` com instruções completas

---

### 🎬 Versão 2.0.0 (27/10/2025)
**🚀 ATUALIZAÇÃO MAJOR - Integração com API TMDB**

**✨ Novas Funcionalidades:**
- ✅ **Integração completa com API do TMDB** (The Movie Database)
- ✅ **Atualização automática de catálogo** - Busca filmes em cartaz e populares
- ✅ **Adição de filmes específicos** - Busque e adicione qualquer filme da base TMDB
- ✅ **Dados enriquecidos dos filmes:**
  - Sinopse completa
  - Nota de avaliação (0-10)
  - ID único do TMDB
  - Gêneros atualizados automaticamente
  - Imagens oficiais em alta qualidade
- ✅ **Sistema de configuração com .env** - Variáveis de ambiente seguras
- ✅ **Manutenção de estoque** - Ao atualizar catálogo, mantém vendas atuais

**🏗️ Arquitetura:**
- ✅ Criada camada `services/` - Serviços externos (TMDB API)
- ✅ Criada camada `utils/` - Funções auxiliares reutilizáveis
- ✅ Implementado `config.py` - Configurações centralizadas
- ✅ Adicionado suporte a múltiplos ambientes (dev, prod, test)

**🔧 Melhorias Técnicas:**
- ✅ Refatoração completa da persistência de dados
- ✅ Implementadas funções helper para JSON
- ✅ Sistema de fallback quando API não disponível
- ✅ Tratamento robusto de erros da API
- ✅ Timeout de 10s para requisições
- ✅ Suporte a filmes em português (pt-BR)
- ✅ Região configurável (padrão: Brasil)

**⚙️ Novas Rotas Administrativas:**
```python
POST /admin/atualizar-catalogo    # Atualiza catálogo completo
POST /admin/adicionar-filme        # Adiciona filme específico
```

**📦 Dependências Adicionadas:**
- `requests==2.31.0` - Requisições HTTP para API
- `python-dotenv==1.0.0` - Gerenciamento de variáveis de ambiente

**🔐 Segurança:**
- ✅ API Keys armazenadas em arquivo .env (não commitado)
- ✅ .gitignore atualizado para proteger credenciais
- ✅ Validação de API Key antes de requisições

**🐛 Bugs Corrigidos:**
- ✅ Corrigido erro de importação em `config.py`
- ✅ Corrigido erro de indentação em `app.py`
- ✅ Corrigido nome de variável em `helpers.py`
- ✅ Corrigido múltiplos erros em `tmdb_service.py`:
  - Import incorreto de `exception`
  - Nome de variável `imagem_base_url`
  - Typo em `realease_date`
  - Sobrescrita de variável em loop

**📚 Documentação:**
- ✅ README atualizado com instruções de configuração da API
- ✅ Adicionados comentários detalhados no código
- ✅ Criado guia de instalação completo

**⚠️ BREAKING CHANGES:**
- Necessário criar arquivo `.env` com `TMDB_API_KEY`
- Nova estrutura de pastas requer reorganização
- Alguns imports podem precisar ser atualizados

**🔄 Migração:**
Para migrar da v1.x para v2.0:
1. Crie arquivo `.env` na raiz com sua API Key do TMDB
2. Instale novas dependências: `pip install -r requirements.txt`
3. Crie pastas `services/` e `utils/` com `__init__.py`
4. Copie arquivos `config.py`, `tmdb_service.py` e `helpers.py`
5. Execute: `python teste_config.py` para validar

### 🎬 Versão 1.1.0 (26/10/2025)
**✨ Melhorias Implementadas:**
- ✅ Corrigido bug da variável `vendas_por_filme` nas rotas
- ✅ Adicionada persistência completa de dados em JSON
- ✅ Implementado campo `data` no histórico de vendas
- ✅ Corrigida estrutura HTML do index.html
- ✅ Melhorado sistema de badges "NOVO" para filmes de 2024
- ✅ Adicionado contador de ingressos vendidos por filme
- ✅ Deploy realizado no Render com sucesso

### 🔧 Versão 1.0.2 (24/10/2025)
**🖼️ Melhorias Visuais:**
- ✅ Adicionadas imagens de cartaz para cada filme (TMDB API)
- ✅ Implementado sistema de cards com hover effects
- ✅ Corrigidos bugs nas páginas recém-criadas
- ✅ Melhorada responsividade mobile

### 📊 Versão 1.0.1 (23/10/2025)
**🎯 Novas Funcionalidades:**
- ✅ Criada página de histórico de vendas
- ✅ Implementado painel administrativo completo
- ✅ Adicionado sistema de busca de filmes
- ✅ Corrigidos bugs e linhas de código duplicadas
- ✅ Implementadas validações robustas

### 🚀 Versão 1.0.0 (21/10/2025)
**🎉 Lançamento Inicial:**
- ✅ Iniciada implementação do framework Flask
- ✅ Migração do sistema Python puro para web
- ✅ Criadas rotas básicas e templates

### 🔄 Versão 0.2.0 (20/10/2025)
**🛠️ Refatoração:**
- ✅ Refatoração completa do código
- ✅ Correção de bugs identificados
- ✅ Melhorias na estrutura do código

### 🎬 Versão 0.1.0 (19/10/2025)
**🌟 Primeira Versão:**
- ✅ Sistema inicial de vendas de ingressos criado
- ✅ Implementação em Python puro (terminal)
- ✅ Funcionalidades básicas de compra e histórico

---

## 📈 Estatísticas

![GitHub Stars](https://img.shields.io/github/stars/CostaCodesFullStack/cinema-flask?style=social)
![GitHub Forks](https://img.shields.io/github/forks/CostaCodesFullStack/cinema-flask?style=social)
![GitHub Issues](https://img.shields.io/github/issues/CostaCodesFullStack/cinema-flask)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/CostaCodesFullStack/cinema-flask)

---

<div align="center">

### ⭐ Se este projeto foi útil, considere dar uma estrela!

**Desenvolvido por Cauã Costa**

[⬆ Voltar ao topo](#-sistema-de-vendas-de-ingressos-de-cinema)

</div>