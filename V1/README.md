Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping_Lambda_AWS.git
2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd WebScraping_Lambda_AWS

3. **Construa sua imagem:**
   ```bash
   docker build -t nome-imagem .
4. **Crie uma porta para testar seu Container:**
   ```bash
   docker run -p 9000:8080 nome-imagem
4. **Faça uma chamada do Container para ver sua execução:**
   ```bash
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' 

