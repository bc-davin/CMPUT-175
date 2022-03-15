class CircularQueue:
# Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception('Capacity Error') 
        self.__items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0
    def enqueue(self, item):
        if self.__count== self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item) 
        else:
            self.__items[self.__tail]=item
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity    
    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item= self.__items[self__head]
        self.__items[self.__head]=None
        self.__count -=1
        self.__head=(self.__head+1) % self.__capacity
        return item
    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]
    def isEmpty(self):
        return self.__count == 0 
    def isFull(self):
        return self.__count == self.__capacity  
    def size(self):
        return self.__count     
    def capacity(self):
        return self.__capacity    
    def clear(self):
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0
    def __str__(self):
        str_exp = "]"
        i=self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[i]) + " "
            i=(i+1) % self.__capacity
        return str_exp + "]"    
    def __repr__(self):
        return (str(self.__items), str(self.__head), str(self.__tail), str(self.__count), str(self.__capacity))
    
    def test1(self):
        strExpression="["
        i=self.__tail-1% self.__capacity
        for j in range(self.__count):
            strExpression+=str(self.__items[i])+" "
            if i != self.__head:
                strExpression += ","
            i = (i-1) % self.__capacity
        strExpression+="["
        return strExpression        
        
def main():
    q=CircularQueue(4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    q=q.test1()
    print(q)

main()
    
    
        
