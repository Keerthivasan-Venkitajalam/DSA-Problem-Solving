/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // dummy node to simplify handling the head of the result list
        ListNode* dummyHead = new ListNode(0);
        ListNode* current = dummyHead;

        int carry = 0;

        // loop until both lists are exhausted and no carry is left
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;  // update carry for next digit

            // create a new node with the digit value of the current sum
            current->next = new ListNode(sum % 10);
            current = current->next;

            // move to the next nodes in both lists
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        // return the next node of dummy (head of the result)
        return dummyHead->next;
    }
};
