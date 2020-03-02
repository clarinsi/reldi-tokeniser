# reldi-tokeniser

A tokeniser developed inside the [ReLDI project](https://reldi.spur.uzh.ch). Supports currently five languages -- Slovene, Croatian, Serbian, Macedonian and Bulgarian, and two modes -- standard and non-standard text.

## Usage

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

Language is a positional argument while tokenisation of non-standard text is an optional one.

## CoNLL-U output

This tokeniser is also an input point to the new neural pipeline for processing South Slavic languages (classla-stanfordnlp)[https://github.com/clarinsi/classla-stanfordnlp], requiring a CoNLL-U format. If the additional ```-d```/```--document``` flag is given, the tokeniser passes through lines starting with ```# newdoc id =``` to preserve document structure.

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
