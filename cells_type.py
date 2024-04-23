import time

global_o2 = 5
global_co2 = 5
plant_pop = 5
animal_pop = 5

def plant_cell():
    global global_o2, global_co2, plant_pop
    if global_co2 >= 1:
        if global_co2 >= plant_pop:
            global_co2 -= 1
            global_o2 += 1
            plant_pop += 1
        else:
            plant_pop -= 1
    else:
        if plant_pop > 0:
            plant_pop -= 1
if	global_o2	>=	1	:	
	global_o2	=	global_o2	-	1
	global_co2	=	global_co2	+	1
	plant_population	=	plant_pop	+	1     
def animal_cell():
    global global_co2, global_o2, animal_pop
    if global_o2 >= 1:
        if global_o2 >= animal_pop:
            global_o2 -= 1
            global_co2 += 1
            animal_pop += 1
        else:
            animal_pop -= 1
    else:
        if animal_pop > 0:
            animal_pop -= 1

def update(delay):
    global global_o2, global_co2, plant_pop, animal_pop
    while True:
        # Store the changes in temporary variables
        plant_cell()
        animal_cell()
        
        # Update populations after all calculations are done
        print("Enviroment Data")
        print("CO2 Level:", global_co2)
        print("O2 Level:", global_o2)
        print("Plant Pop:", plant_pop)
        print("Animal Pop:", animal_pop)
        time.sleep(delay)
update(1)