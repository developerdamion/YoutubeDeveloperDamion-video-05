"""
Hey! Thank you for supporting my youtube channel 
( https://www.youtube.com/channel/UCKrs-v_MlKjzVbe4jyLSrPQ ). 

This is video-05: quickSort Algorithm
( https://youtu.be/7QvC3iC0Smg )

DeveloperDamion
"""

def quickSort(unsortedArray = []):

	if len(unsortedArray) <= 1: return unsortedArray

	largerArray = []
	smallerArray = []
	equalArray = []

	pivotPoint = unsortedArray[ int(len(unsortedArray)/2) ]

	for index in unsortedArray:
		if index > pivotPoint:
			largerArray.append(index)
		elif index < pivotPoint:
			smallerArray.append(index)
		else:
			equalArray.append(index)


	return quickSort(smallerArray) + equalArray + quickSort(largerArray)



if __name__ == "__main__":
	unsortedArray = [4,10,8,7,5]
	print( quickSort(unsortedArray) )