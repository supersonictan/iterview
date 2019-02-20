package interview.ali_2019;

import javafx.util.Pair;

import javax.management.Query;
import java.util.*;

// TODO: 一定要能熟练地写出所有问题的递归和非递归做法！

/*
             1
            / \
           2   3
          / \   \
         4  5   6
 */
/*
 *
 * 104. 二叉树的最大深度[简单]
 * 637. 二叉树的层平均值[简单]
 * 226. 翻转二叉树[简单]
 * 103. 二叉树的锯齿形层次遍历[中等]
 * 102. 二叉树的层次遍历[中等]
 * 107. 二叉树自底向上层次遍历[中等]
 * 111. 二叉树的最小深度[简单]
 * 662. 二叉树最大宽度[中等]
 * 144. 前序遍历[中等]
 * 94. 二叉树的中序遍历[中]
 * 145. 二叉树的后序遍历[难]
 * 236. 二叉树的最近公共祖先[中]
 * 113. 根节点到叶节点路径和等于给定目标[中]
 * 124. 二叉树中的最大路径和[难]
 * 257. 二叉树的所有路径[简单]
 *
 *
 *
 *
 *
 * 958. 二叉树的完全性检验: boolean isCompleteTree(TreeNode root)
 * 222. 完全二叉树的节点个数: int countNodes(TreeNode root)
 * 208. 实现 Trie (前缀树)
 *
 * 951. TODO:翻转等价二叉树
 * TODO:前序、中序遍历构造二叉树
 * TODO：BST
 *
 *
 */

public class Tree2019 {

