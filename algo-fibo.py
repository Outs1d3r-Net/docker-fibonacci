#!/usr/bin/env python3

# -*- coding: utf-8 -*-

###############################################################
# BY: Juan Regis                                              #
# Ref: https://flask.palletsprojects.com/en/1.1.x/quickstart/ #
###############################################################

#===> LIBRARIES
from flask import Flask
import os

app = Flask(__name__)                            # OBJ CLASS FLASK CREATE.
@app.route("/")                                  # DECORATOR FOR TELL FLASK WHAT URL.

#===> FUNCTIONS ,MAIN AND HTML CS
def index():
    pN = 0
    sN = 1

    listaFIBO = []
    listaFIBO.append(str(pN))
    fiboC = 50

    while len(listaFIBO) != fiboC:
        pN,sN = sN,pN+sN
        listaFIBO.append(str(sN))

    r = ' '.join(listaFIBO)

    r = "<h1><center>"+str(r)+"</center></h1>"

    re = """
<!-- CODE SOURCE HTML-->
<html>
    <meta charset='UTF-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0">
    <head>
        <title>Ac 03 - Prof: Antonio</title>
    </head>
    
    <!-- CSS STYLE -->
    <style>
       body{background-color: #ffffff;
			background-image: linear-gradient(#9129c4, #6d6e6d);
       }
       
       #cods{
           background-color: #ffffff;
           border-radius: 12%;
           border: solid 2px black;
       }
      
      #defi{
           background-color: #ffffff;
           border-radius: 5%;
           border: solid 1px black;
       }
    </style>
    
    <!-- TITLE -->
    <center><h1>Sequencia de fibonacci em python</h1>
    
    <!-- IMAGENS -->
    <img src="https://i.ibb.co/QpKSBsR/Python.png" width="10%" />
    <img src="https://i.ibb.co/sRtcXJf/Html5.png" width="10%" />
    <img src="https://i.ibb.co/68GftgT/Css3.png" width="10%" />
    <img src="https://i.ibb.co/1LK4Qg5/Flask.png" width="13%" />
    <img src="https://i.ibb.co/FnXJD1L/docker.png" width="13%" />
    </center><br/>
    
    <pre><h2>Definição:</h2>
    <div id="defi">
            <center>Os números de Fibonacci são usados ​​para criar indicadores técnicos usando uma sequência matemática desenvolvida pelo matemático italiano<br/> comumente referido como "Fibonacci" no século XIII. A sequência de números, começando com zero e um, é criada adicionando os dois números anteriores.<br/>Por exemplo, a parte inicial da sequência é 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144, 233, 377 e assim por diante. Aqui eu exibo os 50 primeiros numeros desta sequencia.</center>
        </pre>
    </div><br/><br/>

    <h2>Codigo fonte:</h2>
    <div id="cods"><code><pre>
	pN = 0                           # Este é o primeiro numero para o calculo Fn = Fn-1 + Fn-2
	sN = 1                           # Este é o segundo numero para formar os valores iniciais como: F1 = 1, F2 = 1

	listaFIBO = []                   # Aqui eu deixou uma lista para armazenar os numeros de fibonacci encontrados pelo meu algoritmo.
        listaFIBO.append(str(pN))        # Aqui eu adiciono o numero 0 na sequincia de fibonacci.
        fiboC = 50                       # Um contador para a quantidade de numeros que eu desejo encontrar.

	while len(listaFIBO) != fiboC:   # Isto é uma condição aonde o calculo interrompe o programa quando a lista estiver os 50 primeiros numeros.
	    pN,sN = sN,pN+sN             # O calculo para gerar os numeros começa aqui.
	    listaFIBO.append(str(sN))    # Utilizando a funcao append() do python para adicionar na lista os numeros de fibonacci encontrados.

	r = ' '.join(listaFIBO)          # Com este codigo eu transformo a lista em uma sequencia de numeros para exibição.
	print(r)                         # Exibindo a sequencia de numeros.
    </pre></code></div>


    <!-- START OF THE FUNCTION OF FIBONACCI         -->
    <h2>Resultado dos """+str(fiboC)+""" primeiros numeros de fibonacci é: </h2>"""+r+"""
    <!-- END OF THE FUNCTION                     -->
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <footer><center>
      <p><b>Author:</b> Juan Regis</p>
      <p><i>Defesa Cibernetica 2º Semestre.</i></p>
    </center></footer>
</html>
"""

    return re

#===> MAIN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)               # HERE I USE PORT TCP/5000
