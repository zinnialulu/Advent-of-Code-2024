input = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]


def stone(mylist: list, memo: dict):
    new_list = []
    for n in mylist:
        # If the value is already in memo, reuse the result
        if n in memo:
            if type(memo[n])==list:
                new_list.append(memo[n][0])
                new_list.append(memo[n][1])
            else:
                new_list.append(memo[n])
        else:
            # Compute the result for this value and store it in memo
            if n == 0:
                memo[0]=1
                new_list.append(1)  # If the number is 0, replace it with 1
            elif len(str(n)) % 2 != 0:
                memo[n]=n*2024
                new_list.append(n * 2024)  # If odd number of digits, multiply by 2024
            else:
                # For even number of digits, split the number into two parts
                l = int(len(str(n)) / 2)
                n_str = str(n)
                # Store the result in the memo dictionary
                memo[n]=[int(n_str[:l]), int(n_str[l:])]
                new_list.append(int(n_str[:l]))
                new_list.append(int(n_str[l:]))
        #print(f"current list is: {new_list}")
        #print(f"current memo is {memo}")
    return new_list

memo={}
def optimize_iterations(input, iterations):
    #memo = {}  # Dictionary to store previously computed values
    for i in range(1, iterations + 1):
        input = stone(input, memo)
        
        # Print some debug information to check the state of the list
        # print(f"Iteration {i}, Current list length: {len(input)}")
        # print(f"memo is {memo}")
        # print(f"Current list: {input}...")  # Only print the first 10 elements for debugging
        print(i)   
    return input, memo

# Run the function for 75 iterations
final_result, memo = optimize_iterations(input, 25)
final_result, memo = optimize_iterations(input, 75)

# Print the number of unique calculations stored in the memoization dictionary
print(f"Total unique values in memo after 75 iterations: {len(memo)}")

