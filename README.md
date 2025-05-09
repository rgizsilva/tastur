# Documentação do Sistema Tastur Connect

## Visão Geral
O Tastur Connect é um sistema de gerenciamento para uma empresa de turismo, desenvolvido com Django e PostgreSQL. O sistema permite o gerenciamento de clientes, parceiros e reservas, com diferentes níveis de acesso para colaboradores e clientes.

## Estrutura do Projeto
O projeto está organizado nos seguintes aplicativos Django:
- **core**: Gerencia autenticação, login e funcionalidades centrais
- **clientes**: Gerencia cadastro e consulta de clientes
- **parceiros**: Gerencia cadastro e consulta de parceiros
- **reservas**: Gerencia cadastro e consulta de reservas

## Banco de Dados
O sistema utiliza PostgreSQL como banco de dados, com as seguintes tabelas principais:
- **CLIENTES**: Armazena informações dos clientes
- **PARCEIROS**: Armazena informações dos parceiros
- **RESERVAS**: Armazena informações das reservas
- **COLABORADORES**: Armazena informações dos colaboradores (funcionários)

## Requisitos do Sistema
- Python 3.10 ou superior
- PostgreSQL 14 ou superior
- Dependências listadas em requirements.txt

## Instalação

### 1. Clonar o repositório
```bash
git clone tastur
cd tastur
```

### 2. Configurar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar servidor
```bash
python manage.py runserver
```
### 5. Acessar painel admin
python manage.py createsuperuser

### 6. Criar super user para o painel Django
http://127.0.0.1:8000/admin/

### 7. Acessa tela de login
http://127.0.0.1:8000
## Funcionalidades

### Colaboradores
- Login com usuário e senha
- Cadastro, consulta, edição e exclusão de clientes
- Cadastro, consulta, edição e exclusão de parceiros
- Cadastro, consulta, edição e exclusão de reservas

### Clientes
- Login com CPF
- Consulta de suas próprias reservas

## Fluxo de Uso

1. **Tela Inicial**: Apresenta opções para acesso como Colaborador ou Cliente
2. **Login**: Autenticação específica para cada tipo de usuário
3. **Painel de Seleção**: Após login, apresenta opções de acordo com o tipo de usuário
4. **Operações CRUD**: Para colaboradores, permite gerenciar clientes, parceiros e reservas
5. **Consulta de Reservas**: Para clientes, permite consultar suas próprias reservas

## Tecnologias Utilizadas
- Django 5.2
- PostgreSQL
- Bootstrap 5
- Crispy Forms
- JavaScript

## Manutenção

### Backup do Banco de Dados
```bash
pg_dump -U tastur_user -d tastur_db > backup.sql
```

### Restauração do Banco de Dados
```bash
psql -U tastur_user -d tastur_db < backup.sql
```

### Atualização de Dependências
```bash
pip install -r requirements.txt --upgrade
```



