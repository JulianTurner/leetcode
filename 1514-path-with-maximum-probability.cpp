#include <vector>
#include <assert.h>
#include <queue>
#include <iostream>
#include <map>
#include <array>


class Solution {
public:
    double maxProbability(int n, std::vector<std::vector<int>>& edges, std::vector<double>& succProb, int start_node, int end_node) {
        std::map<int, std::vector<std::pair<int, int>>> graph{}; //<srcNode, <<targetNode, succProbIndex>>>
        for(int i = 0; i < edges.size(); i++) {
            auto edge = edges[i];
            graph[edge[0]].emplace_back(edge[1], i);
            graph[edge[1]].emplace_back(edge[0], i);
        }
        std::vector<double> foundProbs(n);
        foundProbs[start_node] = 1.0;

        std::priority_queue<std::pair<double, int>> toDo{};
        toDo.emplace(foundProbs[start_node], start_node);

        while (!toDo.empty())
        {
            std::pair<double, int> next = toDo.top();
            toDo.pop();

            if (next.second == end_node)
            {
                return next.first;
            }

            if (graph.count(next.second))
            {
                for (const auto& [targetNode, succProbIndex]: graph[next.second])
                {
                    double reachWithProp = next.first * succProb[succProbIndex];

                    if (reachWithProp > foundProbs[targetNode])
                    {
                        foundProbs[targetNode] = reachWithProp;
                        toDo.emplace(foundProbs[targetNode], targetNode);
                    }
                    
                }
                
            }
            
        }
        return 0.0;
    }
};

int main(int argc, char const *argv[])
{
    int n = 3;
    std::vector<std::vector<int>> edges{{0,1}, {1,2}, {0,2}};
    std::vector<double> succProb{0.5, 0.5, 0.2};
    int start = 0;
    int end = 2;
    double result = Solution().maxProbability(n, edges, succProb, start, end);
    std::cout << result << std::flush;
    return 0;
}
