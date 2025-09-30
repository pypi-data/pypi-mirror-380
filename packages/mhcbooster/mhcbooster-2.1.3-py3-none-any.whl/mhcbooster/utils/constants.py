import pandas as pd
from io import StringIO

PROTON_MASS = 1.007276

SUPERTYPES = ['HLA-A0101', 'HLA-A0201', 'HLA-A0301', 'HLA-A2402', 'HLA-A2601', 'HLA-B0702',
              'HLA-B0801', 'HLA-B2705', 'HLA-B3901', 'HLA-B4001', 'HLA-B5801', 'HLA-B1501']

EPSILON = 1e-7

COMMON_AA = "ARNDCQEGHILKMFPSTWYV"
COMMON_AA_LIST = list(COMMON_AA)
# We can add unknown amino acids to this list as X. We would have to replace unkown AAs in loaded data with
# X then. For now we will continue to drop them.

BLOSUM62_MATRIX = pd.read_csv(StringIO("""
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  X
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3  0
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  0
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  0
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1  0
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  0
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3  0
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3  0
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1  0
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1  0
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1  0
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2  0
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0  0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3  0
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1  0
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4  0
X  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1
"""), sep='\s+').loc[COMMON_AA_LIST, COMMON_AA_LIST].astype("int8")
assert (BLOSUM62_MATRIX == BLOSUM62_MATRIX.T).all().all()

MASS_UNIMOD_MAP = {
    42.0106: '1',
    57.0215: '4',
    79.9663: '21',
    39.9950: '26',
    -18.0106: '27',
    -17.0265: '28',
    15.9949: '35',
    114.0429: '121',
    119.0041: '312',
    229.1629: '737'
}

UNIMOD_MASS_MAP = {
    '1': 42.0106,
    '4': 57.0215,
    '21': 79.9663,
    '26': 39.9950,
    '27': -18.0106,
    '28': -17.0265,
    '35': 15.9949,
    '121': 114.0429,
    '312': 119.0041,
    '737': 229.1629
}

UNIMOD_NAME_MAP = {
    '1': 'Acetyl',
    '4': 'Carbamidomethyl',
    '21': 'Phospho',
    '26': 'Pyro-carbamidomethyl',
    '27': 'Glu->pyro-Glu',
    '28': 'Gln->pyro-Glu',
    '35': 'Oxidation',
    '121': 'GG',
    '312': 'Cysteinyl',
    '737': 'TMT6plex'
}
