class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        has_a_peak = False
        has_lower = False
        prev_item = None
        for item in arr:
            if prev_item is None:
                prev_item = item
            else:
                if not has_a_peak and item > prev_item:
                    prev_item = item
                    has_lower = True
                elif not has_a_peak and has_lower and item < prev_item:
                    has_a_peak = True
                    prev_item = item
                elif has_a_peak and item < prev_item:
                    prev_item = item
                else:
                    return False
        if has_a_peak:
            return True
        else:
            return False
