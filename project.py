main_transport = input('Your options are: car, train, plane:')
print('Main transport:', main_transport)
travel_days = input('Your average amount of travel days per year:')
print('The average amount of travel days per year:', travel_days)
distance = input('Your options are: Domestic, Europe, World:')
print('Distance travelled:', distance)

# average values for each mean of transport (kg of carbon per km) reference: Our World in Data
car_co2 = 0.17 
train_co2 = 0.04 
plane_co2 = 0.24 

#average values for distances in km
Domestic_distance = 100 
Europe_distance = 500
World_distance = 6000

def carbon(main_transport, travel_days, distance):
    if main_transport == 'car':
        carbon_car = car_co2 * int(travel_days)
        if distance == 'Domestic':
            carbon_final = carbon_car * Domestic_distance
        elif distance == 'Europe':
            carbon_final = carbon_car * Europe_distance
        elif distance == 'World':
            carbon_final = carbon_car * World_distance
        else:
            print('Incorrect value for main transport or distance')
    elif main_transport == 'train':
        carbon_train = train_co2 * int(travel_days)
        if distance == 'Domestic':
            carbon_final = carbon_train * Domestic_distance
        elif distance == 'Europe':
            carbon_final = carbon_train * Europe_distance
        elif distance == 'World':
            carbon_final = carbon_train * World_distance
        else:  
            print('Incorrect value for main transport or distance')
    elif main_transport == 'plane':
        carbon_plane = plane_co2 * int(travel_days)
        if distance == 'Domestic':
            carbon_final = carbon_plane * Domestic_distance
        elif distance == 'Europe':
            carbon_final = carbon_plane * Europe_distance
        elif distance == 'World':
            carbon_final = carbon_plane * World_distance
        else:
            print('Incorrect value for main transport or distance')  
    return carbon_final        

carbon_final = carbon(main_transport, travel_days, distance)
print('Your average carbon footprint', carbon_final)
