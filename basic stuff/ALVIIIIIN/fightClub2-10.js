// Binary Search Tree
// - binary tree
// - at every subroot all nodes in the left subtree are < the subroot
//      - all nodes in the right are >= the subroot

//A BST is a fully ordered/strict data structure
// maintaining it is costly

// MaxHeap
// - binary tree
// - at every subroot, all children are less than or eq than the subroot
// at any given index, its left child is index * 2
// right child is index * 2 + 1

class MaxHeap {
    constructor() {
        this.array = [Infinity];
    }

    insert(val) {
        this.array.push(val);
        this.siftUp(this.array.length - 1);
    }

    siftUp(targetIdx) {
        const parentIdx = Math.floor(targetIdx / 2);
        // if my target val is greater than parent val, swap.
        if (this.array[targetIdx] > this.array[parentIdx]) {
            const temp = this.array[parentIdx];
            this.array[parentIdx] = this.array[targetIdx];
            this.array[targetIdx] = temp;
            this.siftUp(parentIdx)
        }
    }
}