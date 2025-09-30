#!/usr/bin/env python3
#
##################################################################################
#
#     Title : pgschema
#    Author : Zaihua Ji, zji@ucar.edu
#      Date : 2025-09-27
#   Purpose : copy tables of a schema to teh same schema name in a different database
#             on the same server
#
#    Github : https://github.com/NCAR/rda-python-dbms.git
#
##################################################################################

import sys
import os
import re
from os import path as op
from time import time as tm
from rda_python_common import PgLOG
from rda_python_common import PgDBI
from rda_python_common import PgSIG
from rda_python_common import PgUtil

PVALS = {
   'db' : 'rdadb',
   'nd' : None,
   'sc' : None,
   'us' : None,
   'ht' : 'rda-db.ucar.edu',
   'mp' : 16,      # number of concurrent processes (one for a table at a time)
   'pn' : 5432,
   'tb' : []
}

#
# main function to run dsarch
#
def main():

   argv = sys.argv[1:]
   opt = None
   for arg in argv:
      if re.match(r'-(\w+)$', arg):
         opt = arg[1:]
         if opt == "b":
            PgLOG.PGLOG['BCKGRND'] = 1
            opt = None
         elif opt not in PVALS:
            PgLOG.pglog(arg + ": Invalid Option", PgLOG.LGWNEX)
      elif opt:
         if isinstance(PVALS[opt], list):
            PVALS[opt].append(arg)
         elif isinstance(PVALS[opt], int):
            PVALS[opt] = int(arg)
            opt = None
         else:
            PVALS[opt] = arg
            opt = None
      else:
         PgLOG.pglog(arg + ": parameter misses leading option", PgLOG.LGWNEX)
   
   PgLOG.PGLOG['LOGFILE'] = "pgschema.log"
   sc = PVALS['sc']

   if not sc:
      print("Dump all or specified tables in a Schema in the current directory; Restore")
      print("Restore the dumped schema to a different Database with the same schema name.")
      print("Existing Schema and tables in the target database will not be overriden.")
      print("Usage:\npgschema [-b] [-m PMAX] [-ht HOSTNAME] [-db DATABASE] -sc SCHEMA  \\")
      print("      [-nd NEWDATABASE] [-us USERNAME] [-tb TABLES] [-pn PORTNO]")
      print("  Option -tb - specify the table names, use wildcard '*' to match mutiple tables")
      print("  Option -ht - host name of database server is running on; default to 'rda-db.ucar.edu'")
      print("  Option -sc - the schema for tables to be transferred from")
      print("  Option -db - the database name, default to 'rdadb'")
      print("  Option -nd - the new database for schema to be transferred to; defaults to <DATABASE>_test")
      print("  Option -us - specify the user name, default to -sc")
      print("  Option -pn - the port number to connect to database, default to 5432")
      print("  Option -mp - the number of processes to dump/restore schema; default to 16")
      print("NOTE: To transfer schema, set both database password entries in file .pgpass")
      print("      under your home directory as HOSTNAME:5432:DATABASE:USERNAME:password.")
      print("For Example to transfer schema wagtail in Dababase rdadb to Database rdadb_test:")
      print("      rda-db.ucar.edu:5432:rdadb:wagtail:<WagtailPassword>")
      print("      rda-db.ucar.edu:5432:rdadb_test:wagtail:<WagtailPassword>")
      sys.exit(0)

   if not PVALS['us']: PVALS['us'] = sc
   if not PVALS['nd']: PVALS['nd'] = f"{PVALS['db']}_test"
   if PVALS['nd'] == PVALS['db']:
      PgLOG.pglog(f"Must transfer schema {sc} to a Database other than {PVALS['db']}", PgLOG.LGWNEX)

   PgLOG.cmdlog("pgschema {}".format(' '.join(argv)))
   PVALS['pgsc'] = PgDBI.pgname(sc)
   transfer_schema(sc, PVALS['tb'])
   PgLOG.cmdlog()
   sys.exit(0)

#
# transfer a whole schema from one database to another
#
def transfer_schema(sc, tables):

   pgsc = PVALS['pgsc']
   db = PVALS['db']
   nd = PVALS['nd']

   tstr = get_table_options(tables)
   # dump schema
   dumpdir = "{}_dump_{}".format(sc, PgUtil.curdate())
   if pgsc != sc: pgsc = "'{}'".format(pgsc)
   cmd = f"pg_dump {db} -h {PVALS['ht']} -n {sc}{tstr} -U {PVALS['us']} -w -Fd -j {PVALS['mp']} -f {dumpdir}/"
   if op.exists(dumpdir):
      PgLOG.pglog(dumpdir + ": Dump directory exists, remove it before running pgschema", PgLOG.LGEREX)
   if not PgLOG.pgsystem(cmd, PgLOG.LOGWRN, 5):   # 4 + 1
      PgLOG.pglog("{db}.{sc}: Error dumping schema", PgLOG.LGEREX)

   # restore schema
   cmd = f"pg_restore -d {nd} -h {PVALS['ht']} -n {sc}{tstr} -U {PVALS['us']} -w -j {PVALS['mp']} -Fd {dumpdir}"
   if not PgLOG.pgsystem(cmd, PgLOG.LOGWRN, 5):
      PgLOG.pglog("{db}.{sc}: Error restoring schema", PgLOG.LGEREX)

def get_table_options(tables):

   tstr = ''
   for tb in tables: tstr += " -t {}".format(PgDBI.pgname(tb))
   
   return tstr

#
# call main() to start program
#
if __name__ == "__main__": main()
