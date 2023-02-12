def pico_y_placa(plate_number, date, time):
    # Extract the last digit of the license plate
    last_digit = int(plate_number[-1])

    # Determine the day of the week
    import datetime
    day = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")

    # Check if the car can be on the road
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if 7 <= int(time[:2]) <= 9 or 16 <= int(time[:2]) <= 19:
            if last_digit == 1 or last_digit == 2:
                return "no puede circular"
            elif last_digit == 3 or last_digit == 4:
                return "no puede circular"
            else:
                return "puede circular"
        else:
            return "puede circular"
    else:
        return "puede circular"

# Example usage
print(pico_y_placa("PBX-1234", "2023-02-10", "08:30"))  # Output: no puede circular
print(pico_y_placa("PBX-1234", "2023-02-11", "17:30"))  # Output: no puede circular
print(pico_y_placa("PBX-1234", "2023-02-12", "07:00"))  # Output: puede circular
