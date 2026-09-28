class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def append (self, data):
        if self.head:
            curnode = self.head
            while curnode.next:
                curnode = curnode.next
            curnode.next = Node(data)
        else:
            self.head = Node(data)
    def print(self):
        if self.head:
            curnode = self.head
            while curnode:
                print(curnode.data)
                curnode = curnode.next
        else:
            print('aaaaaaaaaaaaa')


    def append_rec(self, data):
        if self.head:
            self._append(self.head, data)
        else:
            self.head=Node(data)


    def _append(self, node, data):
        if node.next is None:
            node.next = Node(data)
            return
        return self._append(node.next, data)

    def delete(self, n):
        if self.head:
            curnode = self.head
            count=0
            prev = None
            while curnode:
                if count==n:
                    if prev:
                        prev.next = curnode.next
                    else:
                        self.head = curnode.next
                    return curnode.data
                count += 1
                prev = curnode
                curnode = curnode.next



    def delete_v2(self, n):
        if self.head:
            if n==0:
                for_del = self.head
                self.head = self.head.next
            curnode = self.head
            count=0

            while curnode:
                if count==n-1:
                    for_del=curnode.next
                    curnode.next = curnode.next.next
                    return for_del.data
                count += 1
                curnode = curnode.next

    def delete_v3(self,n):
        if self.head:
            if n==0:
                for_del=self.head
                self.head = self.head.next
                return for_del
            return self._delete(self.head, 0, n)

    def _delete(self, node, count, n):
        if count==n-1 and node.next:
            for_del = node.next
            node.next = node.next.next
            return for_del
        count+=1
        self._delete(node.next, count, n)

    def insert(self, n, data):
        if self.head:
            if n==0:
                curnode = self.head
                self.head=Node(data, curnode)
                return
            return self._insert( self.head,n,0,data)


    def _insert(self, node, n, count, data):
        if node:
            if count ==n-1:
                curnode = node.next
                node.next=Node(data, curnode)
                return
            count+=1
            self._insert(node.next,n,count,data)
        else:
            return

    def reverse(self):
        prev = None #тут храним предыдущий узел, чтобы на него переставить указатель, но так как
        #голова станет хвостом, она должна указывать на None, поэтому сначал сюда None, а потом остальные
        #узлы по очереди
        curnode = self.head #тут храним текущий узел, которому переставляем указатель, начинаем это делать
        #с головы
        while curnode: #пока существует новый узел
            nextnode = curnode.next #запоминаем, кто стоит за текущим узлом, потому что иначе, когда мы переставим
            #текущему узлу указатель, мы потеряем следующий навсегда
            curnode.next = prev #меняем текующему узлу ссылку с того, кто спарва от него (следущий), на того
            #кто слева от него (предыдущий)
            prev = curnode #запоминаем только что обработанный узел как предыдущий для следующего узла, чтобы
            #потом на него переставить указатель
            curnode = nextnode #передвигаемся на следующий узел, который предусмотрительно запомнили в начале
            #цикла
        self.head = prev #после того, как все указатели переставили, поледний узел, с которым мы работыли,
        #объявляем головой


lst = LinkedList()
lst.append_rec(10)
lst.append_rec(20)
lst.append_rec(40)
lst.insert(2,5)
lst.print()
lst.reverse()
print()
lst.print()
