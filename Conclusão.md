## Conclusão


A previsão de vendas é uma parte importante da inteligência de negócios moderna. As vendas podem ser consideradas como uma série temporal e diferentes modelos que abordam séries temporais foram desenvolvidos, como ARIMA, SARIMA, SARIMAX, GARCH, investigando sua previsibilidade (PAVLYSHENKO, 2019).

Assim como neste trabalho, existem diversos estudos buscando prever vendas nos mais variados segmentos. Em sua pesquisa, utilizando dados meteorológicos para prever a venda de bebidas em uma rede de supermercados no Japão, Liu & Ichise (2017) utilizaram diversos algoritmos, como Gradient Boosting Decision Tree (GBDT) e Randon Decision Forest (RandForest) até chegarem à combinação de Long Short-Term Memory (LSTM) network com Stacked Denoising Autoencoder Network para obter um melhor resultado.

Para Boyapati & Mummidi (2020), os algoritmos Randon Forest Regression e Gradient Boost Regretion apresentaram os melhores resultados na previsão de vendas de itens diversos de vários pontos de vendas, com dados colhidos de diversas fontes.

A previsão de vendas de interruptores, pulsadores e tomadas, assim como as de quaisquer outros produtos, depende da análise de dados, do treinamento do modelo, da análise dos testes e da implantação do modelo para a obtenção dos resultados esperados.

Ao longo do presente trabalho, o grupo analisou dados sobre o cenário nacional, testou diferentes formas de tratamento e processamento e diversos algoritmos com o objetivo de encontrar um modelo que nos permitisse alcançar uma previsão de demanda acurada de interruptores, tomadas e pulsadores para o ano de 2020.

Após as etapas de limpeza, adequação e plotagem das informações, e considerando a característica de série temporal dos dados utilizados, nós testamos 5 modelos de previsão, sendo eles: Seasonal Autoregressive Integrated Moving Average (SARIMA), Convolutional Neural Networks (CNN) e a partir da utilização da ferramenta AutoTS, foram considerados o Autoregressive Integrated Moving Average with Exogenous Variables (SARIMAX), Prophet e Vector Autoregression (VAR).

Foi possível perceber que os modelos performaram melhor na previsão da demanda de 2019 do que de 2020, o que pode ser explicado pelos acontecimentos atípicos ocorridos em 2020 em decorrência da pandemia do SARS-CoV-2.

Após as análises e considerações apresentadas no trabalho, o grupo julgou o Auto_SARIMAX como o melhor modelo para a previsão de demanda de tomadas, interruptores e pulsadores de 2020, já que obteve o menor RMSE (1.892610e+06) entre os modelos testados.
