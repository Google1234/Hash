#author:JT
class Object:
    key=0
    value=0
    status='N'
    def __init__(self,key=0,value=0,status='N'):
        self.key=key
        self.value=value
        self.status=status

class hash:
    length=0
    filled=0
    almost_full=1
    slot=[]
    #length:数组初始化时设置的长度 默认为0
    #almost_full：字典至少有almost_full个空闲位置位置可用;almost_full>=1,避免find_slot出现死循环;空闲位置不大于almost_full时，对字典长度进行扩增
    def __init__(self,length=0,almost_full=1):
        for i in range(length+almost_full):
            element=Object()
            self.slot.append(element)
            self.length+=1
        self.almost_full=almost_full
    def hash_function(self,key):
        return key

    def find_slot(self,key):
        index=self.hash_function(key)%self.length
        while self.slot[index].status=='A'and self.slot[index].key!=key:
            index=(index+1)%self.length
        return index

    def lookup(self,key):
        index=self.find_slot(key)
        if self.slot[index].status=='A':
            return self.slot[index].value
        else :
            print('Not Matched!')
            return -1

    def set(self,key,value):
        index=self.find_slot(key)
        if self.slot[index].status=='A':
            self.slot[index].value=value
            return 0
        if self.length-self.filled==self.almost_full:
            #rebuild
            buff=[]
            for i in range(self.length):
                if self.slot[i].status=='A':
                    buff.append([self.slot[i].key,self.slot[i].value])
                    self.slot[i].status='N'
            self.filled=0
            element=Object()
            self.slot.append(element)
            self.length+=1
            for j in range(len(buff)):
                index=self.find_slot(buff[j][0])
                self.slot[index]=Object(buff[j][0],buff[j][1],'A')
                self.filled+=1
            index=self.find_slot(key)
        element=Object(key,value,'A')
        self.slot[index]=element
        self.filled+=1
    def  remove(self,key):
         i=self.find_slot(key)
         if self.slot[i].status!='A':
             return  -1  # key is not in the table
         j = i
         while True: #loop:
             self.slot[i].status='N' #mark slot[i] as unoccupied
             self.filled-=1
             while True: #r2: (note 2)
                 j=(j+1)%self.length
                 if self.slot[j].status!='A':
                     return -1 #loop
                 k= self.hash_function(self.slot[j].key) % self.length #modulo num_slots
                 #determine if k lies cyclically in ]i,j]
                 # |    i.k.j |
                 # |....j i.k.| or  |.k..j i...|
                 if ((i<=j)and((i<k)and (k<=j))) or ((i>j) and ((i<k)or (k<=j))):
                     continue #goto r2
                 element=Object(self.slot[j].key,self.slot[j].value,self.slot[j].status)
                 self.slot[i]=element
                 self.slot[j].status='N'
                 i=j
    def show(self):
        print('Key Value Status:')
        for j in range(self.length):
            print(self.slot[j].key,self.slot[j].value,self.slot[j].status)




