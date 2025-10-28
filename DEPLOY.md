# 🚀 Deploy no Render - Sistema de Cinema

## ✅ Correções Aplicadas

### 1. Configuração de Porta e Host
- ✅ App agora escuta na porta fornecida pela variável `PORT` do Render
- ✅ Host configurado como `0.0.0.0` para aceitar conexões externas
- ✅ Debug desativado por padrão em produção

### 2. Estrutura de Diretórios
- ✅ Diretório `dados/` será criado automaticamente
- ✅ `.gitkeep` adicionado para manter a estrutura

## 📋 Variáveis de Ambiente no Render

Configure as seguintes variáveis de ambiente no painel do Render:

### Obrigatórias:
```
PORT=10000  # Render define automaticamente
```

### Opcionais:
```
DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
TMDB_API_KEY=sua-api-key-do-tmdb
FLASK_ENV=production
```

## 🔧 Configuração do Render

### Build Command:
```bash
pip install -r requirements.txt
```

### Start Command:
```bash
gunicorn app:app
```

## 📝 Checklist de Deploy

- [ ] Fazer commit das alterações
- [ ] Fazer push para o repositório
- [ ] Configurar variáveis de ambiente no Render
- [ ] Verificar se o Procfile está correto
- [ ] Aguardar o build completar
- [ ] Testar a aplicação

## 🐛 Troubleshooting

### Erro 502 Bad Gateway
**Causa:** App não está escutando na porta correta ou no host correto
**Solução:** ✅ Já corrigido! O app agora usa `PORT` e `HOST` do ambiente

### Erro de Importação
**Causa:** Dependências não instaladas
**Solução:** Verificar se `requirements.txt` está completo

### Diretório `dados/` não existe
**Causa:** Diretório ignorado pelo git
**Solução:** ✅ Já corrigido! O app cria o diretório automaticamente

## 📦 Arquivos Importantes

- `Procfile` - Define como o Render deve iniciar a aplicação
- `requirements.txt` - Lista de dependências Python
- `app.py` - Aplicação principal
- `config.py` - Configurações do sistema

## 🎯 Próximos Passos

1. Faça commit e push das alterações:
```bash
git add .
git commit -m "fix: configurar porta e host para produção no Render"
git push
```

2. No painel do Render, force um novo deploy ou aguarde o deploy automático

3. Verifique os logs do Render para confirmar que o servidor está rodando:
```
🚀 Servidor rodando em 0.0.0.0:10000
```

4. Acesse sua aplicação pela URL fornecida pelo Render
