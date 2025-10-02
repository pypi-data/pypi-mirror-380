import os
import sys

from shapes.basics.input import InputParser
from shapes.basics.utils import Generator, LogListener, configure_logging
from shapes.basics.options import Options, OptionsSerDes


def main(argv: list[str] = sys.argv):

    logger = configure_logging()

    options = Options()
    inpPars = InputParser()
    listener = LogListener()
    options.shape.add_listener(listener)
    options.molecule.add_listener(listener)

    try:
        options = inpPars.parseCLI(argv, options)
        listener = LogListener()
        options.molecule.add_listener(listener)
    except Exception as e:
        logger.exception(e)
        logger.error("FULL STOP!!!")
        logger.error(f"Try '{os.path.basename(argv[0])} --help'\n")
        sys.exit(1)

    try:
        gen = Generator(options)
        OptionsSerDes.dump_validated_yaml(options)
        gen.generate_smiles()
        gen.dump_file()

    except Exception as e:
        logger.exception(e)
        sys.exit(2)

if __name__ == "__main__":
    main()
