# !/usr/bin/python
# coding=utf-8
import tltk
import re
from pythainlp.corpus.common import thai_words
from pythainlp.tokenize import dict_trie,word_tokenize,syllable_tokenize
from pythainlp.tag import pos_tag

custom_dict = set(thai_words())
custom_dict.add('ซิน')
trie = dict_trie(dict_source=custom_dict)
text = "อีซินมึงรู้จักเขามั้ย"
token_text = word_tokenize(text, engine="newmm", custom_dict=trie)
trueConsonantcluster = ['กร','คร','ปร','พร','ตร','กล','คล','ปล','พล','กว','คว']
numCharacter = '(อย)'
def checkSwap(syl):
  if len(syl) == 2:
    syl[0],syl[1] = syl[1],syl[0]
  return syl
def word2alpha(word):
  result = re.search('(อย)|(หง)|(หญ)|(หน)|(หม)|(หย)|(หร)|(หล)|(หว)|(กร)|(คร)|(ปร)|(พร)|(ตร)|(กล)|(คล)|(ปล)|(พล)|(กว)|(คว)|[\u0E00-\u0E2E]', word)
  return result.group(), result.start()
def spoonerism2syl(syl):
  syl=checkSwap(syl)
  alpha1,pos1 = word2alpha(syl[0])
  alpha2,pos2 = word2alpha(syl[1])
  s1 = list(syl[0])
  s2 = list(syl[1])
  if len(alpha1) == 1 :
    s1[pos1] = alpha2
    s2[pos2] = alpha1
    syl[0] = "".join(s1)
    syl[1] =  "".join(s2)
  else :
    s1[pos1] = 'ห'
    s1[pos1+1] = alpha2
    s2[pos2] = alpha1
    syl[0] = "".join(s1)
    syl[1] =  "".join(s2)
  del [[alpha1,pos1,alpha2,pos2,s1,s2]]
  return syl
def check_condition(syl):
    #list of สระอุ และ สระอู
    vowel_cond = [chr(3640),chr(3641)]
    alpha_cond, pos_cond = word2alpha(syl)
    syl_list_cond = list(syl)
    
    if alpha_cond == 'ร' or alpha_cond == 'ล':
        looParam = 'ซู'
    elif ('ุ' in syl_list_cond) or ('ู' in syl_list_cond):
        looParam = 'ลี'
    elif (alpha_cond == 'ร' or alpha_cond == 'ล') and (('ุ' in syl_list_cond) or ('ู' in syl_list_cond)):
        looParam = 'ซี'
    else:
        looParam = "ลู"
    del [[vowel_cond, alpha_cond, pos_cond, syl_list_cond]]
    return looParam
def loomain(inputText):
    syl = syllable_tokenize(inputText)
    full = ""
    if "<s/>" in syl :
      syl.remove("<s/>")
    for inSyl in syl:
      inSyl = [check_condition(inSyl),inSyl]
      if len(inSyl) == 2:
          # in 2 syll type
          full = full + "".join(spoonerism2syl(inSyl))
      else:
          return "ไม่สามารถใช้กับคำที่มากกว่า 1 พยางค์ได้"
    print("-->",full)
    del [[syl, inSyl]]
    return full
def spoon(inputText):
    syl = syllable_tokenize(inputText)
    full = ""
    if "<s/>" in syl :
      syl.remove("<s/>")
    if len(syl) == 1:
        full = inputText 
    elif len(syl) == 2 or len(syl) == 3:
        full = full + "".join(spoonerism2syl(syl))
    else:
        raise ValueError('cannot used more than 3 syllable')
    del [[syl]]
    return full
