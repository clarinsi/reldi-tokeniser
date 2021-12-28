# reldi-tokeniser

A tokeniser developed inside the [ReLDI project](https://reldi.spur.uzh.ch). Supports currently five languages -- Slovene, Croatian, Serbian, Macedonian and Bulgarian, and two modes -- standard and non-standard text.

## Usage

### Command line
```
$ echo 'kaj sad s tim.daj se nasmij ^_^.' | ./tokeniser.py hr -n
1.1.1.1-3	kaj
1.1.2.5-7	sad
1.1.3.9-9	s
1.1.4.11-13	tim
1.1.5.14-14	.

1.2.1.15-17	daj
1.2.2.19-20	se
1.2.3.22-27	nasmij
1.2.4.29-31	^_^
1.2.5.32-32	.


```

Language is a positional argument while tokenisation of non-standard text, tagging and lemmatization of symbols and punctuation, and diferent output formats are an optional one.

```
$ python tokeniser.py -h
usage: tokeniser.py [-h] [-c] [-b] [-d] [-n] [-t] {sl,hr,sr,mk,bg}

Tokeniser for (non-)standard Slovene, Croatian, Serbian, Macedonian and
Bulgarian

positional arguments:
  {sl,hr,sr,mk,bg}   language of the text

optional arguments:
  -h, --help         show this help message and exit
  -c, --conllu       generates CONLLU output
  -b, --bert         generates BERT-compatible output
  -d, --document     passes through ConLL-U-style document boundaries
  -n, --nonstandard  invokes the non-standard mode
  -t, --tag          adds tags and lemmas to punctuations and symbols
```

### Python module
```python
# string mode
import reldi_tokeniser

text = 'kaj sad s tim.daj se nasmij ^_^.'

output = reldi_tokeniser.run(text, 'hr', nonstandard=True, tag=True)

# object mode
from reldi_tokeniser.tokeniser import ReldiTokeniser

reldi = ReldiTokeniser('hr', conllu=True, nonstandard=True, tag=True)
list_of_lines = [el + '\n' for el in text.split('\n')]
test = reldi.run(list_of_lines, mode='object')
```

Python module has two mandatory parameters - text and language. Other optional parameters are `conllu`, `bert`, `document`, `nonstandard` and `tag`.

## CoNLL-U output

This tokeniser outputs also CoNLL-U format (flag `-c`/`--conllu`). If the additional ```-d```/```--document``` flag is given, the tokeniser passes through lines starting with ```# newdoc id =``` to preserve document structure.

```
$ echo '# newdoc id = prvi
kaj sad s tim.daj se nasmij ^_^.
haha
# newdoc id = gidru
štaš' | ./tokeniser.py hr -n -c -d
# newdoc id = prvi
# newpar id = 1
# sent_id = 1.1
# text = kaj sad s tim.
1	kaj	_	_	_	_	_	_	_	_
2	sad	_	_	_	_	_	_	_	_
3	s	_	_	_	_	_	_	_	_
4	tim	_	_	_	_	_	_	_	SpaceAfter=No
5	.	_	_	_	_	_	_	_	SpaceAfter=No

# sent_id = 1.2
# text = daj se nasmij ^_^.
1	daj	_	_	_	_	_	_	_	_
2	se	_	_	_	_	_	_	_	_
3	nasmij	_	_	_	_	_	_	_	_
4	^_^	_	_	_	_	_	_	_	SpaceAfter=No
5	.	_	_	_	_	_	_	_	_

# newpar id = 2
# sent_id = 2.1
# text = haha
1	haha	_	_	_	_	_	_	_	_

# newdoc id = gidru
# newpar id = 1
# sent_id = 1.1
# text = štaš
1	štaš	_	_	_	_	_	_	_	_

```
## Pre-tagging

The tokeniser can also pre-annotate text on the part-of-speech (UPOS and XPOS) and lemma level (flag `-t` or `--tag`), if the available tokenisation regexes have sufficient evidence (punctuations, mentions, hashtags, URL-s, e-mails, emoticons, emojis). Default output format in case of pre-tagging is CoNLL-U.

```
$ echo -e "kaj sad s tim.daj se nasmij ^_^. haha" | python tokeniser.py hr -n -t
# newpar id = 1
# sent_id = 1.1
# text = kaj sad s tim.
1	kaj	_	_	_	_	_	_	_	_
2	sad	_	_	_	_	_	_	_	_
3	s	_	_	_	_	_	_	_	_
4	tim	_	_	_	_	_	_	_	SpaceAfter=No
5	.	.	PUNCT	Z	_	_	_	_	SpaceAfter=No

# sent_id = 1.2
# text = daj se nasmij ^_^.
1	daj	_	_	_	_	_	_	_	_
2	se	_	_	_	_	_	_	_	_
3	nasmij	_	_	_	_	_	_	_	_
4	^_^	^_^	SYM	Xe	_	_	_	_	SpaceAfter=No
5	.	.	PUNCT	Z	_	_	_	_	_

# sent_id = 1.3
# text = haha
1	haha	_	_	_	_	_	_	_	_

```
