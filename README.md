# Inteli - Instituto de Tecnologia e Liderança

<p align="center">
  <a href= "https://www.inteli.edu.br/"><img src="docs/assets/images/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>

<br>

# Automação com Reconhecimento de Voz

## Grupo Claus

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/in/heitorprudente/">Heitor Elias Prudente</a>
- <a href="https://www.linkedin.com/in/marcelomiguelassis/">Marcelo Miguel Pereira de Assis</a>
- <a href="https://www.linkedin.com/in/raissa-vieira-de-melo/">Raíssa Vieira de Melo</a>
- <a href="https://www.linkedin.com/in/raphaela-guiland-ferraz/">Raphaela Guiland Ferraz</a>
- <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Gabriel Marques</a>

## 👩‍🏫 Professores:

### Orientador(a)

- Hermano Peixoto

### Instrutores

- Reginaldo Arakaki
- Victor Hayashi
- Hermano Peixoto
- Francisco Escobar
- Geraldo Magela
- Lisane Valdo
- Ana Cristina dos Santos

## 📜 Descrição

O projeto tem como objetivo desenvolver uma solução tecnológica para otimização do processo de acompanhamento das mudanças regulatórias na indústria financeira no Brasil. Esta solução visa atender às necessidades do **Bank of America**, que enfrenta um cenário regulatório cada vez mais complexo devido ao aumento do volume e do ritmo das mudanças em leis, regras e regulamentações (LRR) desde a crise financeira global de 2008.

O principal desafio é a diversidade de normas e regulamentos emitidos por diferentes órgãos reguladores, como Banco Central do Brasil (BACEN), Comissão de Valores Mobiliários (CVM), Brasil Bolsa e Balcão (B3), entre outros. Essas normas são publicadas em diferentes formatos e locais, tornando o processo de monitoramento e conformidade particularmente trabalhoso e exigente em termos de recursos.

Para resolver esse problema, o projeto propõe uma solução que combina técnicas de Processamento de Linguagem Natural (PLN) com aplicações web para automatizar etapas como:

- Monitoramento diário de novas LRRs.
- Classificação automatizada dos normativos com base em critérios pré-definidos.
- Consulta ao repositório por meio de comandos em linguagem natural.

A solução busca reduzir os riscos e aumentar a eficiência operacional, permitindo ao Bank of America alocar recursos de maneira mais eficiente e garantir conformidade regulatória. Essa automação proporcionará uma resposta ágil e precisa às demandas regulatórias, auxiliando na gestão das mudanças e minimizando o esforço manual atualmente envolvido no processo.

O escopo inclui a captura e classificação de LRRs de até dois sites reguladores específicos, conforme indicado pela equipe do Bank of America, com simulação de um fluxo completo de captura, download, classificação e consulta das LRRs usando linguagem natural.

Em resumo, a solução visa simplificar e otimizar o processo de Reg Change, contribuindo para a excelência operacional e conformidade do Bank of America no Brasil.

## 📁 Estrutura de pastas

```
data/
└── processed/
└── raw/
docs/
└── assets/
    └── images/
└── outros/
└── README.md
notebook/
└── intent/
    └── explore/
    └── model/
    └── tests/
└── tagging/
    └── explore/
    └── model/
    └── tests/
src/
└── backend/
    └── src/
        └── config/
        └── controllers/
        └── middlewares/
        └── migrations/
        └── models/
        └── routes/
        └── seeders/
        └── services/
        └── validations/
        └── app.js
    └── index.js
└── frontend/
    └── public/
    └── src/
        └── assets/
        └── components/
        └── pages/
        └── style/
        └── main.jsx
        └── routes.jsx
    └── index.html
└── services/
    └── nlp/
        └── src/
            └── models/
            └── pipelines/
            └── nlp_service.py
        └── requirements.txt
    └── webscraping/
        └── config/
        └── helpers/
        └── scraping/
        └── services/
        └── main.py
.gitignore
README.md
```

Na raiz do projeto, temos o diretório ``data/``, que armazena dados usados no projeto. Ele é dividido em dois subdiretórios: ``processed/``, que contém os dados processados ou transformados para análise e uso, e ``raw/``, que armazena os dados brutos obtidos diretamente de fontes externas, sem modificações.

O diretório ``docs/`` é dedicado à documentação do projeto. Ele contém um subdiretório ``assets/`` que guarda imagens usadas na documentação. Além disso, há um diretório ``outros/`` para armazenar documentos variados que não se encaixam nas outras categorias, e o arquivo ``README.md``, que geralmente oferece uma visão geral do projeto, explicando sua finalidade, como instalá-lo e usá-lo.

