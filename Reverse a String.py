def reverse(word):
    if len(word)<2:
        return word #base case
    else:
        #inductive step
        return word[-1]+reverse(word[1:-1])+word[0]
