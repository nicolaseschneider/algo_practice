// heap is a binary tree based data structure
// where the parent node fulfills the heap property, being that of a max or min heap

// Usage
// priority queue
// in a heap the highest(or lowest) priority element is always stored in the root element
// this is useful when it is necessary to repeatedly remove the object with the highest priority

// there is no implied ordering in a binary heap

// Binary heaps are binary trees with the following properties
// 1) it is a complete tree meaning all levels are filled out (barring the last level maybe)
// // this property allows binary heaps to be storable in arrays
// 2) A binary heap is either a min or max heap. In a min binary heap, The root node must be the lowest value
// // this property must be recursively true for all other nodes in the tree. Max is the same

// a binary heap is a complete binary tree, which can be represented in an array
// 
const BINARY_MIN_HEAP_EXAMPLE = [1,3,6,5,9,8];
// the root element is always at arr[0]
// arr[ Math.floor( ( i - 1 ) / 2 ) ] will return the parent node for a given index; javascript
// python the formula is arr[(i-1)/2], much cleaner
// arr[ (2 * i) + 1 ] returns the left child node
// arr[ (2 * i) + 2 ] returns the right child
