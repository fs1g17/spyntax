from typing import List

def get_temps_blanks(message: str):
    template = []
    blanks = []
    blank = []
    word = ""
    num_brackets = 0

    for i,letter in enumerate(message):
        if i==len(message)-1:
            word += letter
            template += [word]
            continue
                
        if num_brackets%2==0 and letter != '{':
            word += letter
            continue
    
        if letter == '{':
            if len(word) > 0:
                template += [word]
                word = ""
            num_brackets += 1
            continue
        
        if letter == '}':
            blank.append(word)
            blanks.append(blank)
            blank = []
            word = ""
            num_brackets += 1

        if num_brackets%2==1 and letter != '|':
            word += letter
            continue 

        if num_brackets%2==1 and letter == '|':
            blank.append(word)
            word = ""
            continue 
    return template,blanks

# assuming we start with blanks
def DFS(templates:List[str],blanks:List[List[str]],t_index,b_index,spins:List[str],spin:str,next:str):
    if t_index >= len(templates) and b_index >= len(blanks):
        return spins.append(spin)

    if next == "template" and t_index < len(templates):
        new_spin = spin[:]  
        new_spin += templates[t_index]
    
    if next == "template" and t_index >= len(templates):
        new_spin=spin[:]
    
    if next == "template":
        DFS(templates=templates,blanks=blanks,t_index=t_index+1,b_index=b_index,spins=spins,spin=new_spin,next="blanks")
        

    if next == "blanks" and b_index < len(blanks):
        #make a copy of spin
        for blank in blanks[b_index]:
            new_spin = spin[:]
            if len(new_spin) == 0 or not(new_spin[len(new_spin)-1]).isspace():
                prev = " "
            else:
                prev = ""    
            new_spin += prev + blank
            DFS(templates=templates,blanks=blanks,t_index=t_index,b_index=b_index+1,spins=spins,spin=new_spin,next="template")
    
    if next == "blanks" and b_index >= len(templates):
        DFS(templates=templates,blanks=blanks,t_index=t_index,b_index=b_index,spins=spins,spin=spin[:],next="templates")
    
    return spins

def generate_all_sentences(message:str):
    templates,blanks = get_temps_blanks(message)
    if message[0] == '{':
        next = 'blanks'
    else:
        next = 'template'
    spins = DFS(templates=templates,blanks=blanks,t_index=0,b_index=0,spins=[],spin="",next=next)
    return spins