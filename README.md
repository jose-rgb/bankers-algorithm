<h2> 👨🏻‍💻 O algoritmo do banqueiro é um algoritmo clássico utilizado para evitar deadlock e foi estabelecido por Dijkstra e Habemann em 1965. Esse nome foi escolhido por tratar do problema através da seguinte analogia: um banqueiro (o Sistema Operacional) de uma pequena cidade pode negociar com um grupo de clientes (os processos), aos quais ele libera linhas de crédito (que são recursos do sistema). O algoritmo tem como função determinar se a liberação de uma requisição é capaz de levar o sistema a um estado inseguro; se for este o caso, o banqueiro nega a requisição. Algoritmo do banqueiro para um único tipo de recurso Neste caso, para saber se um estado é seguro ou não, o banqueiro leva em consideração cada solicitação de empréstimo. Ele verifica se dispõe de recursos suficientes para atender algum dos clientes. Caso tenha, ele assume que os empréstimos feitos a este cliente serão pagos (devolvidos); em seguida, é considerado o cliente mais próximo do limite de recursos e assim por diante. Se todos os empréstimos puderem ser pagos (devolvidos), o estado é considerado seguro e a requisição inicial pode ser atendida.</h2>


<h2>🛠 Dependências</h2>

É necessário voçê ter o [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) instalado.
```
https://www.python.org/downloads/
```
É a biblioteca [Numpy](https://numpy.org/)
```
https://numpy.org/install/
```

<h2>🚀 Executando o Algoritmo</h2>

Como o algoritmo requer um grande número de funcionalidades, As funções ficaram em um arquivo separado ó [functions.py](https://github.com/jose-rgb/bankers-algorithm/blob/main/functions.py), para deixar o código mais organizado, sendo assim, o arquivo principal é que deve ser executado é o [bankers-algorithm.py](https://github.com/jose-rgb/bankers-algorithm/blob/main/bankers-algorithm.py).

<h2> 🎥 🎞 Vídeo Demonstrativo </h2>
<a href="https://youtu.be/VnJoLpywogw">
    <img align="center" src="https://image.flaticon.com/icons/png/512/1384/1384060.png"  height="40" width="40" />
<a>
