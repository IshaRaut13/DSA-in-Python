"""Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.
Return the maximum score that can be obtained.

Example 1
Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3
Output : 15
Explanation : Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4 , 5 , 6.
Th score is 4 + 5 + 6 => 15."""

"""condition is you can pick cards from start or end but not from middle
Eg: 6,2,3,1 - three from start & one from end
    6,2,3,4 - all from start
    1,7,1,2 - all from end
    1,7,1,6 - three from end & one from start"""


def maxPoint(arr, k):
    lsum, rsum, maxsum = 0, 0, 0
    for i in range(k):
        lsum += arr[i]
        maxsum = lsum

    # rindex is pointing at last index
    rindex = len(arr) - 1
    for i in range(k - 1, -1, -1):
        lsum -= arr[i]
        rsum += arr[rindex]
        rindex -= 1
        maxsum = max(maxsum, (lsum + rsum))
    return maxsum


arr = [6, 2, 3, 4, 7, 2, 1, 7, 1]
# k are the number of cards to be picked up
k = 4
print("Maximum Point obtained from the card is", maxPoint(arr, k))
