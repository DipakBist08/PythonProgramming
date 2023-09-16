#Define a function and that contains a list ,from that list findout highest even number.


def highest_evens(li):
    evens=[]
    for items in li:
        if items%2==0:
            evens.append(items)
    return max(evens)
print(highest_evens([2,10,13,14,100,200,800,202,600]))