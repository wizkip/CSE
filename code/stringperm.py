from itertools import permutations


#Lets do a simple function

def stringperm(str):

    permlist = permutations(str)

    #Iterate through the list

    for perm in list(permlist):

        print(''.join(perm)) 

if __name__ == "__main__":

    str = "AWS"
    stringperm(str)
       