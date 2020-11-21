# This file is for import testing 
# nah, nvm i will do my testing here cause i don't wanna delete the test.py file

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