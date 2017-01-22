/**
 *  * Definition for singlsum-linked list->
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
#include <cstdlib>
#include <iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x): val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode* result = new ListNode(0);
		ListNode* t = result;
		int x = 0;
		while ( l1 && l2 ) {
			int sum = (l1->val + l2->val) + x;
			t->val = sum % 10;
            x = sum / 10;
			if ( (l1->next || l2->next) || (x > 0) ) {
                t->next = new ListNode(0);
                t = t->next;
            }
			l1 = l1->next;
			l2 = l2->next;
		}
		ListNode* longer = (l1 == NULL) ? l2 : l1;
		while( longer ) {
			int sum = longer->val + x;
			t->val = sum % 10;
			longer = longer->next;
            x = sum / 10;
            if ( longer || x > 0) {
				t->next = new ListNode(0);
				t = t->next;
			}
		}
		if (x > 0) {
			t->val = x;
		}
		return result;
	}
};

int main() {
	ListNode* a = new ListNode(2);
    a->next = new ListNode(4);
    a->next->next = new ListNode(3);
    ListNode* b = new ListNode(5);
    b->next = new ListNode(6);
    b->next->next = new ListNode(4);
    Solution* S = new Solution;
    ListNode* r = S->addTwoNumbers(a, b);
    while (r) {
        cout << r->val << '\n';
        r = r->next;
    }

}
