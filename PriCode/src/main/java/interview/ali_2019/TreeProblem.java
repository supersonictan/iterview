package interview.ali_2019;

import javafx.util.Pair;

import java.util.*;

// TODO: 一定要能熟练地写出所有问题的递归和非递归做法！

/*
             1
            / \
           2   3
          / \   \
         4  5   6
 */
/**
 *
 * 144. 前序遍历
 * 94. 二叉树的中序遍历
 * 145. 二叉树的后序遍历
 * 102. 二叉树的层次遍历: List<List<Integer>> levelOrder(TreeNode root)
 * 107. 二叉树的层次遍历 II:自底向上 List<List<Integer>> levelOrderBottom(TreeNode root)
 * 104. 二叉树的最大深度: int maxDepth(TreeNode root)
 * 111. 二叉树的最小深度: int minDepth(TreeNode root)
 * 236. 二叉树的最近公共祖先 public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B)
 * 958. 二叉树的完全性检验
 * 222. 完全二叉树的节点个数
 * 208. 实现 Trie (前缀树)
 * 103. 二叉树的锯齿形层次遍历 public List<List<Integer>> zigzagLevelOrder(TreeNode root)
 * 124. 二叉树中的最大路径和 public int maxPathSum(TreeNode root)
 * 662. 二叉树最大宽度 public int widthOfBinaryTree(TreeNode root)
 * 257. 二叉树的所有路径
 * 113. 路径总和 II: 根节点到叶子节点路径和等于给定目标
 * 951. 翻转等价二叉树
 * 226. 翻转二叉树[简单]: TreeNode invertTree(TreeNode root)
 * 637. 二叉树的层平均值: List<Double> averageOfLevels(TreeNode root)
 *
 *
 */

public class TreeProblem {

    // 104. 二叉树的最大深度
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        int res = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int curLevNum = 1;
        int nextLevNum = 0;

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            curLevNum--;

