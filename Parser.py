f = open("CNF.txt", "r")
run = 0
while run != 5:
    text = f.readline()
    run = run +1
    clauses = 0
    literals = 0
    currentLit = []
    a = 1
    b = 0
    c = 1
    d = 1
    e = 0
    f = 1
    g = 0
    solution = [1,0,1,1]
    current = []
    names = []
    for i in range (0,len(text)):
        if text[i]=="(":
            clauses += 1
            current = []
        
        if text[i] != ")":
                current.append(text[i])
                if text[i].isalpha():
                    
                    if current[-2] == "!":
                        currentLit = []
                    if text[i] not in names:
                        names.append( text[i])
                        literals += 1
                        
                            

        else:
            current.append(text[i])
            
            print ''.join(current)
            

    print(text)
    print "The number of clauses is ",clauses
    print "The number of literals is ",literals
    print "The used literals are ",names
    print "__________________________________"
	
