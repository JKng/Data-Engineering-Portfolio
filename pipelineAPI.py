MANIPULAR UMA API

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas (pegando somente ano, mês e dia, uma vez que datetime.today() retorna, também, minutos e horas)
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

# variáveis que definem a cidade (city) sobre a qual queremos extrair os dados
city = 'Boston'
key = 'ANZQ5K8QQP8BXZ85F4EQ2FPK'

# função join() a url estã dividida em duas partes: a primeira corresponde à url da documentação, 
# enquanto a segunda, onde há f string, elenca as variáveis definidas anteriormente
# e o formato com o qual desejamos que os dados venham (csv ou json)
# o unitGroup= permite passar o sistema de unidade que quer que os dados retornem (Celsius)
# condensação dos dados em dias (include=days), e não em horas ou meses

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)

# ver as primeiras linhas desses dados no terminal (Ctrl+J)
print(dados.head())

file_path = f'home/millenagena/Documents/datapipeline/semana={data_inicio}'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')


