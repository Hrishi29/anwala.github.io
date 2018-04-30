import docclass
from subprocess import check_output


cl = docclass.naivebayes(docclass.getwords)
#remove previous db file


cl.setdb('hrishi.db')
docclass.eTrain(cl)

for i in range(11,21):
		filename = 'test/spam' + str(i) +'.txt'
  
		with open(filename, 'r', encoding='utf-8') as testFile:
			print(filename, cl.classify(testFile.read()))
  

for i in range(11,21):
		filename = 'test/nonspam' + str(i) +'.txt'
  
		with open(filename, 'r', encoding='utf-8') as testFile1:
			print(filename, cl.classify(testFile1.read()))
#classify text: "the banking dinner" as spam or not spam
#print( cl.classify('the banking dinner') )