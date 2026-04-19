class Solution:

    def swap(self, i: int, j: int, arr: List[int]) -> None:
        if i == j:
            return
        arr[i], arr[j] = arr[j], arr[i]

    def quickSort(self, s: int, e: int, arr: List[int]) -> None:
        while s < e:
            pivot_idx = (s + e) // 2
            pivot = arr[pivot_idx]
            
            # Partition logic (Hoare-like for efficiency and avoiding worst cases)
            i, j = s, e
            while i <= j:
                while arr[i] < pivot: i += 1
                while arr[j] > pivot: j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            
            # Tail Recursion Optimization and smaller sub-problem first
            if j - s < e - i:
                self.quickSort(s, j, arr)
                s = i
            else:
                self.quickSort(i, e, arr)
                e = j

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(0, len(nums) - 1, nums)
        return nums
        