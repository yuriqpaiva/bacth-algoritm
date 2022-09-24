from classes.process import Process
from classes.process_list import ProcessList
from classes.colors import Colors

print(f'{Colors.OK}----- Algoritmo de escalonamento em Batch ----- {Colors.RESET}', end='\n')

print('Tipo de algoritmo:')
print(f'{Colors.OK}[1]{Colors.RESET} FIFO')
print(f'{Colors.OK}[2]{Colors.RESET} SJF')
chosen_algoritm = int(input("Sua escolha: "))
print(f'{Colors.OK}------------------------------------------------{Colors.RESET}')

process_quantity = int(input("Quantidade de processos: "))

print(f'{Colors.OK}------------------------------------------------{Colors.RESET}')

process_list = ProcessList()

for index in range(process_quantity):
    print(f'{Colors.OK}----- Inserir dados do processo {index + 1} (P{index + 1}) -----{Colors.RESET}')
    arrive_time = int(
        input(f"Tempo de chegada do processo {index + 1} (P{index + 1}): "))
    execution_time = int(
        input(f"Tempo total de execução do processo {index + 1} (P{index + 1}): "))
    context_change_time = int(
        input(f"Tempo de troca de contexto do processo {index + 1} (P{index + 1}): "))
    print(f'{Colors.OK}------------------------------------------------{Colors.RESET}')

    process_to_push = Process(index + 1, arrive_time,
                              execution_time, context_change_time)
    process_list.push(process_to_push)

if (chosen_algoritm == 2):  # FIFO
    process_list.order_by_arrive_time()
else:  # SJF
    process_list.order_by_arrive_time_and_execution_time()

current_time = 0
response_avg = 0
return_avg = 0
print('Inicializando Execução...')
print(f'{Colors.OK}------------------------------------------------{Colors.RESET}')

process_list.show_ready_processes()
for index in range(len(process_list.value)):
    current_process = process_list.value[index]
    start_time = current_time + current_process.context_change_time
    finish_time = start_time + current_process.execution_time
    print(f'P{current_process.id} entrou na CPU no tempo {start_time}')
    print(f'P{current_process.id} finalizou no tempo {finish_time}')
    current_process.set_ready(False)
    current_time = finish_time
    response_avg += start_time - current_process.arrive_time
    return_avg += finish_time - current_process.arrive_time

    if (process_list.is_there_any_ready_process()):
        print(f'Troca de contexto no tempo {finish_time}')
        process_list.show_ready_processes()

    else:
        break

response_avg /= len(process_list.value)
return_avg /= len(process_list.value)
print(f'\nMédia Tempo de Resposta: {round(response_avg, 2)}')
print(f'Média Tempo de Retorno: {round(return_avg, 2)}')
print(f'{Colors.OK}------------------------------------------------{Colors.RESET}')
