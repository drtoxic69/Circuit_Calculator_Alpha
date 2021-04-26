# parallel_sets = int(input('Enter the number of parallel sets: '))
# values = {}

# for sets in range(parallel_sets):
#    parallel_devision = int(input(f'Enter the number of devision in set_{sets+1}: '))
#    for devisions in range(parallel_devision):
#        sub_parallel_sets = int(input(f'How many parallel sets are their in devision_{devisions+1}: '))
#        if sub_parallel_sets == 0:
#            values[f'values_devision_{devisions+1}'] = list(map(float, input(f'Enter the value of the resistor(s) in devision {devisions+1}: ')))
#        elif sub_parallel_sets > 0:
#            values[f'values_devision_{devisions+1}'] = list(map(list, input('Enter the values in []: ').split()))
#        else:
#            print('dummy there cant be negative sets')





# print(values)
# output: {'values_devision_1': [['1'], ['[', '2', ','], ['[', '1', ',', '1', ']', ']']], 'values_devision_2': [2.0], 'values_devision_3': [['[', '2', ',', '2', ']'], ['1']], 'values_devision_4': [2.0]}

import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
R1 = d.add(elm.Resistor(label='1K$\Omega$'))
d.labelI(R1, '1 mA', top=False)
d.add(elm.Capacitor(d='down', botlabel='0.1$\mu$F'))
d.add(elm.Line( d='Left'))
d.add(elm.Ground)
d.add(elm.SourceV( d='up', label='10V') )
d.save('schematic.svg')
d.draw()


print('worked!')
