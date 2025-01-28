class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        def heapify(arr,n,i):
            lar = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l<n and arr[i] < arr[l]:
                lar = l

            if r < n and arr[lar] < arr[r]:
                lar = r

            if lar != i:
                arr[lar],arr[i] = arr[i],arr[lar]
                heapify(arr,n,lar)


        for i in range(n//2 - 1,-1,-1):
            heapify(arr,n,i)

        for i in range(n-1,-1,-1):
            arr[i],arr[0] = arr[0],arr[i]
            heapify(arr,i,0)

        return arr

        