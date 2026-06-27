"""
class flower:
    def __init__(self,name:str,petals:int,price:float):
        # constructor method to intialize instance variables
        self.name=name
        self.petals=petals
        self.price=price
    #setter methods
    def set_name(self,name:str):
        self.Name=Name
    def set_petals(self,petals:int):
        self.petals=petals
    def set_price(self,price : float):
        self. price=price
    #getter methods
    def get _name(self)->str:
        return self.name
    def get_ petals(self)->int:
        return self.petals
    def get _price (self)->float:
        return self.price
 #example usage 
if__name__ ==__ "main__":
   # create a flower instance 
   my _ flower = flower (name="rose,petals =32,price=(10.99)")
   # retrive and print values 
   print(f"flower name :{my - flower.get-name()}")
   print(f"number of petals :{ my -flower.get- petals()})"
   printf("price:)$ {my- flower .get -price():.2f}")
   # update values 
   # my- flower .set -name ("tulip")
   # my -flower.set -petals (24)
   # my- flower . set - price (8.49)
   # retrive and print  updated values 
   print(f "updated flower name :{ my -flower .get - name : { my -flower .get - name ()}")
   print ( f " updated number of petals : { my - flower . get - petals ()}")        print ( f" updated price : $ { my - flower .get-price () :. 2f }")
"""

"""from abc import ABC, abstract method class polygon (ABC):
    @abstract method
      def area (self->float:)
       """calculate the area of the polygon""'
     pass
    @abstract method
       def perimeter (self)-> float:
    """calculate the perimeter of the polygon"""
    pass
    class triangle(polygon):
    def__int__(self ,a:float, b:float,c:float):
         self .a =a
         self.b=b
         self.c=c
    def area (self) ->float:
# use herons formula for area calculation 
s=(self.a+self.b+self.c)\2
return(s*(s-self.a)*(s-self.b)*(s-self.c)** 0.5)
    def perimeter (self)->float:
return self .a+self.b+self.c
class quadrilaterals (polygon):
    def__int__(self,a:float,b:float,c:float,d:float):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def area (self)->float:
#simplified case:assumeits a rectangle (length*width)
   return self.a*self.b
    def perimeter (self)->float:
   return self.a+self.b+self.c+self.d
class pentagon (polygon):
    def__init__(self,side:float):
    self.side=side
     def area (self)->float:
     #area of a regular pentagon
        return(5*self.side **2)\(4*(5+2*(5**0.5))**0.5)
     def perimeter (self)->float:
   return 5*self.side 
     def main():
       while
         print("select the polygon type :")
         printprint("1.triangle")
         print ("2.quadrilateral ")
         print("3.pentagon")
         print ("4.exist")
choice =input (" enter your choice :")
if choice ='1':
   a= float (input("enter side a:"))
   b=float (input ("enter side b:"))
   c=float (input("enter side c:"))
triangle = triangle(a,b,c)
print(f"triangle area :{triangle.area():.2f}")
    elif chopice =='2':
    a=float(input ("enter side a:"))
    b=float(input("enter side b:"))
    c=float (input("enter side c:"))
    d=float (input ("enter side d:"))
quadrilateral =quadrilateral (a,b,c,d)
print(f"quadrilateral area:{quadrilateral.area():.2f}")
print(f"quadrilateral perimeter : {quad.perimeter():.2f}")
   elif choice =='3';
    side=float (input("enter side length:"))
"""