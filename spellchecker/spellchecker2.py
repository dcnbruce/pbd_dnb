class Spellchecker(object):
	
	def load_words(self, file_name):
		words = open(file_name).readlines()
		words = map(lambda x: x.strip(), words)
		return words

	def check_word(self, words, word) :
			return word in words
			
	def check_words(self, words, sentence):
		words_to_check = sentence.split(' ')
		for word in words_to_check:
			if not self.check_word(words, word):
				print('Word is misspelt : ' + word)
				return False
		return True

spell_check = Spellchecker()	
words = spell_check.load_words("spell.words")	

# print words
# print len(words)
# print len(words[0])
# print words[len(words)-1]

print('zygotic' in words)
print('mistasdas' in words)	
print words[0]
#print load_words("spell.words")[0]
#print check_word(words, 'zygotic')
#print check_word(words, 'mistasdas')
print spell_check.check_word(words, 'zygotic')
print spell_check.check_word(words, 'mistasdas')
print spell_check.check_word(words, 'zygotic mistasdas elementary')