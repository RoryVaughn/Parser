f = open("CNF.txt", "r")
run = 0
while run != 5:
    text = f.readline()
    run = run +1
    clauses = 0
    literals = 0
    names = []
    for i in range (0,len(text)):
        if text[i]=="(":
            clauses += 1
    for l in range (0,len(text)):
        if text[l].isalpha() and text[l] not in names:
            names.append( text[l])
            literals += 1
            

    
    print(text)
    print "The number of clauses is ",clauses
    print "The number of literals is ",literals
    print "The used literals are ",names
    print "__________________________________"
	
