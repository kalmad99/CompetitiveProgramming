def findMergeNode(head1, head2):
    passed = {}
    while head1 is not None:
        passed[head1] = head1.data
        head1 = head1.next
    while head2 is not None:
        if head2 in passed:
            return head2.data
        head2 = head2.next

    s1 = []
    s2 = []
    ans = 0
    while head1 is not None:
        s1.append(head1)
        head1 = head1.next
    while head2 is not None:
        s2.append(head2)
        head2 = head2.next

    if len(s1) > len(s2): 
        mini = len(s2)
    else:
        mini = len(s1)

    counter = 0
    while counter < mini:
        if s1[-1] == s2[-1]:
            ans = s1[-1].data
        s1.pop()
        s2.pop()
        counter += 1

    return ans
