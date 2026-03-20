class Worker:

    workers_nmbr = 0

    def __init__(self, first_name, last_name):
        Worker.workers_nmbr += 1  #takes workers_nmbr variable from Worker class
        self.workers = Worker.workers_nmbr
        self.first_name = first_name
        self.last_name = last_name

workers = []
workers.append(Worker("John", "Doe"))
workers.append(Worker("Jane", "Doe"))

for w in workers:
    print(w.first_name, w.last_name)
