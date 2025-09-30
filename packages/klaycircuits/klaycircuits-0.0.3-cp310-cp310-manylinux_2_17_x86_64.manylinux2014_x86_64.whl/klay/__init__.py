# noinspection PyUnresolvedReferences
from .nanobind_ext import Circuit, NodePtr
NodePtr.__module__ = "klay"

from collections.abc import Sequence


def to_torch_module(self: Circuit, semiring: str = "log", probabilistic: bool = False):
    """
    Convert the circuit into a PyTorch module.

    :param semiring:
        The semiring in which the circuit should be evaluated. Supported options are ("log", "real", "mpe", "godel").
    :param probabilistic:
        If true, construct a probabilistic circuit instead of an arithmetic circuit.
        This means the inputs to a sum node are multiplied by a probability, and
        we can interpret sum nodes as latent Categorical variables.
    """
    from .torch import KnowledgeModule
    indices = self._get_indices()
    return KnowledgeModule(*indices, semiring=semiring, probabilistic=probabilistic)


def to_jax_function(self: Circuit, semiring: str = "log"):
    """
    Convert the circuit into a Jax function.

    :param semiring:
        The semiring in which the circuit should be evaluated. Supported options are ("log", "real", "mpe", "godel").
    """
    from .jax import create_knowledge_layer
    indices = self._get_indices()
    return create_knowledge_layer(*indices, semiring=semiring)


def add_sdd(self: Circuit, sdd: "SddNode", true_lits: Sequence[int] = (), false_lits: Sequence[int] = ()):
    """
    Add an SDD to the Circuit.

    :param true_lits:
        List of literals that are always true and should get propagated away.
    :param false_lits:
        List of literals that are always false and should get propagated away.
    """
    import os
    from pathlib import Path

    sdd.save(bytes(Path("tmp.sdd")))
    self.add_sdd_from_file("tmp.sdd", true_lits, false_lits)
    os.remove("tmp.sdd")


Circuit.to_torch_module = to_torch_module
Circuit.to_jax_function = to_jax_function
Circuit.add_sdd = add_sdd
