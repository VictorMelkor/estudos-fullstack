# 🗄️ Banco de Dados  
> Esta pasta reúne conteúdos e práticas voltadas ao uso de bancos de dados relacionais e NoSQL no contexto de desenvolvimento fullstack, incluindo integração com ORMs e boas práticas de modelagem.

**Tópicos concluídos:** 3  
**Tópicos pendentes:** 4  
**Progresso:** 42.85%

---

## 📘 Conteúdo Planejado ![Badge](https://img.shields.io/badge/Banco%20de%20Dados-SQL%20%26%20NoSQL-blue)

- ✅ Fundamentos de banco de dados  
- ✅ SQL básico  
- ✅ Modelagem relacional  
- ❌ Banco relacional PostgreSQL  
- ❌ NoSQL com MongoDB  
- ❌ Integração com Django ORM  
- ❌ Segurança e boas práticas  

---

## 🧪 O que será praticado nesta pasta:

- Conceitos fundamentais: tabelas, registros, relacionamentos  
- Sintaxe SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`  
- Modelagem de entidades com cardinalidade e normalização  
- Instalação e uso de PostgreSQL com clientes gráficos (DBeaver, PgAdmin)  
- Criação de coleções e consultas em MongoDB  
- Integração com Django ORM: `models.py`, migrations, queries  
- Criação de chaves estrangeiras e relações 1:N e N:N  
- Práticas seguras: injeção de SQL, roles, permissões  

---

## 📁 Organização da pasta

- `01-sql-basico/`: comandos SQL simples e criação de tabelas  
- `02-modelagem/`: diagramas entidade-relacionamento e normalização  
- `03-postgresql/`: instalação, conexão e uso com SQL avançado  
- `04-nosql-mongodb/`: introdução ao MongoDB, comandos básicos  
- `05-django-orm/`: modelos, migrations e operações via Django  
- `06-seguranca/`: tópicos de segurança e boas práticas  

---

## ✅ Recomendações

- Priorize bancos relacionais para a maioria dos projetos web  
- Use sempre scripts versionados (`.sql` ou `.json`) para popular dados  
- Com Django, evite usar queries brutas. Prefira métodos do ORM  
- Em MongoDB, entenda bem o formato `document` e os tipos de dados suportados  
- Pratique relações reais com dados fictícios (ex: blog, ecommerce, escola)  
