// ...existing code...
# Collatz sequence (3n + 1 problem)

A small interactive script that prints the Collatz sequence for a given starting integer until it reaches 1. The implementation is in [`collatz_sequency.py`](Collatz%20sequence/collatz_sequency.py).

The Collatz iteration is:

$$
f(n)=\begin{cases}
\frac{n}{2} & \text{if } n\equiv 0\pmod{2},\\[6pt]
3n+1 & \text{if } n\equiv 1\pmod{2}.
\end{cases}
$$

In inline form: $3n+1$ for odd $n$, otherwise $n/2$.

## Usage

Run the script and enter a positive integer (or type `QUIT` to exit):

```bash
python