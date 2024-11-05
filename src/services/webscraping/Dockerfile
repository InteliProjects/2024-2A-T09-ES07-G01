# Usar uma imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o diretório de trabalho
COPY . .

# Definir variáveis de ambiente (estas podem ser sobrescritas no Railway)
ENV EMAIL_PASSWORD=password
ENV SMTP_SERVER=smtp.gmail.com
ENV RABBITMQ_HOST=rabbitmq
ENV B2_APPLICATION_KEY_ID=id
ENV B2_APPLICATION_KEY=id

# Definir o ponto de entrada para rodar o script Python
CMD ["python", "main.py"]