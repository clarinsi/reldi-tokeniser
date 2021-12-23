#!/usr/bin/python
#-*-encoding:utf-8-*-
import re
import codecs
import sys
import threading
import unicodedata
from reldi_tokeniser.tokeniser import ReldiTokeniser

if sys.platform == 'win32':
  from signal import signal, SIG_DFL
else:
  from signal import signal, SIGPIPE, SIG_DFL

if sys.platform != 'win32':
    if threading.current_thread() is threading.main_thread():
        signal(SIGPIPE, SIG_DFL)

if __name__=='__main__':
  import argparse
  parser=argparse.ArgumentParser(description='Tokeniser for (non-)standard Slovene, Croatian, Serbian, Macedonian and Bulgarian')
  parser.add_argument('lang',help='language of the text',choices=['sl','hr','sr','mk','bg'])
  parser.add_argument('-c','--conllu',help='generates CONLLU output',action='store_true')
  parser.add_argument('-b','--bert',help='generates BERT-compatible output',action='store_true')
  parser.add_argument('-d','--document',help='passes through ConLL-U-style document boundaries',action='store_true')
  parser.add_argument('-n','--nonstandard',help='invokes the non-standard mode',action='store_true')
  parser.add_argument('-t','--tag',help='adds tags and lemmas to punctuations and symbols',action='store_true')
  args=parser.parse_args()

  if args.document:
    args.conllu=True
  if args.tag:
    args.conllu=True
  reldi = ReldiTokeniser(args.__dict__)
  output = sys.stdout
  reldi.run(sys.stdin, output)
