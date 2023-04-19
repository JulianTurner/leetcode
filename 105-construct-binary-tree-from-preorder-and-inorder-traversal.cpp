#include <iostream>
#include <vector>
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
    TreeNode *buildTree(std::vector<int> &preorder, std::vector<int> &inorder)
    {
        return helper(0, 0, inorder.size() - 1, preorder, inorder);
        // buildTree(preorder[0], for inOrder bis i == preorder[0])
    }

    TreeNode *helper(int preStartIndex, int inOrderStartIndex, int inOrderEndIndex, std::vector<int> &preorder, std::vector<int> &inorder)
    {
        if (preStartIndex > preorder.size() - 1 || inOrderStartIndex > inOrderEndIndex)
        {
            return nullptr;
        }

        int rootValue = preorder[preStartIndex];

        int rootIndexInOrder = std::find(inorder.begin(), inorder.end(), rootValue) - inorder.begin();
        TreeNode *left = helper(preStartIndex + 1, inOrderStartIndex, rootIndexInOrder - 1, preorder, inorder);

        int leftSideElements = rootIndexInOrder - inOrderStartIndex;

        TreeNode *right = helper(preStartIndex + 1 + leftSideElements, rootIndexInOrder + 1, inOrderEndIndex, preorder, inorder);

        TreeNode *root = new TreeNode{rootValue, left, right};
        return root;
    }
};

int main()
{
    std::vector<int> preOrder{3, 9, 20, 15, 7};
    std::vector<int> inOrder = {9, 3, 15, 20, 7};

    Solution sl{};
    TreeNode *res = sl.buildTree(preOrder, inOrder); // 3,9,20,null,null,15,7
    // std::cout << res << std::endl;
    delete res;
    return 0;
}
