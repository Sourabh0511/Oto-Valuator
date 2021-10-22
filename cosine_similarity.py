import re
import nltk
import math
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

#Warning: this is slow. There is no caching, so it will take a while to run.

#constants
alpha = .2 #custom constants defined by STASIS paper
beta = .45 #custom constants defined by STASIS paper
delta = .85 #Delta = inverse word order weight. delta = 1.0 means you are "turning off" word order.

threshold = .2 #Minimum thresh

def cosine_similarity(vec_a, vec_b):#Get cosine similarity between two vectors
        if not len(vec_a) == len(vec_b):
                print ("ERROR: Unequal vector magnitudes")#error message. Should never happen
        else:
                return dot_product(vec_a, vec_b) / (magnitude(vec_a) * magnitude(vec_b))

def dot_product(a, b):
        out = 0.0
        for i in range(0, len(a)):
                out = out + a[i] * b[i];
        return out;

def magnitude(lst):
        out = 0.0
        for i in lst:
                out = out + (i*i);
        return math.sqrt(out);
                

def word_similarity(word_a, word_b): #given two words, find the similarity using the STASIS equation
        synsets_a = nltk.corpus.wordnet.synsets(word_a);
        synsets_b = nltk.corpus.wordnet.synsets(word_b);
        if len(synsets_a ) == 0 or (synsets_b == 0):
                if word_a == word_b:
                        return 1.0;
                else:
                        return 0.0;
        shortestPath = None;
        #get path length
        #get path depth
        for a in synsets_a:
                for b in synsets_b:
                        subsumer = a.lowest_common_hypernyms(b)
                        if len(subsumer) == 0:
                                continue;
                        lch = subsumer[0];
                        if shortestPath is None and lch is not None:
                                depth = lch.max_depth() + 1;
                                shortestPath = a.shortest_path_distance(b);
                        elif lch is not None:
                                pathLength = a.shortest_path_distance(b)
                                if pathLength < shortestPath:
                                        depth = lch.max_depth() + 1;
                                        shortestPath = pathLength;
        
        if shortestPath == None:#ensure a path exists
                return 0.0;#If no path exists, return 0.0
        else:
                return word_sim_forumula(depth, shortestPath);
                                        
def word_sim_forumula(h, l):#From STASIS paper, gets similarity between two words in word net. h = height, l = length
        return math.exp(-1*alpha*l) * (math.exp(beta*h) - math.exp(-1*beta*h)) / (math.exp(beta*h) + math.exp(-1*beta*h));
                                
                        

def sentence_similarity(a, b):#Semantic similarity between two groups of text.
        words = [ i for i in set(a+b) if i not in nltk.corpus.stopwords.words('english') ]
        vector_a = []
        vector_b = []
        for i in words:
                best = 0.0;
                for k in a:
                        if i == k:
                                best = 1.0;
                                break;
                        else:
                                simScore = word_similarity(i,k);
                                if simScore > best and simScore > threshold: #If better than "best" and greater than threshold.
                                        best = simScore;
                vector_a.append(best);#add top score to vector A
                best = 0.0;
                for k in b:
                        if i == k:
                                best = 1.0;
                                break;
                        else:
                                simScore = word_similarity(i,k);
                                if simScore > best and simScore > threshold:
                                        best = simScore;
                vector_b.append(best);#add top score to vector B
        return cosine_similarity(vector_a,vector_b);
        
                                

def word_order(a,b):
        words = [ i for i in set(a+b) if i not in nltk.corpus.stopwords.words('english') ]#append a and b, remove stop words
        vector_a = []
        vector_b = []
        for i in words:
                best = 0.0;
                bestIndex = 0;
                index = 0;
                for k in a:
                        index = index + 1;
                        if i == k:
                                best = 1.0;
                                bestIndex = index;
                                break;
                        else:
                                simScore = word_similarity(i,k);
                                if simScore > best and simScore > threshold:
                                        best = simScore;
                                        bestIndex = index;
                vector_a.append(bestIndex);
                best = 0.0;
                for k in b:
                        if i == k:
                                best = 1.0;
                                bestIndex = index;
                                break;
                        else:
                                simScore = word_similarity(i,k);
                                if simScore > best and simScore > threshold:
                                        best = simScore;
                                        bestIndex = index;
                vector_b.append(bestIndex);
        return word_order_calc(vector_a,vector_b);

def word_order_calc(a,b):
        vec_minus = [];
        vec_plus = [];
        for i in range (0, len(a)):
                vec_minus.append(a[i] - b[i]);
                vec_plus.append(a[i] + b[i]);
        return (1 - (magnitude(vec_minus)/magnitude(vec_plus)));
                

def stasis(a, b):#input: tokenized list of strings
        return (delta*sentence_similarity(a,b)) + (1-delta)*word_order(a,b);

def get_cosine_sim(a, b):
    #print stopwords.words('english')
    #print('************')
    #print   string.punctuation
    stop = stopwords.words('english') 
    for x in string.punctuation:
        stop.append(str(x))
    li1 = [i for i in word_tokenize(a.lower()) if i not in stop]
    li2 = [i for i in word_tokenize(b.lower()) if i not in stop]
    return stasis(li1, li2)
#Use example:
#a = ["the", "boy", "bought", "the", "ball"]
#b = ["the", "girl", "kicked", "the", "ball"]
#stasis(a,b)
