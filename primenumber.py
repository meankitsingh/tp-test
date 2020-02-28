import pprint 
import random 

# Function to obtain first 1000 Prime numbers
def obtain_primenumbers():
    prime_list = []
    for Number in range (1, 1001):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break

        if (count == 0 and Number != 1):
            prime_list.append(Number)

    return prime_list


# Function To Fill Data Into A Three Dimensional Array
def ThreeD(a, b, c):
    # Obtaining the list of prime Numbers 
    prime_list = obtain_primenumbers()
    # shuffling the list to give it a random order or to obtain non-consecutive order 
    random.shuffle(prime_list)
    # Filling Shuffled list items into a three dimensional list
    prime_3d_list = [[ [prime  for prime in prime_list] for col in range(b)] for row in range(c)] 
    pprint.pprint(prime_3d_list,indent=2, width=100,compact=True)  


if __name__ == "__main__":
    ThreeD(10,10,10)

