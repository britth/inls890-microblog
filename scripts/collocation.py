import nltk
import os.path
from nltk.corpus import stopwords
from nltk.collocations import *
from urllib import urlopen
unnecessary = ["http", ":", "RT", "@", "&", ";", "I", "'m", "(", ")", "lt", "...", "n't", "``", "''", "gt", "!", "[", "]", "?", "#", "--", "-", "YouTube", ".", ",","=","'s","'ll" ]
url = "http://ils.unc.edu/~heejunk/tweets_1.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_1.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_1.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_1.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_1.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_1.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_1.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_1.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_1.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_2.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_2.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_2.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_2.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_2.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_2.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_2.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_2.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_2.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_3.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_3.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_3.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_3.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_3.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_3.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_3.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_3.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_3.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_4.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_4.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_4.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_4.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_4.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_4.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_4.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_4.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_4.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_5.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_5.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_5.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_5.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_5.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_5.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_5.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_5.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_5.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_6.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_6.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_6.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_6.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_6.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_6.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_6.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_6.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_6.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_7.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_7.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_7.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_7.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_7.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_7.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_7.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_7.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_7.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_8.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_8.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_8.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_8.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_8.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_8.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_8.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_8.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_8.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_9.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_9.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_9.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_9.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_9.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_9.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_9.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_9.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_9.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
  
url = "http://ils.unc.edu/~heejunk/tweets_10.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
filtered_tokens2 = [w for w in filtered_tokens if not w in unnecessary]
text = nltk.Text(filtered_tokens2)
words = [w.lower() for w in text]
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    words, window_size = 7)
output = finder.nbest(bigram_measures.likelihood_ratio, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_likelihood_10.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_likelihood_10.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.pmi, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_pmi_10.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_pmi_10.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.student_t, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_stu_10.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_stu_10.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()
output = finder.nbest(bigram_measures.chi_sq, 100)
save_path = 'D:\Dropbox\ILS890\collocation_result'
file_name = 'output_window7_chi_10.txt'
complete_name = os.path.join(save_path, file_name)
output_file = open('D:\Dropbox\ILS890\collocation_result\output_window7_chi_10.txt', 'w')
for words in output:
    output_file.write( '\t '.join(words)+'\n')
output_file.close()