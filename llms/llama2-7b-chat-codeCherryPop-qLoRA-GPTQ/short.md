Lets review the following types from metacoq extracted into haskell. 
-- layer 0 have no dependencies
data Positive =  XI Positive  | XO Positive  | 
XH

data Byte = X00 | X01| YYSpliceByteListIntoHereYY  |XFE |XFF -- one pair per 2 hex codes. (0-F)*2

next layer: -- 1 dep
data N =   N0  | Npos Positive
data Z =   Z0 | Zpos Positive | Zneg Positive
data MyString =   EmptyString | String Byte MyString
data Nat =  O  | S Nat


next stop, -- 2 dep
data TNumRel =   Le Z | Eq0
data UniversalLevel =    Lzero | Level MyString\ | Lvar Nat
data Prod a b =    Pair a b
next stop, n^3 data 
Prod a b =    Pair a b                     

type SortedLevels = Prod UniversalLevel TNumRel

the tesseract -- 4 dep                   
type TProd_SortedLevels_UniversalLevel = Prod SortedLevels UniversalLevel

next is the 5th level data 
data Tree0 =   Leaf0 | Node0 T0 Tree0 (TProd_SortedLevels_UniversalLevel) Tree0
data TTree =   Leaf | Node T0 Tree UniversalLevel Tree

-- 6 deps
type TTreeTree0Pair = Prod TTree Tree0
--7
data Global_env =  Mk_global_env TTreeTree0Pair\ Global_declarations TMk_retroknowledge_Kername_Kername_37
--8 
type BigMama = (Prod Global_env Term)
