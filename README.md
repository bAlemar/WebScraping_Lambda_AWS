Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/Preco-Imoveis.git

2. **Navegue até o diretório do Docker no repositório clonado:**
   ```bash
   cd Preco-Imoveis/DockerSelenium

3. **Construa sua imagem:**
   ```bash
   docker build -t nome-imagem .
4. **Execute o Contêiner:**
   ```bash
   docker run nome-imagem