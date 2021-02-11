# ETAPA 2

import subprocess
import psutil
import time

**subprocess.run()**
> cria um processo e espera o processo finalizar antes de retornar para o processo que o criou

Exemplo:

```py
subprocess.run("calc")
# CompletedProcess(args='calc', returncode=0)
```
subprocess.run(["programa.exe", "arquivo.ext"]) # open file with a given program

subprocess.Popen() # creates a process and immediatly return to the parent process

In this case, when the process is created the function returns to the parent process, without whait the child process finishes. Executes a child program in a new process.

### psutil

psutil.pids()
> Return process ids

psutil.Process(pid).name()
> Return process name

psutil.Process(pid).exe()
psutil.Process(pid).cwd()
psutil.Process(pid).status()
psutil.Process(pid).create_time()
psutil.Process(pid).create_time()
time.ctime(psutil.Process(pid).create_time()) # human readable date time
  print(p.status())


Nome do usuário dono do processo:



    print(p.username())


Tempo de criação do processo:



    print(p.create_time())


Tempo de criação do processo usando a função time.ctime() do módulo time para mostrar a informação de modo mais legível. É preciso importar o módulo time.



    print(time.ctime(p.create_time()))


Tempo de CPU:



    print(p.cpu_times())


Percentual de uso de CPU em um intervalo definido no parâmetro de 1 segundo:



    print(p.cpu_percent(interval=1.0))


Informação do núcleo de CPU de afinidade:



    print(p.cpu_affinity())


Afinidade indica qual(is) núcleo(s) do processador está sendo utilizado no momento pelo processo.

Percentual de uso de memória:



    print(p.memory_percent())


Informação de uso de memória do processo:



    print(p.memory_info())


Número de threads que o processo tem:



    print(p.num_threads())


Informação de cada thread (tid, tempo de usuário e tempo de sistema):



    print(p.threads())


Ações com o processo:

  

    p.suspend() # Suspender processo
    p.resume() # Voltar de uma suspensão
    p.terminate() # terminar processo
    p.wait(timeout=3) # esperar 3s
  
### Informações do processador

psutil.cpu_times()

Returns cpu times based on five modes:
* user time
* cpu time
* idle time
* interruptions time
* low priority process times(dpc)

To get only cpu physical cores

    psutil.cpu_count(logical=False)


informações de disco
informações de memória
informações de processador
informações de processos
informações de subprocessos

