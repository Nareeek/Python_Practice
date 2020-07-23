    def reverse_list(head):
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head
        