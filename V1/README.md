**Versão 1**
Essa versão é um exemplo de como rodar um container contendo um script de webscraping utilizando as bibliotecas requests e selenium.
Além disso caso queira implementar na AWS deixo o link dos posts que ensino passo a passo para cada etapa desde a criação do docker até implementação do Lambda AWS...


Posts relacionados: 
- https://www.linkedin.com/posts/bernardo-alemar-9117a11a2_voc%C3%AA-sabe-como-testar-uma-fun%C3%A7%C3%A3o-lambda-aws-activity-7161350111363530754-au1S?utm_source=share&utm_medium=member_desktop
- https://www.linkedin.com/posts/bernardo-alemar-9117a11a2_voc%C3%AA-sabe-implementar-seu-webscraping-na-activity-7161675153100288000-7QlW?utm_source=share&utm_medium=member_desktop



Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping_Lambda_AWS.git
2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd WebScraping_Lambda_AWS/V1

3. **Construa sua imagem:**
   ```bash
   docker build -t nome-imagem .
4. **Crie uma porta para testar seu Container:**
   ```bash
   docker run -p 9000:8080 nome-imagem
4. **Faça uma chamada do Container para ver sua execução:**
   ```bash
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' 

