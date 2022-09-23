from classes.process import Process
from classes.process_list import ProcessList

print('----- Algoritmo Batch -----', end='\n')

process_quantity = int(input("Quantidade de processos: "))

process_list = ProcessList()

for index in range(process_quantity):
    print(f'--- Inserir dados do processo {index + 1} -----')
    arrive_time = int(input(f"Tempo de chegada do processo {index + 1}: "))
    execution_time = int(
        input(f"Tempo total de execução do processo {index + 1}: "))
    context_change_time = int(
        input(f"Tempo de troca de contexto do processo {index + 1}: "))
    print('-------------------------------------')

    process_to_push = Process(index + 1, arrive_time, execution_time, context_change_time)
    process_list.push(process_to_push)

process_list.order_by_arrive_time()
process_list.show_ready_processes()

current_time = 0
for index in range(len(process_list.value)):
    current_process = process_list.value[index]
    entry_time = current_time + current_process.context_change_time
    finish_time = entry_time + current_process.execution_time
    print(f'P{current_process.id} entrou na CPU no tempo {entry_time}')
    print(f'P{current_process.id} finalizou no tempo {finish_time}')
    current_process.set_ready(False)
    current_time += finish_time

    if (process_list.is_there_any_ready_process()):
        process_list.show_ready_processes()
        print(f'Troca de contexto no tempo {finish_time}')

    else:
        break
