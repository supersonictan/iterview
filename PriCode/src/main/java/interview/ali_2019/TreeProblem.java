package interview.ali_2019;

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
 * 236. 二叉树的最近公共祖先
 * 958. 二叉树的完全性检验
 * 222. 完全二叉树的节点个数
 * 208. 实现 Trie (前缀树)
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
