**Versão 2**
- Temos um container contendo webscraping utilizando Selenium e bs4. 
- Aplicamos esse container na função lambda AWS que também abasteceu uma base de dados no S3.
- Além disso toda arquitetura do Cloud está formulada com ServerLess FrameWork sendo sua implementação feita com apenas algumas linhas de código no terminal.


Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7
- ServerLess FrameWork 3.38.0
- aws-cli 2.15.15

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping_Lambda_AWS.git
2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd WebScraping_Lambda_AWS/V2

3. **Chave de acesso AWS**
  - Crie um usuário associando-o a política de AdministratorAccess ou use o usuário root.
  - Depois crie sua chave de acesso desse usuário para logar no AWS CLI.

4. **Acesse AWS CLI**
   ```bash
   aws configure

5. **Faça Deploy da sua Aplicação Cloud**
   ```bash
   sls deploy
6. **Chame a função Lambda AWS**
   ```bash
   sls invoke --functon demo

