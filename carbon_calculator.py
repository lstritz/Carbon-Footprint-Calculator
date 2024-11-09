def carbon_car(car_co2, travel_days, distance):
    """Calculates the Carbon footprint for a car user

    Args:
        car_co2 (int): Average car co2 from Our World in Data
        travel_days (str): User input, average amount of travel days per year
        distance (str): User input, Chooses distance travelled 

    Returns:
        carbon_transport(flt): Average carbon footprint for a car user
    """
    carbon_car_days = car_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_car_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_car_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_car_days * World_distance
    return carbon_transport

def carbon_train(train_co2, travel_days, distance):
    """Calculates the Carbon footprint for a train user
    
    Args:
        train_co2 (int): Average train co2 from Our World in Data
        travel_days (str): User input, average amount of travel days per year
        distance (str): User input, Chooses distance travelled

    Returns:
        carbon_transport(flt): Average carbon footprint for a train user
    """
    carbon_train_days = train_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_train_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_train_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_train_days * World_distance
    return carbon_transport

def carbon_plane(plane_co2, travel_days, distance):
    """Calculates the Carbon footprint for a plane user

    Args:
        plane_co2 (int): Average plane co2 from Our World in Data
        travel_days (str): User input, average amount of travel days per year
        distance (str): User input, Chooses distance travelled

    Returns:
        carbon_transport(flt): Average carbon footprint for a plane user
    """
    carbon_plane_days = plane_co2 * int(travel_days)
    if distance == 'Domestic':
        carbon_transport = carbon_plane_days * Domestic_distance
    elif distance == 'Europe':
        carbon_transport = carbon_plane_days * Europe_distance
    elif distance == 'World':
        carbon_transport = carbon_plane_days * World_distance
    return carbon_transport

def carbon(main_transport, travel_days, distance):
    """Calculates the Carbon footprint after diffeenciating between the main transport: car, train, plane

    Args:
        main_transport (str): User input: car, train or plane
        travel_days (str): User input between 0 and 365
        distance (str): User input: Domestic, Europe, World

    Returns:
        carbon_transport(flt): The average carbon footprint per year for one of the transport options
    """
    if main_transport == 'car':
        return carbon_car(car_co2, travel_days, distance)
    elif main_transport == 'train':
        return carbon_train(train_co2, travel_days, distance)
    elif main_transport == 'plane':
        return carbon_plane(plane_co2, travel_days, distance)  
    else:
        print('Incorrect value for main transport, travel days or distance. Try again')
        main_transport = input('Your options are: car, train, plane:')
        print('Main transport:', main_transport)
        travel_days = input('Your average amount of travel days per year:')
        print('The average amount of travel days per year:', travel_days)
        distance = input('Your options are: Domestic, Europe, World:')
        print('Distance travelled:', distance)
    return carbon_final        

print('This is a simple carbon footprint calculator. Please insert the following values')

main_transport = input('Your options are: car, train, plane:')
print('Main transport:', main_transport)

travel_days = input('Your average amount of travel days per year:')
while int(travel_days) <0 or int(travel_days)>366:
    print('Your chosen amount of travel days per year is invalid. Please try again')
    travel_days = input('Your average amount of travel days per year:')       
if int(travel_days)>=0 and int(travel_days)<=365:
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
print('Your average carbon footprint', carbon_final, 'kg of CO2 per year')


# test functions

def test_carbon_car():
    day = 2
    distance = 'World'
    assert carbon_car(car_co2,day,distance) == 2 * car_co2 * World_distance
    
    day = -1
    distance = 'Europe'
    assert carbon_car(car_co2,day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 400
    distance = 'Domestic'
    assert carbon_car(car_co2, day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 4
    distance = 'Domestic'
    assert carbon_car(car_co2, day, distance) == 4 * car_co2 * Domestic_distance
    
    day = 7
    distance = 'Europe'
    assert carbon_car(car_co2, day, distance) == 7 * car_co2 * Europe_distance
    
def test_carbon_train():
    day = 80
    distance = 'World'
    assert carbon_train(train_co2, day, distance) == 80 * train_co2 * World_distance
    
    day = -6
    distance = 'Europe'
    assert carbon_train(train_co2, day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 399
    distance = 'Domestic'
    assert carbon_train(train_co2, day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 10
    distance = 'Domestic'
    assert carbon_train(train_co2, day, distance) == 10 * train_co2 * Domestic_distance
    
    day = 23
    distance = 'Europe'
    assert carbon_train(train_co2, day, distance) == 23 * train_co2 * Europe_distance
    
def test_carbon_plane():
    day = 100
    distance = 'World'
    assert carbon_plane(plane_co2, day, distance) == 100 * plane_co2 * World_distance
    
    day = -70
    distance = 'Europe'
    assert carbon_plane(plane_co2, day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 367
    distance = 'Domestic'
    assert carbon_plane(plane_co2, day, distance) != 'Your chosen amount of travel days per year is invalid. Please try again'
    
    day = 15
    distance = 'Domestic'
    assert carbon_plane(plane_co2, day, distance) == 15 * plane_co2 * Domestic_distance
    
    day = 26
    distance = 'Europe'
    assert carbon_plane(plane_co2, day, distance) == 26 * plane_co2 * Europe_distance
    
def test_carbon(): 
    transport = 'plane'
    days = 2
    distance = 'World'
    assert carbon(transport, days, distance) == carbon_final and carbon_final == 2880