# Problem Set 4A
# Name: João Mota
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    print(sequence)
    if len(sequence) == 1:
        return [sequence]

    permutations = []
    for i, char in enumerate(sequence):
        # Remove the current character from the sequence
        rest = sequence[:i] + sequence[i+1:]
        # Recursively get permutations of the rest of the sequence
        sub_permutations = get_permutations(rest)
        # Add the current character to the beginning of each sub-permutation
        for sub_perm in sub_permutations:
            permutations.append(char + sub_perm)

    return permutations

'''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''



if __name__ == '__main__':
    def test_get_permutations():
        # Test 1: Single character string
        assert get_permutations('a') == ['a'], "Test failed for single character input"

        # Test 2: Two character string
        result = get_permutations('ab')
        assert sorted(result) == sorted(['ab', 'ba']), "Test failed for two character input"

        # Test 3: Three character string
        result = get_permutations('abc')
        assert sorted(result) == sorted(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']), "Test failed for three character input"

        print("All tests passed!")


    # Run the tests
    test_get_permutations()


#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

     #delete this line and replace with your code here

