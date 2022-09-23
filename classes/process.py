class Process:
    def __init__(self,id, arrive_time, execution_time, context_change_time, ready = True):
        self.id = id
        self.arrive_time = arrive_time
        self.execution_time = execution_time
        self.context_change_time = context_change_time
        self.ready = ready

    def set_ready(self, new_value):
        self.ready = new_value