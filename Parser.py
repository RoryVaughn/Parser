f = open("CNF.txt", "r")
run = 0
a = 1
b = 1
c = 1
d = 1
e = 1
g = 1
h = 1
while run != 5:
    text = f.readline()
    run = run +1
    clauses = 0
    literals = 0
    solve = []
    current = []
    names = []
    for i in range (0,len(text)):
        if text[i]=="(":
            clauses += 1
            clauseSolve = 0
            current = []
            solve = []
            count = 0
        
        if text[i] != ")":
            current.append(text[i])
            if text[i].isalpha():
                solve.append(text[i])

                    
                    
                
            
        else:
            current.append(text[i])
            print (" + ".join(solve))
            for x in range (0,len(solve)):
                if solve[x].isalpha():
                    count += 1
            if count%2 == 0 and eval(" + ".join(solve)) == count:
                clauseSolve = 1
            print ("this clause is", clauseSolve)
                
                

            print eval (" + ".join(solve))
            
            print ''.join(current)
            
                
            
        if text[i].isalpha() and text[i] not in names:
            names.append( text[i])
            literals += 1
            

    
    print(text)
    print "The number of clauses is ",clauses
    print "The number of literals is ",literals
    print "The used literals are ",names
    print "__________________________________"
	
