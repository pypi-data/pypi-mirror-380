import code

from mesomath.__about__ import __version__ as VERSION

from mesomath.babn import BabN as bn
from mesomath.npvs import Blen as bl
from mesomath.npvs import Bsur as bs
from mesomath.npvs import Bvol as bv
from mesomath.npvs import Bcap as bc
from mesomath.npvs import Bwei as bw
from mesomath.npvs import BsyG as bG
from mesomath.npvs import BsyS as bS
from mesomath.npvs import Bbri as bb

message = f"""\nWelcome to Babylonian Calculator {VERSION}
    ...the calculator that every scribe should have!

Use: bn(number) for sexagesimal calculations
Metrological classes: bl, bs, bv, bc, bw, bG, bS and bb loaded.

jccsvq fecit, 2025."""


def main():
    """Entry point for babcalc"""

    local_vars = globals().copy()  # Start with all global variables
    local_vars.update(locals())  # Add all local variables at this point

    code.interact(
        banner=message,
        local=local_vars,
        exitmsg="\n--- Exiting Babylonian Calculator, Bye! ---\n",
    )


if __name__ == "__main__":
    main()
