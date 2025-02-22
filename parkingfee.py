#from google.colab import output
import pprint as pp
import datetime as dt

parkingfee = 0
data = {
    "arrived_date": 0,
    "arrived_time": 0,
    "leave_date": 0,
    "leave_time": 0
}

def welcomeMsg():
  print(f"\t\t{'︵'*14}\n\t\t{'┃'}BEM-VINDO AO VIMAPARK!{'┃'}\n\t\t{'︶'*14}")
  print("Este é um serviço que calcula a tarifa do nosso estacionamento!\nEntão, por favor, insira as seguintes informações com este padrão:\n\t     HH:MM (horário) e DD.MM.AAA (dia)")
  while True:
    start = input('\nDigite "ok" se você entendeu e deseja continuar, ou "q" para sair: \n').casefold()
    if(start == "q"):
      break
    elif(start == "ok"):
      print(data)
      inputFields()
      #output.clear()
      calcFee()
      return
    else:
      #output.clear()
      print('Insira apenas "ok" ou "q"!')

def switch(value):
  global parkingfee
  if(value >= 5):
    parkingfee = 5
    return parkingfee
  elif(value <= 2):
    parkingfee = 10
    return parkingfee
  else:
    parkingfee = 11
    return parkingfee

def inputFields():
  while True:
    arriveDate = input("Insira a data atual: ")
    if(validateDate(arriveDate) == False):
      print("Data inválida!")
      continue
    else:
      data.update({"arrived_date": validateDate(arriveDate)})
      pp.pp(data)

    arriveTime = input("Insira a hora atual: ")
    if(validateTime(arriveTime) == False):
      print("Hora inválida!")
      continue
    else:
      data.update({"arrived_time": validateTime(arriveTime)})
      print("Obrigado! Divirta-se no VIMAPARK!")
      #output.clear()
        
    print("VIMAPARK espera que você tenha se divertido! Para efetuar o pagamento\nda tarifa do estacionamento, por favor, insira as informações com o\nseguinte formato:\n\t\t HH:MM (horário) e DD.MM.AAA (dia)")
    pp.pp(data)
    leaveDate = input("\nInsira a data atual: ")
    if(validateDate(leaveDate) == False):
      print("Data inválida!")
      continue
    else:
      data.update({"leave_date": validateDate(leaveDate)})
      pp.pp(data)

    leaveTime = input("Insira a hora atual: ")
    if(validateTime(leaveTime) == False):
      print("Hora inválida!")
      continue
    else:
      data.update({"leave_time": validateTime(leaveTime)})
      pp.pp(data)
      break

#https://chat.openai.com/c/d866d440-e574-4578-8943-d17c07eec140
def validateDate(ipt):
  def isLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return 29
    else: return 28
  def maxDaysInMonth(month):
    if(month == 2): return True
    elif(month == 4 or month == 6 or month == 9 or month == 11):
      return 30
    else: return 31

  validChars = [".", "/"]
  dataList = []
  yearOfCreation = 2023
  for i in range(len(validChars)):
    charIndex = ipt.find(validChars[i])
    if(charIndex >= 0):
      dataList = ipt.split(validChars[i])
  if(len(dataList) == 3):
    for j in range(len(dataList)): dataList[j] = int(dataList[j])
    if((dataList[1] == 2) and (dataList[0] <= isLeapYear(dataList[2])) and (dataList[2] >= yearOfCreation)):
      return dataList
    elif((dataList[0] <= maxDaysInMonth(dataList[1])) and (dataList[1] <= 12) and (dataList[2] >= yearOfCreation)):
      return dataList
    else: return False
  else: return False

def validarData(ipt):
  padraoData = '%d.%m.%Y %H:%M'
  data = '21.02.2005 14:45'
  return dt.datetime.strptime(data, padraoData)

def validateTime(ipt):
  timeList = []
  ipt = ipt.strip()
  dotsIndex = ipt.find(":")
  if(dotsIndex == 2 and len(ipt) == 5):
    hourSlice = slice(0, dotsIndex)
    minSlice = slice(dotsIndex + 1, len(ipt))
    hours = ipt[hourSlice]
    mins = ipt[minSlice]
    try:
      hours = int(hours)
      mins = int(mins)
      if((hours <= 23) and (hours >= 0) and (mins >= 0) and (mins <= 59)):
        timeList = [hours, mins]
        return timeList
      else:
        return False
    except Exception as exc:
      print("O horário inserido não é válido!")
      print(exc)
      return False
  elif(len(ipt) <= 2):
    try:
      ipt = int(ipt)
      if(ipt >= 23):
        timeList = [ipt]
        return timeList
    except Exception as exc:
      print("O horário inserido não é válido!")
      print(exc)
      return False
  else: return False

def convertMinToHours():
  arrivedMinutesValue = data["arrived_time"]
  leaveMinutesValue = data["leave_time"]
  arrivedMinutes = arrivedMinutesValue[1]
  leaveMinutes = leaveMinutesValue[1]
  totalMinutes = leaveMinutes + arrivedMinutes
  minutesInHours = totalMinutes / 60
  return int(minutesInHours)

def convertDaysToHours():
  arrivedDateValues = data["arrived_date"]
  leaveDateValues = data["leave_date"]
  arrivedDay = arrivedDateValues[0]
  leaveDay = leaveDateValues[0]
  if(arrivedDay == leaveDay): return False
  totalDays = leaveDay - arrivedDay
  daysInHours = totalDays * 24
  return daysInHours

def calcTotalHours():
  arrivedHoursValue = data["arrived_time"]
  leaveHoursValue = data["leave_time"]
  arrivedHours = arrivedHoursValue[0]
  leaveHours = leaveHoursValue[0]
  totalHours = 0
  if(convertDaysToHours() == False):
    totalHours = (leaveHours - arrivedHours) + convertMinToHours()
  else:
    totalHours = (leaveHours - arrivedHours) + convertMinToHours() + convertDaysToHours()

  if(totalHours % 1 != 0):
    return int(totalHours) + 1
  return int(totalHours)

def calcFee():
  payment = calcTotalHours() * switch(calcTotalHours())

  print(f'{("="*33)}')
  print(f'┃    VIMAPARK ESTACIONAMENTO   \t┃')
  print(f'┃\t\t\t     \t┃')
  print(f'┃Data de chegada: {data["arrived_date"]}\t┃')
  print(f'┃Hora de chegada: {data["arrived_date"]}     \t┃')
  print(f'┃Data de saída: {data["arrived_date"]}    \t┃')
  print(f'┃Hora de chegada: 20:00h     \t┃')
  print(f'┃\t\t\t     \t┃')
  print(f'┃Taxa aplicada: R$5/h     \t┃')
  print(f'┃Total: R${payment}     \t\t┃')
  print(f'{("="*33)}')

welcomeMsg()
pp.pp(data)