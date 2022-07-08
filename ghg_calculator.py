# ghg_calculator.py

def calculate_emissions(activity_data, emission_factor):
    """
    Calculate GHG emissions.

    :param activity_data: Amount of activity (e.g., kWh, liters, etc.)
    :param emission_factor: Emission factor (e.g., kg CO2 per kWh)
    :return: Total emissions
    """
    return activity_data * emission_factor

if __name__ == "__main__":
    activity_data = float(input("Enter the amount of activity (e.g., kWh): "))
    emission_factor = float(input("Enter the emission factor (e.g., kg CO2 per kWh): "))
    emissions = calculate_emissions(activity_data, emission_factor)
    print(f"Total GHG emissions: {emissions} kg CO2")
