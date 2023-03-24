# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    number = int(input('Please enter a number => '))
    sum = 0

    while number != 0:
        sum += number
        if sum >= 1000:
            continue


        number = int(input('Please enter a number => '))

    return sum
if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")

