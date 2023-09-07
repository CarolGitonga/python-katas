def count_times(stringList, queryList):
    # Create an array to store the results
    results = []
    # Iterate through the query list
    for q in queryList:
        count = 0
    # Iterate through the input list and count the occurrences of the query string
        for n in stringList:
            count += n.count(q)
        results.append(count)
    # Return the array of results
    return results

stringList = ['ab', 'ab', 'abc']
queryList = ['ab', 'abc', 'bc']
print(count_times(stringList, queryList))