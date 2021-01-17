def has_cycle(head):
    temp = head
    passed = []
    while temp.next is not None:
        if temp not in passed:
            passed.append(temp)
        else:
            break
        temp = temp.next
    if temp.next is None:
        return 0
    else:
        return 1