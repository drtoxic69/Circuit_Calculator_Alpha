from numpy import reciprocal

def resistor_values(**resistorValues):
    seriesValues = sum(resistorValues['seriesValues'])
    parallelValues = 0
    for req in resistorValues['parallelValues']:
        parallelValues += 1/req 
    return seriesValues, 1/parallelValues
    
print(resistor_values(seriesValues=[10,20,30,40], parallelValues=[10,20,30,40]))