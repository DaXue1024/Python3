import re

short_str='M4561GABCDEFG2abcvg777'
long_str='123456ABCDEFGabcvg778'
list1=[]
list2=[]
list2=[]
for i in range(0,len(short_str)):   
	if short_str[i] in long_str:      #对短字符串中的每个字符进行遍历，如果出现在长字符串里
		new_str=short_str[i:]         #截取该字符到结尾处为新的短字符串
		#print (new_str)
		for a in range(0,(len(new_str)+i)):   
			list1.append(short_str[i:i+a+1])  #每次累加一个字符，产生从该字符起始到结束的所有组合（4,45,456,4561,...），存到list1
			#print (short_str[i:a+1])
#print (len(list1))

for each in list1:                            
	if each in long_str:                       #检测list1中的元素是否存在于长字符串中
		list2.append(each) 					   #存在的话添加到list2
print (set(list2))
list3=sorted(set(list2),key=len,reverse=False)     #对list2进行由短到长的排序，存成list3(此步可省略)
test_str="-".join(list3)						   #将list2串联成一个字符串test_str
for m in list3:
	match=re.findall(m,test_str) 				  #对于list3中的每个元素，查找塌是否存在于test_str中
	if len(match)>1:							  #如果仅存在一次就输出（把重复的去掉，比如AB属于ABC和ABCD，所以去掉AB）
		pass
	else:
		print (match)





		
	
	

		