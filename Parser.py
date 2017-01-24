f = open("CNF.txt", "r")
run = 0
a = 0
b = 1
c = 0
d = 0
e = 0
g = 0
h = 1
true = "1"
false = "0"
while run != 5:
    text = f.readline()
    run = run +1
    clauses = 0
    literals = 0
    solve = []
    current = []
    fitness = 0
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
            if text[i - 1] == "!":
                if eval(text[i]) == 1:
                    solve.append(false)
                else:
                    solve.append(true)
            else:
                if text[i].isalpha():
                    solve.append(text[i])
                    
        else:
            current.append(text[i])
            print ''.join(current)
            for x in range (0,len(solve)):
                if solve[x].isalpha():
                    count += 1
            if eval(" + ".join(solve)) >= 1:
                clauseSolve = "true"
                fitness += 1
            else:
                clauseSolve = "false"
            print "This clause is", clauseSolve
            print "number of true literals -", eval (" + ".join(solve))
            print " "

        if text[i].isalpha() and text[i] not in names:
            names.append( text[i])
            literals += 1

    print(text)
    print "The fitness is",fitness, "out of",clauses, "for this expression."
    if fitness == clauses:
        print "This expression is solved"
    print "The number of clauses is ",clauses
    print "The number of literals is ",literals
    print "The used literals are ",names
    print "_________________________________________________________________"
    print "_________________________________________________________________"
