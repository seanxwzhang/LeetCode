// Given a nested list of integers, implement an iterator to flatten it.

// Each element is either an integer, or a list -- whose elements may also be integers or other lists.

// Example 1:
// Given the list [[1,1],2,[1,1]],

// By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

// Example 2:
// Given the list [1,[4,[6]]],

// By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
#include <stack>
#include <vector>
#include <deque>

using namespace std;
class NestedIterator {
    deque<vector<NestedInteger> *> stack;
    deque<unsigned> indStack;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        indStack.push_back(0);
        stack.push_back(&nestedList);
    }

    int next() {
        this->hasNext();    
        auto cur_stack_ptr = stack.back();
        auto cur_index = indStack.back();
        auto res = (*cur_stack_ptr)[cur_index].getInteger();
        indStack.back()++;
        return res;
    }

    bool hasNext() {
        while(!indStack.empty()) {
            auto cur_stack_ptr = stack.back();
            auto cur_index = indStack.back();
            if (cur_index == cur_stack_ptr->size()) {
                indStack.pop_back();
                stack.pop_back();
            } else {
                if ((*cur_stack_ptr)[cur_index].isInteger())
                    return true;
                indStack.back()++;
                stack.push_back(&((*cur_stack_ptr)[cur_index].getList()));
                indStack.push_back(0);
            }
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */