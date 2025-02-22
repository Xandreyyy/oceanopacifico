import random
import requests
from googletrans import Translator
import pprint as pp

apikey = "a8phdjp9xdpwbyggc8q1w3jh4vo2hcldvrjx7sxi65il16gvn"
link = "http://api.wordnik.com/v4/words.json/randomWord?api_key="+apikey
req = requests.get(link)
info = req.json()
wordnik = info['word']
pp.pp(wordnik)
googletrans = Translator()
traducao = googletrans.translate(wordnik, src="en", dest="pt").text
palavra_escolhida = traducao
pp.pp(palavra_escolhida)

palavra = ["_"]*len(palavra_escolhida)
letras = []
vidas = 5
acabou = False

def poucohp(vidas):
    if vidas <4 and letra not in palavra:
        print(f"Você tem ❤️{vidas} restante(s)!")
        
def ganhou():
  global acabou
  acabou = True
  print("\n🌟🎊🎊🎊🎊🎊🌟")
  print("🎉🎉🎉GG🎉🎉🎉")
  print("🌟🎊🎊🎊🎊🎊🌟")

def letra_palavra():
    global palavra_escolhida, palavra, vidas
    poucohp(vidas)
    if len(letra)==1:
        if letra in palavra_escolhida:
            for i in range(len(palavra_escolhida)):
                if letra == palavra_escolhida[i]:
                    palavra[i] = letra
            print(f'✔️ A letra: "{letra}" está na palavra!')
            print(" ".join(palavra))
        elif letra != palavra_escolhida:
            print(f'❌ A letra: "{letra}" não está na palavra! ')
            vidas -=1

def chute():
    global vidas
    if len(letra)>1:
        certeza = input(f'Você tem certeza que deseja chutar a palavra "{letra}"? (S/N) ')
        if certeza.lower() == "s" and letra == palavra_escolhida:
            ganhou()
        elif certeza.lower() == "s" and letra != palavra_escolhida:
            vidas -= 3

print("▬"*27)
print("Bem-vindo ao Jogo da Forca! \nBoa sorte! ")
print("▬"*27)
print(f"A palavra possui {len(palavra_escolhida)} letras. ")

while vidas>0 and acabou == False:
    letra = input("\nLetra: ")
    if letra in letras:
        print("Você já usou essa letra!")
    elif letra.isalpha():
        letras.append(letra)
        letra = letra.lower()
        chute()
        letra_palavra()
    else:
        print("Digite apenas letras! ")
    if vidas ==0:
        print(f'\nAcabaram suas vidas! A palavra era: "{palavra_escolhida.capitalize()}".')
    elif "_" not in palavra:
        ganhou()
