# Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum.
def unsorted_integers(integers, target):
 
    # consider each element except the last
    for i in range(len(integers) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(integers)):
 
            # if the desired sum is found, print it
            if integers[i] + integers[j] == target:
                print((integers[i], integers[j]))
                return
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    integers = [5, 10, 4, 7, 6, 2]
    target = 11
 
    unsorted_integers(integers, target)
 

 