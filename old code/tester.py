class SeriesMixed:        
    def __init__(self, series_side, top_value, bottom_resistor): 
        self.series_side = series_side
        self.top_value = top_value
        self.bottom_resistor = bottom_resistor


    def top_side(self, series_side, top_value, req_top):
        if self.series_side.lower() == 't':            
            for req_top in self.top_value:
                req_top += req_top
    

    def reqParallel(self, req_top, bottom_resistor, Req_parallel1):
        return Req_parallel1 = (1/req_top) + (1/self.bottom_resistor)           
            

    def the_prints(self, series_prints):
        print(series_prints)


s1 = SeriesMixed(input('[T]op or [B]ottom or [Both]:'), list(map(int, input('Enter the value of the resistors on top: ').split())), int(input('Enter the value of the resistor on bottom: ')))
s1.top_side(self.series_side, self.top_value)
s1.the_prints(f'The req: {Req_parallel1}')