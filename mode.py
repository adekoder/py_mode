def find_mode(seq):

	num_occurance={}
	
	for num in seq:
		if num not in num_occurance:
			num_occurance[num] = seq.count(num)
		
	mode_list = []
	
	max_occurance  = max(num_occurance.values())
	if max_occurance == 1: # if the number count is not great
		return None
	#used to get the numbers  that occured most 
	
	for key in num_occurance.keys():
		if  num_occurance[key] == max_occurance:
			mode_list.append(key)  #used to get all the number that occured same times and is the maximum
	return mode_list , max_occurance
	



result = find_mode([1,2,2,3,4,5,3,7,7,8,8,9,9,8,9,0,9,7,5,4,2,3,5,6,7,1,2,12,3,4,33])
if result != None:
	print("the mode %s , ocurances %sx "%(result[0] , result[1]))
else:
	print("no mode")


