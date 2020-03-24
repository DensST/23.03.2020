import requests
import os
print("____________________Connection_localhost_________________") #Подключение к моему локальному серверу.
loc = requests.post('http://localhost/') #Название сервера к которому хотим подключиться. 
print(loc)
x = loc.headers
for xx, xxx in x.items(): #Перебор в цикле.
	print("{0} : {1}".format(xx, xxx)) # Благодаря этому, данные будут выводиться (в консоль).
os.system('pause') #Приостанавливание работы приложения.
print("____________________Connection_Site _________________") #Подключаюсь к веб серверу.
site = requests.post('https://httpbin.org/get')
print(site)
a = site.headers
for aa, aaa in a.items():
	print("{0} : {1}".format(aa, aaa))
