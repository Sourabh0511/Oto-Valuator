from rake import *
import semantic_formula
import csv
import os
from cosine_similarity import *
from plot_module import *
import commands
from graphplot import *
import matplotlib.pyplot as plt



'''
keywords = []

#text = 'To simulate portions of the desired final product with a quick and easy program that does a small specific job.  It is a way to help see what the problem is and how you may solve it in the final project.'
# Split text into sentences
sentenceList = split_sentences(text)
#stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" 
stoppath = "SmartStoplist.txt"  #SMART stoplist misses some of the lower-scoring keywords, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
stopwordpattern = build_stop_word_regex(stoppath)

# generate candidate keywords
phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

# calculate individual word scores
wordscores = calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)

sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)

totalKeywords = len(sortedKeywords)
	
rake = Rake("SmartStoplist.txt")
keywords.append(rake.run(text))
'''
'''
def compile_java(java_file):
	subprocess.check_call(['javac', java_file])

def execute_java(java_file, stdin):
	java_class,ext = os.path.splitext(java_file)
	cmd = ['java', java_class]
	proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout,stderr = proc.communicate(stdin)
	##print ('This was "' + stdout + '"')
	return stdout
'''
"""function to normalize based on training data"""

a = 1
b = 0
c = 1
d = 1
e = 1
def normalize(student_ans, keyword_score, lsa_score, formula_score, cosine_score,semantic_score):
	#print student_ans
	#print(keyword_score)
	print(lsa_score)
	print(formula_score)
	print(cosine_score)
	print(semantic_score)
	print('___________________________')
	return ((a*keyword_score)+(b*lsa_score)+(c*formula_score)+(d*cosine_score)+(e*semantic_score))###############
	#return keyword_score*2

expected_ans = ''
student_ans_li = []
student_usn_li = []
final_score_li = []
student_name_li = []
teacher_score_li = []


with open('/home/ubuntu/Desktop/semantics/src/data/q1old.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	z=0
	for x in reader:
		if z==0:
			z=1
			continue
		x['Question'] 
		expected_ans = x['Expected answer']
		student_ans_li.append(x['Answer given'])
		teacher_score_li.append(x['Score-Teacher'])


#compile_java('USAGE.java')

f = 0
final_score = 3
for student_ans in student_ans_li:
	try :
		keyword_score = get_keyword_score(expected_ans, student_ans)####CHECK_STOP_LIST
	except:
		final_score = 0
		final_score_li.append('0')
		continue

	print(student_ans)
	print(keyword_score)
	if keyword_score <= 0.1:
		final_score = 0
	elif keyword_score >= 0.750 :###############ADJUST-Full score
		score = semantic_formula.similarity(expected_ans, student_ans, False)
		#print(score)
		#print('!!!!!!!!!!!!!!!!!!')
		if score >= 0.35:#############Nor for structure
			final_score = 4.25
		else:
			f = 1
	elif 0<keyword_score<0.8 or f == 1 :
		lsa_score = 0#GENSIM_LSA_FUNC()
		formula_score = semantic_formula.similarity(expected_ans, student_ans, False)###False
		print(formula_score)
		myarg = expected_ans.replace(' ','@')+'#'+student_ans.replace(' ','@')
		#print myarg
		#semantic_score = 0
		semantic_score = float(commands.getstatusoutput('java USAGE '+myarg)[1])
		print(commands.getstatusoutput('java USAGE '+myarg))
		#print semantic_score
		print('%%%%%%%%%%%%%%')
		cosine_score = get_cosine_sim(expected_ans, student_ans)
		print(cosine_score)
		final_score = normalize(student_ans, keyword_score, lsa_score, formula_score, cosine_score, semantic_score)
	print('\n------------------------\n')
	if final_score > 5: final_score = 5
	final_score_li.append(final_score)

print(final_score_li)
print('*********************************')

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

with open('new_data_q1_OUTPUT.csv','w') as mycsv:
	c = csv.writer(mycsv, dialect='mydialect')
	c.writerow(['Name','USN','EXP-ANS','ANSWER','TEACHER-SCORE','THRESHOLD-SCORE'])
	for x in range(len(student_ans_li)):##################
		c.writerow([
				''.encode('utf8'),
				''.encode('utf8'),
				str(expected_ans).encode('utf8'),
				student_ans_li[x].encode('utf8'),
				#"".encode('utf8'),##############
				str(teacher_score_li[x]).encode('utf8'),
				str(final_score_li[x]).encode('utf8')
			])


#PLOT_TEACHER_SCORE_FINAL_SCORES
#THIS_IS_FOR_EACH_QUESTION
#plot(teacher_score_li, final_score_li)

radius = [x for x in range(1, 25)]
#teacher_score_li = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
#final_score_li = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
print(len(radius))
print(len(teacher_score_li))
print(len(final_score_li))

print(teacher_score_li)
print(final_score_li)

plt.plot(radius, teacher_score_li, label='Teacher-Score')
plt.plot(radius, final_score_li, marker='o', linestyle='--', color='r', label='Threshold-Score')

plt.xlabel('Teacher-Score')
plt.ylabel('Scores')
plt.title('Project Accuracy')
plt.legend()
plt.show()

