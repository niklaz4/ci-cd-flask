# Use a imagem oficial do Python para Flask
FROM python:3.8-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação para o diretório de trabalho
COPY . .

# Instala as dependências
RUN pip install -r requirements.txt

# Define a porta que a aplicação irá escutar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]