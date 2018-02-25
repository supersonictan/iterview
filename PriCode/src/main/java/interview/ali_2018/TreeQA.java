package interview.ali_2018;

import java.util.*;

/**
 *
 * 66. 前序遍历
 * 67. 中序遍历
 * 68. 后序遍历
 * 69. 广度优先遍历,二叉树层次遍历
 * 97. 二叉树最大深度
 * 88. 最近公共祖先-递归
 * 二叉树中叶节点个数
 * 175.翻转二叉树-可以破坏原结构
 * 判断二叉树是不是完全二叉树
 * 73. 前序遍历和中序遍历树构造二叉树
 * 72. 中序遍历和后序遍历树构造二叉树
 * 7. 二叉树的序列化和反序列化
 * 442. 实现Trie
 * 二叉树第K层节点个数
 * 二叉树是否等价
 *
 *
 * **/

public class TreeQA {
    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }


    // 66. 前序遍历
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null) return null;
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);
        while (!s.isEmpty()) {
            TreeNode node = s.pop();
            res.add(node.val);
            if (node.right != null) s.push(node.right);
            if (node.left != null) s.push(node.left);
        }
        return res;
    }
    // 67. 中序遍历
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return null;
        Stack<TreeNode> s = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
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
    // 68. 后序遍历
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
    // 69. 广度优先遍历,二叉树层次遍历
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
    // 97. 二叉树最大深度
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

    // 88. 最近公共祖先-递归
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null) return null;
        if (root == A || root == B) return root;
        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);

        if (left != null && right != null) return root;
        if (left != null) return left;
        return right;
    }
    // 二叉树中叶节点个数
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
    // 175. 翻转二叉树-可以破坏原结构
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
    // 判断二叉树是不是完全二叉树
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
    // 73. 前序遍历和中序遍历树构造二叉树
    public TreeNode buildTree_preInoder(List<Integer> preorder, List<Integer> inorder) {
        TreeNode root = null;
        List<Integer> pre_l = new ArrayList<Integer>();
        List<Integer> pre_r = new ArrayList<Integer>();
        List<Integer> in_l  = new ArrayList<Integer>();
        List<Integer>  in_r = new ArrayList<Integer>();
        int root_index = 0;
        if (!preorder.isEmpty() && !inorder.isEmpty()) {
            root = new TreeNode(preorder.get(0));
            for (int i = 0; i < inorder.size(); i++) {
                if (preorder.get(0) == inorder.get(i)) {
                    root_index++;
                }
            }
            for (int i = 0; i < root_index; i++) {
                pre_l.add(preorder.get(i+1));
                in_l.add(inorder.get(i));
            }
            for (int i=root_index+1; i<inorder.size(); i++) {
                pre_r.add(preorder.get(i));
                in_r.add(inorder.get(i));
            }
            root.left = buildTree_preInoder(pre_l, in_l);
            root.left = buildTree_preInoder(pre_r, in_r);
        }
        return root;
    }

    // 72. 中序遍历和后序遍历树构造二叉树
    public TreeNode buildTree_postInoder(List<Integer> postOrder, List<Integer> inorder) {
        List<Integer> postL = new ArrayList<Integer>();
        List<Integer> postR = new ArrayList<Integer>();
        List<Integer> inorderL = new ArrayList<Integer>();
        List<Integer> inorderR = new ArrayList<Integer>();

        // 在中序中找根节点
        TreeNode root = null;
        int root_idx = 0;
        if (!postOrder.isEmpty() && !inorder.isEmpty()) {
            root = new TreeNode(postOrder.get(postOrder.size() - 1));
            for (int i = 0; i < inorder.size(); i++) {
                if (postOrder.get(i) == postOrder.get(postOrder.size() - 1)) {
                    break;
                }
                root_idx++;
            }
            for (int i=0; i < root_idx; i++) {
                inorderL.add(inorder.get(i));  // 注意in和post分别add自己集合的顺序
                postL.add(postOrder.get(i));
            }
            for (int i=root_idx+1; i < inorder.size(); i++) {
                inorderR.add(inorder.get(i));
                postR.add(postOrder.get(i-1));
            }
            root.left = buildTree_postInoder(postL, inorderL);
            root.right = buildTree_postInoder(postR, inorderR);
        }
        return root;
    }
    // 7. 序列化反序列化
    public String serialize(TreeNode root) {
        String res = "{";
        if (root == null) return "{}";
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        res += root.val;
        while (!queue.isEmpty()) {
            TreeNode cur = queue.remove();
            if (cur == null) continue;
            if (cur.left != null) {
                res += "," + cur.left.val;
            }else {
                res += ",#";
            }
            if (cur.right != null) {
                res += "," + cur.right.val;
            }else {
                res += ",#";
            }
            queue.add(cur.left);
            queue.add(cur.right);
        }
        int i = res.length()-1;
        //System.out.println(res);
        while (res.charAt(i)=='#' || res.charAt(i)==','){
            i--;
        }
        res = res.substring(0,i+1);
        return res += "}";
    }
    public TreeNode deserialize(String data) {
        if (data.equals("{}")) return null;
        String[] field = data.substring(1, data.length()-1).split(",");
        List<TreeNode> queue = new ArrayList<TreeNode>();
        TreeNode root = new TreeNode(Integer.parseInt(field[0]));
        queue.add(root);
        int idx = 0;
        boolean isLeft = true;
        for (int i=1;i<field.length;i++) {
            if (!field[i].equals("#")){
                TreeNode node = new TreeNode(Integer.parseInt(field[i]));
                if (isLeft) queue.get(idx).left = node;
                else queue.get(idx).right = node;
                queue.add(node);
            }
            if (!isLeft) idx++;
            isLeft = !isLeft;
        }
        return root;
    }

}
