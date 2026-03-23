# 📁 Quick Sort
> A Python implementation of the quicksort algorithm, a divide and conquer sorting approach that partitions around a pivot and recursively sorts each partition.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

---

## 📌 About

This project implements quicksort from scratch and serves as a direct companion to the Merge Sort project, both are O(n log n) divide and conquer sorting algorithms, but they take different approaches. Where merge sort splits first and sorts on the way back up, quicksort partitions around a pivot first and recurses into each partition. Built to understand pivot based partitioning, three way list comprehension filtering, and how duplicates are handled cleanly.

---

## 🧠 What I Learned

- **Pivot-based partitioning** — Choosing the first element as the pivot and splitting the remaining elements into three groups — less than, equal to, and greater than the pivot — using a separate list comprehension for each
- **Three-way partitioning with list comprehensions** — Using `pivot_less`, `pivot_equal`, and `pivot_greater` as three separate lists keeps the logic clean and naturally handles duplicate values without any extra logic
- **Recursion returning new lists** — Unlike merge sort which sorts in place, this implementation returns a new sorted list at each level and concatenates them with +, making the recursive flow easier to follow
- **Handling duplicates** — Collecting all elements equal to the pivot in `pivot_equal` means duplicates are never lost or double-sorted, which is a subtle but important correctness detail
- **Quicksort vs merge sort** — Understanding the key trade-offs: quicksort uses less memory since it doesn't require auxiliary arrays at each level, but its worst-case is O(n²) if the pivot is always the smallest or largest element — merge sort guarantees O(n log n) in all cases
- **Docstrings with Args and Returns** — Writing structured docstrings that document what the function accepts and what it gives back, following a professional documentation standard

---

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|---|---|
| Python 3.x | Core Language |

## 💡 How It Works
```
Original:  [20, 3, 14, 1, 5]
Pivot: 20

pivot_less    = [3, 14, 1, 5]
pivot_equal   = [20]
pivot_greater = []

Recurse into pivot_less → [3, 14, 1, 5]
Pivot: 3
  pivot_less    = [1]
  pivot_equal   = [3]
  pivot_greater = [5, 14]
  ...and so on

Final: [1, 3, 5, 14, 20] ✅
```

**Example Output:**
```
quick_sort([20, 3, 14, 1, 5])              # [1, 3, 5, 14, 20]
quick_sort([83, 4, 24, 2])                 # [2, 4, 24, 83]
quick_sort([4, 42, 16, 23, 15, 8])         # [4, 8, 15, 16, 23, 42]
quick_sort([87, 11, 23, 18, 18, 23, 11])   # [11, 11, 18, 18, 23, 23, 87]
```

---

## 🚀 Future Improvements

- [ ]  Try a different pivot strategy (e.g. median-of-three) to avoid worst-case O(n²) on sorted inputs
- [ ]  Benchmark against merge sort and Python's built-in `sorted()` on large lists
- [ ]  Implement an in-place version that sorts without creating new lists at each level
- [ ]  Add a step counter to track how many comparisons each pivot choice requires

---

## 📂 Project Structure
```
quick-sort/
│
├── QuickSortAlgorithm.py    # quick_sort function with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — completing the sorting algorithm trilogy alongside Merge Sort and Binary Search*