    // 104. 二叉树的最大深度[简单]
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int res = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        while (!q.isEmpty()) {
            int size = q.size();
            res++;

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
        }
        return res;
    }
    public int maxDepthRec(TreeNode root) {
        if(root == null) {
            return 0;
        }

        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }

    // 637. 二叉树的层平均值[简单]
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

    // 226. 翻转二叉树[简单]
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
        invertTree(root.left);
        invertTree(root.right);

        return root;
    }

    // 103. 二叉树的锯齿形层次遍历[中等]
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;

        int level = 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        List<Integer> tmp;
        while (!q.isEmpty()) {
            tmp = new ArrayList<Integer>();
            int size = q.size();
            level++;

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();

                if (level % 2 == 0) {
                    tmp.add(0, n.val);
                } else {
                    tmp.add(n.val);
                }

                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
            res.add(tmp);
        }
        return res;
    }

    // 102. 二叉树的层次遍历[中等]
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        List<Integer> tmp;
        while (!q.isEmpty()) {
            tmp = new ArrayList<Integer>();
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                tmp.add(n.val);

                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
            res.add(tmp);
        }

        return res;
    }

    // 107. 二叉树的自底向上层次遍历[中等]
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        List<Integer> tmp;
        while(!q.isEmpty()) {
            int size = q.size();
            tmp = new ArrayList<Integer>();

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                tmp.add(n.val);

                if (n.left !=null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
            res.add(0, tmp);
        }
        return res;
    }

    // 111. 二叉树的最小深度[简单]
    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int res = 0;

        while (!q.isEmpty()) {
            res++;
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();

                if (n.left == null && n.right == null) return res;

                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
        }
        return res;
    }

    // 662. 二叉树最大宽度[中等]
    public int widthOfBinaryTree(TreeNode root) {
        /**
         * https://www.jianshu.com/p/fb59df4fc894
         * 采取二叉树的层次遍历，如果用空节点来占据每层中首尾非空节点中间的空位置来计算每层最大宽度,容易发生超时(因为第n次有2^n个节点，增长速度极快)。
         * 因此根据在一颗二叉树中,左孩子在其所在层次中的下标为其父节点的下标*2，右孩子在其所在层次中的下标等于其父节点的下标*2+1 的规律（下标值从0开始)。
         * 构造（TreeNode, index）的二元组来记录每个非空节点的位置，便可在层次遍历时只向队列中加入非空节点来缩短遍历所需要的时间。
         *
         * 给二叉树的节点从1开始编号，那么i节点的左右子节点的编号分别为2i和2i+1，
         * 因此可以使用编号来计算宽度：width=最右节点的编号 - 最左节点的编号。
         * 用一个队列来记录每一层的最左边节点的编号，那么每一层的宽度就可以直接利用编号计算出来，它们的最大值就是二叉树的宽度。
         */
        if (root == null) return 0;

        int res = 0;
        LinkedList<Pair<TreeNode, Integer>> q = new LinkedList<Pair<TreeNode, Integer>>();
        q.offer(new Pair<TreeNode, Integer>(root, 1));

        while (!q.isEmpty()) {
            int size = q.size();
            int left = q.getFirst().getValue();
            int right = q.getLast().getValue();
            res = Math.max(res, right - left + 1);

            for (int i = 0; i < size; i++) {
                Pair<TreeNode, Integer> pair = q.poll();
                if (pair.getKey().left != null)
                    q.offer(new Pair<TreeNode, Integer>(pair.getKey().left, 2*pair.getValue()));
                if (pair.getKey().right != null)
                    q.offer(new Pair<TreeNode, Integer>(pair.getKey().right, 2*pair.getValue() + 1));
            }
        }
        return res;
    }

    // 144. 前序遍历
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();

        if (root == null) return res;

        Stack<TreeNode> q = new Stack<TreeNode>();
        q.push(root);

        while (!q.isEmpty()) {
            TreeNode n = q.pop();
            res.add(n.val);

            if (n.right != null) q.push(n.right);
            if (n.left != null) q.push(n.left);
        }
        return res;
    }
    List<Integer> preorderRecursionList = new ArrayList<Integer>();
    public List<Integer> preorderRecursion(TreeNode root) {
        if(root!=null){
            preorderRecursionList.add(root.val);
            preorderTraversal(root.left);
            preorderTraversal(root.right);
        }
        return preorderRecursionList;
    }

    // 94. 二叉树的中序遍历[中]
    List<Integer> inorderRecList = new ArrayList<Integer>();
    public List<Integer> inorderRecursion(TreeNode root) {
        if (root != null) {
            inorderRecursion(root.left);
            inorderRecList.add(root.val);
            inorderRecursion(root.right);
        }
        return inorderRecList;
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode cur = root;

        while (true) {
            while (cur != null) {
                s.push(cur);
                cur = cur.left;
            }

            if (s.isEmpty()) break;

            TreeNode tmp = s.pop();
            res.add(tmp.val);
            cur = tmp.right;
        }
        return res;
    }

    // 145. 二叉树的后序遍历[难]
    public List<Integer> postorderList = new ArrayList<Integer>();
    public List<Integer> postorderTraversalRec(TreeNode root) {//递归写法
        if (root != null) {
            postorderTraversalRec(root.left);
            postorderTraversalRec(root.right);
            postorderList.add(root.val);
        }
        return postorderList;
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;

        Stack<TreeNode> s = new Stack<TreeNode>();
        Stack<TreeNode> output = new Stack<TreeNode>();

        s.push(root);
        while (!s.isEmpty()) {
            TreeNode n = s.pop();
            output.push(n);

            if (n.left != null) s.push(n.left);
            if (n.right != null) s.push(n.right);
        }

        while (!output.isEmpty()) res.add(output.pop().val);
        return res;
    }

    // 236. 二叉树的最近公共祖先
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null) return null;

        if (A == root || B == root) return root;

        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);

        if (left != null && right != null) return root;
        if (left != null) return left;
        return right;
    }

    // 113. 根节点到叶节点路径和等于给定目标
    private int target;
    private List<List<Integer>> res = new ArrayList<List<Integer>>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root == null)  return res;
        this.target = sum;

        dfs(root, 0, new ArrayList<Integer>());

        return res;
    }
    private void dfs(TreeNode root, int tmpSum, List<Integer> list) {
        if (root == null) return;

        int sum = tmpSum + root.val;
        list.add(root.val);

        if (sum == target && root.left == null && root.right == null) res.add(new ArrayList<Integer>(list));

        dfs(root.left, sum, list);
        dfs(root.right, sum, list);

        list.remove(list.size() - 1);
    }

    // 124. 二叉树中的最大路径和[难]
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
        maxPathSumDfs(root);
        return maxPathResult;
    }
    public int maxPathSumDfs(TreeNode root) {
        if (root == null) return 0;

        int left = maxPathSumDfs(root.left);
        int right = maxPathSumDfs(root.right);

        // 以上四种情况的最大值
        int tmpSum = Math.max(root.val, Math.max(left + root.val, right + root.val));
        int tmpSum2 = Math.max(left + root.val + right, tmpSum);

        maxPathResult = Math.max(tmpSum2, maxPathResult);

        // 父节点 + 当前根最大路径不是棵树的
        return tmpSum;
    }

    // 257. 二叉树的所有路径
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<String>();
        String s = "";

        binaryTreePathDfs(root, s, res);

        return res;
    }
    public void binaryTreePathDfs(TreeNode root, String s, List<String> list) {
        if (root == null) return;

        s += root.val;

        if (root.left == null && root.right == null) {
            list.add(s);
        } else {
            s += "->";
        }

        binaryTreePathDfs(root.left, s, list);
        binaryTreePathDfs(root.right, s, list);
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
