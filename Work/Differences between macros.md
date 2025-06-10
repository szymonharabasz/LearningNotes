1. Centrality parameter file
2. Max multiplicity class
3. `selectBest` - different flag names, but the meaning should be the same
4. `if (btRing == null) continue` is commented out in the old version
   **Doesn't change the results**
5. In old file:
```C++
Float_t mvaValue = calcMVA();
```
Appears before:
```C++
if (mom > 700 && maxima < 2)
	continue;
```
   **Doesn't change the results**
6. In old file:
   ```C++
   cand1 = HCategoryManager::getObject(cand1, candCat, j);
   ```
   Appears after:
   ```C++
   if (!sorterFlag[j])
	   continue;
   ```
**Doesn't change the results**
7. Change in `helperFunctions_multbin.h` `NMULTS` to `5`.


In `loopDST_gen8_workingcopy` - check the influence of (4).

#### AOB:
Write to Claudia about writing committees
Write to Niklas about the writing committee
