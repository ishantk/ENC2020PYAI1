maharashtra = 136980
tamil_nadu = 4210
delhi = 19567
gujrat = 24212
uttar_pradesh = 45661

# Problem: State with max cases :)
# in case i start writing if/else i may end up in putting so many use cases
# any fo rn-number of states, this program may grow complex

# Problem: Add up the cases and evaluate total

total_cases = maharashtra + tamil_nadu + delhi + gujrat + uttar_pradesh
print(total_cases)

# Multi Value Container: Indexed => List
states = [136980, 4210, 19567, 24212, 45661]                            # so on and so forth we can have more data in List :)

total_cases = states[0] + states[1] + states[2] + states[3] + states[4] # +....... for n-number of states
print(total_cases)

# Loops or Iterations comes into picture when we have indexed data to be processed

i = 0
total_cases = 0
while i < 5:
    total_cases += states[i]
    i+=1

print(total_cases)

# In python we don't have do-while loop :)

total_cases = 0
for i in range(0, 5):
    total_cases += states[i]

print(total_cases)