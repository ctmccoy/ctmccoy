from Miles import convertToMiles
from Kilometers import convertToKilometers

def main():
    # Initialize flag variables
    processing = True
    validValue = True
    
    while processing:
        # Reset validValue at the start of each loop iteration
        validValue = True
  
        try:
            # Accept a distance value from the user
            distance = float(input("Please enter a distance value: "))
            
            #blank print statement for a space between prompts
            print()
            
        except ValueError:
            #blank print statement for a space between prompts
            print()

            print("Invalid input. Please enter a numeric value for the distance.")
            validValue = False
            
            #blank print statement for a space between prompts
            print()
            
        if validValue:
            # Accept the unit of length from the user
            unit = input("What is the unit of length (M = miles, KM = kilometers): ").strip().upper()
            
            #blank print statement for a space between prompts
            print()

            # Decision structure to check the unit and perform the appropriate conversion
            if unit == "M":
                converted_distance = convertToKilometers(distance)
                print(f"Your distance of {distance} miles is equivalent to {converted_distance:.2f} kilometers.")
                
                #blank print statement for a space between prompts
                print()
                
            elif unit == "KM":
                converted_distance = convertToMiles(distance)
                print(f"Your distance of {distance} kilometers is equivalent to {converted_distance:.2f} miles.")
                
                #blank print statement for a space between prompts
                print()
                
            else:
                print("You entered an invalid unit of length.")
                validValue = False
                
                #blank print statement for a space between prompts
                print()
        
        # Ask the user if they want to continue
        if validValue:
            continue_processing = input("Press X to quit or Enter to continue processing: ").strip().upper()
            
            #blank print statement for a space between prompts
            print()

            if continue_processing == "X":
                processing = False
                print("End processing of distances.")

if __name__ == "__main__":
    main()

#blank print statement for a space between prompts
print()

