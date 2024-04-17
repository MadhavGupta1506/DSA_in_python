def merge(num1, m, num2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    num2.extend(num1)
    l1=[]
    j=0
    i=0
    while(j<n and i<m+n):
        print("num1:",num1[i])
        print( "num2:",num2[j])
        if(num1[i]<num2[j]):
            i+=1
        elif(num1[i]>=num2[j]):
            num1.insert(num2[j],i)
            i+=1
            j+=1