O diretório ``notebooks/`` contém notebooks Jupyter ou outros arquivos de exploração de dados e modelagem. Ele é subdividido em dois diretórios principais: ``intent/`` e ``tagging/``, cada um relacionado a diferentes aspectos do processamento de linguagem natural (PLN) no projeto. Dentro de cada um deles, há subdiretórios como ``explore/`` para notebooks de exploração de dados, ``model/`` para notebooks relacionados ao desenvolvimento e avaliação de modelos, e ``tests/`` para notebooks contendo testes de validação.

O diretório ``src/`` é onde o código-fonte principal do projeto está localizado. Ele é dividido em três partes principais: ``backend/``, ``frontend/`` e ``services/``.

No ``src/backend/``, temos a estrutura de um servidor backend provavelmente desenvolvido em Node.js. Dentro de ``src/backend/src/``, há subdiretórios como ``config/`` para configurações da aplicação, ``controllers/`` que contém a lógica de controle da aplicação, ``middlewares/`` para middlewares utilizados, ``migrations/`` para scripts de migração de banco de dados, ``models/`` para definir as entidades do banco de dados, ``routes/`` que especifica as rotas da API, ``seeders/`` para dados de inicialização, services/ para serviços que encapsulam a lógica de negócios, ``validations/`` para validações de dados, e o arquivo principal ``app.js``. O arquivo index.js serve como ponto de entrada para o servidor.

O diretório ``src/frontend/`` contém o código para o frontend do projeto. Há um subdiretório ``public/`` que provavelmente contém arquivos públicos, como imagens e o favicon. O subdiretório ``src/`` é onde está o código principal do frontend, dividido em ``assets/`` para recursos como imagens e estilos, ``components/`` para componentes reutilizáveis da interface, ``pages/`` que representa as diferentes páginas da aplicação, ``style/`` para arquivos de estilo (como CSS), e arquivos como ``main.jsx`` e ``routes.jsx`` que contêm o código de entrada principal e as definições de rotas da aplicação. O arquivo ``index.html`` é o ponto de entrada para o frontend.

O diretório ``services/`` é subdividido em dois serviços específicos: ``nlp/`` e ``webscraping/``.

Dentro de ``services/nlp/``, que se refere ao serviço de processamento de linguagem natural, encontramos o diretório ``src/`` com subdiretórios como ``models/`` para armazenar modelos de PLN e ``pipelines/`` para scripts que definem a pipeline de processamento de textos. O arquivo ``nlp_service.py`` implementa o serviço de PLN. O arquivo requirements.txt lista as dependências necessárias para rodar este serviço.

O subdiretório ``webscraping/`` contém arquivos e pastas relacionados a tarefas de raspagem de dados da web. Há subdiretórios como ``config/`` para configurações, ``helpers/`` que provavelmente contém funções auxiliares, ``scraping/`` para scripts que realizam a raspagem propriamente dita, e ``services/`` para serviços que encapsulam a lógica de raspagem de dados. O arquivo principal ``main.py`` provavelmente é o ponto de entrada para o serviço de raspagem.

Na raiz do projeto, há também arquivos importantes como ``.gitignore`` para especificar quais arquivos ou diretórios devem ser ignorados pelo Git, e ``README.md`` para fornecer informações gerais sobre o projeto e instruções de uso.

## 🔧 Instalação

Para rodar o projeto na versão de desenvolvimento, local, é necessária as seguintes bibliotecas:

- Node.js (Versão >= 18)
- Git
- Docker e Docker Compose
- Python (Versão >= 3.8)

Após a instalação das dependências, siga os passos abaixo:

**1. Clone o repositório:**
    
```bash
git clone https://github.com/Inteli-College/2024-2A-T09-ES07-G01
```	

**2. Instale as Dependências Internas do Frontend:**
```bash
cd claus-fork/src/frontend

npm install
```	

**3. Crie o arquivo `.env` com as variáveis de ambiente necessárias.**
> Este arquivo deve estar na raiz das pastas `src/backend`,  `src/frontend`,  `src/services` e `src/stt`. Todas essas pastas contém o arquivo `.env.local.sample` que pode ser copiado e renomeado para `.env` e preenchido com as informações necessárias.

**4. Execute a Aplicação (Frontend) Localmente:**
```bash
npm run dev
```
Após isso, é possível acessar a aplicação usando o endereço `http://localhost:5173`.

