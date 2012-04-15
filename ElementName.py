# Accepts a name and attempts to make a name out of elements
import re

result = ''
cnt = 0
foundOne = True

elementList = { 'Ac':': ''Actinium',
'Ag': 'Silver',
'Al': 'Aluminum',
'Am': 'Americium',
'Ar': 'Argon',
'As': 'Arsenic',
'At': 'Astatine',
'Au': 'Gold',
'B': 'Boron',
'Ba': 'Barium',
'Be': 'Beryllium',
'Bh': 'Bohrium',
'Bi': 'Bismuth',
'Bk': 'Berkelium',
'Br': 'Bromine',
'C': 'Carbon',
'Ca': 'Calcium',
'Cd': 'Cadmium',
'Ce': 'Cerium',
'Cf': 'Californium',
'Cl': 'Chlorine',
'Cm': 'Curium',
'Co': 'Cobalt',
'Cn': 'Copernicium',
'Cr': 'Chromium',
'Cs': 'Cesium',
'Cu': 'Copper',
'Db': 'Dubnium',
'Ds': 'Darmstadtium',
'Dy': 'Dysprosium',
'Er': 'Erbium',
'Es': 'Einsteinium',
'Eu': 'Europium',
'F': 'Fluorine',
'Fe': 'Iron',
'Fm': 'Fermium',
'Fr': 'Francium',
'Ga': 'Gallium',
'Gd': 'Gadolinium',
'Ge': 'Germanium',
'H': 'Hydrogen',
'He': 'Helium',
'Hf': 'Hafnium',
'Hg': 'Mercury',
'Ho': 'Holmium',
'Hs': 'Hassium',
'I': 'Iodine',
'In': 'Indium',
'Ir': 'Iridium',
'K': 'Potassium',
'Kr': 'Krypton',
'La': 'Lanthanum',
'Li': 'Lithium',
'Lr': 'Lawrencium',
'Lu': 'Lutetium',
'Md': 'Mendelevium',
'Mg': 'Magnesium',
'Mn': 'Manganese',
'Mo': 'Molybdenum',
'Mt': 'Meitnerium',
'N': 'Nitrogen',
'Na': 'Sodium',
'Nb': 'Niobium',
'Nd': 'Neodymium',
'Ne': 'Neon',
'Ni': 'Nickel',
'No': 'Nobelium',
'Np': 'Neptunium',
'O': 'Oxygen',
'Os': 'Osmium',
'P': 'Phosphorus',
'Pa': 'Protactinium',
'Pb': 'Lead',
'Pd': 'Palladium',
'Pm': 'Promethium',
'Po': 'Polonium',
'Pr': 'Praseodymium',
'Pt': 'Platinum',
'Pu': 'Plutonium',
'Ra': 'Radium',
'Rb': 'Rubidium',
'Re': 'Rhenium',
'Rf': 'Rutherfordium',
'Rg': 'Roentgenium',
'Rh': 'Rhodium',
'Rn': 'Radon',
'Ru': 'Ruthenium',
'S': 'Sulfur',
'Sb': 'Antimony',
'Sc': 'Scandium',
'Se': 'Selenium',
'Sg': 'Seaborgium',
'Si': 'Silicon',
'Sm': 'Samarium',
'Sn': 'Tin',
'Sr': 'Strontium',
'Ta': 'Tantalum',
'Tb': 'Terbium',
'Tc': 'Technetium',
'Te': 'Tellurium',
'Th': 'Thorium',
'Ti': 'Titanium',
'Tl': 'Thallium',
'Tm': 'Thulium',
'U': 'Uranium',
'Uub': 'Ununbium',
'Uuh': 'Ununhexium',
'Uun': 'Ununnilium',
'Uuo': 'Ununoctium',
'Uup': 'Ununpentium',
'Uuq': 'Ununquadium',
'Uus': 'Ununseptium',
'Uut': 'Ununtrium',
'Uuu': 'Ununumium',
'V': 'Vanadium',
'W': 'Tungsten',
'Xe': 'Xenon',
'Y': 'Yttrium',
'Yb': 'Ytterbium',
'Zn': 'Zinc',
'Zr': 'Zirconium'}

def findElementName(tmpName):
    # End case
    if (len(tmpName) == 0):
        return "-"
    else:    
        
        # Try three chars
        result = getPossibleElement(tmpName[0:3])
        if (result):
            tmp = findElementName(tmpName[3:])
            if (tmp != None):
                tmpName = tmpName[3:]
                return [result, tmp]
            
        # Try two chars
        result = getPossibleElement(tmpName[0:2])
        if (result):
            tmp = findElementName(tmpName[2:])
            if (tmp != None):
                tmpName = tmpName[2:]
                return [result, tmp]
            
        # Try one char
        result = getPossibleElement(tmpName[0])
        if (result):
            tmp = findElementName(tmpName[1:])
            if (tmp != None):
                tmpName = tmpName[1:]
                return [result, tmp]
             
        foundOne = False
        return None

def getPossibleElement(strToCheck):
    strToCheck = strToCheck.capitalize()
    if (strToCheck in elementList): 
        return strToCheck
    else:
        return None
    
def iterFlatten(root):
    if isinstance(root, (list, tuple)):
        for element in root:
            for e in iterFlatten(element):
                yield e
    else:
        yield root

print "Enter name: "
origName = str(raw_input())
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
name = origName.translate(None, delchars)
elementName = []
tmpName = name.lower()

elementName = findElementName(tmpName)
elementName = list(iterFlatten(elementName))
if None in elementName:
    foundOne = False
else:
    foundOne = True

#print "final steps.." 
fullAbbrevName = ''
fullElName = ''
firstTime = True
print origName
# print elementName

if (foundOne):
    
    
    for el in elementName:
        if (el == '-'):
            break
        if (firstTime):
            fullAbbrevName = el
            fullElName = elementList[el]
            firstTime = False
        else: 
            fullAbbrevName = fullAbbrevName + " - " + el
            fullElName = fullElName + " - " + elementList[el]
    print fullAbbrevName
    print fullElName
    
else:
    print "Could not create name out of elements."
    
