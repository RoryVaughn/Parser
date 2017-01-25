import random
import time
f = open("CNF.txt", "r")
run = 0
a = random.randint(0, 1)
b = random.randint(0, 1)
c = random.randint(0, 1)
d = random.randint(0, 1)
e = random.randint(0, 1)
g = random.randint(0, 1)
h = random.randint(0, 1)
i = random.randint(0, 1)
j = random.randint(0, 1)
k = random.randint(0, 1)
l = random.randint(0, 1)
m = random.randint(0, 1)
n = random.randint(0, 1)
o = random.randint(0, 1)
p = random.randint(0, 1)
q = random.randint(0, 1)
r = random.randint(0, 1)
s = random.randint(0, 1)
t = random.randint(0, 1)
u = random.randint(0, 1)
v = random.randint(0, 1)
w = random.randint(0, 1)
x = random.randint(0, 1)
y = random.randint(0, 1)
z = random.randint(0, 1)
chromosomes = [a, b, c, d, e, g, h, i, j, k, l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
true = "1"
false = "0"
text = f.readline()
##begin the parsing
while run != 5:
    ##resets for each expression
    solved = 0
    generation = 0
    then = time.time()
    while solved != 1:
        ##updates the values of the chromosomes based on the mutation
        if generation >= 0:
            a = chromosomes[0]
            b = chromosomes[1]
            c = chromosomes[2]
            d = chromosomes[3]
            e = chromosomes[4]
            g = chromosomes[5]
            h = chromosomes[6]
            i = chromosomes[7]
            j = chromosomes[8]
            k = chromosomes[9]
            l = chromosomes[10]
            m = chromosomes[11]
            n = chromosomes[12]
            o = chromosomes[13]
            p = chromosomes[14]
            q = chromosomes[15]
            r = chromosomes[16]
            s = chromosomes[17]
            t = chromosomes[18]
            u = chromosomes[19]
            v = chromosomes[20]
            w = chromosomes[21]
            x = chromosomes[22]
            y = chromosomes[23]
            z = chromosomes[24] 
        print "_________________________________________________________________"
        print "_________________________________________________________________"
        clauses = 0
        literals = 0
        solve = []
        current = []
        fitness = 0
        names = []
        ##loops through the expression and parses
        for i in range (0,len(text)):
            if text[i]=="(":
                clauses += 1
                clauseSolve = 0
                current = []
                solve = []
                count = 0
            ##separates each of the clauses and parses the "!"(not) operator
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
            ## evaluates truthfulness of the expression as well as fitness
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
    ##Genetic mutation
                if fitness/clauses >= .7:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 7:
                            chromosomes[j] = random.randint(0, 1)
                elif fitness/clauses >= .5:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 5:
                            chromosomes[j] = random.randint(0, 1)
                elif fitness/clauses >= .3:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 3:
                            chromosomes[j] = random.randint(0, 1)
                else:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 2:
                            chromosomes[j] = random.randint(0, 1)
            ##checks literals in the clause
            if text[i].isalpha() and text[i] not in names:
                names.append( text[i])
                literals += 1
        ##prints info about the full expression
        print(text)
        print "The fitness is",fitness, "out of",clauses, "for this expression."
        if fitness == clauses:
            print "This expression is solved"
            run += 1
            solved = 1
            text = f.readline()
        print "The number of clauses is ",clauses
        print "The number of literals is ",literals
        print "The used literals are ",names
        print "_________________________________________________________________"
        print "_________________________________________________________________"
        print chromosomes
        print "The current generation is ",generation
        generation += 1
        ##delta time
    now = time.time()
    print now - then
    raw_input("Hit enter to continue to the next expression...") 
    
