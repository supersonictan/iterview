package interview.ali_2019;

/*
* 235. 二叉搜索树的最近公共祖先
* */
public class BST {

    // 235. 二叉搜索树的最近公共祖先
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        /*
        * 利用搜索树的性质，减少递归的次数
        * 如果p和q都小于root，去左边找就行。
        * 如果p和q在两侧的，直接就是root，这个可以通过val来判断
        * */
        if (root == null || root == p || root == q) return root;

        if (p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if (p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
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
