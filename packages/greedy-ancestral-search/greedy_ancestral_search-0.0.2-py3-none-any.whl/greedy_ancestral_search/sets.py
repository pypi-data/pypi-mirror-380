import itertools
import logging
from typing import Callable

import networkx as nx

from . import utils

logger = logging.getLogger(__name__)


def compute_d(
    prefix_set: set[int],
    downstream_set: set[int],
    ci_tester: Callable,
    cond_set_size: int,
    G: nx.Graph,
    sep_sets: dict[frozenset[int], set[int]],
) -> set[int]:
    assert prefix_set & downstream_set == set()

    pairs = itertools.chain(
        itertools.product(prefix_set, downstream_set),
        itertools.combinations(downstream_set, 2),
    )
    d_set = set()
    found = []

    # find v-structures
    for u, v in pairs:
        if G.has_edge(u, v):
            continue

        sep_set = sep_sets[frozenset((u, v))] - prefix_set
        if not len(sep_set) == cond_set_size:
            continue

        for w in downstream_set & set(G[u]) & set(G[v]):
            if w in sep_set or w in d_set:
                continue

            if ci_tester(u, v, prefix_set - {u} | sep_set | {w}):
                continue

            d_set.add(w)
            logger.debug(f"Found v-structure {u} -> {w} <- {v}")

            found.append((u, v, w, sep_set))

    # find descendants
    for u, v, w, sep_set in found:
        nodes = utils.connected_nodes(G, {w}, downstream_set - d_set - sep_set - {v, u})
        for node in nodes:
            if ci_tester(u, v, prefix_set - {u} | sep_set | {node}):
                continue
            d_set.add(node)
            logger.debug(f"Found v-structure descendant {node}")

    return d_set


def compute_f(
    prefix_set: set[int],
    downstream_set: set[int],
    cond_set_size: int,
    G: nx.Graph,
    sep_sets: dict[frozenset[int], set[int]],
) -> set[int]:
    assert prefix_set & downstream_set == set()

    f_set = set()

    for u, v in itertools.product(prefix_set, downstream_set):
        if G.has_edge(u, v) or v in f_set:
            continue

        if not len(sep_sets[frozenset((u, v))] - prefix_set) == cond_set_size:
            continue

        f_set.add(v)
        logger.debug(f"Found M1 {v}")

    return f_set
