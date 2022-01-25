#!/usr/bin/python
#-*-encoding:utf-8-*-
import re
import codecs
import sys
import threading
import unicodedata


import os
from io import StringIO

reldir=os.path.dirname(os.path.abspath(__file__))

def read_abbrevs(file):
  abbrevs={'B':[],'N':[],'S':[]}
  for line in open(os.path.join(reldir,file),encoding='utf8'):
    if not line.startswith('#'):
      abbrev,type=line.strip().split('\t')[:2]
      abbrevs[type].append(abbrev)
  return abbrevs

abbrevs={
  'hr':read_abbrevs('hr.abbrev'),
  'sr':read_abbrevs('sr.abbrev'),
  'sl':read_abbrevs('sl.abbrev'),
  'mk':read_abbrevs('mk.abbrev'),
  'bg':read_abbrevs('bg.abbrev')
}

num=r'(?:(?<!\d)[+-])?\d+(?:[.,:/]\d+)*(?:[.](?!\.)|-[^\W\d_]+)?'
# emoswithspaces emoticon=r'[=:;8][\'-]*(?:\s?\)+|\s?\(+|\s?\]+|\s?\[+|\sd\b|\sp\b|d+\b|p+\b|s+\b|o+\b|/|\\|\$|\*+)|-\.-|\^_\^|\([\W]+\)|<3|</3|<\\3|\\o/'
emoticon=r'[=:;8][\'-]*(?:\)+|\(+|\]+|\[+|D+\b|P+\b|S+\b|O+\b|d+\b|p+\b|s+\b|o+\b|/|\\|\$|\*+)|-\.-|\^_\^|\([^\w\s]+\)|<3|</3|<\\3|\\o/'
url=r'https?://[-\w/%]+(?:[.#?=&@;][-\w/%]+)+|\b[\w-]+\.(?:[\w-]+\.)?(?:com|org|net|gov|edu|int|io|eu|si|hr|rs|ba|me|mk|it|at|hu|bg|ro|al|de|ch|be|dk|se|no|es|pt|ie|fr|fi|cl|co|bo|br|gr|ru|uk|us|by|cz|sk|pl|lt|lv|lu|ca|in|tr|il|iq|ir|hk|cn|jp|au|nz)/?\b'
word=r'(?:[*]{2,})?\w+(?:[@­\'-]\w+|[*]+\w+)*(?:[*]{2,})?'
#open('punct','w').write(''.join([chr(i) for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P')]))
punct = open(os.path.join(reldir,'punct'), encoding="utf-8").read()

