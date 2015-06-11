=begin
Insertion Sort Advanced Analysis
Insertion Sort is a simple sorting technique which was covered in previous challenges. In the running time challenge, we directly counted how many shifts (or swaps) it takes for insertion sort to finish sorting an array. However, some arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of times Insertion Sort shifts over elements when sorting an array?

Input:
The first line contains the number of test cases T. T test cases follow. The first line for each case contains N, the number of elements to be sorted. The next line contains N integers a[1],a[2]…,a[N].

Output:
Output T lines, containing the required answer for each test case.

Constraints:
1 <= T <= 5
1 <= N <= 100000
1 <= a[i] <= 1000000

Sample Input:
2
5
1 1 1 2 2
5
2 1 3 1 2

Sample Output:
0
4
=end
def merge(left_arr, right_arr)
  merged_array = []
  i, j, inversions = 0, 0, 0

  for k in 0...(left_arr.size + right_arr.size) do
     if ((left_arr[i] != nil and right_arr[j] != nil and left_arr[i] <= right_arr[j]) or (left_arr[i] != nil and right_arr[j] == nil))
        merged_array << left_arr[i]
        i += 1
     else
        merged_array << right_arr[j]
        j += 1
        inversions += left_arr.size - i        
     end
  end

  return merged_array, inversions
end

def sort_and_count(arr)
  return arr, 0 if (arr.size == 1)
  
  mid = arr.size / 2;
   
  left_arr  = arr[0...mid]
  right_arr = arr[(mid)...arr.size]

  left_sorted_part, left_inversions    = sort_and_count(left_arr)
  right_sorted_part, right_inversions  = sort_and_count(right_arr)
  merged_array, merge_inversions       = merge(left_sorted_part, right_sorted_part)

  return merged_array, (left_inversions + right_inversions + merge_inversions)
end

NUMBER_OF_TEST_CASES = gets.to_i

NUMBER_OF_TEST_CASES.times do
  number_of_elements_to_be_sorted = gets.to_i
  array_of_elements_to_be_sorted = gets.strip.split.map {|i| i.to_i}

  puts sort_and_count(array_of_elements_to_be_sorted)[1]
end