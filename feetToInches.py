def main():
    feetInput = int(input("How many feet?: "))
    feetValueInInches = 12
    totalInches = feet_to_inches(feetInput,feetValueInInches)
    print(f'There are {totalInches} inches in {feetInput} feet.')

def feet_to_inches(num1, num2):
    result = num1*num2
    return result



main()