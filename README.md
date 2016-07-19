# reldi-tokeniser

A tokeniser developed inside the [ReLDI project](https://reldi.spur.uzh.ch). Supports three languages -- Croatian, Serbian and Slovene, and two modes -- for standard and non-standard text.

## Usage

```
$ echo 'kaj sad s tim.daj se nasmij ^_^. | ./tokeniser.py hr -n
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
