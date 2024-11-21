from utils import implies

from implementation import (
    # Inputs
    iR00, iR10, iR20,
    iR01, iR11, iR21,
    iR02, iR12, iR22,

    iB00, iB10, iB20,
    iB01, iB11, iB21,
    iB02, iB12, iB22,

    # Outputs
    R00, R10, R20,
    R01, R11, R21, 
    R02, R12, R22,

    B00, B10, B20,
    B01, B11, B21,
    B02, B12, B22,

    G00, G10, G20,
    G01, G11, G21,
    G02, G12, G22
)


# Verify that if there is a winning configuration (all red or all blue) in a row, column, or diagonal,
# then all the green lights in that row, column, or diagonal must be lit.

# Red win conditions
assert implies(iR00 & iR10 & iR20, G00 & G10 & G20) # First row
assert implies(iR01 & iR11 & iR21, G01 & G11 & G21) # Second row
assert implies(iR02 & iR12 & iR22, G02 & G12 & G22) # Third row

assert implies(iR00 & iR11 & iR22, G00 & G11 & G22) # Main diagonal
assert implies(iR02 & iR11 & iR20, G02 & G11 & G20) # Anti-diagonal
assert implies(iR00 & iR01 & iR02, G00 & G01 & G02) # First column

assert implies(iR10 & iR11 & iR12, G10 & G11 & G12) # Second column
assert implies(iR20 & iR21 & iR22, G20 & G21 & G22) # Third column

# Blue win conditions
assert implies(iB00 & iB10 & iB20, G00 & G10 & G20) # First row
assert implies(iB01 & iB11 & iB21, G01 & G11 & G21) # Second row
assert implies(iB02 & iB12 & iB22, G02 & G12 & G22) # Third row

assert implies(iB00 & iB11 & iB22, G00 & G11 & G22) # Main diagonal
assert implies(iB02 & iB11 & iB20, G02 & G11 & G20) # Anti-diagonal
assert implies(iB00 & iB01 & iB02, G00 & G01 & G02) # First column

assert implies(iB10 & iB11 & iB12, G10 & G11 & G12) # Second column
assert implies(iB20 & iB21 & iB22, G20 & G21 & G22) # Third column

# Verify that if all the green lights in a row, column, or diagonal are lit, and no other green lights are lit,
# then there must be a winning configuration (either all red or all blue) in that line.
assert implies(G00 & G10 & G20 & ~(G01 | G11 | G21 | G02 | G12 | G22) , (iR00 & iR10 & iR20) | (iB00 & iB10 & iB20)) # First row
assert implies(G01 & G11 & G21 & ~(G00 | G10 | G20 | G02 | G12 | G22) , (iR01 & iR11 & iR21) | (iB01 & iB11 & iB21)) # Second row
assert implies(G02 & G12 & G22 & ~(G00 | G10 | G20 | G01 | G11 | G21) , (iR02 & iR12 & iR22) | (iB02 & iB12 & iB22)) # Third row

assert implies(G00 & G11 & G22 & ~(G01 | G10 | G20 | G02 | G12 | G21) , (iR00 & iR11 & iR22) | (iB00 & iB11 & iB22)) # Main diagonal
assert implies(G02 & G11 & G20 & ~(G01 | G10 | G21 | G00 | G12 | G22) , (iR02 & iR11 & iR20) | (iB02 & iB11 & iB20)) # Anti-diagonal

assert implies(G00 & G01 & G02 & ~(G10 | G20 | G11 | G21 | G12 | G22) , (iR00 & iR01 & iR02) | (iB00 & iB01 & iB02)) # First column
assert implies(G10 & G11 & G12 & ~(G00 | G20 | G01 | G21 | G02 | G22) , (iR10 & iR11 & iR12) | (iB10 & iB11 & iB12)) # Second column
assert implies(G20 & G21 & G22 & ~(G00 | G10 | G01 | G11 | G02 | G12) , (iR20 & iR21 & iR22) | (iB20 & iB21 & iB22)) # Third column

# Verify that if one of the green lights are on, none of the red or blue lights are on
assert implies(G00 | G10 | G20
             | G01 | G11 | G21
             | G02 | G12 | G22,

             ~(R00 | R10 | R20
             | R01 | R11 | R21
             | R02 | R12 | R22

             | B00 | B10 | B20
             | B01 | B11 | B21
             | B02 | B12 | B22))
