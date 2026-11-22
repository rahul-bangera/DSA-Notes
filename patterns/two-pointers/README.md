# 👉👈 Two Pointers

## When to use
Sorted array/string, pair with target sum, palindrome check, remove duplicates in place, container/area problems.

## Core idea
Two indexes move using a rule, so impossible pairs are skipped → O(n) instead of O(n²).

## Animation: pair sum in a sorted array (target 10)
<div data-anim="two"></div>

## Java template (opposite ends)
```java
int l = 0, r = n - 1;
while (l < r) {
    int sum = a[l] + a[r];
    if (sum == target) return new int[]{l, r};
    else if (sum < target) l++;   // need bigger
    else r--;                     // need smaller
}
```

## Variants
- Opposite ends: pair sum, palindrome, container with most water
- Same direction (slow/fast): remove duplicates, linked-list cycle

## Checklist
- [ ] Sorted (or can I sort)?
- [ ] Which pointer moves when sum is too small / too big?
- [ ] Loop condition is `l < r`, not `<=`?

## Complexity
Time O(n) after sorting | Space O(1)
