29-Sep-'25


**Functional Assignment Fix:**
I did not correctly assign the functional in the initial molecule creation:

```python
mol.xc = functional
mf = dft.UKS(mol) if spin > 0 else dft.RKS(mol)
```
This likely defaulted to PySCF's LDA functional. 

Fixed with:
```python
mf = dft.UKS(mol, xc=functional) if spin > 0 else dft.RKS(mol, xc=functional)
```

