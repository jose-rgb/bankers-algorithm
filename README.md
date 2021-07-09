<h2> 👨🏻‍💻 The banker's algorithm is a classic algorithm used to avoid deadlock and was established by Dijkstra and Habemann in 1965. This name was chosen because it addresses the problem through the following analogy: a banker (the Operating System) in a small town can trade with one customer group (the processes), to which it releases lines of credit (which are system resources). The algorithm's function is to determine if the release of a request is capable of taking the system to an insecure state; if this is the case, the banker denies the request. Banker's Algorithm for a Single Resource Type In this case, to know whether a state is safe or not, the banker takes into account each loan request. He checks if he has enough resources to serve any of the customers. If so, it assumes that the loans made to this customer will be paid (returned); then it is considered the client closest to the resource limit, and so on. If all loans can be repaid (returned), the state is considered secure and the initial application can be granted..</h2>


<h2>🛠 dependencies</h2>

É necessário voçê ter o [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) instalado.
```
https://www.python.org/downloads/
```
is the library [Numpy](https://numpy.org/)
```
https://numpy.org/install/
```

<h2>🚀 Running the Algorithm</h2>

As the algorithm requires a large number of features, the functions were in a separate file or [functions.py](https://github.com/jose-rgb/bankers-algorithm/blob/main/functions.py), to make the code more organized, so the main file should be executed is the [bankers-algorithm.py](https://github.com/jose-rgb/bankers-algorithm/blob/main/bankers-algorithm.py).

<h2>🎥 Demo Video </h2>
<a href="https://youtu.be/VnJoLpywogw">
    <img align="center" src="https://image.flaticon.com/icons/png/512/1384/1384060.png"  height="40" width="40" />
<a>
