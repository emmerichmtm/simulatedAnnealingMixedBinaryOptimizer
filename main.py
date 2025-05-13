import numpy as np
import matplotlib.pyplot as plt

# ---------- custom objective -------------------------------------------------
def objective(x):
    # x = [x0, x1, b0, b1]   (last two are 0/1)
    x0, x1, b0, b1 = x
    # Rosenbrock part (continuous)
    f_cont = (1 - x0) ** 2 + 100 * (x1 - x0 ** 2) ** 2
    # Penalty: want exactly ONE binary variable equal to 1
    penalty = 7 * abs((b0 + b1) - 1)
    return f_cont + penalty
# -----------------------------------------------------------------------------

def simulated_annealing(objective, bounds, var_types,
                        n_iterations, step_size, temp, init):
    best = init.copy()
    best_eval = objective(best)
    curr, curr_eval = best.copy(), best_eval
    history = [curr_eval]

    for i in range(1, n_iterations + 1):
        candidate = curr.copy()

        # Propose a move dimension-wise
        for k, vtype in enumerate(var_types):
            if vtype == "continuous":
                rng = bounds[k][1] - bounds[k][0]
                candidate[k] += np.random.randn() * step_size * rng
                candidate[k] = np.clip(candidate[k], bounds[k][0], bounds[k][1])
            else:                                   # binary flip
                if np.random.rand() < 0.25:
                    candidate[k] = 1 - candidate[k]

        cand_eval = objective(candidate)

        # Record global best
        if cand_eval < best_eval:
            best, best_eval = candidate.copy(), cand_eval

        # Metropolis acceptance
        diff = cand_eval - curr_eval
        T = temp / float(i)
        if diff < 0 or np.random.rand() < np.exp(-diff / T):
            curr, curr_eval = candidate.copy(), cand_eval

        history.append(curr_eval)

    return best, best_eval, history


# ------------- problem definition -------------------------------------------
var_types = ["continuous", "continuous", "binary", "binary"]
bounds    = np.array([[-2, 2],       # x0
                      [-1, 3],       # x1
                      [0, 1],        # b0
                      [0, 1]])       # b1
init      = np.array([0.5, 0.5, 0, 1], dtype=float)

# hyper-parameters
n_iter   = 800
step     = 0.25
temp0    = 8.0
# -----------------------------------------------------------------------------

best, best_val, hist = simulated_annealing(objective, bounds, var_types,
                                           n_iter, step, temp0, init)

# ------------- outputs -------------------------------------------------------
print("Best vector found:", best)
print("Objective value :", best_val)

# Convergence curve
plt.plot(hist)
plt.xlabel("Iteration"); plt.ylabel("Objective")
plt.title("SA Convergence – custom objective")
plt.tight_layout(); plt.show()

# Save artefacts if desired
# np.savetxt("optimum.txt", best, fmt="%.6f")
# plt.savefig("convergence.png", dpi=150)
