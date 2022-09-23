class ProcessList:
    def __init__(self, value=[]) -> None:
        self.value = value

    def push(self, process_to_push):
        self.value.append(process_to_push)

    # Debug only
    def print_list(self):
        for index in range(len(self.value)):
            print(f"----- Processo {index + 1} -----")
            print(f"Tempo de chegada: {self.value[index].arrive_time}")
            print('-------------------------------')

    def show_ready_processes(self):
        ready_processes = []
        for process in self.value:
            if (process.ready == True):
                ready_processes.append(process)
        
        print('Fila de Prontos: ', end="")
        for index in range(len(ready_processes)):
            if (index + 1 == len(ready_processes)):
                print(f'P{ready_processes[index].id}.', end="\n")
            else:
                print(f'P{ready_processes[index].id}, ', end="")

    def is_there_any_ready_process(self):
        ready_processes = []
        for process in self.value:
            if (process.ready == True):
                ready_processes.append(process)

        if (len(ready_processes) > 0):
            return True

        else:
            return False

    def order_by_arrive_time(self):
        self.value.sort(key=lambda process: process.arrive_time, reverse=False)
