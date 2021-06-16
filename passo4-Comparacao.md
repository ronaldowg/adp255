Comparação entre os algoritmos
=======================

Ao todo, cinco algoritmos foram utilizados para prever o comportamento do total das vendas de interruptores. As tabelas abaixo apresentam a performance de cada um:

**Ano 2020**

|  Ranking |  Algoritmo | RMSE  | Relativo  | 
|---|---|---|---|
|  1 | auto_SARIMAX   |  1.892610e+06 |  100% |  
|  2 | Prophet  | 3.196887e+06  |  60% |   
|  3 | VAR  |  3.391929e+06  | 56% |  
|  4 |  SARIMAX |  5.269293+06 | 36%  |  
|  5 |  CNN | 13.180175+06   | 2% |  

**Ano 2019**

|  Ranking |  Algoritmo | RMSE  | Relativo  | 
|---|---|---|---|
|  1 | auto_SARIMAX   |  2.280062e+06 |  100% |  
|  2 | CNN  | 2.930361+06 |  78% |   
|  3 | VAR  |  3.560624e+06 | 64% |  
|  4 |  Prophet | 3.740836e+06   | 61% |  

Para fins de comparação de performance dos algoritmos, utilizou-se a Raiz do Erro Quadrático Médio (RMSE) e a comparação relativa do melhor com os demais.

$$
RMSD = \sqrt{\frac{\sum_{i=1}^N(x_i-\hat{x_i})^2}{N}}
$$

O RMSE é normalmente utilizado para computar a acurácia dos resultados numéricos com a vantagem de apresentar valores do erro nas mesmas dimensões da variável analisada.

No ano de 2019, o total de vendas variou de 19.011266e+06 a 26.826165e+06, obtendo o auto_SARIMAX um erro de apenas 2.280062e+06 quando comparado com o CNN

No ano de 2020, o total de vendas apresentou uma amplitude muito maior do que em relação aos anos anteriores, variande de 16.697718e+06 a 41.851313e+06. O auto_SARIMAX apresentou um erro médio de 1.892610e+06, contra 13.180175+06 do CNN.

Já no ano de 2019, com o total de vendas variando de 19.011266e+06 a 26.826165e+06, auto_SARIMAX um erro de apenas 2.280062e+06, estando o CNN logo atrás com o valor de 2.930361+06.

O AutoTS, além de sugerir e rodar os algoritmos de sua biblioteca, também roda uma validação cruzada utilizando o modelo XGBoost. Desse forma, o RSME é calculado a partir da média das validações, alcançando resultados superiores. Tanto no ano de 2019 quanto em 2020, o auto_SARIMAX apresentou a melhor performance, todavia esse é um algoritmo univariado, ou seja, a predição da variável é realizada a partir dos dados históricos da mesma variável. Já os algoritmos VAR e CNN são multivariados, sendo este último implementado em camadas profundas, deep learning. Percebe-se que no ano de 2019 o algoritmo CNN obteve o melhor resultado dentre os modelos multivariados, porém com o pior desempenho em 2020. Uma possível explicação desse comportamento está no ano atípico vivenciado em 2020 devido à pandemia do SARS-CoV-2.