langs={
  'hr':{
    'abbrev':r'|'.join(abbrevs['hr']['B']+abbrevs['hr']['N']+abbrevs['hr']['S']),
    'num':num,
    'url':url,
    'htmlesc':r'&#?[a-z0-9]+;',
    'tag':r'</?[a-z][\w:]*>|<[a-z][\w:]*/?>',
    'mail':r'[\w.-]+@\w+(?:[.-]\w+)+',
    'mention':r'@[a-z0-9_]+',
    'hashtag':r'#\w+(?:[.-]\w+)*',
    'emoticon':emoticon,
    'word':word,
    'arrow':r'<[-]+|[-]+>',
    'dot':r'[.!?/]{2,}',
    'space':r'\s+',
    'other':r'(.)\1*',
    'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
  },

  'sr':{
    'abbrev':r'|'.join(abbrevs['sr']['B']+abbrevs['sr']['N']+abbrevs['sr']['S']),
    'num':num,
    'url':url,
    'htmlesc':r'&#?[a-z0-9]+;',
    'tag':r'</?[a-z][\w:]*>|<[a-z][\w:]*/?>',
    'mail':r'[\w.-]+@\w+(?:[.-]\w+)+',
    'mention':r'@[a-z0-9_]+',
    'hashtag':r'#\w+(?:[.-]\w+)*',
    'emoticon':emoticon,
    'word':word,
    'arrow':r'<[-]+|[-]+>',
    'dot':r'[.!?/]{2,}',
    'space':r'\s+',
    'other':r'(.)\1*',
    'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
  },

  'sl':{
    'abbrev':r'|'.join(abbrevs['sl']['B']+abbrevs['sl']['N']+abbrevs['sl']['S']),
    'num':num,
    'url':url,
    'htmlesc':r'&#?[a-z0-9]+;',
    'tag':r'</?[a-z][\w:]*>|<[a-z][\w:]*/?>',
    'mail':r'[\w.-]+@\w+(?:[.-]\w+)+',
    'mention':r'@[a-z0-9_]+',
    'hashtag':r'#\w+(?:[.-]\w+)*',
    'emoticon':emoticon,
    'word':word,
    'arrow':r'<[-]+|[-]+>',
    'dot':r'[.!?/]{2,}',
    'space':r'\s+',
    'other':r'(.)\1*',
    'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
  },

  'mk':{
    'abbrev':r'|'.join(abbrevs['mk']['B']+abbrevs['mk']['N']+abbrevs['mk']['S']),
    'num':num,
    'url':url,
    'htmlesc':r'&#?[a-z0-9]+;',
    'tag':r'</?[a-z][\w:]*>|<[a-z][\w:]*/?>',
    'mail':r'[\w.-]+@\w+(?:[.-]\w+)+',
    'mention':r'@[a-z0-9_]+',
    'hashtag':r'#\w+(?:[.-]\w+)*',
    'emoticon':emoticon,
    'word':word,
    'arrow':r'<[-]+|[-]+>',
    'dot':r'[.!?/]{2,}',
    'space':r'\s+',
    'other':r'(.)\1*',
    'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
  },


  'bg':{
    'abbrev':r'|'.join(abbrevs['bg']['B']+abbrevs['bg']['N']+abbrevs['bg']['S']),
    'num':num,
    'url':url,
    'htmlesc':r'&#?[a-z0-9]+;',
    'tag':r'</?[a-z][\w:]*>|<[a-z][\w:]*/?>',
    'mail':r'[\w.-]+@\w+(?:[.-]\w+)+',
    'mention':r'@[a-z0-9_]+',
    'hashtag':r'#\w+(?:[.-]\w+)*',
    'emoticon':emoticon,
    'word':word,
    'arrow':r'<[-]+|[-]+>',
    'dot':r'[.!?/]{2,}',
    'space':r'\s+',
    'other':r'(.)\1*',
    'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
  }
}

#transform abbreviation lists to sets for lookup during sentence splitting
for lang in abbrevs:
  for type in abbrevs[lang]:
    abbrevs[lang][type]=set([e.replace('\\.','.') for e in abbrevs[lang][type]])

spaces_re=re.compile(r'\s+',re.UNICODE)

def generate_tokenizer(lang):
  els=langs[lang]
  token_re=re.compile(r'|'.join([langs[lang][e] for e in langs[lang]['order']]),re.UNICODE|re.IGNORECASE)
  return token_re

def tokenize(tokenizer,paragraph):
  return [(e.group(0),e.start(0),e.end(0)) for e in tokenizer.finditer(paragraph.strip())]#spaces_re.sub(' ',paragraph.strip()))]

def sentence_split_nonstd(tokens,lang):
  boundaries=[0]
  for index in range(len(tokens)-1):
    token=tokens[index][0]
    if token[0] in '.!?…': #if sentence ending punctuation
      boundaries.append(index+1)
    elif token.endswith('.'): #if abbreviation
      if token.lower() not in abbrevs[lang]['N']: #if not in non-splitting abbreviations
        if token.lower() in abbrevs[lang]['S']: #if in splitting abbreviations
          boundaries.append(index+1)
        elif len(token)>2:
          if tokens[index+1][0][0].isupper(): #else if next is uppercase
            boundaries.append(index+1)
            continue
          if index+2<len(tokens): # else if next is space and nextnext is uppercase
            if tokens[index+1][0][0].isspace() and tokens[index+2][0][0].isupper():
            #tokens[index+1][0][0] not in u'.!?…':
              boundaries.append(index+1)
  boundaries.append(len(tokens))
  sents=[]
  for index in range(len(boundaries)-1):
    sents.append(tokens[boundaries[index]:boundaries[index+1]])
  return sents

