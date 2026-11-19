'''7. Student Result Generator (Method Overloading Concept) 
A school system calculates student results differently depending on
available data. 
Create a Result class where a method can calculate
the result using either two 
subjects or three subjects. 
'''

class Result():
    def calculate(self,m1,m2,m3=None):
        if m3 is None:
            total=m1+m2
            average=total/2
        else:
            total=m1+m2+m3
            average=total/3
        print("Total Marks:",total)
        print("Average marks:",average)
obj=Result()
print("Two subjects:")
obj.calculate(80,90)
print("\nThree subjects:")
obj.calculate(80,90,85)
