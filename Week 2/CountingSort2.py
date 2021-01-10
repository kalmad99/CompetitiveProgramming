def count(nums):
    total = 0
    intmax = 0
    countarray = []
    output = []
    arr = []
    for i in nums:
        if i > intmax:
            intmax = i

    for i in range(intmax+1):
        countarray.append(0)

    for i in nums:
        output.append(0)
        countarray[i]+=1

    for i in countarray:
        total += i
        arr.append(total)

    for i in range(len(nums)):
        output[arr[nums[i]]-1] = nums[i]
        arr[nums[i]]-=1

    return output

print(count([2, 4, 1, 3, 5]))
print(count([1,2,3,4,5]))
print(count([2, 12, 2, 1, 5, 3]))
print(count([10, 7, 12, 4, 9, 13]))



# // Java implementation of Counting Sort
# class CountingSort { 
# 	void sort(char arr[]) 
# 	{ 
# 		int n = arr.length; 
# 
# 		// The output character array that will have sorted arr 
# 		char output[] = new char[n]; 
# 
# 		// Create a count array to store count of inidividul 
# 		// characters and initialize count array as 0 
# 		int count[] = new int[256]; 
# 		for (int i = 0; i < 256; ++i) 
# 			count[i] = 0; 
# 
# 		// store count of each character 
# 		for (int i = 0; i < n; ++i) 
# 			++count[arr[i]]; 
# 
# 		// Change count[i] so that count[i] now contains actual 
# 		// position of this character in output array 
# 		for (int i = 1; i <= 255; ++i) 
# 			count[i] += count[i - 1]; 
# 
# 		// Build the output character array 
# 		// To make it stable we are operating in reverse order. 
# 		for (int i = n - 1; i >= 0; i--) { 
# 			output[count[arr[i]] - 1] = arr[i]; 
# 			--count[arr[i]]; 
# 		} 
# 
# 		// Copy the output array to arr, so that arr now 
# 		// contains sorted characters 
# 		for (int i = 0; i < n; ++i) 
# 			arr[i] = output[i]; 
# 	} 
# 
# 	// Driver method 
# 	public static void main(String args[]) 
# 	{ 
# 		CountingSort ob = new CountingSort(); 
# 		char arr[] = { 'g', 'e', 'e', 'k', 's', 'f', 'o', 
# 					'r', 'g', 'e', 'e', 'k', 's' }; 
# 
# 		ob.sort(arr); 
# 
# 		System.out.print("Sorted character array is "); 
# 		for (int i = 0; i < arr.length; ++i) 
# 			System.out.print(arr[i]); 
# 	} 
# } 
# /*This code is contributed by Rajat Mishra */

# Python program for counting sort

# The main function that sort the given string arr[] in
# alphabetical order
# def countSort(arr):
#
# 	# The output character array that will have sorted arr
# 	output = [0 for i in range(len(arr))]
#
# 	# Create a count array to store count of inidividul
# 	# characters and initialize count array as 0
# 	count = [0 for i in range(256)]
#
# 	# For storing the resulting answer since the
# 	# string is immutable
# 	ans = ["" for _ in arr]
#
# 	# Store count of each character
# 	for i in arr:
# 		count[ord(i)] += 1
#
# 	# Change count[i] so that count[i] now contains actual
# 	# position of this character in output array
# 	for i in range(256):
# 		count[i] += count[i-1]
#
# 	# Build the output character array
# 	for i in range(len(arr)):
# 		output[count[ord(arr[i])]-1] = arr[i]
# 		count[ord(arr[i])] -= 1
#
# 	# Copy the output array to arr, so that arr now
# 	# contains sorted characters
# 	for i in range(len(arr)):
# 		ans[i] = output[i]
# 	return ans
#
# # Driver program to test above function
# arr = "geeksforgeeks"
# ans = countSort(arr)
# print("Sorted character array is % s" %("".join(ans)))
#
# # This code is contributed by Nikhil Kumar Singh
