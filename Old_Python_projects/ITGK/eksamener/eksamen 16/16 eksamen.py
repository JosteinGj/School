import numpy as np
def initElection(parties): return [[0 for i in parties] for a in range(5)]

def updateElection(table,dist,data):
    table[dist]+=data
    return table
def printleadP(election,parties):
    sums=[0]*len(election[0])
    election=np.array(election)
    election=election.transpose()
    for i in range(len(sums)):
        sums[i]+=sum(election[i])
    vals=zip(parties,sums)
    winner=max(vals, key= lambda x:x[1])
    print ("{0[0]} is leading the election with {0[1]}".format(winner))


def leadindex(list):
 return list.index(max(list))


def printresults(election,parties):

    delegates=[0]*(len(parties)+2)

    for i in range(len(election)):
        a=leadindex(election[i])
        if max(election[i])==0:
            delegates[-1]+=1
        elif max(election[a]) in election[a+1:]:
            delegates[-2]+=1
        else:
            delegates[election[i].index(max(election[i]))]+=1
    print(delegates)

    for i,val in enumerate(parties):
        print("{: <25}{} {}".format(parties[i],delegates[i],("delegate" if delegates[i]==1 else "delegates") ))

    print("{: <25}{} {}".format("undicied(tied)",delegates[-1],
                                ("delegate" if delegates[-1]==1 else "delegates")))
    print("{: <25}{} {}".format("undicied(no votes)",delegates[-2],("delegate" if delegates[-2]==1 else "delegates")))
printresults([[1,2,3],[0,0,0],[0,0,0],[1,2,3],[3,2,1],[3,2,1],[2,3,1]],["a","b","c"])

