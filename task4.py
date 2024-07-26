# FUNCTION DEFINITION
def LYV(YEAR): #LEAP YEAR VERIFICATION FUNCTION 
    if YEAR % 4 == 0:
        if YEAR % 100 == 0:
            if YEAR % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# MAIN CODE
YEAR = int(input("ENTER YEAR TO VERIFY WHETHER IT'S A LEAP YEAR OR NOT... : "))
ANS = LYV(YEAR)

# OUTPUT/RESULT
print("\nQ: ", YEAR, " IS A LEAP YEAR?")
if ANS == True:
    print(YEAR," is a multiple of 4 hence it's a leap ")
else:
    print(YEAR," is not a multiple of 4 hence it's not a leap ")


