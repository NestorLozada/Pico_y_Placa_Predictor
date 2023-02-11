def pico_y_placa(plate_number, date, time):
    # Extract the last digit of the license plate
    last_digit = int(plate_number[-1])

    # Determine the day of the week
    import datetime
    day = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")

    # Check if the car can be on the road
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if 7 <= int(time[:2]) <= 9:
            return last_digit in [1, 2]
        elif 16 <= int(time[:2]) <= 19:
            return last_digit in [3, 4]
        else:
            return True
    else:
        return True

# Example usage
print(pico_y_placa("PBX-1234", "2023-02-10", "08:30"))  # Output: False
print(pico_y_placa("PBX-1234", "2023-02-11", "17:30"))  # Output: False
print(pico_y_placa("PBX-1234", "2023-02-12", "07:00"))  # Output: True
