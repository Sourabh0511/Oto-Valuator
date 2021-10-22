import commands


expected_ans = ' What is the role of a prototype program in problem solving?'
student_ans = 'To ease the understanding of problem under discussion and to ease the understanding of the program itself '
myarg = expected_ans.replace(' ','@')+'#'+student_ans.replace(' ','@')
print myarg
print commands.getstatusoutput('java USAGE '+myarg)

#print(semantic_score)
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')