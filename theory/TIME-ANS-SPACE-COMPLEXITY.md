## <u>Big O Notation Growth Hierarchy</u>

### TIME COMPLEXITY

1. **Count the iterations.**
2. **Remove all constants.**
   > * $N$ and $N \log N$ are **not** constants.
   > * $65,765$ are constants.
   > * $2N + 100$ — we can remove $2$ and $100$ as they are constants.
   > * **Do not** remove exponents (like the square in $\mathcal{O}(N^2)$) or bases (like base $2$ in $\log_2 N$).

3. **Keep only the most dominating term / remove lower-order terms.**
   * *Example:* $N + N^2 + N \log_2 N$ — among these, $N$ and $N \log_2 N$ are smaller, so we are left with $\mathcal{O}(N^2)$.

---

$$
\mathcal{O}(1) \quad \rightarrow \quad \mathcal{O}(\log_2 N) \quad \rightarrow \quad \mathcal{O}(\sqrt{N}) \quad \rightarrow \quad \mathcal{O}(N) \\
\rightarrow \quad \mathcal{O}(N \log_2 N) \quad \rightarrow \quad \mathcal{O}(N\sqrt{N}) \quad \rightarrow \quad \mathcal{O}(N^2) \quad \rightarrow \quad \mathcal{O}(N^3) \quad \rightarrow \quad \mathcal{O}(2^N)
$$


### <u>Space Complexity</u>

**How much memory/space is utilized at the peak point of execution.**

* **Definition:** Measures the total amount of computer memory (RAM) an algorithm requires relative to the input size ($N$).

* **Auxiliary Space:** The extra or temporary space used by the algorithm *excluding* the input storage itself.