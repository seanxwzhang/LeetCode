// A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

// Return a deep copy of the list.

/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
 #include <unordered_map>

 using namespace std;
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (!head)
            return NULL;
        unordered_map<RandomListNode *, RandomListNode *> hashmap;
        RandomListNode* start = head;
        RandomListNode* copy = new RandomListNode(head->label);
        RandomListNode* start_copy = copy;
        hashmap[head] = copy;
        while(head->next) {
            head = head->next;
            copy->next = new RandomListNode(head->label);
            copy = copy->next;
            copy->label = head->label;
            hashmap[head] = copy;
        }
        while(start) {
            hashmap[start]->random = hashmap[start->random];
            start = start->next;
        }
        return start_copy;
    }
};