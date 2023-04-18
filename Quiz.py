import random
pontos = 0
vidas = 1

def diff():
    global dificuldade
    if pontos >=6:
        dificuldade = perguntas_dif
    elif pontos >=3:
        dificuldade = perguntas_med
    else:
        dificuldade = perguntas_ez

def gerarpergunta():
    global p_escolhida
    p_escolhida = random.choice(list(dificuldade.keys()))
    print(dificuldade[p_escolhida]["pergunta"])
    for k, v in dificuldade[p_escolhida]["alternativas"].items():
        print(k, v)

def acertoerro():
    global pontos
    global vidas
    if resposta.isalpha():
        if resposta.lower() == dificuldade[p_escolhida]["gabarito"]:
            pontos +=1
            del dificuldade[p_escolhida]
            print("\nAcertou!\n")
        else:
            print("\nResposta errada! 🧠❌\n")
            vidas -=1
    else:
        print('\nInsira apenas "a, b, c ou d"! \n')

perguntas_ez = {
    "p1": {
    "pergunta": "O dragão é um animal: ",
    "alternativas": {"a)": "mitológico", "b)": "invertebrado", "c)": "extinto", "d)": "pré-histórico"},
    "gabarito": "a"
    },
    "p2": {
    "pergunta": 'O que se comemora no "thanksgiving"?',
    "alternativas": {"a)": "ação de graças", "b)": "natal", "c)": "dia das mães", "d)": "dia do agradecimento"},
    "gabarito": "a"
    },
    "p3": {
    "pergunta": "Quantos lados possui um losangulo?",
    "alternativas": {"a)": "3", "b)": "4", "c)": "5", "d)": "6"},
    "gabarito": "b"
    },
    "p4": {
    "pergunta": 'O que significa a expressão "dar o braço a torcer"?',
    "alternativas": {"a)": "confiar em uma pessoa", "b)": "mudar de opinião", "c)": "desconfiar de uma pessoa", "d)": "sacrificar-se"},
    "gabarito": "b"
    },
    "p5": {
    "pergunta": "Qual é o significado da sigla USP?",
    "alternativas": {"a)": "Único Sistema Paulista", "b)": "Universale Selbstladepistole", "c)": "Unidos do São Paulo", "d)": "Universidade de São Paulo"},
    "gabarito": "d"
    }
}
perguntas_med = {
    "p1": {
        "pergunta": "Qual destas Sete Maravilhas do Mundo ainda existem?",
        "alternativas": {"a)": "Estátua de Zeus", "b)": "Farol de Alexandria", "c)": "Pirâmide de Gizé", "d)": "Os Jardins Suspenos da Babilônia"},
        "gabarito": "c"
    },
    "p2": {
        "pergunta": "Qual destas palavaras tem a sílaba tônica aberta?",
        "alternativas": {"a)": "medíocre", "b)": "côncavo", "c)": "vovó", "d)": "bebê"},
        "gabarito": "c"
    },
    "p3": {
    "pergunta": "Que lado do triângulo retângulo é oposto ao ânulo de 90 graus?",
    "alternativas": {"a)": "base cossênica", "b)": "cateto adjacente", "c)": "cateto oposto", "d)": "hipotenusa"},
    "gabarito": "d"
    },
    "p4": {
    "pergunta": "Qual é o nome da antiparticula oposta ao elétron?",
    "alternativas": {"a)": "pósitron", "b)": "nêutron", "c)": "quark", "d)": "antielétron"},
    "gabarito": "a"
    },
    "p5": {
    "pergunta": 'Qual é o significado da palavra "plácida"?',
    "alternativas": {"a)": "irritada", "b)": "apressada", "c)": "inquieto", "d)": "sossegada"},
    "gabarito": "d"
    }
}
perguntas_dif = {
    "p1": {
    "pergunta": "Qual é a velocidade de escape da Terra?",
    "alternativas": {"a)": "40.320km/h", "b)": "6.443km/h", "c)": "12.890km/h", "d)": "9.999km/h"},
    "gabarito": "a"
    },
    "p2": {
    "pergunta": "Qual é o elemento químico mais abundante no universo?",
    "alternativas": {"a)": "carbono", "b)": "oxigênio", "c)": "hidrogênio", "d)": "cálcio"},
    "gabarito": "c"
    },
    "p3": {
    "pergunta": "Quais das 3 leis de Newton estão na sequência correta?",
    "alternativas": {"a)": "Princípio Fundamental da Dinâmica, Lei da Ação e Reação e Lei da Inércia", "b)": "Lei da Inércia, Princípio Fundamental da Dinâmica e Lei da Ação e Reação", "c)": "Lei da Ação e Reação, Princípio Fundamental da Dinâmica e Lei da Inércia", "d)": "Princípio Fundamental da Dinâmica, Lei da Inércia e Lei da Natureza"},
    "gabarito": "b"
    },
    "p4": {
    "pergunta": "Qual é a capital da Hungria?",
    "alternativas": {"a)": "Mônaco", "b)": "Budapeste", "c)": "Liechtenstein", "d)": "Ancara"},
    "gabarito": "b"
    },
    "p5": {
    "pergunta": "Qual das datas abaixo condiz com o nascimento e a morte de Getúlio Vargas?",
    "alternativas": {"a)": "31/09/1905 - 22/03/1995", "b)": "23/09/1899 - 12/01/1977", "c)": "29/01/1898 - 03/12/1943", "d)": "19/04/1882 - 24/08/1954"},
    "gabarito": "c"
    }
}

while vidas >0 and pontos <9:
    diff()
    gerarpergunta()
    resposta = input("Qual será sua resposta? ")
    acertoerro()

if pontos == 9:
    print("GG! 🧠✔️\n")