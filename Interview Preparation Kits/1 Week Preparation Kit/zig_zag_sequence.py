# Below shows the original code for the problem that is suppose to zig zag an array of numbers. Only 3 lines of code or less must be modified in the original code to make the "findZigZagSequence" work properly.

# Original Code
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


# Solution
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2) # This line was changed to always receive the middle or lower-middle index of an odd or even array respectively
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # This line was changed since st and ed are variables to switch numbers in different positions. After switching the modified middle index or a[mid] and a[n-1], then the third and second to last indexes are meant to be switched. Modifying this line switches the third and second to last indexes.
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # change this line to execute and eventually exit out of the while loop

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
