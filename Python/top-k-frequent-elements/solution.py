from collections import Counter
import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements in a list using a Min-Heap.
    
    Args:
        nums: List of integers.
        k: Number of most frequent elements to return.
        
    Returns:
        List of the k most frequent integers.
    """
    # 1. Count frequencies of each element: O(N)
    counts = Counter(nums)
    
    # 2. Use a Min-Heap to keep track of the top k elements: O(N log k)
    # We store tuples of (frequency, element) in the heap.
    # The heap will maintain the k elements with the highest frequencies.
    heap = []
    
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        # If heap size exceeds k, remove the element with the smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)
            
    # 3. Extract elements from the heap: O(k log k)
    return [item[1] for item in heap]