package main

import(
  "fmt"
)

type Node struct {
  data int
  next *Node
}

func main() {
  var head *Node
  for i := 1; i <= 5; i++ {
    head = insertAtBeginning(head, i)
  }
  printList(head)
}

func insertAtBeginning(head *Node, data int) *Node {
  // create a new node
  newNode := &Node{}
  newNode.data = data
  newNode.next = head
  head = newNode

  return head
}

func printList(head *Node) {
  for current := head; current != nil; current = current.next {
    fmt.Printf("%d ", current.data)
  }
}
