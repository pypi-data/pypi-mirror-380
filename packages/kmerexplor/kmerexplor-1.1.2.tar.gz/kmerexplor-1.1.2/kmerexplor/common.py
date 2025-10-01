### Const

import os
import sys
import shutil

# ~ APPPATH = os.path.dirname(os.path.realpath(__file__))
# ~ DEFAULT_TAGSET = "human-quality"


# ~ def get_tags_file(args):
    # ~ """ Function doc """
    # ~ ### Find tags file
    # ~ ## --tags used to specify tags file
    # ~ if args.tags:
        # ~ tags_file = args.tags
    # ~ ## tags file specified from --builtin-tags option (default: human)
    # ~ else:
        # ~ tags_file = BUILTIN_TAGS[args.builtin_tags]
    # ~ ### Is tag file here ?
    # ~ if not os.path.isfile(tags_file):
        # ~ print("\n FileError: tags file '{}' not Found.\n".format(tags_file))
        # ~ sys.exit(exit_gracefully(args))
    # ~ return tags_file


def exit_gracefully(args, files_type=None):
    """ Function doc """
    ### In debug mode, do not remove temporary files.
    if args.debug:
        print("\n In debug mode, you should remove manually {} temp directory".format(args.tmp_dir))
    elif args.tmp_dir:
            shutil.rmtree(args.tmp_dir)
    ### With EOF, the program exit succesfully.
    if  args.debug: print("EOF")
