"""
Date: 2021 04 09
Problems: CV + Code
Result: Pass
        The interview experience is the best till now. Very nice interviewer.
"""
from collections import deque


class Node:
    def __init__(self):
        self.val = ""
        self.children = []


class Problem1:
    """
    Print N-ary Tree

    @FakeMesa ~/P/A/mola (master)> tree
    .
    ├── README.md
    ├── charts
    │   └── mola
    │       ├── Chart.yaml
    │       ├── README.md
    │       ├── templates
    │       │   ├── autoscaling.yaml
    │       │   ├── deployment.yaml
    │       │   ├── nginx-config.yaml
    │       │   ├── scheduledscaling.yaml
    │       │   ├── service.yaml
    │       │   ├── serviceaccount.yaml
    │       │   └── sigsci-config.yaml
    │       └── values.yaml
    ├── cw-fill-query.json
    ├── pipelines
    │   ├── auto-multi-deploy.pp
    │   ├── delete-resources.pp
    │   └── simple-deploy.pp
    └── values
        ├── aor.yaml
        ├── ava.yaml
        ├── base_values.yaml
        └── target_environment_values.yaml

    I defined the Node class.
    The interviewer defined the tree generation function and the test sample when I wrote the BFS.

    I - Consider corner case exception?
    Int - No.

    Wrote the BFS, stuck.

    I - Can we have a pointer designating the parent in the Node class?
    Int - Yes, but it is not difficult as you think. How do you traverse the tree to print the example?
    I - Preorder if we treat the top as left.
    Int - Yes.

    Wrote the DFS, stuck.

    Int - How much space you need to indent?
    I - Depends on the depth of the tree.

    Wrote the depth, stuck in \beta.

    Int - You can concatenate the string out of for loop.
    I - Still stuck.
    Int - WROTE \beta himself!

    Int - You did not print leaves.
    I - Try to add new print commands in \alpha.
    Int - You can simply remove \alpha.

    Finished.
    """

    def mNode(self, val, children):
        n = Node()
        n.val = val
        n.children = children
        return n

    def BFS(self, root):
        q = deque()
        q.append(root)
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                level.append(n.val)
                for child in n.children:
                    q.append(child)
            res.append(level)

    def traverse(self, root, depth):
        # \alpha
        # if not root.children:
        #     return
        # \alpha

        # \beta
        result = ""
        for _ in range(depth):
            result += "|   "
        # \beta

        result += "──" + "  " + root.val
        print(result)

        depth += 1

        for child in root.children:
            self.traverse(child, depth + 1)


if __name__ == "__main__":
    sol = Problem1()

    r = sol.mNode("root", [
        sol.mNode("folder1", [
            sol.mNode("folder11", [
                sol.mNode("file1", [])
            ]),
            sol.mNode("file2", []),
        ]),
        sol.mNode("file3", []),
        sol.mNode("folder2", [
            sol.mNode("file4", [])
        ])
    ])

    sol.traverse(r, 0)
