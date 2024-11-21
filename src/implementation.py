from z3 import Bools

# Board indices are arranged as:
# 00 | 10 | 20
# -----------
# 01 | 11 | 21
# -----------
# 02 | 12 | 22

# Defining inputs: iRij and iBij, for the red and blue players respectively
iR00, iR01, iR02 = Bools('iR00 iR01 iR02')
iR10, iR11, iR12 = Bools('iR10 iR11 iR12')
iR20, iR21, iR22 = Bools('iR20 iR21 iR22')

iB00, iB01, iB02 = Bools('iB00 iB01 iB02')
iB10, iB11, iB12 = Bools('iB10 iB11 iB12')
iB20, iB21, iB22 = Bools('iB20 iB21 iB22')

# Red win conditions
W1R = iR00 & iR01 & iR02  # First column
W2R = iR10 & iR11 & iR12  # Second column
W3R = iR20 & iR21 & iR22  # Third column
W4R = iR00 & iR10 & iR20  # First row
W5R = iR01 & iR11 & iR21  # Second row
W6R = iR02 & iR12 & iR22  # Third row
W7R = iR00 & iR11 & iR22  # Main diagonal
W8R = iR02 & iR11 & iR20  # Anti-diagonal

# Blue win conditions
W1B = iB00 & iB01 & iB02  # First column
W2B = iB10 & iB11 & iB12  # Second column
W3B = iB20 & iB21 & iB22  # Third column
W4B = iB00 & iB10 & iB20  # First row
W5B = iB01 & iB11 & iB21  # Second row
W6B = iB02 & iB12 & iB22  # Third row
W7B = iB00 & iB11 & iB22  # Main diagonal
W8B = iB02 & iB11 & iB20  # Anti-diagonal

# Combine win conditions
W1 = W1R | W1B  # First column
W2 = W2R | W2B  # Second column
W3 = W3R | W3B  # Third column
W4 = W4R | W4B  # First row
W5 = W5R | W5B  # Second row
W6 = W6R | W6B  # Third row
W7 = W7R | W7B  # Main diagonal
W8 = W8R | W8B  # Anti-diagonal

# Expression for 'win' mode
W = W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8

# Expression for each green LED
G00 = W1 | W4 | W7
G10 = W2 | W4
G20 = W3 | W4 | W8
G01 = W1 | W5
G11 = W2 | W5 | W7 | W8
G21 = W3 | W5
G02 = W1 | W6 | W8
G12 = W2 | W6
G22 = W3 | W6 | W7

# Expression for each red LED
R00, R01, R02 = iR00 & ~W, iR01 & ~W, iR02 & ~W
R10, R11, R12 = iR10 & ~W, iR11 & ~W, iR12 & ~W
R20, R21, R22 = iR20 & ~W, iR21 & ~W, iR22 & ~W

# R00, R01, R02 = iR00, iR01, iR02
# R10, R11, R12 = iR10, iR11, iR12
# R20, R21, R22 = iR20, iR21, iR22

# Expression for each blue LED
B00, B01, B02 = iB00 & ~W, iB01 & ~W, iB02 & ~W
B10, B11, B12 = iB10 & ~W, iB11 & ~W, iB12 & ~W
B20, B21, B22 = iB20 & ~W, iB21 & ~W, iB22 & ~W

# B00, B01, B02 = iB00, iB01, iB02
# B10, B11, B12 = iB10, iB11, iB12
# B20, B21, B22 = iB20, iB21, iB22
