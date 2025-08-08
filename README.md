
# Calctime
### Calculates the execution time of a given function.
#### Run Locally  

Clone the project  

~~~bash  
git clone https://github.com/diogolourencodev/calctime
~~~

Install dependencies  

> Just the ```time``` library


# How to use
## Topic 1
- Just copy and paste the function into your code
- Run your function with:
```python3
@Calctime
def your_function():
  return function

your_function()
```
A better usage example, using a simple portscanner
```python3
import socket
import time

def Calctime(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Execution time: {tempo_execucao:.2f} seconds.")
        return resultado
    return wrapper

ip = 'www.wikipedia.org'

@Calctime
def scan(ip):
	open_ports = []
	for port in range(444):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.04)
		
		r = s.connect_ex((ip, port))
		if r == 0:
			open_ports.append(port)
	for port in open_ports:
		print(f'{port} open')

scan(ip)
```
