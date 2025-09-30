import random
import pytest
import torch

from tqdm import tqdm
import jax.numpy as jnp

import klay
from klay.utils import generate_random_dimacs, eval_pysdd, eval_d4_torch_naive
from klay.compile import compile_sdd #, compile_d4


def check_sdd_torch(sdd, weights):
    wmc_gt = eval_pysdd(sdd, weights)

    klay_weights = jnp.log(jnp.array(weights))
    circuit = klay.Circuit()
    circuit.add_sdd(sdd)
    kl = circuit.to_jax_function()
    result = float(kl(klay_weights).item())
    assert wmc_gt == pytest.approx(result, abs=1e-4), f"Expected {wmc_gt}, got {result}"


def check_d4_torch(nnf_file, weights):
    wmc_gt = eval_d4_torch_naive(nnf_file, torch.tensor(weights).log())

    klay_weights = jnp.log(jnp.array(weights))
    circuit = klay.Circuit()
    circuit.add_d4_from_file(nnf_file)
    kl = circuit.to_jax_function()
    result = float(kl(klay_weights).item())
    assert wmc_gt == pytest.approx(result, abs=1e-4), f"Expected {wmc_gt}, got {result}"


def fuzzer(nb_trials, nb_vars):
    for i in tqdm(range(nb_trials)):
        generate_random_dimacs('tmp.cnf', nb_vars, nb_vars//2, seed=i)
        weights = [random.random() for _ in range(nb_vars)]

        sdd = compile_sdd('tmp.cnf')
        check_sdd_torch(sdd, weights)

        # compile_d4('tmp.cnf', 'tmp.nnf')
        # check_d4_torch("tmp.nnf", weights)


if __name__ == "__main__":
    nb_trails = 50
    nb_vars = 50
    print("Running Fuzz Tester on 3-CNFs")
    print("Number of Trials:", nb_trails)
    print("Number of Variables:", nb_vars)
    fuzzer(nb_trails, nb_vars)