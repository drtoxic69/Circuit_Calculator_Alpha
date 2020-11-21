class calculator:    
    # The instruction 
    print('When you have to enter multiple values you have to enter with a space.')
    print('For example you have to enter 4 and 2 then you should enter like this: 4 2')

    # The values
    def __init__(self):
        self.connected = input('What is the circuit connected in? [S]eries or [P]arallel or [M]ixed: ')        
        self.ask_which_one = input('Which is not given? [C]urrent or [V]oltage: ')

        if self.ask_which_one.lower() == 'c':
            self.voltage = int(input('Enter the voltage of the battery: '))
            self.current = 'not given'

        elif self.ask_which_one.lower() == 'v':
            self.current = int(input('Enter the current flowing to the circuit: '))
            self.voltage = 'not given'
            
        else:
            exit('You had to type c or v!')

    
    # The number of resistors in a circuit of series and parallel
    def numOfResistors(self):
        if self.connected.lower() == 's' or self.connected.lower() == 'p':
            global num_resistor

            try:
                num_resistor = int(input('Enter the no. resistors in the circuit: '))
            except ValueError:
                exit('Invalid Input! You had to type a whole number!')
                
            if num_resistor == 1:
                calculator.numOfResistors.single_value = int(input('Enter the value of the resistor: '))
                return calculator.numOfResistors.single_value

            elif num_resistor > 1: 
                calculator.numOfResistors.multiple_value = list(map(int, input('Enter the values of the resistors: ').split()))
                return calculator.numOfResistors.multiple_value

            elif num_resistor == 0:
                exit('To run this command you need atleast one resistor: ')

            
    # The calculation for a series circuit
    # The outputs of the series calculation
    def seriesCalculation(self):
        if self.connected.lower() == 's':

            print('_____________________________________________________________________________________')
            print('')
            
            if self.ask_which_one.lower() == 'c':

                if num_resistor == 1:
                    print(f'The R(eq) of the circuit: {calculator.numOfResistors.single_value} ohms')

                elif num_resistor > 1:
                    print(f'The R(eq) of the circuit: {sum(calculator.numOfResistors.multiple_value)} ohms')

                if self.current.lower() == 'not given':
                    if num_resistor == 1:
                        self.current = self.voltage/calculator.numOfResistors.single_value
                        print(f'The I(ckt): {self.current} A')

                    elif num_resistor > 1:
                        self.current = self.voltage/sum(calculator.numOfResistors.multiple_value)
                        print(f'The I(ckt): {self.current} A')
                    print(f'I(ckt) = I(r1) = I(r2) = ... = {self.current} A')

                    if num_resistor == 1:
                        print(f'The voltage of the resistor: {calculator.numOfResistors.single_value*self.current} V')

                    elif num_resistor > 1:
                        for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'The voltage of the resistor: {value_resistor*self.current} V')

            elif self.ask_which_one.lower() == 'v':
                
                if num_resistor == 1:
                    print(f'R(eq) of the circuit: {calculator.numOfResistors.single_value}')

                elif num_resistor > 1:
                    print(f'R(eq) of the circuit: {sum(calculator.numOfResistors.multiple_value)}')

                
        
    # The calculations for a parallel circuit
    # The outputs of the parallel circuit
    def parallelCalculation(self):
        if self.connected.lower() == 'p':
            if num_resistor == 1:
                exit('Invalid input! if there is one resistor in a circuit then it is a series circuit!')
            
            elif num_resistor > 1:
                global Req
                Req = 0
                for req in calculator.numOfResistors.multiple_value:
                    Req += 1/req
                print(f'The R(eq): {1/Req}')

            # The calculation of current and voltage in parallel
            if self.ask_which_one.lower() == 'c':
                if self.current.lower() == 'not given':
                    self.current = self.voltage/(1/Req)
                    print(f'The I(ckt): {self.current}')
                    print(f'V(b) = V(1) = V(2) = ... = {self.voltage}')

                    for current_resistor in calculator.numOfResistors.multiple_value:
                            print(f'The current of the resistor: {self.voltage/current_resistor} A')

                
    # Step by step 
    def stepByStep(self):
        step_by_step = input('Do you want the answer step by step? (Y/N) ')
        if self.connected.lower() == 's':
            if self.ask_which_one.lower() == 'c':
                if step_by_step.lower() == 'y':
                    if num_resistor > 1:
                        print(f'''
====================================================================================
[*note: please draw the circuit yourself]
R(eq) = R(1) + R(2) + ... + R(n)
      = {sum(calculator.numOfResistors.multiple_value)} ohms
        
I(ckt) = V(b)/R(eq) [By Ohm's law]
       = {self.current} A

I(ckt) = I(r1) = I(r2) = ... = I(n) = {self.current} A [current is same to all devices when connected in series]
''')

                        for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'''
V = IR [By Ohm's law]
  = {self.current} x {value_resistor}
  = {value_resistor*self.current} V
                        ''') 

                    elif num_resistor == 1:
                        print(f'''
====================================================================================
[draw the circuit yourself]
R(eq) = R1 + R2 + ... + Rn
      = {calculator.numOfResistors.single_value} ohms

I(ckt) = V(b)/R(eq) [By Ohm's law]
       = {self.current} A
I(ckt) = I(r1) = I(r2) = ... =I(n) = {self.current} A

V = IR [By Ohm's law]
  = {self.current} x {calculator.numOfResistors.single_value}
  = {self.current*calculator.numOfResistors.single_value} V
                    ''')
            
                else:
                    print('Ok then, have a nice day!')

        # Parallel step-by-step
        elif self.connected.lower() == 'p':
            if step_by_step.lower() == 'y':
                print(f'''
====================================================================================
[PLease draw the circuit yourself]
1/R(eq) = 1/R(1) + 1/R(2) + ... + 1/R(n)
        = {1/Req} ohms

I(ckt) = V/R(eq)
       = {self.current} A

V(b) = V(r1) = V(r2) = ... = {self.voltage} V
                ''')
                for value_resistor in calculator.numOfResistors.multiple_value:
                        print(f'''
I = V/R [By Ohm's law]
  = {self.voltage} / {value_resistor}
  = {self.voltage/value_resistor} A
                        ''')
            
            elif step_by_step.lower() == 'n':
                exit('Ok then, have a nice day!')

            else:
                exit('Invalid Input! you had to input y or n')
                


c = calculator()
c.numOfResistors()
c.seriesCalculation()
c.parallelCalculation()
c.stepByStep()