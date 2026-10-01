# Write your solution here:
class Task:

    total_task=[]

    def __init__(self, description, name, time):
        self.__id = self.number_of_task()
        self.__description = description
        self.__name = name
        self.__time = time
        self.__completed = False
    
    @property
    def id(self):
        return self.__id

    @property
    def programmer(self):
        return self.__name

    @property
    def workload(self):
        return self.__time

    @property
    def description(self):
        return self.__description

    @property
    def is_completed(self):
        return self.__completed

    def number_of_task(self):
        self.total_task.append(self)
        return len(self.total_task)

    def mark_finished(self):
        self.__completed = True
    
    def is_finished(self):
        return self.__completed

    def __str__(self):

        complete=""
        if self.__completed == True:
            complete = "FINISHED"
        else:
            complete = "NOT FINISHED"

        return f"{self.__id}: {self.__description} ({self.__time} hours), programmer {self.__name} {complete}"

    def __repr__(self):

        
        complete=""
        if self.__completed == True:
            complete = "FINISHED"
        else:
            complete = "NOT FINISHED"

        return f"{self.__id}: {self.__description} ({self.__time} hours), programmer {self.__name} {complete}"
        
class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description, name, time):
        self.__orders.append(Task(description , name, time))

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return list(set([item.programmer for item in self.__orders]))

    def mark_finished(self, id):
        for item in self.__orders:
            if id == item.id:
                item.mark_finished()
                return
        raise ValueError
            

    def finished_orders(self):
        return [item for item in self.__orders if item.is_completed==True]

    def unfinished_orders(self):
        return [item for item in self.__orders if item.is_completed==False]

    def status_of_programmer(self, name):
        fc=0
        fs=0
        tc=0
        ts=0
        for item in self.__orders:
            if item.programmer == name:
                if item.is_completed == True:
                    tc+=1
                    ts+=item.workload
                else:
                    fc+=1
                    fs+=item.workload
        if (fc==0 and fs==0) and (tc==0 and ts==0):
            raise ValueError
        return (tc,fc,ts,fs)        
    
    
if __name__=="__main__":
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.add_order("program mobile app", "Andy", 5)
    t.add_order("program something with pygame", "Andy", 50)
    t.add_order("code better facebook", "Jonas", 5000)
    t.mark_finished(1)
    t.mark_finished(2)
    print(t.status_of_programmer("Andy"))
    #t.mark_finished(2)
    #t.all_orders()
 #   t1 = Task("program hello world", "Eric", 3)
 #   print(t1.id, t1.description, t1.programmer, t1.workload)
 #   print(t1)
 #   print(t1.is_finished())
 #   t1.mark_finished()
 #   print(t1)
 #   print(t1.is_finished())
 #   t2 = Task("program webstore", "Adele", 10)
 #   t3 = Task("program mobile app for workload accounting", "Eric", 25)
 #   print(t2)
 #   print(t3)

 #   orders = OrderBook()
 #   orders.add_order("program webstore", "Adele", 10)
 #   orders.add_order("program mobile app for workload accounting", "Eric", 25)
 #    orders.add_order("program app for practising mathematics", "Adele", 100)

 #   for order in orders.all_orders():
 #       print(order)

 #   print()

 #   for programmer in orders.programmers():
 #       print(programmer)

 #   orders.mark_finished(1)
 #   orders.mark_finished(2)

 #   for order in orders.all_orders():
 #       print(order)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)  
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.add_order("program mobile gane", "Eric", 5)
    t.mark_finished(99)

    