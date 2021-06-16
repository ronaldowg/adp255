Variáveis Explicativas
=======================

A partir dos modelos desenvolvidos, foi possível identificar as variáveis que mais explicam o comportamento do total de vendas de interruptores.

Primeiramente as seguintes variáveis foram analisadas:

1.   Histórico demanda interruptores. 

2.   Índice da atividade econômica. 

3.   Direcionamento financ. construção civil 

4.   Financiamento imobiliário 

5.   PIB (Setor Construção) 

6.   Taxa de crescimento Setor Construção

7.   Consumo de energia elétrica 

8.   Geração (e transmissão de energia) 

9.   Índice de confiança da Construção (ICST) 

10.  Taxa de desemprego 

11.  Variação mensal do PIB (Calculada a partir de 5.)  

12.  Índice de Confiança do Empresário Industrial 

Após o teste de causalidade de Granger conforme descrito no [Passo 2](passo2) e, após os testes dos diferentes algoritmos conforme o [Passo 3](passo3), as seguintes variáveis foram selecionadas com maior poder explicativo:

1.   Índice de Confiança do Empresário Industrial.

2.   Índice da atividade econômica. 

3.   PIB (Setor Construção).

4.   Consumo de energia elétrica.

5.   Geração de Energia Elétrica.

6.   Índice de confiança da Construção (ICST). 

Percebe-se que as variáveis explicativas estão relacionadas a área de energia elétrica e ao aspecto geral da economia do setor. Quanto ao primeiro aspecto, pode-se especular que o aumento de consumo e geração de energia estejam relacionados à expansão da construção civil e ao próprio crescimento da economia. Já quanto quanto às demais variáveis, o crescimnento do PIB do setor, aliado com a confiança dos stackholders, ajudam a prever o total de vendas de interruptores no país.

Todavia, é necessário cautela quanto a conclusões da influência das variáveis sobre a venda total de interruptores. Isto, pois, não é possível afirmar que, por exemplo, o consumo de energia elétrica influencia o total de vendas. O que pode-se afirmar é que a partir do comportamento das variáveis escolhidas é possível inferir o comportamento futuro do total de vendas de interruptores. Os modelos utilizados não apontam relações de causa e efeito, ou seja, o aumento do consumo de energia elétrica, por exemplo, pode ser um resultado do crescimento econômico, o qual influencia tanto no consumo de energia quanto no total de vendas.

Por fim, cabe ressaltar que provavelmente existam melhores variáveis que ajudem na predição do total de vendas de interruptores. Essa conclusão tem como base o desempenho superior do algoritmo auto_SARIMAX, que é univariado, quando comparado com os demais algoritmos multivariados. Ou seja, a predição do total de vendaas é mais preciso quando olhamos apenas para o desempenho passado do que quando utilizamos demais variáveis. Especula-se que existam outras variáveis exógenas influenciadoras do comportamento de vendas, que de alguma forma são representadas pelo próprio histórico da variável de vendas total. Sendo assim, de forma indireta, a partir do passado de vendas, é possível capturar já o efeito dessas variáveis para prever o futuro.