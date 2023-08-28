# Subtracts sourdough's hydration from dough
# Flour weight is in baker's percentage: 100% flour, 60% hydration = 100g flour, 60g water

def tryInput(prompt, default):
    try:
        return int(input(prompt))
    except:
        return default

# input
numDough = tryInput("Enter # of dough balls (def 3): ", 3)
flourWeight = tryInput("Enter flour weight of 1 dough ball (def 170g): ", 170)
doughHydration = tryInput("Enter Pizza Hydration % (def 60%): ", 60)
sdPercentage = tryInput("Enter Total Sourdough % (def 25%): ", 25)
sdHydration = tryInput("Enter Sourdough Hydration % (def 50%): ", 50) 

# total gram amts
totalFlour = flourWeight * numDough
totalWater = totalFlour * (doughHydration / 100)
totalSourD = totalFlour * (sdPercentage / 100)

# calculate sourdough's effect
sdWater = totalSourD * (sdHydration / 100)
sdFlour = totalSourD - sdWater
totalFlour -= sdFlour
totalWater -= sdWater

print('\n\nFlour:    {:.2f} g'.format(totalFlour))
print('Water:    {:.2f} g'.format(totalWater))
print('SourD:    {:.2f} g'.format(totalSourD))
print('\nFor {:.0f} dough balls'.format(numDough))
input('\n\nPress Enter to exit...')