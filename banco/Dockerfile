# Use uma imagem do PostgreSQL
FROM postgres:latest

# Defina as variáveis de ambiente do PostgreSQL
ENV POSTGRES_DB = postgres
ENV POSTGRES_USER = alysson
#senha do banco de dados
ENV POSTGRES_PASSWORD = 1984 

# Copie o arquivo SQL com os comandos para criar as tabelas
#na parte "comando.sql" é o nome do meu arquivo do banco de dados
COPY init.sql /docker-entrypoint-initdb.d/