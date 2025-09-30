import random
import numpy as np
from ase.build import bulk, make_supercell


def get_reference_structures(frac=1.0, supercell=1):
    fcc = bulk("Cu", "fcc", a=frac * 3.58)
    bcc = bulk("Cu", "bcc", a=frac * 2.84)
    hcp = bulk("Cu", "hcp", a=frac * 2.53)

    if supercell > 1:
        fcc = make_supercell(fcc, np.eye(3) * supercell)
        bcc = make_supercell(bcc, np.eye(3) * supercell)
        hcp = make_supercell(hcp, np.eye(3) * supercell)

    return fcc, bcc, hcp


def get_noisy_structures(frac=1.0, noise=0.05, supercell_size=6):
    fcc, bcc, hcp = get_reference_structures(frac=frac)

    sfcc = make_supercell(fcc, supercell_size * np.eye(3))
    sbcc = make_supercell(bcc, supercell_size * np.eye(3))
    shcp = make_supercell(hcp, supercell_size * np.eye(3))

    sfcc.translate(noise * np.random.randn(len(sfcc), 3))
    sbcc.translate(noise * np.random.randn(len(sbcc), 3))
    shcp.translate(noise * np.random.randn(len(shcp), 3))

    return sfcc, sbcc, shcp


def get_multicomponent_structures(frac=1.0, supercell=1, ratio=0.5, seed: int = None):
    fcc = bulk("Au", "fcc", a=frac * 4.08)
    bcc = bulk("Au", "bcc", a=frac * 3.31)
    hcp = bulk("Au", "hcp", a=frac * 2.88)

    if supercell > 1:
        fcc = make_supercell(fcc, np.eye(3) * supercell)
        bcc = make_supercell(bcc, np.eye(3) * supercell)
        hcp = make_supercell(hcp, np.eye(3) * supercell)

    if seed is not None:
        random.seed(seed)

    for struct in [fcc, bcc, hcp]:
        indices = list(range(len(struct)))
        selected = random.sample(indices, k=int(ratio * len(struct)))
        for i in selected:
            struct[i].symbol = "Ag"

    return fcc, bcc, hcp
