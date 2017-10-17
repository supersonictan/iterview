package interview.ali_2017;


import java.util.*;

/**
 * Created by tanzhen on 2017/10/8.
 前序遍历
 中序遍历
 后序遍历
 广度优先遍历,二叉树层次遍历
 二叉树第K层节点个数
 二叉树深度
 翻转二叉树-可以破坏原结构
 二叉树是否等价
 最近公共祖先-递归
 二叉树中叶节点个数
 判断二叉树是不是完全二叉树
 前序遍历和中序遍历树构造二叉树
 中序遍历和后序遍历树构造二叉树
 442. 实现Trie
 *
 */
public class TreeQuestion {


    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    /*前序遍历*/
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null) return null;
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);
        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            res.add(cur.val);
            if (cur.right != null) s.push(cur.right);
            if (cur.left != null) s.push(cur.left);
        }
        return res;
    }
    /*中序遍历*/
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return null;
        List<Integer> res = new ArrayList<Integer>();
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
    /*后序遍历*/
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root==null) return null;
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> s = new Stack<TreeNode>();
        Stack<TreeNode> output = new Stack<TreeNode>();
        s.push(root);
        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            output.push(cur);
            if (cur.left!=null)  s.push(cur.left);
            if (cur.right != null) s.push(cur.right);
        }
        while (!output.isEmpty()) res.add(output.pop().val);
        return res;
    }
    /*广度优先遍历,二叉树层次遍历*/
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        int curLevelNode = 1;
        int nextLevelNode = 0;
        List<Integer> tmp = new ArrayList<Integer>();
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            curLevelNode --;
            tmp.add(cur.val);
            if (cur.left != null) {
                q.add(cur.left);
                nextLevelNode ++;
            }
            if (cur.right != null) {
                q.add(cur.right);
                nextLevelNode ++;
            }

            if (curLevelNode == 0) {
                res.add(tmp);
                tmp = new ArrayList<Integer>();
                curLevelNode = nextLevelNode;
                nextLevelNode = 0;
            }
        }
        return res;
    }
    /*二叉树第K层的节点个数*/
    public static int getNodeNumKthLevel(TreeNode root, int k){
        if(root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        int i = 1;
        int currentLevelNodes = 1;      // 当前Level，node的数量
        int nextLevelNodes = 0;         // 下一层Level，node的数量

        while( !queue.isEmpty() && i<k){
            TreeNode cur = queue.poll();      // 从队头位置移除
            currentLevelNodes--;            // 减少当前Level node的数量
            if(cur.left != null){               // 如果有左孩子，加到队尾
                queue.add(cur.left);
                nextLevelNodes++;           // 并增加下一层Level node的数量
            }
            if(cur.right != null){          // 如果有右孩子，加到队尾
                queue.add(cur.right);
                nextLevelNodes++;
            }
            if(currentLevelNodes == 0){ // 说明已经遍历完当前层的所有节点
                currentLevelNodes = nextLevelNodes;     // 初始化下一层的遍历
                nextLevelNodes = 0;
                i++;            // 进入到下一层
            }
        }

        return currentLevelNodes;
    }
    /*二叉树的最大深度*/
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        int cur_levelNum = 1;
        int next_lev_num = 0;
        int res=0;
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            cur_levelNum--;
            if (cur.left != null) {
                q.add(cur.left);
                next_lev_num++;
            }
            if (cur.right != null) {
                q.add(cur.right);
                next_lev_num++;
            }
            if (cur_levelNum ==0) {
                res++;
                cur_levelNum = next_lev_num;
                next_lev_num=0;
            }
        }
        return res;
    }
    /*翻转二叉树-可以破坏原结构*/
    public void invertBinaryTree(TreeNode root) {
        if (root==null) return ;
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);
        while (!s.isEmpty()) {
            TreeNode cur = s.pop();
            TreeNode tmp = cur.left;
            cur.left = cur.right;
            cur.right = tmp;

            if (cur.right!=null) s.push(cur.right);
            if (cur.left!=null) s.push(cur.left);
        }
    }
    /*二叉树是否等价*/
    public boolean isIdentical(TreeNode r1, TreeNode r2) {
        if (r1==null && r2==null) return true;
        if (r1==null ||r2==null) return false;
        Stack<TreeNode> s1 = new Stack<TreeNode>();
        Stack<TreeNode> s2 = new Stack<TreeNode>();
        s1.add(r1);
        s2.add(r2);
        while (!s1.isEmpty() && !s2.isEmpty()) {
            TreeNode n1 = s1.pop();
            TreeNode n2 = s2.pop();
            if (n1==null && n2==null) continue;
            else if (n1!=null&&n2!=null&&n1.val==n2.val) {
                s1.push(n1.right);
                s2.push(n2.right);
                s1.push(n1.left);
                s2.push(n2.left);
            }else {
                return false;
            }
        }
        return true;
    }
    /*最近公共祖先-递归*/
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root==null) return null;
        if (root==A||root==B) return root;

        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);

        if (left!=null && right!=null) return root;
        if (left !=null) return left;
        return right;
    }
    /*二叉树中叶节点个数*/
    public static int getNodeNumLeaf(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);

        int leafNodes = 0;              // 记录上一个Level，node的数量
        while( !q.isEmpty() ){
            TreeNode cur = q.poll();      // 从队头位置移除
            if(cur.left != null){               // 如果有左孩子，加到队尾
                q.add(cur.left);
            }
            if(cur.right != null){              // 如果有右孩子，加到队尾
                q.add(cur.right);
            }
            if(cur.left==null && cur.right==null){          // 叶子节点
                leafNodes++;
            }
        }

        return leafNodes;
    }
    /*判断二叉树是不是完全二叉树*/
    public static boolean isCompleteBinaryTree(TreeNode root){
        if(root == null)return false;

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        boolean mustHaveNoChild = false;
        boolean result = true;

        while(!q.isEmpty()){
            TreeNode cur = q.poll();
            if (mustHaveNoChild){
                if(cur.left!=null || cur.right!=null){
                    result = false;
                    break;
                }
            } else {
                if(cur.left!=null && cur.right!=null){      // 如果左子树和右子树都非空，则继续遍历
                    q.add(cur.left);
                    q.add(cur.right);
                }else if(cur.left!=null && cur.right==null){    // 如果左子树非空但右子树为空，说明已经出现空节点，之后必须都为空子树
                    mustHaveNoChild = true;
                    q.add(cur.left);
                }else if(cur.left==null && cur.right!=null){    // 如果左子树为空但右子树非空，说明这棵树已经不是完全二叉完全树！
                    result = false;
                    break;
                }else{          // 如果左右子树都为空，则后面的必须也都为空子树
                    mustHaveNoChild = true;
                }
            }
        }
        return result;
    }

    /*442.实现Trie*/
    class TrieNode {
        boolean exist;
        char ch;
        TrieNode[] children;
        public TrieNode() {}
        public TrieNode(char ch){this.ch = ch;}
    }
    public class Trie {
        private TrieNode root;
        public Trie() {root = new TrieNode();}

        public void insert(String word) {
            if(word==null || word.length()==0) return;
            TrieNode pre = root;
            for(int i=0; i<word.length(); i++) {
                int idx = word.charAt(i) - 'a';
                if(pre.children == null) pre.children = new TrieNode[26];
                if(pre.children[idx] == null) pre.children[idx] = new TrieNode(word.charAt(i));
                pre = pre.children[idx];
                if (i==word.length()-1) pre.exist=true;
            }
        }
        public boolean search(String word) {
            /**
             * 复制root到结点pre，然后遍历查找word的每一个字符word.charAt(i)，
             * 若循环里某个pre.children[index]不存在，或者word的最后一个字符的exist标记为false，
             * 则返回false。否则，循环结束，返回true
             */
            if (word == null || word.length() == 0) return false;
            TrieNode pre = root;
            for (int i = 0; i < word.length(); i++) {
                int index = word.charAt(i) - 'a';
                if (pre.children == null || pre.children[index] == null) return false;
                if (i == word.length()-1 && pre.children[index].exist == false) return false;
                pre = pre.children[index];
            }
            return true;
        }
        public boolean startsWith(String prefix) {
            /*是不要求word的最后一个字符的exist标记为true。
              只要遍历完String prefix，就返回true
             */
            if (prefix == null || prefix.length() == 0) return false;
            TrieNode pre = root;
            for (int i = 0; i < prefix.length(); i++) {
                int index = prefix.charAt(i) - 'a';
                if (pre.children == null || pre.children[index] == null) return false;
                pre = pre.children[index];
            }
            return true;
        }
    }



    /*前序遍历和中序遍历树构造二叉树*/
    /*public TreeNode buildTree(int[] preorder, int[] inorder) {
        TreeNode root = null;
        int[] preorder_l, preorder_r, inorder_l, inorder_r;
        int root_idx=0;
        //中序中找到root_idx
        if (preorder.length!=0 || inorder.length!=0){
            root = new TreeNode(preorder[0]);
            for (int i=0; i<inorder.length; i++){
                if (preorder[0] == inorder[i]) break;
                root_idx++;
            }
        }
        for (int i=0; i<root_idx; i++) {
            preorder_l
        }
    }*/
}
