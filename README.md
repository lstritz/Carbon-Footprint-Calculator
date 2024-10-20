# Carbon-Footprint-Calculator
This simple carbon footprint calulator is an estimate of the users carbon footprint in a year based on their traveling frequency and destination. The user can only select one option.
Lea Stritzke (5785189)

# Here we define the main variables for the carbon footprint calculation
"""
    Args:
        main_transport (str) #User chooses the main transport. The function only works if we type the specifically listed variables: car, train plane. Input: string, 

        travel_days (str) #User chooses the average amount of travel days, where the average has to be estimated by the user himself. 

        distance (str) #User chooses the most frequent traveling destination to approximate the carbon footprint. The function only works if we type the specifically listed variables: Domestic (within their country), Europe, World. 
"""

# possible improvements in following versions:
    - add more means of transport and their corresponding 
    - limit amount of travel days to 365
    - for the destination cases, make them more exact -  approximate the average distances within every country
    - select different amount of travel days for each mean of transport
    
# average values for each mean of transport (kg of carbon per km) reference: Our World in Data
    car_co2 (int)
    train_co2 (int)
    plane_co2 (int)

# average values for distances in km
    Domestic_distance (int)
    Europe_distance (int)
    World_distance (int)

# possible improvements in following versions:
    - for the destination cases, make them more exact -  make a better approximation of the average CO2 consumption within every distance range (make the concumption dependant on the exact distance itself)

# function carbon
    def carbon(main_transport, travel_days, distance):
    """
    
    Args:
        main_transport (str)
        travel_days (str)
        distance (str)
    
    int(travel_days) #converts string to an integer in order to proceed proper multiplication. 
    
    all if, elif, else statements make it possible that the calculator uses only one selected option

    Returns: 
        carbon_final (flt) is the product of the main variables multiplied by their assigned average carbon consumption and average distance.
    """

# general improvements
    - add more variables not only depending transport like: recycling, groceries, clothing, energy usage 
    - make the user select given main variables and not type 
    - estimate of the carbon neutralization price for the produced amount of carbon in order so the user can neutralize their carbon consumption

