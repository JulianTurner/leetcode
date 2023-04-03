#include <iostream>
#include <queue>

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
    bool isCompleteTree(TreeNode *root)
    {
        std::queue<TreeNode *> queue;
        queue.push(root);

        bool blockInserts = false;

        while (!queue.empty())
        {
            TreeNode &currentNode = *(queue.front());

            if (currentNode.left)
            {
                if (blockInserts)
                {
                    return false;
                }

                queue.push(currentNode.left);
            }
            else
            {
                blockInserts = true;
            }

            if (currentNode.right)
            {
                if (blockInserts)
                {
                    return false;
                }

                queue.push(currentNode.right);
            }
            else
            {
                blockInserts = true;
            }

            queue.pop();
        }

        return true;
    }
};

int main()
{
    TreeNode root(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, nullptr, new TreeNode(7)));

    Solution sl{};
    bool res = sl.isCompleteTree(&root);
    std::cout << res << std::endl;
    return 0;
}
