connected = input("what is the circuit connected in? [S]eries or [P]arallel or [M]ixed: ")

#The values
print("If you want to find the value or dont know the value then type 'not given'")
i = input("Enter the current flowing to the circiut: ")
v = int(input ("Enter the Voltage of the battery : "))

#The number of the resistors in the circuit
if connected.lower() == 's' or connected.lower() == 'p':
    print('Enter multiple value(for ex. > 4 2 ) like this with space.')
    value = list((map(int,input("Enter the VALUES of the resistor: ").split())))
    print('_____________________________________________________________________________________')
    print('')

#The calculation of, when connected in series 
if connected.lower() == 's':
    Req = 0
    for req in value:
        Req+=req
    print (f'The Req of the circuit: {Req}')
    
    if i.lower() == 'not given':
        i=v/Req
        print (f'The I(ckt): {i} A')
    print (f"I(ckt) = I(r1) = I(r2) = ... = {i} A")

    for resistor_value in value:
        print(f'The voltage of the resistor: {resistor_value*i} V')
    
    step_by_step = input("Do you want the answer step by step.(Y/N) ")
    if step_by_step.lower() == 'y':
        print(f'''
 ====================================================================================  
 [draw the circuit yourself]                              
 R(eq) = R1+R2=...= Rn                                    
       = {Req}                                            
         ===                                                 
  By Ohm's Law                                              
  I(ckt) = V/R(eq)                                        
         = {i}                                            
           ===                                            
  I(ckt) = I(r1) = I(r2) = ... = I(n) = {i}               
                                                                                             
 V of each resistors refer above, and this is the format: 
 V(n) = IR                                                 
      = {i} x r                                           
      = *the above answer.                                
====================================================================================       
          ''')
    else:
        print('Ok then, have a nice day!')

#The calculation when, it is connected in Parallel 
elif connected.lower() == 'p':
    Req2 = 0
    for req2 in value:
        Req2 += 1/req2
    print (f'The R(eq) of the circuit: {Req2}')

    if i.lower() == 'not given':
        i = v/(1/Req2)
        print (f'The I(ckt): {i}')
    print (f'V(b) = V(1) = V(2) = ... = {v}')
    
    for current in (value):
        print(f'The current(I) of the resistor: {v/current} A')

    step_by_step2 = input("Do you want the answer step by step? (Y/N) ")
    if step_by_step2.lower() == 'y':
        print(f'''                                                                                                  
 ====================================================================================        
 [draw the circuit yourself]                              
 1/R(eq) = 1/R1+1/R2=...+ 1/Rn                            
        = {Req2}                                          
           ===                                               
  By Ohm's Law                                              
  I(ckt) = V/R(eq)                                        
         = {i}                                            
           ===                                            
  V(b) = V(r1) = V(r2) = ... = V(n) = {v}                 
                                                                                            
 I of each resistors refer above, and this is the format: 
 I(n) = V/R                                                
      = {v} x r                                           
      = *the above answer.                                                                                      
====================================================================================  
        ''')
    else:
        print("Ok then, have a nice day!")

#The calculation, when conneted in mixed
#The inputs
elif connected.lower() == 'm':
    ask_user = input('What do you want to solve first? [P]arallel or [S]eries? ')
    
    if ask_user.lower() == 'p':
        
        #The Parallel set
        parallel_count = int(input("Enter the number of parallel set of resistors in your circuit: "))
        value_parallel = list()
        for value_parallel_count in range(parallel_count):
            value_parallel.append(value_parallel_count)

        #The series asking 
        series_resistors_count = input('Is there series resistor in either side([Y]es/[N]o): ')
        if series_resistors_count.lower() == 'y':
            class SeriesMixed:
                def __init__(self):
                    self.series_side = input('[T]op or [B]ottom or [Both]:')
                    
                    if self.series_side.lower() == 't':
                        self.top_value = list(map(int, input('Enter the values of the resistors on top: ').split()))
                        self.bottom_resistor = int(input('Enter the value of the resistor on bottom: '))
                        
                    elif self.series_side.lower() == 'b':
                        self.bottom_value = list(map(int, input('Enter the values of the resistors on bottom: ').split()))
                        self.top_resistor = int(input('Enter the value of the resistor on top: '))

                    elif self.series_side.lower() == 'both':
                        self.both_top_value = list(map(int, input('Enter the values of the resistors on top: ').split()))
                        self.both_bottom_value = list(map(int, input('Enter the values of the resistors on bottom: ').split()))

                    else:
                        print('Invalid input. You had to type "t" or "b" or "both".')
                        exit()
                    
                
                # The calculations for the req in top 
                def reqParallel(self):
                    
                    if self.series_side.lower() == 't':
                        req_topFinal = sum(self.top_value)
                        Req_parallel1 = (1/req_topFinal) + (1/self.bottom_resistor)  
                        return f'The Req of the circuit: {1/Req_parallel1} ohms'

                    elif self.series_side.lower() == 'b':
                        req_bottomFinal = sum(self.bottom_value)
                        Req_parallel2 = (1/req_bottomFinal) + (1/self.top_resistor)
                        return f'The Req of the circuit: {1/Req_parallel2} ohms'
                    
                    elif self.series_side.lower() == 'both':
                        both_req_top = sum(self.both_top_value)
                        both_req_bottom = sum(self.both_bottom_value)
                        
                        Req_parallel3 = (1/both_req_top) + (1/both_req_bottom)
                        return f'The Req of the circuit: {1/Req_parallel3} ohms'
                        
                
            s1 = SeriesMixed()
            print(s1.reqParallel())
    
        else:
            print("you had to type 'y'/'n'")

    #series set calculation 
    elif ask_user.lower() == 's':
         #The series set 
        series_set_count = int(input('Enter the number of series set of resistors in your circuit: '))
        value_series = list()
        for value_series_count in range(series_set_count):
            value_series.append(value_series_count)
                
        #The value of series resistors
        for resistors_in_series in value_series:
            value_of_series_res = list(map(int,input('Enter the value of the series resistors(Enter multiple value): ').split()))
        print('_____________________________________________________________________________________')
        print('')
    else:
        print('you had to type p or s!')    

    #The prints, when connected in parallel
    #The Req of the resistors connected in parallel
    print(f'The Req of the circuit: {1/Req_both}')

    #The Req of the resistors connected in series
    Req4 = 0
    for req4 in value_of_series_res:
        Req4 += req4
    print (f'The Req of the resistors connected in series: {Req4}')

    #The final Req
    Req_main = (1/Req_both)+Req4
    print(f"The Req if the circuit: {Req_main}")

    #The I(ckt) and I of all the resistors
    if i.lower() == 'not given':
        i=v/Req_main
        print(f'he I(ckt): {i}')
    
    #The voltage of the resistors 
    print(f'V(b) = V(1) = V(2) = ... = {v}')

    #The current of the resistors 
    print("haha")
else:
    print('in (what is the circuit connected in? [S]eries or [P]arallel or [M]ixed:) you had to enter s or p or m, not anything else.')