#include <iostream>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool isCompleteTree(TreeNode *root)
    {
        std::cout << "Hello";

        return true;
    }
};

int main()
{
    // ich starte mal neu obwohl es daran warwscheinlich nicht liegt
    TreeNode root(1, &TreeNode(2, &TreeNode(4), &TreeNode(5)), &TreeNode(3, &TreeNode(6), nullptr));

    Solution sl{};
    bool res = sl.isCompleteTree(&root);
    std::cout << res << std::endl;
    return 0;
}
