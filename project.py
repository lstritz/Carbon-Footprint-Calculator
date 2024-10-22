def carbon_car(car_co2, travel_days, distance):
    carbon_car_days = car_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_car_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_car_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_car_days * World_distance
    else:
        print('Incorrect value for main transport or distance')
    return carbon_transport

def carbon_train(train_co2, travel_days, distance):
    carbon_train_days = train_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_train_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_train_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_train_days * World_distance
    else:  
        print('Incorrect value for main transport or distance')
    return carbon_transport

def carbon_plane(plane_co2, travel_days, distance):
    carbon_plane_days = plane_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_plane_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_plane_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_plane_days * World_distance
    else:
        print('Incorrect value for main transport or distance')
    return carbon_transport

def carbon(main_transport, travel_days, distance):
    if main_transport == 'car':
        amount = carbon_car(car_co2, travel_days, distance)
        return amount
    elif main_transport == 'train':
        return carbon_train(train_co2, travel_days, distance)
    elif main_transport == 'plane':
        return carbon_plane(plane_co2, travel_days, distance)  
    else:
        print('Incorrect value for main transport or distance')
        main_transport = input('Your options are: car, train, plane:')
        print('Main transport:', main_transport)
        travel_days = input('Your average amount of travel days per year:')
        print('The average amount of travel days per year:', travel_days)
        distance = input('Your options are: Domestic, Europe, World:')
        print('Distance travelled:', distance)
    return carbon_final        

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

# average values for distances in km
Domestic_distance = 100 
Europe_distance = 500
World_distance = 6000

carbon_final = carbon(main_transport, travel_days, distance)
print('Your average carbon footprint', carbon_final)