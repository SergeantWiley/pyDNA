
# pyDNA

pyDNA is a multirole and multifunctional library used for teaching the methods of programming and debugging. Its intended to share the wonders of programming through interactive guide in understanding programming architecture and advices for debugging. It also contains methods of coming up with knew and passionate projects for young and future programmers. pyDNA like the name suggests is for python. It has different levels of programming from simple functions to data analytics, data transformations, and all the way to low level programming language. 

## Language DNA

LanDNA or Language DNA is a low level programming language used to demonstrate the value in using code in a dynamic and modular way. 

First is declaring a variable. Traditionally, using a unique symbol for low level programming languages help distingush varaibles. In this case, the $ symbol is used
```python
VAR(var_name, seq)
VAR("$Seq_1", "TATGATTATCTTTATATAATGCG")
```
Using the DISP function, we are able to print out the varaible.
```python
DISP("$Seq_1")
Output: GATTATCTTTATATAATGCG
```
To execute transcription, use the EXE function. The new_var is optional however if not used, the seq_var will change. To prevent this, passing a new varaible creates. During transcription, Ts are replaced with Us
```python
EXE(seq_var, promoter, direction='right', new_var=None)
EXE("$Seq_1","TAT",new_var="$RNA")
DISP("$Seq_1")
DISP("$RNA")
Output: GATTATCTTTATATAATGCG
        CUAAUAGAAAUAUAUUACGC
```
After transcription, the RNA may go through Protien synthesis
```python
PRO(seq_var)
```
