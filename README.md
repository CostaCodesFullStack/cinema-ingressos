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

---

## 🛠️ Tecnologias

### Backend
```
Python 3.8+      - Linguagem de programação
Flask 3.0+       - Framework web
Gunicorn 23.0    - Servidor WSGI para produção
```

### Frontend
```
HTML5           - Estruturação semântica
CSS3            - Estilização moderna
Jinja2          - Template engine
```

### Ferramentas
```
JSON            - Persistência de dados
Git             - Controle de versão
Render          - Plataforma de deploy
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

### Passo a Passo

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/cinema-flask.git
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

4️⃣ **Crie a estrutura de pastas**
```bash
mkdir -p dados static templates
```

5️⃣ **Execute a aplicação**
```bash
# Modo desenvolvimento
python app.py

# Modo produção
gunicorn app:app
```

6️⃣ **Acesse no navegador**
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
├── 📄 requirements.txt          # Dependências do projeto
├── 📄 README.md                 # Documentação
│
├── 📁 templates/                # Templates HTML (Jinja2)
│   ├── index.html              # Página inicial - Listagem de filmes
│   ├── compra.html             # Formulário de compra
│   ├── sucesso.html            # Confirmação de compra
│   ├── historico.html          # Histórico de vendas
│   └── admin.html              # Painel administrativo
│
├── 📁 static/                   # Arquivos estáticos
│   └── style.css               # Estilos CSS globais
│
└── 📁 dados/                    # Persistência de dados
    ├── filmes.json             # Catálogo de filmes
    └── historico.json          # Registro de vendas
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
![Página Inicial](https://via.placeholder.com/800x400/0f0f0f/ffffff?text=Listagem+de+Filmes)
- Cards de filmes com design moderno
- Informações de preço e disponibilidade
- Sistema de busca integrado

### 🎫 Página de Compra
![Compra](https://via.placeholder.com/800x400/1f1f1f/ffffff?text=Formulário+de+Compra)
- Tabela de preços clara
- Validações em tempo real
- Feedback visual de erros

### ⚙️ Painel Admin
![Admin](https://via.placeholder.com/800x400/0f0f0f/ffffff?text=Painel+Administrativo)
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
- [ ] Sistema de login/registro
- [ ] Níveis de acesso (admin, operador, cliente)
- [ ] Proteção de rotas com decorators
- [ ] Tokens JWT para API

#### Funcionalidades Avançadas
- [ ] Sistema de sessões de cinema (horários)
- [ ] Escolha de assentos interativa
- [ ] Integração com API TMDB (sinopses, trailers)
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
⚡ Versão Atual: 1.1.0
🚀 Status: Em Produção
🐛 Bugs Conhecidos: 0
✅ Última Atualização: Outubro 2025
```

---

## 📅 Histórico de Atualizações

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

![GitHub Stars](https://img.shields.io/github/stars/seu-usuario/cinema-flask?style=social)
![GitHub Forks](https://img.shields.io/github/forks/seu-usuario/cinema-flask?style=social)
![GitHub Issues](https://img.shields.io/github/issues/seu-usuario/cinema-flask)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/seu-usuario/cinema-flask)

---

<div align="center">

### ⭐ Se este projeto foi útil, considere dar uma estrela!

**Desenvolvido por Cauã Costa**

[⬆ Voltar ao topo](#-sistema-de-vendas-de-ingressos-de-cinema)

</div>