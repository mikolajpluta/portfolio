por=0       #zmienna globalna do zliczania porownan
zam=0       #zmienna globalna do zliczania zamian


#quickSort
def partition(l,s,e):
    global por
    global zam
    pivot = l[e]
    p1=s
    p2=e-1
    while True:
        while l[p1]<=pivot and p1<e:
            p1+=1
            por+=1
        while l[p2]>=pivot and p2>0:
            p2-=1
            por+=1
        if p1<p2:                               # zliczamy tylko porownania elementow, wiec operacja
            l[p1],l[p2]=l[p2],l[p1]             # if p1<p2 nie jest liczona jako porownanie elementow tablicy
            por+=2
            zam+=1
        else:
            por+=2
            break
    l[p1],l[e]=l[e],l[p1]
    zam+=1
    return p1
def quick_sort(l, s, e):
    global por
    global zam
    if s>=e:
        return
    p=partition(l,s,e)
    quick_sort(l,s,p-1)
    quick_sort(l,p+1,e)

#MergeSort
def merge(arr,l,r):
    global por
    k=0
    p1=0
    p2=0
    while p1<len(l) and p2<len(r):
        if l[p1]<=r[p2]:
            arr[k]=l[p1]
            p1+=1
            k+=1
            por+=1
        else:
            arr[k]=r[p2]
            p2 += 1
            k+=1
            por += 1
    while p1<len(l):
        arr[k]=l[p1]
        p1+=1
        k+=1
    while p2<len(r):
        arr[k]=r[p2]
        p2+=1
        k+=1

def merge_sort(l):
    global por
    if len(l)>1:
        m=len(l)//2
        left=l[:m]
        right=l[m:]
        merge_sort(left)
        merge_sort(right)
        merge(l,left,right)

#heap sort
def heapify(l,n,i):
    global por
    global zam
    left = i*2+1
    right=i*2+2
    maks=i
    if left<n and l[left]>l[maks]:
        maks=left
        por += 1
    if right<n and l[right]>l[maks]:
        maks=right
        por += 1
    if maks != i:
        l[maks],l[i] = l[i],l[maks]
        zam += 1
        heapify(l,n,maks)
def build_max_heap(l):
    for i in range(len(l)//2-1,-1,-1):
        heapify(l,len(l),i)
def heap_sort(l):
    global zam
    build_max_heap(l)
    for i in range(len(l)-1,-1,-1):
        l[0],l[i]=l[i],l[0]
        zam += 1
        heapify(l,i,0)

#insertion sort
def insertion_sort(l):
    global por
    global zam
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
            zam += 1
            por += 1
        l[j+1]=key
        zam += 1
        por += 1

#bubble sort
def BubbleSort(l):
    global por
    global zam
    for i in range(len(l)):
        for j in range(len(l)-1,i,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1]=l[j-1],l[j]
                por += 1
                zam += 1
            por += 1

#selection sort
def SelectionSort(l):
    global por
    global zam
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
                por += 1
            por += 1
        l[i],l[min]=l[min],l[i]
        zam += 1

