# Mixed‑Variable Simulated Annealing Optimizer

Python reference implementation of **simulated annealing (SA)** that can tackle decision vectors containing **both continuous and binary variables**.  The repository ships with two ready‑to‑run examples:

1. **Sum‑of‑Squares minimisation** – a simple benchmark.
2. **Rosenbrock + binary‑penalty** – illustrates how to blend a classical continuous test‑function with discrete logic constraints.

The core SA engine stays the same; you only swap in your own `objective()` definition.

---

## Features

* **Mixed variable types** – flag each dimension as `"continuous"` or `"binary"`.
* **Easy objective plug‑in** – any Python callable that returns a scalar.
* **No gradients required** – works on non‑smooth, non‑convex landscapes.
* **Auto‑generated artefacts**

  * `convergence.png` – objective value vs. iteration.
  * `optimum.txt` – best vector (ASCII, one value / row).
* Clean, dependency‑light code (≈ 80 LOC for engine + example script).

---

## Quick‑Start (5 min)

```bash
# 1 . clone (or drop the files somewhere)
$ git clone https://github.com/your‑handle/sa‑mixed.git
$ cd sa‑mixed

# 2 . create an isolated environment (optional but recommended)
$ python -m venv .venv
$ source .venv/bin/activate  # on Windows use .venv\Scripts\activate

# 3 . install runtime deps (numpy & matplotlib only)
$ pip install -r requirements.txt

# 4 . run a demo
$ python sa_mixed.py
```

After \~1 s you’ll see a convergence plot and two new files:

```text
./convergence.png   # 800‑step SA trace
./optimum.txt       # best vector found
```

---

## File Structure

```text
sa‑mixed/
├── sa_engine.py       # the generic SA routine (imported by all examples)
├── examples/
│   ├── sa_sumSquares.py   # minimal 4‑var demo (2 cont + 2 bin)
│   └── sa_rosenbrock.py   # Rosenbrock + binary penalty example
├── convergence.png    # produced after running a script
├── optimum.txt        # produced after running a script
└── README.md          # (this file)
```

> **Note**:  The example scripts write artefacts to the project root. Feel free to redirect paths.

---

## Customising the Optimiser

1. **Define your search space**

   ```python
   var_types = ["continuous", "binary", "continuous", ...]
   bounds    = np.array([[-5, 5], [0, 1], [‑3, 3], ...])
   init      = np.array([ 1.2 ,   0  ,  -0.7 , ...])
   ```
2. **Write an objective**

   ```python
   def objective(x: np.ndarray) -> float:
       # x is the full mixed vector – use it however you like
       return some_scalar
   ```
3. **Tune hyper‑parameters** (`n_iterations`, `step_size`, `temp`).

That’s it – call `simulated_annealing()`.

---

## Hyper‑Parameter Cheat‑Sheet

| Symbol         | Meaning                            | Typical range |
| -------------- | ---------------------------------- | ------------- |
| `n_iterations` | Search length                      | 10² – 10⁴     |
| `step_size`    | Proposal scale (fraction of range) | 0.1 – 0.5     |
| `temp`         | Initial temperature                | 5 – 30        |

Lower `step_size` → finer search but slower coverage.  Increase `temp` if the run gets stuck early.

---

## Requirements

* Python 3.8+
* numpy
* matplotlib
  *(all installable via `pip install -r requirements.txt`)*

---

## License

MIT – do whatever you like, but no warranty.  See `LICENSE` for details.

---

## Citing or Learning More

If you use this template in academic work, please acknowledge with a short citation to this repository.  For background on simulated annealing consult:

* Kirkpatrick et al., “Optimization by Simulated Annealing”, *Science*, 1983.
* Černý, “Thermodynamical Approach to the Traveling Salesman Problem”, 1985.

Happy optimization! 🎉
