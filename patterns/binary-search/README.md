# 🔍 Binary Search

## When to use
Sorted data, first/last position, "minimum X such that condition holds" (search on answer), any O(log n) hint.

## Core idea
Check the middle, throw away the half that cannot contain the answer.

## Animation: find 11 in [1,3,5,7,9,11,13]
<div data-anim="bs"></div>

## Java template
```java
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;   // avoids overflow
    if (a[mid] == target) return mid;
    else if (a[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1;
```

## Checklist
- [ ] `mid = lo + (hi - lo) / 2`
- [ ] Loop `lo <= hi` and move with `mid ± 1` (no infinite loop)
- [ ] Can I phrase a true/false condition? Then search on the answer

## Complexity
Time O(log n) | Space O(1)
