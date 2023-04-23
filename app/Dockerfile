FROM python:3.9-slim

# Adiciona o usuário "admUser" ao contêiner
RUN useradd -m -s /bin/bash admUser

# Define o usuário padrão para "admUser"
USER admUser

# Define o diretório de trabalho para o usuário "admUser"
WORKDIR /home/admUser/app

# Copia o arquivo de requirements para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia todo o projeto para o diretório de trabalho
COPY . .

# Define o comando padrão a ser executado
CMD [ "python3", "-u", "app.py" ]

