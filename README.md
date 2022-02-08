# obtencaoDadosMGLUDashboard
## Ideia do projeto 
Estou começando agora a estudar Data Science, tive a ideia de focar em aprender SQL, Python e as ferramentas Power BI e Qilk. 
Essa semana criei meu primneiro Dashboard no Power BI, logo tive a ideia de obter os dados através da web e inserir esses dados no meu dashboard, após o estudo achei que a melhor for seria através de um Web Scraping com Python utilizando as bibliotecas Selenium, BeautifullSoup e Pandas

## Projeto
Após a refatoração do projeto, criei uma função para abrir o link em segundo plano utilizando options=option no webdriverChrome(), essa função foi chamada de abrirURL.
Depois criei uma função chamada salvarCsv, ela recebia como parâmetro o arquivo HTML e o nome de salvamento do arquivo csv. Depois transformava o arquivo HTML através do BeaultifulSoup e criava uma dataframe, para depois salvar em um arquivo csv.

