import re

short_str='M4561GABCDEFG2abcvg777'
long_str='123456ABCDEFGabcvg778'
list1=[]
list2=[]
list2=[]
for i in range(0,len(short_str)):   
	if short_str[i] in long_str:      
		new_str=short_str[i:]         
		#print (new_str)
		for a in range(0,(len(new_str)+i)):   
			list1.append(short_str[i:i+a+1]) 
			#print (short_str[i:a+1])
#print (len(list1))

for each in list1:                            
	if each in long_str:                      
		list2.append(each) 					 
print (set(list2))
list3=sorted(set(list2),key=len,reverse=False)    
test_str="-".join(list3)					
for m in list3:
	match=re.findall(m,test_str) 				  
	if len(match)>1:							 
		pass
	else:
		print (match)





		
	
	

		
