import asyncio
import math

#Bubble Sort
async def bubble_sort(array): 
    n = len(array) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 
        await asyncio.sleep(0.001)
        
#Insertion Sort
async def insertion_sort(array): 
    # Traverse through 1 to len(array) 
    for i in range(1, len(array)): 
  
        key = array[i] 
  
        # Move elements of array[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < array[j] : 
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = key
        await asyncio.sleep(0.001)
    return True

#Selection Sort        
async def selection_sort(array):
    # Traverse through all array elements 
    for i in range(len(array)): 
        
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 
                
        # Swap the found minimum element with  
        # the first element         
        array[i], array[min_idx] = array[min_idx], array[i] 
        await asyncio.sleep(0.001)
        
#Pankcake Sort
async def pancake_sort(array):
    # Reverses array[0..i] */  
    def flip(array, i): 
        start = 0
        while start < i: 
            temp = array[start] 
            array[start] = array[i] 
            array[i] = temp 
            start += 1
            i -= 1
    # Returns index of the maximum 
    # element in array[0..n-1] */ 
    def findMax(array, n): 
        mi = 0
        for i in range(0,n): 
            if array[i] > array[mi]: 
                mi = i 
        return mi 
    # Start from the complete 
    # array and one by one 
    # reduce current size 
    # by one 
    n = len(array)
    curr_size = n 
    while curr_size > 1: 
        # Find index of the maximum 
        # element in  
        # array[0..curr_size-1] 
        mi = findMax(array, curr_size) 
  
        # Move the maximum element 
        # to end of current array 
        # if it's not already at  
        # the end 
        if mi != curr_size-1: 
            # To move at the end,  
            # first move maximum  
            # number to beginning  
            flip(array, mi) 
  
            # Now move the maximum  
            # number to end by 
            # reversing current array 
            flip(array, curr_size-1) 
        curr_size -= 1
        await asyncio.sleep(0.001)

#Shell Sort        
async def shell_sort(array): 
    # Start with a big gap, then reduce the gap 
    n = len(array) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = array[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and array[j-gap] >temp: 
                array[j] = array[j-gap] 
                j -= gap
  
            # put temp (the original a[i]) in its correct location 
            array[j] = temp 
        await asyncio.sleep(0.3)
        gap //= 2
      
#Cocktail sort
async def cocktail_sort(array): 
    n = len(array) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
  
        # reset the swapped flag on entering the loop, 
        # because it might be true from array previous 
        # iteration. 
        swapped = False
  
        # loop from left to right same as the bubble 
        # sort 
        for i in range (start, end): 
            if (array[i] > array[i + 1]) : 
                array[i], array[i + 1]= array[i + 1], array[i] 
                swapped = True

        await asyncio.sleep(0.001)
        # if nothing moved, then array is sorted. 
        if (swapped == False): 
            break
  
        # otherwise, reset the swapped flag so that it 
        # can be used in the next stage 
        swapped = False
  
        # move the end point back by one, because 
        # item at the end is in its rightful spot 
        end = end-1
  
        # from right to left, doing the same 
        # comparison as in the previous stage 
        for i in range(end-1, start-1, -1): 
            if (array[i] > array[i + 1]): 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
  
        # increase the starting point, because 
        # the last stage would have moved the next 
        # smallest number to its rightful spot. 
        start = start + 1

#HSV colour standard to HEX  
def hsv2hex(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
        
#Check if sorted
def is_sorted(array):
    for i in range(len(array) -1):
        if array[i] > array[i+1]:
            return False
    return True
        
if __name__ == "__main__":
    print("Open via main.py")
    exit()