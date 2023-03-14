# Extrair dados da previsão do tempo de uma API
# Criar uma pasta Local utilizando Python;
# Salvar os arquivos extraídos em csv.

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas (pegando somente ano, mês e dia, uma vez que datetime.today() retorna, também, minutos e horas)
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

# variáveis que definem a cidade (city) sobre a qual queremos extrair os dados
city = 'inUSA'
key = '23digits'

# função join() a url estã dividida em duas partes: a primeira corresponde à url da documentação, 
# enquanto a segunda, onde há f string (útil para passar uma variável à url), elenca as variáveis definidas anteriormente
# e o formato com o qual desejamos que os dados venham (csv ou json)
# o unitGroup= permite passar o sistema de unidade que quer que os dados retornem (Celsius)
# condensação dos dados em dias (include=days), e não em horas ou meses

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)

# ver as primeiras linhas desses dados no terminal (Ctrl+J) digitar o comando python3 seguido do nome deste arquivo .py
print(dados.head())



