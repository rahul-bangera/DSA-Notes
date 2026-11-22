# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

![Level](https://img.shields.io/badge/Medium-orange) ![Pattern](https://img.shields.io/badge/pattern-sliding--window-blue)

**Pattern:** Sliding Window (fixed) | **Difficulty:** Medium | **Status:** 🟡 Revise

## 🎯 Problem
Count subarrays of size `k` whose average is `>= threshold`.

## 💡 Intuition
Average ≥ threshold ⇔ **sum ≥ threshold × k**. Compare sums, no division needed.

## 🧪 Tiny example
`arr=[2,2,2,2,5,5,5,8], k=3, threshold=4` → target sum = 12

| Window | Sum | ≥ 12? |
|---|---|---|
| [2,2,2] | 6 | ❌ |
| [2,2,5] | 9 | ❌ |
| [2,5,5] | 12 | ✅ |
| [5,5,5] | 15 | ✅ |
| [5,5,8] | 18 | ✅ |

Answer = **3**

## ☕ Java Solution
```java
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum = 0, count = 0;
        for (int i = 0; i < k; i++) sum += arr[i];
        if (sum >= threshold * k) count++;

        for (int i = k; i < arr.length; i++) {
            sum -= arr[i - k];
            sum += arr[i];
            if (sum >= threshold * k) count++;
        }
        return count;
    }
}
```
> Alternative: `sum / k >= threshold` also passes, but integer division drops decimals. Prefer `sum >= threshold * k`.

## ⏱ Complexity
Time O(n) | Space O(1)

## ❌ Mistakes I made
1. Wrote `sum += [i]` instead of `sum += arr[i]`
2. Wrote `sum += arr[i - k]` instead of `sum -= arr[i - k]` (the leaving element must be **subtracted**)

## 🧷 Remember
> Enter → `+= arr[i]`, Leave → `-= arr[i-k]`

## 🔁 Revision
- [ ] +3 days
- [ ] +7 days
- [ ] +30 days