**5. Inicie Backend e Serviços:**
```bash
cd claus-fork

docker-compose up backend log-service service-intent stt
````

**6. Execute Testes Locais:**
```bash
npm run test
```

## 🗃 Histórico de lançamentos
- 1.0.0 - 10/10/2024
    - Refinamento de funcionalidades do frontend.
    - Refinamento de documentação.
    - Refinamento de readme do repositório.
    - Entrega dos artefatos da sprint 5.

- 0.4.0 - 27/09/2024 
    - Documentação dos Wireframes e Mockups.
    - Integração de POST de logs para as telas de E-mail e Histórico.
    - Correções na documentação e ajustes no conteúdo.
    - Implementação de testes de integração nas telas de Home, Histórico e E-mail.
    - Correção na estrutura da pasta assets.
    - Adição de carregamento com componente de Loading.
    - Correção de erros na página de E-mails.
    - Atualização e correção da paginação.
    - Revisão dos requisitos do sistema.
    - Refatoração do módulo PLN de Intenção.
    - Refatoração do endpoint de busca de documentos.
    - Ajustes de estilização em diversos componentes.
    - Implementação de testes unitários (Filtros, Tabela, DateFilterButton e ModalRegisterEmail, Header e ResultsCount).
    - Implementação do recurso de edição de tags.
    - Atualização da Pilha de Tecnologias.
    - Documentação dos testes unitários e de integração.
    - Atualização da documentação do frontend e comparação com o mockup.
    - Documentação do processo de deploy da solução integrada.
    - Implementação de malha fechada e envio de e-mails automatizado.
    - Entrega dos artefatos da sprint 4.

- 0.3.0 - 13/09/2024
  - Nova estrutura do frontend utilizando Vite.
  - Criação de componentes do frontend.
  - Documentação atualizada sobre o Banco de Dados.
  - Criação do componente de Modal e estrutura inicial da tela de Notificações.
  - Definição da arquitetura do Backend.
  - Implementação de filtros no frontend.
  - Filtros de Órgão e Tag no frontend.
  - Desenvolvimento completo da tela de Notificações.
  - Conclusão da integração do Backend na Sprint 3.
  - Integração da tela Home com backend e filtros.
  - Criação da tela de Histórico.
  - Atualização da documentação com a arquitetura do Backend.
  - Adição do tópico sobre o Backend da solução na documentação.
  - Adição do tópico sobre o Frontend da solução na documentação.
  - Adequação da estrutura ao padrão do Escritório de Projetos.
  - Referência à arquitetura na documentação do Backend.
  - Entrega dos artefatos da sprint 3.

- 0.2.0 - 30/08/2024
  - Adição das pastas `src/` e `frontend/`.
  - Definição da arquitetura para processamento de linguagem natural (PLN).
  - Implementação do módulo de PLN para Tagging.
  - Criação dos testes para validação do PLN de Tagueamento.
  - Desenvolvimento de um Crawler para download de arquivos PDF da CVM.
  - Documentação do Sistema de Áudio.
  - Testes do PLN/NLU para reconhecimento de intenções.
  - Implementação do módulo de PLN/NLU de Intenção.
  - Integração do frontend com a API de reconhecimento de fala (STT).
  - Implementação do módulo de envio de e-mails pós-scraping.
  - Inclusão de novos artefatos da Sprint 2.
  - Integração com serviço de NLP na nuvem.
  - Atualização da pilha de tecnologias.
  - Entrega dos artefatos da sprint 2.

- 0.1.0 - 16/08/2024
  - Atualização do template de documentação.
  - Adição do tópico de problema no entendimento de negócios.
  - Inclusão dos requisitos do sistema. 
  - Expansão dos tópicos 1.1.1 e 1.1.2 em entendimento de negócios.
  - Documentação sobre o entendimento do design.
  - Inclusão das tendências da área de domínio.
  - Definição das experiências esperadas para o usuário.
  - Elaboração dos padrões de trabalho.
  - Descrição detalhada da solução proposta.
  - Identificação das partes interessadas e competências necessárias.
  - Matriz de riscos e oportunidades.
  - Estimativa de investimento.
  - Desenho do sistema.
  - Proposta de UX.
  - Criação do Canvas de Proposta de Valor.
  - Definição da pilha de tecnologias.
  - Entrega dos artefatos da sprint 1.

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-2A-T09-ES07-G01">Claus</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2024-2A-T09-ES07-G01">INTELI, Heitor Elias Prudente, Marcelo Miguel Pereira de Assis, Raíssa Vieira de Melo, Raphaela Guiland Ferraz, Victor Gabriel Marques</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>