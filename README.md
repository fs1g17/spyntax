# Spyntax 

## Description 
Spyntax is a tool for generating all the possible sentences from spintax. 

## Installation 
```cmd
pip install spyntax
```
## Demo
```python 
from spyntax import *
spins = generate_all_sentences("{Hi|Hello}, this is a {neat|nice|cool} tool!")
for spin in spins:
    print(spin)
```
```cmd
 Hi, this is a neat tool!
 Hi, this is a nice tool!
 Hi, this is a cool tool!
 Hello, this is a neat tool!
 Hello, this is a nice tool!
 Hello, this is a cool tool!
 ```
## About 
The tool parses the message and uses Depth First Search to generate all possible outcomes and returns them as a list. Currently nested spintax is not supported.