            if (cur.left != null) {
                q.offer(cur.left);
                nextLevNum++;
            }
            if (cur.right != null) {
                q.offer(cur.right);
                nextLevNum++;
            }
            if (curLevNum == 0) {
                curLevNum = nextLevNum;
                res++;
                nextLevNum = 0;
            }
        }
        return res;
    }
    public int maxDepthRec(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int left_height = maxDepth(root.left);
            int right_height = maxDepth(root.right);
            return java.lang.Math.max(left_height, right_height) + 1;
        }
    }

    // 111. 二叉树的最小深度
    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int curLevNum = 1;
        int nextLevNum = 0;
        int res = 1;

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            curLevNum--;

            if (cur.left != null) {
                nextLevNum++;
                q.offer(cur.left);
            }
            if (cur.right != null) {
                nextLevNum++;
                q.offer(cur.right);
            }

            if (cur.left == null && cur.right == null) {
                return res;
            }

            if (curLevNum == 0) {
                res++;
                curLevNum = nextLevNum;
                nextLevNum = 0;
            }
        }
        return res;
    }
    public int minDepthRec(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return getMin(root);
    }
    public int getMin(TreeNode root){
        if (root == null) {
            return Integer.MAX_VALUE;
        }

        if (root.left == null && root.right == null) {
            return 1;
        }

        return Math.min(getMin(root.left), getMin(root.right)) + 1;
    }

    // 102. 二叉树的层次遍历
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int curLevelNum = 1;
        int nextLevelNum = 0;
        List<Integer> tmp = new ArrayList<Integer>();

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            tmp.add(cur.val);
            curLevelNum--;

            if (cur.left != null) {
                nextLevelNum++;
                q.offer(cur.left);
            }
            if (cur.right != null) {
                nextLevelNum++;
                q.offer(cur.right);
            }

            if (curLevelNum == 0) {
                curLevelNum = nextLevelNum;
                nextLevelNum = 0;
                res.add(tmp);
                tmp = new ArrayList<Integer>();
            }
        }
        return res;
    }

    // 107. 二叉树的层次遍历 II:自底向上
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        int curLevelNode = 1;
        int nextLevelNode = 0;

        List<Integer> tmp = new ArrayList<Integer>();
        while (!queue.isEmpty()) {
            TreeNode cur = queue.removeFirst();
            tmp.add(cur.val);
            curLevelNode--;

            if (cur.left != null) {
                queue.add(cur.left);
                nextLevelNode++;
            }
            if (cur.right != null) {
                queue.add(cur.right);
                nextLevelNode++;
            }

            if (curLevelNode == 0) {
                res.add(tmp);
                tmp = new ArrayList<Integer>();
                curLevelNode = nextLevelNode;
                nextLevelNode = 0;
            }
        }
        Collections.reverse(res);
        return res;
    }

    // 144. 前序遍历
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;

        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);

        while(!s.isEmpty()) {
            TreeNode cur = s.pop();
            res.add(cur.val);

            if (cur.right != null) s.push(cur.right);
            if (cur.left != null) s.push(cur.left);
        }
        return res;
    }
    public void preorderRecursion(TreeNode root) {
        if (root != null) {
            System.out.println(root.val);
            preorderRecursion(root.left);
            preorderRecursion(root.right);
        }
    }

    // 94. 二叉树的中序遍历
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) {
            return res;
        }

        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode cur = root;
        while (true) {
            while (cur != null) {
                s.push(cur);
                cur = cur.left;
            }

            if (s.isEmpty()) break;

            cur = s.pop();
            res.add(cur.val);
            cur = cur.right;
        }
        return res;
    }
    public void inorderRecursion(TreeNode root) {
        if (root != null) {
            inorderRecursion(root.left);
            System.out.println(root.val);
            inorderRecursion(root.right);
        }
    }

    // 145. 二叉树的后序遍历:先left,right,root -> s1中:root,right,left->s2中:left,right,root
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;

        Stack<TreeNode> s = new Stack<TreeNode>();
        Stack<TreeNode> output = new Stack<TreeNode>();
        s.push(root);

        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            output.push(cur);
            if (cur.left != null) s.push(cur.left);
            if (cur.right != null) s.push(cur.right);
        }

        while (!output.isEmpty()) res.add(output.pop().val);
        return res;
    }
    public List<Integer> res = new ArrayList<Integer>();
    public List<Integer> postorderTraversalRec(TreeNode root) {//递归写法
        if(root == null)
            return res;
        postorderTraversal(root.left);
        postorderTraversal(root.right);
        res.add(root.val);
        return res;
    }

    // 236. 二叉树的最近公共祖先
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null) return null;
        if (root == A || root == B) return root;

        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);

        if (left != null && right != null) return root;
        if (left != null) return left;
        return right;
    }

    // 958. 二叉树的完全性检验
    public boolean isCompleteTree(TreeNode root) {
        if (root == null) return false;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        boolean mustNoChild = false;
        boolean res;

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();

            if (mustNoChild) {
                if (cur.left != null || cur.right != null) {
                    return false;
                }
            } else {
                if (cur.left != null && cur.right != null) {
                    q.offer(cur.left);
                    q.offer(cur.right);
                } else if (cur.left != null && cur.right == null) {
                    q.offer(cur.left);
                    mustNoChild = true;
                } else if (cur.left == null && cur.right == null) {
                    mustNoChild = true;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    // 222. 完全二叉树的节点个数
    // 简洁做法
    public int countNodes(TreeNode root) {
        /**
         *二叉树的第n层最多为2n个节点,二叉树最多有2^n−1个节点
         * 基于这两个性质，我们可以这样思考。
         * 如果右子树的高度等于整棵二叉树的高度-1的话，
         * 那么左子树一定是一棵满二叉树，这个时候我们就很容易的计算出总结点数nodes=2**(h)-1 + 1 +右子树节点数（这里的+1表示root节点）。
         * 如果右子树的高度不等于整棵二叉树的高度-1的话，那么左子树不一定是一棵满二叉树，但是有一点可以确定，右子树一定是一棵满二叉树，
         * 这个时候我们就很容易的计算出总结点数nodes=2**(h-1)-1 + 1 +左子树节点数（这里的+1表示root节点）。
         * 根据这个思路我们只要不断循环下去直到root==None结束
         */
        if (root == null) return 0;

        int height = 0;
        TreeNode left = root;
        TreeNode right = root;

        while (right != null) {
            left = left.left;
            right = right.right;
            height++;
        }

        if (left == null) {  // left == null 表示满二叉树
            return (1 << height) - 1;
        } else {
            return countNodes(root.left) + countNodes(root.right) + 1;
        }
    }
    public int countNodes2(TreeNode root) {
        if (root == null) return 0;
        int left = getLeftHeight(root);
        int right = getRightHeight(root);

        if (left == right) {
            // 表示是满二叉树，二叉树的节点数直接由公式2^n-1得到
            // leftHeight即为层数， 1 << leftHeight使用位运算计算2^leftHeight，效率更高
            // 注意(1 << leftHeight) - 1 的括号必须有！！
            return (1 << left) - 1;
        } else {
            return countNodes2(root.left) + countNodes2(root.right) + 1;
        }
    }
    public int getLeftHeight(TreeNode root) {
        if (root == null) return 0;
        int count = 0;
        while (root != null) {
            count++;
            root = root.left;
        }
        return count;
    }
    public int getRightHeight(TreeNode root) {
        if (root == null) return 0;
        int count = 0;
        while (root != null) {
            count++;
            root = root.right;
        }
        return count;
    }

    // 208. 实现 Trie (前缀树)
    class Trie {
        /*https://hxraid.iteye.com/blog/618962
        * https://segmentfault.com/a/1190000003709971
        * */
        private TrieNode root;

        /** Initialize your data structure here. */
        public Trie() {
            root = new TrieNode();
        }
        /** Inserts a word into the trie. */
        public void insert(String word) {
            HashMap<Character, TrieNode> children = root.children;

            for (int i = 0; i < word.length(); i++) {
                TrieNode next;
                if (children.containsKey(word.charAt(i))) {
                    next = children.get(word.charAt(i));
                } else {
                    next = new TrieNode(word.charAt(i));
                    children.put(word.charAt(i), next);
                }
                children = next.children;

                if (i == word.length() - 1) {
                    next.isLeaf = true;
                }
            }
        }
        /** Returns if the word is in the trie. */
        public boolean search(String word) {
            TrieNode res = searchNode(word);
            if (res != null && res.isLeaf) {
                return true;
            }
            return false;
        }
        /** Returns if there is any word in the trie that starts with the given prefix. */
        public boolean startsWith(String prefix) {
            return searchNode(prefix) != null;
        }
        private TrieNode searchNode(String word) {
            HashMap<Character, TrieNode> children = root.children;
            TrieNode next = null;
            for (int i = 0; i < word.length(); i++) {
                if (children.containsKey(word.charAt(i))) {
                    next = children.get(word.charAt(i));
                    children = next.children;
                } else {
                    return null;
                }
            }
            return next;
        }
    }

    // 103. 二叉树的锯齿形层次遍历
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int depth = 1;
        int curLevelNum = 1;
        int nextLevelNum = 0;

        List<Integer> tmp = new ArrayList<Integer>();
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            curLevelNum--;
            if (depth % 2 == 1) {
                tmp.add(node.val);
            } else {  // 偶数层反着插
                tmp.add(0, node.val);
            }

            if (node.left != null) {
                q.offer(node.left);
                nextLevelNum++;
            }
            if (node.right != null) {
                q.offer(node.right);
                nextLevelNum++;
            }

            if (curLevelNum == 0) {
                depth++;
                curLevelNum = nextLevelNum;
                nextLevelNum = 0;
                res.add(tmp);
                tmp = new ArrayList<Integer>();
            }
        }
        return res;
    }

    // 124. 二叉树中的最大路径和
    private int maxPathResult = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        /*
         * 思路：首先我们分析一下对于指定某个节点为根时，最大的路径和有可能是哪些情况。
         * 第一种是左子树的路径加上当前节点，
         * 第二种是右子树的路径加上当前节点，
         * 第三种是左右子树的路径加上当前节点（相当于一条横跨当前节点的路径），
         * 第四种是只有自己的路径。
         * 乍一看似乎以此为条件进行自下而上递归就行了，然而这四种情况只是用来计算以当前节点根的最大路径，
         * 如果当前节点上面还有节点，那它的父节点是不能累加第三种情况的。
         * 所以我们要计算两个最大值，一个是当前节点下最大路径和，另一个是如果要连接父节点时最大的路径和。
         * 我们用前者更新全局最大量，用后者返回递归值就行了。
         * */
        maxPathSumHelper(root);
        return maxPathResult;
    }
    public int maxPathSumHelper(TreeNode root) {
        if (root == null) return 0;

        int left = maxPathSumHelper(root.left);
        int right = maxPathSumHelper(root.right);

        // 以上四种情况的最大值
        int currSum = Math.max(Math.max(left + root.val, right + root.val), root.val);
        int currSum2 = Math.max(currSum, left + right + root.val);

        maxPathResult = Math.max(currSum2, maxPathResult);

        // 父节点 + 当前根最大路径不是棵树的
        return currSum;
    }

    // 662. 二叉树最大宽度
    public int widthOfBinaryTree_practise(TreeNode root) {
        if (root == null) return 0;
        LinkedList<Pair<TreeNode, Integer>> q = new LinkedList<Pair<TreeNode, Integer>>();
        q.offer(new Pair<TreeNode, Integer>(root, 1));
        int max = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            int len = q.getLast().getValue() - q.getFirst().getValue() + 1;
            max = Math.max(max, len);

            for (int i = 0; i < size; i++) {
                Pair<TreeNode, Integer> p = q.poll();

                if (p.getKey().left != null) q.offer(new Pair<TreeNode, Integer>(p.getKey().left, 2 * p.getValue()));
                if (p.getKey().right != null) q.offer(new Pair<TreeNode, Integer>(p.getKey().right, 2 * p.getValue() + 1));
            }
        }
        return max;
    }
    public int widthOfBinaryTree(TreeNode root) {
        /*
        * https://www.jianshu.com/p/fb59df4fc894
        * 采取二叉树的层次遍历，如果用空节点来占据每层中首尾非空节点中间的空位置来计算每层最大宽度,容易发生超时(因为第n次有2^n个节点，增长速度极快)。
        * 因此根据在一颗二叉树中,左孩子在其所在层次中的下标为其父节点的下标*2，右孩子在其所在层次中的下标等于其父节点的下标*2+1 的规律（下标值从0开始)。
        * 构造（TreeNode, index）的二元组来记录每个非空节点的位置，便可在层次遍历时只向队列中加入非空节点来缩短遍历所需要的时间。
        *
        * 给二叉树的节点从1开始编号，那么i节点的左右子节点的编号分别为2i和2i+1，
        * 因此可以使用编号来计算宽度：width=最右节点的编号 - 最左节点的编号。
        * 用一个队列来记录每一层的最左边节点的编号，那么每一层的宽度就可以直接利用编号计算出来，它们的最大值就是二叉树的宽度。
        * */
        if (root == null) return 0;

        int max = 0;
        LinkedList<Pair<TreeNode, Integer>> q = new LinkedList<Pair<TreeNode, Integer>>();
        q.offer(new Pair<TreeNode, Integer>(root, 1));

        // 每一次while循环都是遍历新的层
        while (!q.isEmpty()) {
            int size = q.size();

            int len = q.getLast().getValue() - q.getFirst().getValue() + 1;

            max = Math.max(len, max);

            for (int i = 0; i < size; i++) {
                Pair<TreeNode, Integer> pair = q.poll();
                if (pair.getKey().left != null)
                    q.offer(new Pair<TreeNode, Integer>(pair.getKey().left, 2 * pair.getValue()));
                if (pair.getKey().right != null)
                    q.offer(new Pair<TreeNode, Integer>(pair.getKey().right, 2 * pair.getValue() + 1));
            }
        }
        return max;
    }

    // 257. 二叉树的所有路径
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList<String>();
        String s = "";
        binaryTreePath(root, s, list);

        return list;
    }
    public void binaryTreePath(TreeNode root, String s, List<String> list) {
        if (root == null) return;

        s += root.val;

        if (root.left == null && root.right == null) {
            list.add(s);
        } else {
            s += "->";
        }

        // s是值传递，内部方法修改后不可变
        binaryTreePath(root.left, s, list);
        binaryTreePath(root.right, s, list);
    }

    // 113. 路径总和 II: 根节点到叶子节点路径和等于给定目标
    private int target;
    private List<List<Integer>> result = new ArrayList<List<Integer>>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        this.target = sum;
        dfs(root, 0, new ArrayList<Integer>());
        return result;
    }
    private void dfs(TreeNode root, int tmpSum, List<Integer> list) {
        if (root == null) return;

        int pathSum = tmpSum + root.val;
        list.add(root.val);

        if (root.left == null && root.right == null && pathSum == target) result.add(new ArrayList<Integer>(list));  // list还需要继续用

        dfs(root.left, pathSum, list);
        dfs(root.right, pathSum, list);

        // 满足条件的已经放到返回list中了,之后回溯查找需要把每次遍历加入的值去掉
        list.remove(list.size() - 1);
    }

    // 226. 翻转二叉树
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
        invertTree(root.left);
        invertTree(root.right);

        return root;
    }

    // 637. 二叉树的层平均值
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<Double>();
        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        while (!q.isEmpty()) {
            int size = q.size();
            double sum = 0;

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                sum += n.val;

                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }

            res.add(sum/size);
        }
        return res;
    }















    // TODO:951. 翻转等价二叉树
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        if(root1 == null && root2 == null) return true;

        if(root1 != null && root2 != null){
            if(root1.val != root2.val) return false;
            return
                    (flipEquiv(root1.left,root2.right) && flipEquiv(root1.right,root2.left)) ||
                            (flipEquiv(root1.left,root2.left) && flipEquiv(root1.right,root2.right));
        }
        return false;
    }


    class TrieNode {
        Character c;
        HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
        boolean isLeaf = false;

        public TrieNode(){}
        public TrieNode(Character c) {
            this.c = c;
        }
    }
    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }



}
