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
chromosomes = [a, b, c, d, e, g, h, i, j, k, l]
true = "1"
false = "0"
text = f.readline()
while run != 5:
    solved = 0
    generation = 0
    then = time.time()
    while solved != 1:
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
                
        print "_________________________________________________________________"
        print "_________________________________________________________________"
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
    ##Genetic part
                if fitness/clauses >= .3:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 3:
                            chromosomes[j] = random.randint(0, 1)
                elif fitness/clauses >= .5:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 5:
                            chromosomes[j] = random.randint(0, 1)
                else:
                    for j in range (0,len(chromosomes)):
                        rando = random.randint(0, 10)
                        if rando >= 7:
                            chromosomes[j] = random.randint(0, 1)
                        
                            
                        
                        
                    

            if text[i].isalpha() and text[i] not in names:
                names.append( text[i])
                literals += 1

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
    now = time.time()
    print now - then
    raw_input("Hit enter to continue to the next expression...") 
    
