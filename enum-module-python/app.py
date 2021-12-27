from enum import Enum

class ManchesterUnited(Enum):
    FW = "CRISTIANO RONALDO",
    MF = "PAUL POGBA",
    DF = "LUKE SHAW",
    GK = "DAVID DE GEA",
    NICKNAME = "THE RED DEVILS",
    GROUND = "OLD TRAFFORD",
    FOUNDED = 1878
 
# Access Enum Constant and get its Value
print(ManchesterUnited.FOUNDED)

# Information about the enum Member - get its details
print(repr(ManchesterUnited.FOUNDED))


    
    