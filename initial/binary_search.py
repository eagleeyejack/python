def binary_search(x, search_list):
		iterations = 1
		left = 0 # Determines the starting index of the list we have to search in
		right = len(search_list)-1 # Determines the last index of the list we have to search in
		mid = (right + left)//2 # In Python, // means floored division, 
		while search_list[mid] != x: # If this is not our search element
				# If the current middle element is less than x then move the left next to mid
				# Else we move right next to mid
				if  search_list[mid] < x:
						left = mid + 1
				else:
						right = mid - 1
				mid = (right + left)//2
				iterations += 1
				print('iterations = ' + str(iterations))
				
		return mid

print(binary_search(99, [4,8,9,10,24,32,45,56, 99]))