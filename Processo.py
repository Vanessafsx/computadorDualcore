import threading
import time

class Processo(threading.Thread):
    def __init__(self, pid, execution_time, quantum, core):
        super().__init__()
        self.pid = pid
        self.execution_time = execution_time
        self.quantum = quantum
        self.core = core
        self.wait_time = 0
        self.execution_count = 0
    
    def run(self):
        while self.execution_time > 0:
            self.execution_count += 1
            self.core.acquire()
            
            print(f"Processo {self.pid} executando no núcleo")
            execution_slice = min(self.quantum, self.execution_time)
            time.sleep(execution_slice / 1000)
            
            self.core.release()
            self.execution_time -= execution_slice
            self.wait_time += execution_slice
    
    def get_execution_count(self):
        return self.execution_count
    
    def get_wait_time(self):
        return self.wait_time

def main():
    quantum = int(input("Digite o valor do quantum (em ms): "))
    execution_times = [int(x) for x in input("Digite os tempos de execução dos processos (em ms), separados por espaço: ").split()]
    
    core_locks = [threading.Lock() for _ in range(2)]
    processes = []

    for i, execution_time in enumerate(execution_times):
        process = Processo(i + 1, execution_time, quantum, core_locks[i % 2])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for process in processes:
        print(f"Tempo de espera do Processo {process.pid}: {process.get_wait_time()} ms")
        print(f"Tempo de processamento no Núcleo: {process.get_execution_count() * quantum} ms")
    
if __name__ == "__main__":
    main()
