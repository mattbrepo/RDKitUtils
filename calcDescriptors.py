from rdkit import Chem
import rdkit.Chem.Descriptors as Descriptors

molecule = 'CCCO'
rdkit_molecule = Chem.MolFromSmiles(molecule)

molecular_weight = Descriptors.ExactMolWt(rdkit_molecule)
logp = Descriptors.MolLogP(rdkit_molecule)
h_bond_donor = Descriptors.NumHDonors(rdkit_molecule)
h_bond_acceptors = Descriptors.NumHAcceptors(rdkit_molecule)
rotatable_bonds = Descriptors.NumRotatableBonds(rdkit_molecule)
number_of_atoms = Chem.rdchem.Mol.GetNumAtoms(rdkit_molecule)
number_of_heavy_atoms = Chem.rdchem.Mol.GetNumHeavyAtoms(rdkit_molecule)
formal_charge = Chem.rdmolops.GetFormalCharge(rdkit_molecule)
number_of_rings = Chem.rdMolDescriptors.CalcNumRings(rdkit_molecule)
molar_refractivity = Chem.Crippen.MolMR(rdkit_molecule)

print("Molecular Weight (g/mL): %s" % molecular_weight)
print("Log P: %s" % logp)
print("H Bond Donors: %s" % h_bond_donor)
print("H Bond Acceptors: %s" % h_bond_donor)
print("Rotatable Bonds: %s" % rotatable_bonds)
print("Number of Atoms: %s" % number_of_atoms)
print("Number of Heavy Atoms: %s" % number_of_heavy_atoms)
print("Formal Charge: %s" % formal_charge)
print("Number of Rings: %s" % number_of_rings)
print("Molar Refractivity: %s" % molar_refractivity)