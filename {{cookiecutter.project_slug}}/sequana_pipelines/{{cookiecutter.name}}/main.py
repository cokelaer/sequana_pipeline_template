import sys
import os
import argparse

from sequana_pipetools.options import *
from sequana_pipetools.misc import Colors

col = Colors()

NAME = "{{cookiecutter.name}}"


class Options(argparse.ArgumentParser):
    def __init__(self, prog=NAME, epilog=None):
        usage = col.purple(sequana_prolog.format(**{"name": NAME}))
        super(Options, self).__init__(usage=usage, prog=prog, description="",
            epilog=epilog,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

        # add a new group of options to the parser
        so = SlurmOptions()
        so.add_options(self)

        # add a snakemake group of options to the parser
        so = SnakemakeOptions(working_directory=NAME)
        so.add_options(self)

        so = InputOptions()
        so.add_options(self)

        so = GeneralOptions()
        so.add_options(self)

        pipeline_group = self.add_argument_group("pipeline")

        pipeline_group.add_argument("--TODO", dest="TODO", default=4, type=int)


def main(args=None):

    if args is None:
        args = sys.argv

    if "--version" in sys.argv:
        from sequana_pipetools.misc import print_version
        print_version(NAME)
        sys.exit(0)

    # whatever needs to be called by all pipeline before the options parsing
    init_pipeline(NAME)

    # option parsing including common epilog
    options = Options(NAME, epilog=sequana_epilog).parse_args(args[1:])

    from sequana.snaketools import Module
    m = Module(NAME)
    m.is_executable()

    from sequana import logger
    logger.level = "INFO"
    # the real stuff is here
    manager = PipelineManager(options, NAME)

    # create the beginning of the command and the working directory
    manager.setup()

    # fill the config file with input parameters
    cfg = manager.config.config
    # EXAMPLE TOREPLACE WITH YOUR NEEDS
    cfg.input_directory = os.path.abspath(options.input_directory)
    cfg.input_pattern = options.input_pattern

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown()


if __name__ == "__main__":
    main()
