# Program: Interplanetary Weights Calculator
# Class: Early College Python
# Author: MS1

# CONSTANTS 
fMERCURY = 0.38
fVENUS = 0.91
fMOON = 0.165
fMARS = 0/38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066

# Input (Prompt for Name & Earth Weight)
sName = input("Enter your name, human: ")
fWeight = float(input(f"Enter your weight, disgusting {sName}: "))

# Calulations
fMercuryWt = fMERCURY * fWeight
fVenusWt = fVENUS * fWeight
fMoonWt = fMOON * fWeight
fMarsWt = fMARS * fWeight
fJupiterWt = fJUPITER * fWeight
fSaturnWt = fSATURN * fWeight
fUranusWt = fURANUS * fWeight
fNeptuneWt = fNEPTUNE * fWeight
fPlutoWt = fPLUTO * fWeight

# OUTPUT (Display results to screen)
print(f"Hmmm... interesting..\nAfter deep calculations, this is {sName}'s weight on all the planets: ")
print(f"{'Weight on Mercury:':25s} {fMercuryWt:15,.2f}")
print(f"{'Weight on Venus:':25s} {fVenusWt:15,.2f}")
print(f"{'Weight on the Moon:':25s} {fMoonWt:15,.2f}")
print(f"{'Weight on Mars:':25s} {fMarsWt:15,.2f}")
print(f"{'Weight on Jupiter:':25s} {fJupiterWt:15,.2f}")
print(f"{'Weight on Saturn:':25s} {fSaturnWt:15,.2f}")
print(f"{'Weight on Uranus:':25s} {fUranusWt:15,.2f}")
print(f"{'Weight on Neptune:':25s} {fNeptuneWt:15,.2f}")
print(f"{'Weight on Pluto:':25s} {fPlutoWt:15,.2f}")
