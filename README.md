# Python_Happy_Sad


instalar virtualenv se nao tiver instalado ainda
py -m pip install virtualenv
python -m pip install --upgrade pip

execute o cmd abaixo
py -m virtualenv venv

ative o env
. venv\scripts\activate

pip install -r requirements.txt

pytest Test_HappySad.py
py HappySadMain.py





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



