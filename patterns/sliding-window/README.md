# 🪟 Sliding Window

## When to use
Words like **contiguous subarray / substring**, **size k**, **longest / shortest / max / min**, **at most K**.

## Core idea
Don’t recompute each window. **Add the new element, remove the old one** → O(n) instead of O(n·k).

## Animation: max sum of window size 3
<div data-anim="sliding"></div>

## Fixed-size template (Java)
```java
int windowValue = 0, best = 0;
for (int i = 0; i < k; i++) windowValue += arr[i];   // 1. build first window
best = windowValue;                                   // 2. store its result
for (int i = k; i < n; i++) {                         // 3. slide
    windowValue += arr[i];                            //    add right
    windowValue -= arr[i - k];                        //    remove left
    best = Math.max(best, windowValue);               // 4. update after EVERY slide
}
```

## Checklist
- [ ] First window built?
- [ ] Result updated **inside** the loop?
- [ ] `+=` for entering, `-=` for leaving?

## Variants
Fixed size (this page) · Variable size (expand right, shrink left) · At most K distinct
