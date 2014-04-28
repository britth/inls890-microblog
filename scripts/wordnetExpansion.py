import nltk
from nltk.corpus import wordnet as wn, stopwords
from nltk.tag import *


def get_wordnet_pos(treebank_tag):
    '''
    Used to convert POS to a format usable with wordnet
    '''
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return ''


def expand_queries(file):
    '''
    For each term in a query, takes the first synset of the word from wordnet and adds all synonyms of that synset
    '''
    file = open(file)
    for sentence in file:
        sentence = sentence.strip()
        if sentence.find('<text>') != -1:
            query = sentence[sentence.find('>')+1: sentence.rfind('<')]
            additions = ''
            updated_q = nltk.pos_tag(nltk.wordpunct_tokenize(query.lower()))
            full_q = query
            for word, pos in updated_q:
               if word not in stopwords.words('english'):
                   looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'                   
                   synsets = wn.synsets(word)
                   if looking_for in str(synsets):
                       new_words = (wn.synset(looking_for).lemma_names) #was .definition
                       for new_word in new_words:
                           if new_word.lower() != word.lower():
                               full_q = full_q +' '+ str(new_word)
                   else:
                       if wn.morphy(word) != None:
                           word = wn.morphy(word)
                           looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'
                           print str(looking_for) + ' THIS IS WORD'
                           synsets = wn.synsets(word)
                           if looking_for in str(synsets):
                               new_words = (wn.synset(looking_for).lemma_names) #was .definition
                               for new_word in new_words:
                                   if new_word.lower() != word.lower():
                                       full_q = full_q +' '+ str(new_word)
            print query + ' '+ full_q


def expand_queries_hyponyms(file):
    '''
    For each term in a query, takes the first hyponym (narrower term) from wordnet and add all synonyms for that hyponym
    '''
    file = open(file)
    for sentence in file:
        sentence = sentence.strip()
        if sentence.find('<text>') != -1:
            query = sentence[sentence.find('>')+1: sentence.rfind('<')]
            additions = ''
            updated_q = nltk.pos_tag(nltk.wordpunct_tokenize(query.lower()))
            full_q = query
            for word, pos in updated_q:
               if word not in stopwords.words('english'):
                   looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'
                   synsets = wn.synsets(word)                   
                   if looking_for in str(synsets):
                       new_words = (wn.synset(looking_for).hyponyms()) #was .definition
                       if new_words != []:
                           added = str(new_words[0])[str(new_words[0]).find("'")+1:str(new_words[0]).rfind("'")]
                           additions = (wn.synset(added).lemma_names)
                           for addition in additions:
                               if addition.lower() != word.lower():
                                   full_q = full_q+' '+str(addition)
                   else:
                       if wn.morphy(word) != None:
                           word = wn.morphy(word)
                           looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'
                           synsets = wn.synsets(word)
                           if looking_for in str(synsets):
                               new_words = (wn.synset(looking_for).hyponyms()) #was .definition
                               if new_words != []:
                                   added = str(new_words[0])[str(new_words[0]).find("'")+1:str(new_words[0]).rfind("'")]
                                   additions = (wn.synset(added).lemma_names)
                                   for addition in additions:
                                       if addition.lower() != word.lower():
                                           full_q = full_q+' '+str(addition)
            print query + ' '+ full_q


def expand_queries_hypernyms(file):
    '''
    For each term in a query, takes the first hypernym (broader term) from wordnet and adds all synonyms for that hypernym
    '''
    file = open(file)
    for sentence in file:
        sentence = sentence.strip()
        if sentence.find('<text>') != -1:
            query = sentence[sentence.find('>')+1: sentence.rfind('<')]
            additions = ''
            updated_q = nltk.pos_tag(nltk.wordpunct_tokenize(query.lower()))
            full_q = query
            for word, pos in updated_q:
               if word not in stopwords.words('english'):
                   looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'
                   synsets = wn.synsets(word)
                   if looking_for in str(synsets):
                       new_words = (wn.synset(looking_for).hypernyms()) #was .definition
                       if new_words != []:
                           added = str(new_words[0])[str(new_words[0]).find("'")+1:str(new_words[0]).rfind("'")]
                           additions = (wn.synset(added).lemma_names)
                           for addition in additions:
                               if addition.lower() != word.lower():
                                   full_q = full_q+' '+str(addition)
                   else:
                       if wn.morphy(word) != None:
                           word = wn.morphy(word)
                           looking_for = str(word)+'.'+str(get_wordnet_pos(pos))+'.01'
                           synsets = wn.synsets(word)
                           if looking_for in str(synsets):
                               new_words = (wn.synset(looking_for).hypernyms()) #was .definition
                               if new_words != []:
                                   added = str(new_words[0])[str(new_words[0]).find("'")+1:str(new_words[0]).rfind("'")]
                                   additions = (wn.synset(added).lemma_names)
                                   for addition in additions:
                                       if addition.lower() != word.lower():
                                           full_q = full_q+' '+str(addition)
            print query + ' '+ full_q

            
def format_xml(file):
    '''
    Used to structure wordnet expansion lists into XML files for use in Indri
    '''
    file = open(file)
    queryNo = 0
    print '<parameters>'
    for line in file.readlines():
        line = line.split()
        queryNo = queryNo + 1
        new_line = ''
        for word in line:
            if '_' in word:
                word = word.replace('_', ' ')
            new_line = new_line+' ' + word
        print '\t<query>\n\t\t<number>'+str(queryNo)+'</number>\n\t\t<text>'+new_line.strip()+'</text>\n\t</query>'
    print '</parameters>'