def sentence_split(tokens,lang):
  boundaries=[0]
  for index in range(len(tokens)-1):
    token=tokens[index][0]
    if token[0] in '.!?…' or (token.endswith('.') and token.lower() not in abbrevs[lang]['N'] and len(token)>2 and tokens[index+1][0][0] not in '.!?…'):
      if tokens[index+1][0][0].isupper():
        boundaries.append(index+1)
        continue
      if index+2<len(tokens):
        if tokens[index+2][0][0].isupper():
          if tokens[index+1][0].isspace() or tokens[index+1][0][0] in '-»"\'„':
            boundaries.append(index+1)
            continue
      if index+3<len(tokens):
        if tokens[index+3][0][0].isupper():
          if tokens[index+1][0].isspace() and tokens[index+2][0][0] in '-»"\'„':
            boundaries.append(index+1)
            continue
      if index+4<len(tokens):
        if tokens[index+4][0][0].isupper():
          if tokens[index+1][0].isspace() and tokens[index+2][0][0] in '-»"\'„' and tokens[index+3][0][0] in '-»"\'„':
            boundaries.append(index+1)
            continue
    if token[0] in '.!?…':
      if index+2<len(tokens):
        if tokens[index+2][0][0].isdigit():
          boundaries.append(index+1)
          continue
  boundaries.append(len(tokens))
  sents=[]
  for index in range(len(boundaries)-1):
    sents.append(tokens[boundaries[index]:boundaries[index+1]])
  return sents

process={'standard':lambda x,y,z:sentence_split(tokenize(x,y),z),'nonstandard':lambda x,y,z:sentence_split_nonstd(tokenize(x,y),z)}

def to_text(sent):
  text=''
  for idx,(token,start,end) in enumerate(sent):
    if idx==0 and token[0].isspace():
      continue
    text+=token
  return text+'\n'

def run(text, lang, conllu=False, bert=False, document=False, nonstandard=False, tag=False):
  output = StringIO()
  reldi = ReldiTokeniser(lang, conllu, bert, document, nonstandard, tag, output)
  split_text = [el + '\n' for el in text.split('\n')]
  reldi.run(split_text)
  contents = output.getvalue()
  output.close()
  return contents

