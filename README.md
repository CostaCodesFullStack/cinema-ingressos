# 🎬 Sistema de Vendas de Ingressos de Cinema

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> Sistema completo de gerenciamento de vendas de ingressos de cinema com painel administrativo, desenvolvido com Flask e design responsivo.

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Demonstração](#-demonstração)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Capturas de Tela](#-capturas-de-tela)
- [Roadmap](#-roadmap)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Contato](#-contato)

## 🎯 Sobre o Projeto

O **Sistema de Vendas de Ingressos de Cinema** é uma aplicação web full-stack desenvolvida para gerenciar a venda de ingressos de filmes em cartaz. O sistema oferece uma interface intuitiva para usuários comprarem ingressos, com validações robustas e um painel administrativo completo para acompanhamento de vendas e estoque.

### Problema Resolvido

- Automatização do processo de venda de ingressos
- Controle preciso de estoque de ingressos por filme
- Cálculo automático de meia-entrada (menores de 18 anos e estudantes)
- Acompanhamento em tempo real de vendas e arrecadação
- Interface responsiva para acesso em qualquer dispositivo

## 🎥 Demonstração

### Fluxo Principal
1. **Listagem de Filmes** → Usuário visualiza filmes disponíveis com preços e estoque
2. **Seleção e Compra** → Escolha do filme, quantidade e tipo de ingresso
3. **Validação** → Sistema valida dados e disponibilidade
4. **Confirmação** → Comprovante de compra com detalhes da transação

### Painel Admin
- Dashboard com estatísticas gerais
- Controle de estoque em tempo real
- Ranking de filmes mais vendidos
- Histórico completo de transações

## ✨ Funcionalidades

### 🎫 Para Usuários

- [x] **Listagem de Filmes em Cartaz**
  - Exibição de título, preço e disponibilidade
  - Design de cards modernos e responsivos
  
- [x] **Sistema de Compra Inteligente**
  - Cálculo automático de meia-entrada
  - Validação de idade (0-120 anos)
  - Validação de quantidade disponível
  - Verificação de estoque em tempo real

- [x] **Busca de Filmes**
  - Sistema de busca por título
  - Feedback visual quando nenhum resultado é encontrado

- [x] **Comprovante de Compra**
  - Exibição de detalhes da transação
  - Tipo de ingresso e valor total

### 👨‍💼 Painel Administrativo

- [x] **Dashboard de Estatísticas**
  - Total de vendas realizadas
  - Valor total arrecadado
  - Visualização gráfica com código de cores

- [x] **Gerenciamento de Estoque**
  - Monitoramento em tempo real
  - Alertas visuais por nível de estoque:
    - 🔴 Crítico (< 20 ingressos)
    - 🟡 Atenção (< 50 ingressos)
    - 🟢 Normal (≥ 50 ingressos)

- [x] **Histórico de Vendas**
  - Registro completo de todas as transações
  - Informações detalhadas por venda
  - Total arrecadado

- [x] **Ranking de Filmes**
  - Filmes mais vendidos
  - Quantidade de ingressos por filme

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+** - Linguagem de programação
- **Flask 3.0+** - Framework web minimalista e poderoso
- **Jinja2** - Template engine para renderização dinâmica

### Frontend
- **HTML5** - Estruturação semântica
- **CSS3** - Estilização moderna com:
  - Flexbox e Grid Layout
  - Media Queries para responsividade
  - Animações e transições suaves
  - Variáveis CSS customizadas

### Arquitetura
- **MVC Pattern** - Separação de responsabilidades
- **RESTful Routes** - URLs semânticas e intuitivas
- **Server-Side Rendering** - Renderização no servidor

## 📦 Instalação

### Pré-requisitos

```bash
Python 3.8 ou superior
pip (gerenciador de pacotes Python)
```

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/cinema-flask.git
cd cinema-flask
```

2. **Crie um ambiente virtual (recomendado)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install flask
```

4. **Execute a aplicação**
```bash
python app.py
```

5. **Acesse no navegador**
```
http://localhost:5000
```

## 🚀 Como Usar

### Comprando Ingressos

1. Acesse a página inicial
2. Navegue pelos filmes disponíveis
3. Clique em "🎟️ Comprar" no filme desejado
4. Preencha os dados:
   - Idade do comprador
   - Se possui carteira de estudante
   - Quantidade de ingressos
5. Clique em "Finalizar Compra"
6. Receba o comprovante com os detalhes

### Acessando o Painel Admin

1. Clique em "⚙️ Admin" no menu de navegação
2. Visualize as estatísticas gerais
3. Monitore o estoque de cada filme
4. Confira os filmes mais vendidos

### Consultando Histórico

1. Clique em "📊 Histórico" no menu
2. Visualize todas as vendas realizadas
3. Confira o total arrecadado

## 📁 Estrutura do Projeto

```
cinema-flask/
│
├── app.py                 # Aplicação principal Flask
│
├── templates/             # Templates HTML
│   ├── index.html         # Página inicial (listagem de filmes)
│   ├── compra.html        # Página de compra de ingressos
│   ├── sucesso.html       # Confirmação de compra
│   ├── historico.html     # Histórico de vendas
│   └── admin.html         # Painel administrativo
│
├── static/                # Arquivos estáticos
│   └── style.css          # Estilos CSS
│
└── README.md              # Documentação do projeto
```

### Arquitetura do Código

#### `app.py` - Backend
```python
# Estrutura modular com 6 rotas principais:

@app.route('/')                      # Página inicial
@app.route('/comprar/<filme>')       # Processo de compra
@app.route('/sucesso')               # Confirmação
@app.route('/historico')             # Histórico de vendas
@app.route('/admin')                 # Painel administrativo
@app.route('/buscar')                # Busca de filmes
```

#### Sistema de Dados
```python
# Estrutura de filmes (dicionário)
filmes = {
    "Nome do Filme": {
        "estoque": int,    # Quantidade disponível
        "preco": float     # Preço da inteira
    }
}

# Estrutura de histórico (lista)
historico = [
    {
        "filme": str,       # Nome do filme
        "tipo": str,        # "Inteira" ou "Meia"
        "quantidade": int,  # Qtd de ingressos
        "total": float      # Valor total pago
    }
]
```

## 🎨 Capturas de Tela

### Página Inicial
- Cards de filmes com design moderno
- Informações de preço e disponibilidade
- Barra de busca integrada

### Página de Compra
- Tabela de preços (inteira e meia)
- Formulário intuitivo e validado
- Mensagens de erro claras

### Painel Admin
- Cards de estatísticas com cores vibrantes
- Listagem de estoque com alertas visuais
- Ranking ordenado de vendas

## 🎯 Validações Implementadas

### Validações de Frontend (HTML5)
- Campos obrigatórios (`required`)
- Tipos de input apropriados (`number`, `select`)
- Valores mínimos (`min="0"`, `min="1"`)

### Validações de Backend (Python)
- ✅ Idade entre 0 e 120 anos
- ✅ Quantidade maior que zero
- ✅ Estoque disponível
- ✅ Filme existente no catálogo
- ✅ Todos os campos preenchidos
- ✅ Valores numéricos válidos

## 🔐 Regras de Negócio

### Cálculo de Meia-Entrada
```python
# Condições para meia-entrada:
if idade < 18 OR estudante == "sim":
    preco = preco_inteira / 2
    tipo = "Meia"
else:
    preco = preco_inteira
    tipo = "Inteira"
```

### Controle de Estoque
```python
# Validação antes da venda:
if estoque >= quantidade_solicitada:
    # Processa a venda
    estoque -= quantidade_solicitada
else:
    # Retorna erro de estoque insuficiente
```

## 🚧 Roadmap

### Versão 2.0 (Em Planejamento)

- [ ] **Persistência de Dados**
  - [ ] Integração com SQLite
  - [ ] Migrações de banco de dados
  - [ ] Backup automático

- [ ] **Autenticação**
  - [ ] Sistema de login
  - [ ] Diferentes níveis de acesso
  - [ ] Proteção de rotas administrativas

- [ ] **Funcionalidades Avançadas**
  - [ ] Sistema de sessões de cinema
  - [ ] Escolha de assentos
  - [ ] Integração com API TMDB (imagens e sinopses)
  - [ ] Geração de QR Code nos ingressos

- [ ] **Pagamentos**
  - [ ] Integração com gateway de pagamento
  - [ ] Múltiplas formas de pagamento
  - [ ] Confirmação por email

- [ ] **Relatórios**
  - [ ] Gráficos com Chart.js
  - [ ] Exportação para PDF/Excel
  - [ ] Análise de tendências

- [ ] **UX/UI**
  - [ ] Modo escuro/claro
  - [ ] Temas personalizáveis
  - [ ] Animações avançadas

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova funcionalidade incrível'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrão de Commits
- `Add:` Nova funcionalidade
- `Fix:` Correção de bug
- `Update:` Atualização de código existente
- `Docs:` Alterações na documentação
- `Style:` Mudanças de formatação/estilo

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 👤 Autor

**Cauã Costa**

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)
- Email: seu.email@example.com

## 🙏 Agradecimentos

- Flask Documentation pela excelente documentação
- Comunidade Python pelo suporte
- Todos que contribuíram com feedback e sugestões

---

<div align="center">

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Desenvolvido com ❤️ e ☕ por Cauã Costa**

</div>