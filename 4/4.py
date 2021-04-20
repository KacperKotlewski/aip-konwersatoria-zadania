#%%
import time
import copy

listOfNumberLists = [
    [14,40,31,28,3,15,17,51], 
    [3, 14, 15, 17, 28, 31, 50, 60], 
    [51, 40, 31, 28, 17, 15, 14, 3], 
    [23, 23, 23, 23, 23, 23, 23, 23]
]

def timeFunction(function):
    def wrapper():
        estimated = []
        for i in range(10):
            table = copy.deepcopy(listOfNumberLists)
            start = time.perf_counter()
            answers = [function(e) for e in table]
            estimated.append((time.perf_counter() - start))
        print("--- średnia ilość sekund na 10 wykonań ---")
        print("--- %s sekund ---" % (sum(estimated)/len(estimated)))
        print(answers)
    return wrapper

#%%
@timeFunction
def selection_sort(T):
    for n in range(len(T)):
        lowest = n
        for i in range(n+1, len(T)):
            if T[lowest] > T[i]:
                lowest = i   
        T[n], T[lowest] = T[lowest], T[n]
    return T

selection_sort()
# %%
@timeFunction
def bubble_sort(T):
    n = len(T)
    for i in range(n):
        for j in range(i, n)[::-1]:
            if T[j] < T[j-1]:
                T[j], T[j-1] = T[j-1], T[j]
    return T

bubble_sort()
# %%

@timeFunction
def insertion_sort(K):
    for i in range(0, len(K)):
        key = K[i]
        n = 1
        while n <= i and key < K[i-n] :
                K[i-n + 1] = K[i-n]
                n += 1
        K[i-n +1] = key
    return K

insertion_sort()
# %%
