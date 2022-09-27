x = 0
y = 1
z = 0
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not( x or y or z ) == ((not x) and (not y) and (not z)):
                print(True)
            else:
                print(False)

