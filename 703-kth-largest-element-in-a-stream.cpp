#include <vector>
#include <assert.h>
#include <queue>
#include <iostream>

class KthLargest
{
private:
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> pQ{};

public:
    KthLargest(int k, std::vector<int> &nums) : k(k)
    {
        for (auto num : nums)
        {
            if (pQ.size() < k)
            {
                pQ.push(num);
            }
            else
            {
                if (num > pQ.top())
                {
                    pQ.pop();
                    pQ.push(num);
                }
            }
        }
    }

    int add(int val)
    {
        if (pQ.empty() || pQ.size() < k)
        {
            pQ.push(val);
        }
        else if (val > pQ.top())
        {
            pQ.pop();
            pQ.push(val);
        }

        return pQ.top();
    }
};

int main(int argc, char const *argv[])
{
    std::vector<int> initial = {0};
    KthLargest kthLargest{2, initial};

    assert(kthLargest.add(-1) == -1); // return 4
    assert(kthLargest.add(1) == 0);   // return 5
    assert(kthLargest.add(-2) == 0);  // return 5
    assert(kthLargest.add(-4) == 0);  // return 8
    assert(kthLargest.add(3) == 1);   // return 8

    // std::vector<int> initial = {4, 5, 8, 2};
    // KthLargest kthLargest{3, initial};

    // assert(kthLargest.add(3) == 4);  // return 4
    // assert(kthLargest.add(5) == 5);  // return 5
    // assert(kthLargest.add(10) == 5); // return 5
    // assert(kthLargest.add(9) == 8);  // return 8
    // assert(kthLargest.add(4) == 8);  // return 8
    std::cout << "Success" << std::flush;
    return 0;
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */