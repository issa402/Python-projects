import sys

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Please provide two command-line arguments: temperature and velocity")
        return

    # Parse the command-line arguments as floats
    try:
        temperature = float(sys.argv[1])
        velocity = float(sys.argv[2])
    except ValueError:
        print("Invalid input! Please provide numeric values for temperature and velocity.")
        return

    # Check if the temperature and velocity are within the valid range
    if abs(temperature) > 50 or velocity > 120 or velocity < 3:
        print("Invalid input! Temperature should be within -50 to 50 degrees Fahrenheit, "
              "velocity should be between 3 and 120 miles per hour.")
        return

    # Compute the wind chill using the given formula
    wind_chill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * pow(velocity, 0.16)

    # Print the wind chill
    print("Wind Chill:", wind_chill)

if __name__ == "__main__":
    main()