class bookmymovie:
    
           


    def options(self):  
            print("1=Show the seats")
            print("2=Buy a ticket")
            print("3=Statistics")
            print("4=Show booked tickets User info")
            print("5=Exit")
            self.option=int(input())
            
            
            if self.option== 1:
                self.show_seats()
            elif self.option == 2:
                self.buy_ticket()
            elif self.option == 3:
                self.stats()
            elif self.option == 4:
                self.info()
            elif self.option == 5:
                self.exit()
            else:
                print("\nNot Valid Choice Try again")


    def __init__(self):
        print("Enter the row number")
        self.row = int(input())
        print("Enter the column number ")
        self.col = int(input())
        self.no_of_seats = self.row * self.col             
        self.matrix = []                                    
        self.seat_count = 0                                 
        self.current_income = 0                            
        self.total_income = 0                               
        self.u_details = {}                                 

        for i in range(self.row):                         
            a = []
            for j in range(self.col):
                a.append("S")
            self.matrix.append(a)
        print(end=" ")

    def show_seats(self):           
        print("Cinema ->")
        a = 0
        b = 0
        print(end="  ")
        for j in range(1, self.col + 1):        
            b = b + 1
            print(b, end=" ")
        print()
        for i in self.matrix:
            a = a + 1
            print(a, end=" ")
            print(" ".join(i), sep=",")
            self.options()


    def buy_ticket(self):  
        price_per_seat=150
        print("Enter the row Number")
        a=int(input())
        print("Enter the column Number")
        b=int(input())
        if self.matrix[a-1][b-1] == "B":                       
            print("This seat is already booked")
            self.options()
        else:   
                print('price per seat is 500')
                print('enter the number of seats')
                seats=int(input())
                print('total amount to be paid',price_per_seat*seats,'press Y to continue')
                
                self.pr=input()

        if self.pr == 'Y' or self.pr == 'y':                
            u_dict = {}
            name = input("For Booking, Enter your name\n")
            gender = input("Enter your gender\n")
            Age = input("Enter your age\n")
            mobile_number = input("Enter your Contact Number\n")
            self.row1 = a - 1
            self.col1 = b - 1
            self.matrix[self.row1][self.col1] = "B"            
            self.seat_count = self.seat_count + 1               
                     
            
            u_dict[(self.row1+1), (self.col1+1)] = list((name, gender, Age, mobile_number, ))
            self.u_details.update(u_dict)
            print("yoUr ticket has been booked")   
            self.options()
        else:
            print("Booking couldn't be processed")  


 

    def stats(self):                   
        print("Number of purchased tickets : ", self.seat_count)
        print("Current Income : $", self.current_income)
       
        self.options()


    def info(self):   
        print('enter your ticket row')
        self.check_a=int(input())
        print('enter the ticket column')
        self.check_b=int(input())
        if self.matrix[self.check_a-1][self.check_b-1] == 'B':
            details=self.u_details[(self.check_a, self.check_b)]
            print("name=",details[0])
            print("age",details[1])
            print('gender',details[2])
            print('mobile Number',details[3])
            self.options()
        
        else:                      
            print("This seat has not booked yet")
            self.options()


    def exit(self):                   
        return None


movie = bookmymovie()
movie.options()