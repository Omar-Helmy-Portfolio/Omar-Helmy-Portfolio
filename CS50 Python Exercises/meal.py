# Required To:
# Take Time From User in ##:## or #:##
# Convert Time Function To Float
# Determine Meal Type : (7->8, 12->13, 18->19)
# Return Nothing Outside Ranges.
#####################################
# Algorithm:
def main():
    # Take Input From User
    time = input("Time: ").strip()
    # Convert Time (minutes) To Hours (Float).
    hours = convert(time)
    # Find Meal Type.
    check_meal_type(hours)


def convert(time):
    hrs, mins = time.split(":")
    hrs = float(hrs)
    mins = float(mins)/60
    hours = hrs + mins
    return hours


def check_meal_type(hours):
    if 7 <= hours <= 8:
        print("breakfast time")
    if 12 <= hours <= 13:
        print("lunch time")
    if 18 <= hours <= 19:
        print("dinner time")
    else:
        pass


if __name__ == '__main__':
    main()
