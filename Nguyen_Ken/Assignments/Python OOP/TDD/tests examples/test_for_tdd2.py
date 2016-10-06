test_list = [1,2,3,4,5]

def filter(iterable, function):
    matches = []
    for num in iterable:
        if function(num):
            matches.append(num)
    return matches

print filter(test_list, lambda num: num % 2 == 1)



def reduce(iterable, function, memo):
        for num in iterable:
           memo = function(memo,num)
        return memo

print reduce(test_list, lambda memo, num: memo+num, 0)


def reject(iterable, function):
        rejected = []
        for num in iterable:
            if not function(num):
                rejected.append(num)
        return rejected

print reject(test_list, lambda num: num % 2 == 1)
