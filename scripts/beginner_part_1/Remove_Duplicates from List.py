class Remove_Duplicates:
	
	def __init__(self, list1):
		self.list=list1
	
	def remove(self): 
		final_list = [] 
		for num in self.list:
			if num not in final_list: 
				final_list.append(num) 
		return final_list 


list = [1, "hello", 8, 1, "hello", 4, 2] 
removeclass = Remove_Duplicates(list)
print(removeclass.remove())


