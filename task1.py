"""
Author: ng ka ho (32360770)

Taks 1
For example, given the list: [8,3,5,1], your program should output 8351.
"""

def combine_number_to_string(numbers):
    """ 
    combine the numbers into string

	Parameters
	----------
	numbers: int[] 
		a int array to be cominbed into string

	Returns
	----------
	result : string
        the result of combination of int []
	"""
    
    result = ""
    
    # check the array is not empty first
    if len(numbers) == 0:
        print("Cannot be empty")
        return result

    # start to combine the number
    for number in numbers:
        result += f"{number}"

    return result

if __name__ == "__main__":
    taks1 = combine_number_to_string([8,3,5,1])
    print(taks1)
