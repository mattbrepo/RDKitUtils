from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem

ATOM_NUMS = 110

def printValences():
  tab = Chem.GetPeriodicTable()
  max_num_val = 3
  s = ''
  for i in range(1, ATOM_NUMS + 1):
    xs = tab.GetValenceList(i)
    z = '('
    for x in xs:
      z = z + str(x) + ','
    for i in range(len(xs), max_num_val):
      z = z + str('-') + ','
    z = z[:-1] # remove last comma
    z = z + ')'
    s = s + z + ', '
  s = s[:-2] # remove last comma
  print('VALENCES (' + str(max_num_val) + '): ' + s)

def printDefaultValence():
  tab = Chem.GetPeriodicTable()
  s = ''
  for z in range(1, ATOM_NUMS + 1):
    v = tab.GetDefaultValence(z)
    s = s + str(v) + ', '
  s = s[:-2] # remove last comma
  print('DEF_VALENCE: ' + s)
  
def printNouterElecs():
  tab = Chem.GetPeriodicTable()
  s = ''
  for z in range(1, ATOM_NUMS + 1):
    v = tab.GetNOuterElecs(z)
    s = s + str(v) + ', '
  s = s[:-2] # remove last comma
  print('OUTER_ELECTR: ' + s)

#
# Main
#

#printValences()
#printDefaultValence()
printNouterElecs()
