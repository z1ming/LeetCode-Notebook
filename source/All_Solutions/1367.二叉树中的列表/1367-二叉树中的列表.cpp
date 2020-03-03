class Solution {
    bool work(ListNode* head, TreeNode* root)
    {
        if(head==nullptr)return 1;
        if(root==nullptr||root->val!=head->val)return 0;
        return work(head->next,root->left)||work(head->next,root->right);
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if(root==nullptr)return 0;
        return work(head,root)||isSubPath(head,root->left)||isSubPath(head,root->right);
    }
};