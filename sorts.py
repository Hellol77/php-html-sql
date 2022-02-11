import random,timeit
#
#
#quick sort
def quick_sort(A,first,last):
    global Qc
    global Qs
    if first >= last: 
        return
    left,right=first+1,last
    
    pivot=A[first]
    while left<=right:
        while left<=last and A[left]<pivot:
            Qc+=1
            left+=1
        while right>first and A[right]>pivot:
            Qc+=1
            right-=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            Qs+=2
            left+=1
            right-=1
    A[first],A[right]=A[right],A[first]
    Qs+=2
    quick_sort(A,first,right-1)
    quick_sort(A,right+1,last)
#
#
#quick sort + insertion sort
#
#
Qic,Qis=0,0
def quick_sort_insertion(A,first,last):
    global Qic
    global Qis
    if last-first<40:
        for j in range(first,last+1):
            for i in range(j,0,-1):
                if A[i-1]>A[i]:
                    Qic+=1
                    A[i-1],A[i]=A[i],A[i-1]
                    Qis+=2
        return
    if first >= last: 
        return
    left,right=first+1,last
    
    pivot=A[first]
    while left<=right:
        
        while left<=last and A[left]<pivot:
            Qic+=1
            left+=1
        while right>first and A[right]>pivot:
            Qic+=1
            right-=1
        if left<=right:
            A[left],A[right]=A[right],A[left]
            Qis+=2
            left+=1
            right-=1
    A[first],A[right]=A[right],A[first]
    Qis+=2
    quick_sort(A,first,right-1)
    quick_sort(A,right+1,last)
    
#	
#
#merge sort
#
#

def merge_sort(A,first,last):
    if first>=last:
        return
    merge_sort(A,first,(first+last)//2)
    merge_sort(A,(first+last)//2+1,last)
    merge_two_sorted_lists(A,first,last)

def merge_two_sorted_lists(A,first,last):
    global Mc
    global Ms
    m=(first+last)//2
    i,j=first,m+1
    B=[]
    while i <= m and j <=last:
        if A[i]<=A[j]:
            Mc+=1
            B.append(A[i])
            Ms+=1
            i+=1
        else:
            Mc+=1
            B.append(A[j])
            Ms+=1
            j+=1
    for k in range(i,m+1):
        B.append(A[k])
        Ms+=1
    for k in range(j,last+1):
        B.append(A[k])
        Ms+=1
    for i in range(first,last+1):
        A[i]=B[i-first]
        Ms+=1
#
#
# merge sort + insertion sort
#
#
Mic,Mis=0,0
def merge_sort_insertion(A,first,last):
    global Mic
    global Mis
    if last-first<40:
        for j in range(first,last+1):
            for i in range(j,0,-1):
                if A[i-1]>A[i]:
                    Mic+=1
                    A[i-1],A[i]=A[i],A[i-1]
                    Mis+=2
        return
    merge_sort(A,first,(first+last)//2)
    merge_sort(A,(first+last)//2+1,last)
    merge_insertion_two_sorted_lists(A,first,last)

def merge_insertion_two_sorted_lists(A,first,last):
    global Mic
    global Mis
    m=(first+last)//2
    i,j=first,m+1
    B=[]
    while i <= m and j <=last:
        if A[i]<=A[j]:
            Mic+=1
            B.append(A[i])
            Mis+=1
            i+=1
        else:
            Mic+=1
            B.append(A[j])
            Mis+=1
            j+=1
    for k in range(i,m+1):
        B.append(A[k])
        Mis+=1
    for k in range(j,last+1):
        B.append(A[k])
        Mis+=1
    for i in range(first,last+1):
        A[i]=B[i-first]
        Mis+=1

#
#
#heap_sort
#
#
def heap_sort(C):
    global Hc
    global Hs
    n=len(C)
    #make_heap
    for k in range(n-1,-1,-1):
        heapify_down(C,k,n)
    for k in range(len(C)-1,-1,-1):
        C[0],C[k]=C[k],C[0]
        Hs+=2
        n=n-1
        heapify_down(C,0,n)
    
        
#n은 전체 노드 수 
#C[k]가 힙성질 위배할 경우 밑으로 내려가면서 힙성질을 만족하는 위치를 찾는다
def heapify_down(C,k,n):
    global Hc
    global Hs
    while 2*k+1<n:
        L,R=2*k+1,2*k+2
        if L<n and C[L]>C[k]:
            Hc+=1
            m=L
        else:
            Hc+=1
            m=k
        if R<n and C[R]>C[m]:
            Hc+=1
            m=R
        if m!=k:
            C[k],C[m]=C[m],C[k]
            k=m
            Hs+=2
        else:
            break
            
def check_sorted(A):
    for i in range(n-1):
        if A[i]>A[i+1]: return False
    return True
    


Qc,Qs,Mc,Ms,Hc,Hs=0,0,0,0,0,0

n=int(input())
random.seed()
A=[]

for i in range(n):
    A.append(random.randint(-1000,1000))
B=A[:]
C=A[:]
D=A[:]
E=A[:]
print("")

print("Quick sort")
print("time=",timeit.timeit("quick_sort(A,0,n-1)",globals=globals(),number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc,Qs))
print("Merge sort:")
print("time =",timeit.timeit("merge_sort(B,0,n-1)",globals=globals(),number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc,Ms))
print("Heap sort:")
print("time =",timeit.timeit("heap_sort(C)",globals=globals(),number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc,Hs))
print("quick_sort_insertion")
print("time=",timeit.timeit("quick_sort_insertion(D,0,n-1)",globals=globals(),number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qic,Qis))
print("merge_sort_insertion:")
print("time =",timeit.timeit("merge_sort_insertion(E,0,n-1)",globals=globals(),number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mic,Mis))
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))