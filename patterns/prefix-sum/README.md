# ➕ Prefix Sum

## When to use
Many range-sum queries, "subarray sum equals K", counting subarrays with a property.

## Core idea
Precompute running totals once; any range sum is the difference of two prefixes.

## Tiny example
`a = [2, 4, 1, 3]` → `prefix = [0, 2, 6, 7, 10]`
sum(1..2) = prefix[3] − prefix[1] = 7 − 2 = **5**

## Java template
```java
int[] pre = new int[n + 1];
for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + a[i];
int rangeSum = pre[r + 1] - pre[l];   // sum of a[l..r]
```

## Subarray sum = K (HashMap)
```java
Map<Integer, Integer> seen = new HashMap<>();
seen.put(0, 1);
int sum = 0, count = 0;
for (int x : a) {
    sum += x;
    count += seen.getOrDefault(sum - k, 0);
    seen.merge(sum, 1, Integer::sum);
}
```

## Checklist
- [ ] `pre` has size n+1 and `pre[0] = 0`
- [ ] Range sum = `pre[r+1] - pre[l]`

## Complexity
Build O(n) | Query O(1)
