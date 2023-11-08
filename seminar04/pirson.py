import numpy as np

# Create random list called xarr
rng = np.random.default_rng(seed=42)
xarr = rng.random((3, 3))
print("\nRandom list xarr\n", xarr)

# Run corrcoef function with Pirson method for the xarr
R1 = np.corrcoef(xarr)
print("\nPirson's correlation of xarr\n", R1)

# Create random list called yarr
yarr = rng.random((3, 3))
print("\nRandom list yarr\n", yarr)

# Run corrcoef function with Pirson method row by row for xarr and yarr
R2 = np.corrcoef(xarr, yarr)
print("\nPirson's correlation row by row for xarr and yarr\n", R2)

# Run corrcoef function with Pirson method column by column for xarr and yarr
R3 = np.corrcoef(xarr, yarr, rowvar=False)
print("\nPirson's correlation column by column for xarr and yarr\n", R3)
