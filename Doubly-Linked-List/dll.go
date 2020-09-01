package main

import (
  "fmt"
)

type Node struct {
  data int
  prev *Node
  next *Node
}

func main() {
  var head *Node

  for i := 1; i <= 5; i++ {
    head = insertAtBeginning(head, i)
  }
  printListReverse(head)
}

func insertAtBeginning(head *Node, data int) *Node {
  // create a new node
  newNode := &Node{}
  newNode.data = data

  // If the list is empty
  if head == nil {
    head = newNode
    return head
  }

  newNode.next = head
  head.prev = newNode
  head = newNode
  return head
}

func printList(head *Node) {
  for current := head; current != nil; current = current.next {
    fmt.Printf("%d ", current.data)
  }
}

func printListReverse(head *Node) {

  if head == nil {
    return
  }

  var reversePointer *Node

  // Traverse to the last node of the doubly linked list
  for current := head; current != nil; current = current.next {
    reversePointer = current
  }

  // Traverse back to the first node of the doubly linked list
  for ; reversePointer != nil; reversePointer = reversePointer.prev {
    fmt.Printf("%d ", reversePointer.data)
  }
}
