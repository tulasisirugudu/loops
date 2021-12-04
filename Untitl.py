# char maxRepeating(string str)
# {
#     int n = str.length();
#     int count = 0;
#     char res = str[0];
#     int cur_count = 1;
 
#     // Traverse string except last character
#     for (int i=0; i<n; i++)
#     {
#         // If current character matches with next
#         if (i < n-1 && str[i] == str[i+1])
#             cur_count++;
 
#         // If doesn't match, update result
#         // (if required) and reset count
#         else
#         {
#             if (cur_count > count)
#             {
#                 count = cur_count;
#                 res = str[i];
#             }
#             cur_count = 1;
#         }
#     }
 
#     return res;
# }
 
# // Driver code
# int main()
# {
#     string str = "aaaabbaaccde";
#     cout << maxRepeating(str);
#     return 0;
# }
# Python program to
# compute sum of digits in 
# number.
   
# Function to get sum of digits 
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 12345
print(getSum(n))
