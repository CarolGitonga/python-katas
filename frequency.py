def frequency_occurences(stringList, queryList):
    # Create a dictionary to store the frequency of each string in the input list
    string_counts = {}
    for n in stringList:
        if n in string_counts:
            string_counts[n] += 1
        else:
            string_counts[n] = 1    
   # Create an array to store the results
    results = []    

  # Iterate through the query list
    for q in queryList:  
        # Look up the frequency of the query string in the dictionary
        if q in string_counts:
            results.append(string_counts[q])
        else:
            results.append(0)
    # Return the array of results
    return results  
# Print the list
stringList = ['ab', 'ab', 'abc']
queryList = ['ab', 'abc', 'bc']
print(frequency_occurences(stringList, queryList))         