class ReldiTokeniser:
  def __init__(self, lang, conllu=False, bert=False, document=False, nonstandard=False, tag=False, output=StringIO()):
    self.output = output
    args = {
      'lang': lang,
      'conllu': conllu,
      'bert': bert,
      'document': document,
      'nonstandard': nonstandard,
      'tag': tag
    }
    if args['document']:
      args['conllu'] = True
    if args['tag']:
      args['conllu'] = True
    self.args = args
    lang = args['lang']
    self.mode = 'standard'
    if args['nonstandard']:
      self.mode = 'nonstandard'
    self.tokenizer = generate_tokenizer(lang)
    if args['tag']:
      self.punct_re = re.compile(r'^[' + re.escape(punct) + ']+$', re.UNICODE)
      self.symb_re = re.compile(r'^[' + re.escape('#%&<>+=°x÷$@µ©™®§') + ']+$')
      self.hashtag_re = re.compile(r'^' + langs[lang]['hashtag'] + '$')
      self.mention_re = re.compile(r'^' + langs[lang]['mention'] + '$')
      self.mail_re = re.compile(r'^' + langs[lang]['mail'] + '$')
      self.url_re = re.compile(r'^' + langs[lang]['url'] + '$')
      self.emoticon_re = re.compile(r'^' + langs[lang]['emoticon'] + '$')
      self.emoji_re = re.compile('^[\U00010000-\U0010ffff]+$', flags=re.UNICODE)


  def represent_tomaz(self,input,par_id,mode):
    if mode == 'string':
      output=''
    elif mode == 'object':
      metadata = ''
      data = []
    token_id=0
    sent_id=0
    if self.args['conllu']:
      text = '# newpar id = ' + str(par_id)+'\n'
      if mode == 'string':
        output+=text
      elif mode == 'object':
        metadata+=text
    for sent_idx,sent in enumerate(input):
      sent_id+=1
      token_id=0
      if self.args['conllu']:
        text='# sent_id = '+str(par_id)+'.'+str(sent_id)+'\n'
        text+='# text = '+to_text(sent)
        if mode == 'string':
          output += text
        elif mode == 'object':
          metadata += text
          doc_sent = []
      for token_idx,(token,start,end) in enumerate(sent):
        if not token[0].isspace():
          token_id+=1
          lemma='_'
          xpos='_'
          upos='_'
          if self.args['tag']:
            #'order':('abbrev','num','url','htmlesc','tag','mail','mention','hashtag','emoticon','word','arrow','dot','space','other')
            if self.args['lang']=='bg':
              if self.url_re.match(token):
                xpos='Np'
                upos='PROPN'
                lemma=token
              elif self.mail_re.match(token):
                xpos='Np'
                upos='PROPN'
                lemma=token
              elif self.mention_re.match(token):
                xpos='Np'
                upos='PROPN'
                lemma=token
              elif self.hashtag_re.match(token):
                xpos='Np'
                upos='PROPN'
                lemma=token
              elif self.emoticon_re.match(token):
                xpos='I'
                upos='INTJ'
                lemma=token
              elif self.emoji_re.match(token):
                xpos='I'
                upos='INTJ'
                lemma=token
              elif self.punct_re.match(token):
                if not self.symb_re.match(token):
                  upos='PUNCT'
                  xpos='punct'
                  lemma=token
            else:
              if self.url_re.match(token):
                xpos='Xw'
                upos='SYM'
                lemma=token
              elif self.mail_re.match(token):
                xpos='Xw'
                upos='SYM'
                lemma=token
              elif self.mention_re.match(token):
                xpos='Xa'
                upos='SYM'
                lemma=token
              elif self.hashtag_re.match(token):
                xpos='Xh'
                upos='SYM'
                lemma=token
              elif self.emoticon_re.match(token):
                xpos='Xe'
                upos='SYM'
                lemma=token
              elif self.emoji_re.match(token):
                xpos='Xe'
                upos='SYM'
                lemma=token
              elif self.punct_re.match(token):
                xpos='Z'
                lemma=token
                if self.symb_re.match(token):
                  upos='SYM'
                else:
                  upos='PUNCT'
          if self.args['conllu']:
            SpaceAfter=True
            if len(sent)>token_idx+1:
              SpaceAfter=sent[token_idx+1][0].isspace()
            elif len(input)>sent_idx+1:
              SpaceAfter=input[sent_idx+1][0][0].isspace()
            if mode == 'string':
              if SpaceAfter:
                output+=str(token_id)+'\t'+token+'\t'+lemma+'\t'+upos+'\t'+xpos+'\t_'*5+'\n'
              else:
                output+=str(token_id)+'\t'+token+'\t'+lemma+'\t'+upos+'\t'+xpos+'\t_'*4+'\tSpaceAfter=No\n'
            elif mode == 'object':
              tok = {'id': tuple([token_id]), 'text': token, 'lemma': lemma, 'xpos': xpos, 'upos': upos, 'misc': '_'}
              if not SpaceAfter:
                tok['misc'] = 'SpaceAfter=No'
              doc_sent.append(tok)
          elif self.args['bert']:
            output+=token+' '
          else:
            output+=str(par_id)+'.'+str(sent_id)+'.'+str(token_id)+'.'+str(start+1)+'-'+str(end)+'\t'+token+'\n'
      if mode == 'string':
        if self.args['bert']:
          output=output.strip()
        output+='\n'
      elif mode == 'object':
          data.append({'sentence': doc_sent, 'metadata': metadata})
          metadata = ''
    if mode == 'object':
      return data
    return output

  def run(self, input, mode='string'):
    if mode == 'object':
      assert self.args['conllu'], Exception('For obtaining objects, tag `conllu` must be set to True!')
      document = []
      pre_metadata = ''
    par_id = 0
    for line in input:
      if line.strip() == '':
        continue
      par_id += 1
      if self.args['document']:
        if line.startswith('# newdoc id = '):
          par_id = 0
          if mode == 'object':
            pre_metadata += line
          else:
            self.output.write(line)
          continue
      out = self.represent_tomaz(process[self.mode](self.tokenizer, line, lang), par_id, mode)
      if mode == 'object':
        if pre_metadata and len(out) > 0:
          out[0]['metadata'] = pre_metadata + out[0]['metadata']
        document.append(out)
      else:
        self.output.write(out)
      if self.args['bert']:
        self.output.write('\n')

    if mode == 'object':
      return document

    return None
