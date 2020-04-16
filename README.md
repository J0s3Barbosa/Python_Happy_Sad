### About the project: ###

```sh

Projeto usando a linguagem Python

Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número, em seguida você faz a soma desses resultados. A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma. Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial é considerado feliz.

Tomamos o 7, que é um número feliz:

7² = 49

4² + 9² = 97

9² + 7² = 130

1² + 3² + 0² = 10

1² + 0² = 1

Podemos observar nesse exemplo que os números 49, 97, 130 e 10 também são felizes. Existem infinitos números felizes.

E um número triste? Como sabemos que um número não será feliz?

Desenvolva um programa que determine se um número é feliz ou triste. Faça o programa utilizando TDD e retornando True para números felizes e False para números tristes!

```
### Run the project: ###

```sh
Install virtualenv if not yet

py -m pip install virtualenv
python -m pip install --upgrade pip

Run the command below to run virtualenv
py -m virtualenv venv

Activate venv
. venv\scripts\activate

Install Requirements
pip install -r requirements.txt


```
### Run tests: ###

```sh
pytest Test_HappySad.py
```

### Run desktop app: ###

```sh
py tkinterMain.py
```

### Run flask app: ###

```sh

py flask_main.py

http://localhost:5000/
http://localhost:5000/happysadnumber/7
http://localhost:5000/happysadnumber/97


```

 





