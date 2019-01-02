package interview.ali_2019;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TreeProblem {

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

    // 68. 后序遍历:先left,right,root -> s1中:root,right,left->s2中:left,right,root
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return null;
        List<Integer> res = new ArrayList<Integer>();
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







    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }



}
