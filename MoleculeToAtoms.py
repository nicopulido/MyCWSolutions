def isTheSameBracket(subFormula):
    opening = subFormula[0]
    closing = { '(': ')', '[': ']', '{': '}' }[opening]
    depth = 1
    i = 1
    while i < len(subFormula) and depth > 0:
        if subFormula[i] == opening:
            depth += 1
        elif subFormula[i] == closing:
            depth -= 1
        i += 1
    # result is the substring inside the matched brackets
    return {"i": i - 1, "result": subFormula[1:i-1]}

def createToken(formula, i):
    start = i
    result = formula[i]
    i += 1
    while i < len(formula) and formula[i].isalpha() and not formula[i].isupper():
        result += formula[i]
        i += 1
    return {"token": result, "i": i - 1}

def createDigit(formula, i):
    result = ''
    while i < len(formula) and formula[i].isdigit():
        result += formula[i]
        i += 1
    return {"result": result, "i": i - 1}



def parse_molecule(formula):
    result = {} #dictionary to store values and keys
    token = "" #token to create keys for dictionaries
    i = 0

    while i < len(formula):

        if formula[i] in '[({':
            subResult = isTheSameBracket(formula[i:])
            subMolecule = parse_molecule(subResult["result"])
            i += subResult["i"]

            if i < len(formula) - 1 and formula[i + 1].isdigit():
                for key in subMolecule:
                    subMolecule[key] *= int(formula[i + 1])
                i += 1

            for key, value in subMolecule.items():

                if key in result:
                    result[key] += value
                else:
                    result[key] = value
            i += 1



        if i < len(formula) and formula[i].isupper():

            subToken = createToken(formula, i)
            token = subToken["token"]
            i = subToken["i"] + 1
            count = 1

            if i < len(formula) and formula[i].isdigit():
                digit = createDigit(formula, i)
                count = int(digit["result"])
                i = digit["i"] + 1

            if token in result:
                result[token] += count
            else:
                result[token] = count

    return result
            

print(parse_molecule("Na{S10PNaClN}K{Na10K9Fe{C5O9NaP(H5O(Cl7HP7Fe{P9CaFeS{NaC4OH}Cu})Cl5)}PK}Fe"))

#link to kata : https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
"""For a given chemical formula represented by a string, 
count the number of atoms of each element contained in the
molecule and return an object (associative array in PHP,
Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them.
The index outside the brackets tells you that you have to multiply count 
of each atom inside the bracket on this index. For example, in Fe(NO3)2 
you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested.
Index after the braces is optional."""