# 1456. Maximum Number of Vowels in a Substring of Given Length

![Level](https://img.shields.io/badge/Medium-orange) ![Pattern](https://img.shields.io/badge/pattern-sliding--window-blue)

**Pattern:** Sliding Window (fixed) | **Difficulty:** Medium | **Status:** 🟡 Revise

## 🎯 Problem
Max number of vowels in any substring of length `k`.

## 💡 Intuition
Keep a running vowel `count`. A vowel entering → `count++`, a vowel leaving → `count--`.

## 🧪 Tiny example
`s="abciiidef", k=3`

| Window | Vowels | Max so far |
|---|---|---|
| abc | 1 | 1 |
| bci | 1 | 1 |
| cii | 2 | 2 |
| **iii** | **3** | **3** |
| iid | 2 | 3 |
| ide | 2 | 3 |
| def | 1 | 3 |

## ☕ Java Solution
```java
class Solution {
    public int maxVowels(String s, int k) {
        int count = 0, maxNum = 0;
        for (int i = 0; i < k; i++) if (isVowel(s.charAt(i))) count++;
        maxNum = count;

        for (int i = k; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) count++;
            if (isVowel(s.charAt(i - k))) count--;
            maxNum = Math.max(maxNum, count);   // inside the loop!
        }
        return maxNum;
    }
    private boolean isVowel(char c) {
        return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
    }
}
```

## ⏱ Complexity
Time O(n) | Space O(1)

## ❌ Mistakes I made
1. Put `maxNum = Math.max(...)` **after** the loop, so it only saw the first and last windows and missed the middle max (3).

## 🧷 Remember
> Build first window → store result → slide → **update after every slide**

## 🔁 Revision
- [ ] +3 days
- [ ] +7 days
- [ ] +30 days
