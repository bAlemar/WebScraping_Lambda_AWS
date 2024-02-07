Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping_Lambda_AWS.git

2. **Navegue até o diretório do Docker no repositório clonado:**
   ```bash
   cd WebScraping_Lambda_AWS

3. **Construa sua imagem:**
   ```bash
   docker build -t nome-imagem .
4. **Execute o Contêiner:**
   ```bash
   docker run nome-imagem