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

    def order_by_arrive_time_and_execution_time(self):
        data_list = self.value
        new_list = []

        while data_list:
            minimum = data_list[0]
            for process in data_list:
                if process.arrive_time < minimum.arrive_time or (process.arrive_time >= minimum.arrive_time and process.execution_time < minimum.execution_time):
                    minimum = process
            new_list.append(minimum)
            data_list.remove(minimum)

        self.value = new_list
