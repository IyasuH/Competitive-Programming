#User function Template for python3

class Solution: 
    def select(self, arr, i):
        arr=arr[i:]
        if arr == []:
            return
        minVal = arr[0]
        for x in range(i):
            if arr[x]<minVal:
                temp=arr[x]
                arr[x]=minVal
                minVal=temp
        return minVal
            
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for x in range(n):
            minimum=self.select(arr,x)
            minIndx = arr.index(minimum)
            temp=arr[x]
            arr[x]=minimum
            arr[minIndx]=temp
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends