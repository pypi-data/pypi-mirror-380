"""
Example 05: Recurrent Time Series Prediction

This example demonstrates how to evolve a recurrent neural network (EvoNet) 
to predict future values in a time series. The task is defined as:

    Predict x[t + PRED_LEN] given x[t]

Key aspects:
- The network receives a warmup phase (WARMUP_STEPS) to stabilize its state.
- Fitness is measured as mean squared error (MSE) between predicted and actual values.
- Multiple evaluation runs (EVAL_RUNS) with different seeds are averaged 
  to improve robustness.
- During training, intermediate predictions are visualized and saved as frames.
- After evolution, the best network is tested on a new time series 
  (generalization test).
"""

import numpy as np

from evolib import (
    Population,
    Individual,
    plot_approximation,
    generate_timeseries,
    resume_or_create,
    save_checkpoint,
    resume_from_checkpoint,
)

# Parameters
PATTERN = "trend_switch"
SEQ_LEN = 300
PRED_LEN = 7
WARMUP_STEPS = max(PRED_LEN, 20)
EVAL_RUNS = 10

FRAME_FOLDER = "05_frames"
CONFIG_FILE = "./configs/05_recurrent_timeseries.yaml"

FULL_SEQ = generate_timeseries(SEQ_LEN + PRED_LEN, pattern=PATTERN)
INPUT_SEQ = FULL_SEQ[:-PRED_LEN]
TARGET_SEQ = FULL_SEQ[PRED_LEN:]


def gen_y_pred(
    indiv: Individual, input_seq: list[float], module: str = "brain"
) -> list[float]:

    """
    Generate predictions for x[t+PRED_LEN] from x[t] using the individual's network.

    Args:
        indiv: Individual containing the network.
        input_seq: Input time series (length = N).
        module: Which module to use from the individual's para (default: "brain").

    Returns:
        List of predictions aligned with target_seq[WARMUP_STEPS:].
    """

    net = indiv.para[module].net
    net.reset(full=True)

    # Warmup phase
    for time_step in range(WARMUP_STEPS):
        net.calc([input_seq[time_step]])

    # Prediction of x[time_step + PRED_LEN] from x[time_step]
    preds = []
    for time_step in range(WARMUP_STEPS, len(input_seq)):
        y_pred = net.calc([input_seq[time_step]])[0]
        preds.append(y_pred)

    return preds


# Fitness: MSE between predicted and actual
def eval_timeseries_fitness(indiv: Individual) -> float:

    total_mse = 0
    for _ in range(EVAL_RUNS):
        seed = np.random.randint(0, 2**32 - 1)
        full_seq = generate_timeseries(SEQ_LEN + PRED_LEN, pattern=PATTERN, seed=seed)
        input_seq = full_seq[:-PRED_LEN]
        target_seq = full_seq[PRED_LEN:]

        # Prediction of x[time_step + PRED_LEN] from x[time_step]
        preds = gen_y_pred(indiv, input_seq)

        y_true = target_seq[WARMUP_STEPS:]
        preds = np.array(preds)
        total_mse += np.mean((preds - y_true) ** 2)

    mse = total_mse / EVAL_RUNS

    indiv.fitness = mse
    indiv.extra_metrics["mse"] = mse
    return indiv.fitness


def checkpoint(pop: Population) -> None:
    save_checkpoint(pop, run_name="05_recurrent_timeseries")


# Visualization + Checkpoint
def on_generation_end(pop: Population) -> None:

    checkpoint(pop)

    best = pop.best()

    print(
        f"[Gen {pop.generation_num}] best fitness={best.fitness:.5f}, "
        f"ms: {best.para['brain'].evo_params.mutation_strength:.5f}"
    )

    preds = gen_y_pred(best, INPUT_SEQ)

    plot_approximation(
        preds,
        TARGET_SEQ[WARMUP_STEPS:],
        title=(
            f"Prediction of x[t+{PRED_LEN}] from x[t] Testpattern\n"
            f"MSE={best.fitness:.4f}"
        ),
        pred_label="Prediction",
        show=False,
        show_grid=False,
        save_path=f"{FRAME_FOLDER}/gen_{pop.generation_num:03d}.png",
    )


# Main loop
def main() -> None:
    print(
        "[Start] Depending on the configuration and available resources, this will take"
        "some time ..."
    )
    pop = resume_or_create(
        CONFIG_FILE,
        fitness_fn=eval_timeseries_fitness,
        run_name="05_recurrent_timeseries",
    )

    pop.run(verbosity=0, on_generation_end=on_generation_end)

    best = pop.best()
    net = best.para["brain"].net
    net.print_graph(
        name="05_recurrent_timeseries",
        engine="dot",
        thickness_on=True,
        fillcolors_on=True,
    )

    # Generalization Test- New series with same Pattern but different seed
    test_seq = generate_timeseries(len(INPUT_SEQ) + PRED_LEN, pattern=PATTERN, seed=219)
    test_input = test_seq[:-PRED_LEN]
    test_target = test_seq[PRED_LEN:]

    preds = gen_y_pred(best, test_input)

    test_target = test_target[WARMUP_STEPS:]

    plot_approximation(
        preds,
        test_target,
        title=f"Generalization Test (new series, seed=219, " f"pattern={PATTERN})",
        show=False,
        save_path=f"{FRAME_FOLDER}/00_Generalization_Test.png",
    )


if __name__ == "__main__":
    main()
