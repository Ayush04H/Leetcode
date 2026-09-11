class Node{
    int val;
    Node next;
    Node(int val){
        this.val = val ;
        this.next = null;
    }
}
class MyLinkedList {
    Node head;
    int size;

    public MyLinkedList() {
        // head is null initially, meaning the list is completely empty
        head = null; 
        size = 0;
    }
    
    public int get(int index) {
        if(index < 0 || index >= size){
            return -1;
        } 
        
        // Start directly at head since it's the first real node
        Node curr = head; 
        for(int i = 0; i < index; i++){
            curr = curr.next;
        }
        return curr.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val); 
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0 || index > size){
            return;
        }
        
        Node newNode = new Node(val);
        
        // SPECIAL CASE: Adding to the very front of the list
        if (index == 0) {
            newNode.next = head;
            head = newNode;
            size++;
            return;
        }
        
        // Normal case: adding anywhere else
        Node curr = head;
        for(int i = 0; i < index - 1; i++){ // Stop ONE node before the index
            curr = curr.next;
        }
        
        newNode.next = curr.next;
        curr.next = newNode;
        size++; 
    }
    
    public void deleteAtIndex(int index) {
        if(index < 0 || index >= size){
            return;
        }
        
        // SPECIAL CASE: Deleting the very first node
        if (index == 0) {
            head = head.next;
            size--;
            return;
        }
        
        // Normal case: deleting anywhere else
        Node curr = head;
        for(int i = 0; i < index - 1; i++){ // Stop ONE node before the index
            curr = curr.next;
        }
        
        if(curr.next != null){
            curr.next = curr.next.next;
        }
        size--; 
    }
}