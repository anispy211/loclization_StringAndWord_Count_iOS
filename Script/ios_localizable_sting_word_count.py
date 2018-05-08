#author: Aniruddha Kadam
#github: https://github.com/anispy211


import re

print "==================================================================================="
print "=================          Welcome to iOS Localization            ================="
print "==================================================================================="

# Regex
TAG_RE = re.compile(r'<[^>]+>')
HTML_TAG_RE = re.compile(r'<*>.*?(?=</*>)')
CUSTOM_ACTOR_LINK_RE = re.compile(r'customlink://target::actor|')
CUSTOM_SINGLEOBJ_LINK_RE = re.compile(r'customlink://actors::singleobject2|')
SPECIAL_CHAR_RE = re.compile('[%@.|:]')
BRACKETS_RE = re.compile('<>')


file = open("Localizable.strings","r") 

newFile = open("output.txt","w")

sentenceCount = 0
wordCount = 0
for line in file: 
    
		if line.find("=") != -1:
			sentence = re.findall(r'"([^"]*)";', line)		    
			s = ''.join(sentence)
			s = CUSTOM_ACTOR_LINK_RE.sub('', s)
			s = CUSTOM_SINGLEOBJ_LINK_RE.sub('', s)
			s = SPECIAL_CHAR_RE.sub('', s)
			s = TAG_RE.sub('', s)
			s = HTML_TAG_RE.sub('', s)
			s = BRACKETS_RE.sub('', s)
			wordCount  = wordCount + len(s.split())
			sentence  = s
			#print sentence
			newFile.write(sentence + "\n") 
			sentenceCount = sentenceCount + 1


		 
		 
print "Sentence Count :", sentenceCount
print "Word Count     :", wordCount
print "==================================================================================="
 
