#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : COMMAND LINE PARAMETERS PROCESSOR
#

import getopt
import os
import sys

cmd_help = f"""Python Console Database Browser

Specify database type using -d or --db_type")

Supported databases: sqlite, mysql, postres, oracle")

e.g. """+sys.argv[0]+""" -d sqlite <filename>")"""

def prn_cmd_help():
  for line in cmd_help.split('\n'):
    print(line)

def cmd_params(argv):
  dbfile = ""
  DB = None
  try:
    optlist, args = getopt.getopt(argv[1:], 'vhd:',['version','help','db_type'])
    for name, value in optlist:
      if name in ("-v","--version"):
        here = os.path.abspath(os.path.dirname(__file__))
        version_ns = {}  # type: ignore
        with open(os.path.join(here, "_version.py")) as f:
          exec(f.read(), {}, version_ns)
        print(f"pydbro {version_ns['__version__']}")
        exit(0)
      if name in ['-h', '--help']:
        prn_cmd_help()
        exit()
      elif name in ['-d', '--db_type']:
        DB = value
    if DB is None:
      prn_cmd_help()
      exit()
    if len(args) == 1 and DB == "sqlite":
      dbfile = args[0]
    return(DB,dbfile)
  except Exception as e:
    print("Error Message "+str(e))
    exit()

