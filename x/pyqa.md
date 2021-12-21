# Python Questions & Answers

Q: Must the values or keys of a dict be immutable?
A: The keys must be immutable, the values may be immutable.

---

Q: Does floating point arithmetic behave exactly like normal arithmetic on real numbers?
A: No, floating point provides only an approximation to real numbers.

---

Q: Will a bisection search run faster than linear search on all input?
A: No, It has a higher asymptotic complexity, but there can be inputs on which it will runmore slowly. Consider, for example, searching for an element that happens to the first element of the list.

---

Q: What does the following code print?

```python
T = (0.1, 0.1)
x = 0.0
for i in range(len(T)):
    for j in T:
        x += i+j
        print(x, end=' ')
print(i)
```

## A: 0.1 0.2 1.3 2.4 1

Q: What does the following code print?

```python
def f(s):
    if len(s) <= 1:
        return s
    return f(f(s[1:])) + s[0]

print(f('mat'), end=' ')
print(f('math'))
```

A: atm hatm

---
