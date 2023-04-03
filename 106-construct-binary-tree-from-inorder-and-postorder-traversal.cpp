#include <iostream>
#include <queue>
#include <algorithm>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

    ~TreeNode()
    {
        delete left;
        delete right;
    }
};
class Solution
{
public:
    TreeNode *buildTree(std::vector<int> &inorder, std::vector<int> &postorder)
    {
        if (inorder.empty())
            return nullptr;
        if (inorder.size() == 1)
        {
            return new TreeNode{inorder[0]};
        }

        int rootInt = postorder[postorder.size() - 1];

        TreeNode *root = new TreeNode{rootInt};

        auto iteratorOnRoot = std::find(inorder.begin(), inorder.end(), rootInt);
        int rootIndex = iteratorOnRoot - inorder.begin();

        std::vector<int> leftInorder{inorder.begin(), iteratorOnRoot};
        std::vector<int> leftPostorder{postorder.begin(), postorder.begin() + leftInorder.size()};

        std::vector<int> rightInorder{iteratorOnRoot + 1, inorder.end()};
        std::vector<int> rightPostorder{postorder.end() - 1 - rightInorder.size(), postorder.end() - 1};

        root->left = buildTree(leftInorder, leftPostorder);
        root->right = buildTree(rightInorder, rightPostorder);

        return root;
    }
};

int main()
{
    std::vector<int> preOrder{9, 3, 15, 20, 7};
    std::vector<int> postOrder = {9, 15, 7, 20, 3};

    Solution sl{};
    TreeNode *res = sl.buildTree(preOrder, postOrder);
    // std::cout << res << std::endl;
    return 0;
}
