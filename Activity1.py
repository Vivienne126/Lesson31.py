class A:
    def __init__(self, a):
        self.a=a
    def __lt__(self,other):
        if self.a<other.a:
            return("Object 1 is less than Object 2")
        else:
            return("Obj 2 is less than Obj1")    
    def __eq__(self, other):
        if self.a==other.a:
            print("Both are equal")
        else:
            print("Both are not equal")
obj1=A(2)
obj2=A(3)
print("Passed values are: " , obj1.a , obj2.a) 
print(obj1<obj2)

obj3=A(4)
obj4=A(4)
print("Passed values are: " , obj3.a , obj4.a) 
print(obj1==obj2)
     
