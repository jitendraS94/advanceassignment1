import logging
logging.basicConfig(filename="Assignment1.log",level=logging.INFO,format=("%(levelname)s %(asctime)s %(name)s %(message)s"))

class Assignment1:
    logging.info(" Advance Assignment1 solution")

    def Hello_python(self):
        logging.info("we are in the print hello python funtion")
        try:
            a = int(input("Enter the number 1 if you want to print a Hello python :-"))
            while a == 1:
                b = "Hello Python"
                logging.info(b)
                return  b
            else:
                return "plese enter the right number"
            logging.info("Hello Python")
        except Exception as e:
            logging.exception(e)

class Arithmetical_op:
    logging.info("Arithmetical_op")
    def addition1(*args):
        logging.info("we are in the addition1 funtion")
        try:
            addition = 0
            for i in l:
                addition += i
            logging.info("addition of number %s",addition )
            """addition of number"""
            print("addition of number")
            return addition
        except Exception as e:
            logging.exception(e)

    def  devision(self):
        logging.info("This is a divition funtion")
        try:
            a= int(input("Enter the number :-"))
            b= int(input("Enter the number :-"))
            div = a/b
            logging.info("Devision of number %s ", div)
            return div
        except Exception  as e:
            logging.exception(e)

class Triangle:
    logging.info("Triangle")
    def area_of_tringle(self):
        logging.info("area_of_triangle")
        try:
            base = float(input("Enter the number :-"))
            height = float(input("Enter the number :-"))
            area = (base * height)/2
            logging.info("area_of_triangle is %s ",area)
            return area
        except Exception as e:
            logging.exception(e)

class Swap_variable:
    logging.info("Swap_variable")
    def SWAP_var(self):
        try:
            a = int(input("Enter the number :-"))
            b = int(input("Enter the number :-"))
            a ,b = b , a
            logging.info("swap variable is %s %s",a ,b)
            return a ,b
        except Exception as e:
            logging.exception(e)
import random
class Random:
    logging.info("Random number")
    def Random_num(self):
        try:
            n = int(input("input the enter number :-"))
            for i in range(n):
                a1 =int(input("input the random first  number :-"))
                a2 = int(input("input the random second number :-"))
                logging.info(random.randint(a1,a2))
                return random.randint(10,15)
        except Exception as e:
            logging.exception(e)

class All_class(Assignment1,Arithmetical_op,Triangle,Swap_variable,Random):
    pass

i = Assignment1
i.Hello_python
print(i.Hello_python(""))
j = Arithmetical_op
"""please enter the number which you want to add"""
l = [15,25,35,35]
print(j.addition1(l))
print(j.devision("div"))
k = Triangle
k.area_of_tringle
print(k.area_of_tringle("area"))
p = Swap_variable
p.SWAP_var
print(p.SWAP_var("SWAP_var"))
r = Random
r.Random_num
print(r.Random_num(""))
A = All_class
print(A.devision("div"))

