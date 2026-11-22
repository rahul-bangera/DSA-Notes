# 🪟 Sliding Window

## When to use
Words like **contiguous subarray / substring**, **size k**, **longest / shortest / max / min**, **at most K**.

## Core idea
Don’t recompute each window. **Add the new element, remove the old one** → O(n) instead of O(n·k).

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

<!-- PROBLEMS:START -->
## 📋 Problems solved
| # | Problem | Level |
|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters.md) | 🟡 Medium |
| 1343 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](1343-subarrays-size-k-avg-threshold.md) | 🟡 Medium |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](1456-max-vowels-substring-k.md) | 🟡 Medium |
<!-- PROBLEMS:END -->
