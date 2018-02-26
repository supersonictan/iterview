package interview.ali_2018;



import java.util.*;

/**
 * ---------- 快排思想 ----------
 * 5.第K大数字
 * 80.中位数
 *
 *
 * ---------- 二分查找 ----------
 * 457.经典二分查找问题
 * 14.二分查找:找到target第一次出现的下标
 * 159.寻找旋转排序数组中的最小值
 * 62.旋转排序数组搜索target
 * 28.搜索二维矩阵:每行中的整数从左到右是排序的,每行的第一个数大于上一行的最后一个整数。
 * 38.搜索二维矩阵2:每行中的整数从左到右是排序的,每一列的整数从上到下是排序的,在每一行或每一列中没有重复的整数.
 * 633.找到1~n数字中个一重复的，不排序，空间O(1)
 * 428.x的n次幂O(logn)
 *
 *
 * ---------- 动态规划 ----------
 * 111. 爬楼梯:每次只能爬一步或者两步，多少种不同的方法爬到顶部
 *
 * ---------- 多指针 ----------
 * 56.两数之和:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target
 * 57.三数之和=target的所有组合
 * 58.四数之和
 * 59.最接近的三数之和
 * 排序只有0,1,2的数组,O(n)
 *
 *
 * ---------- 树 ----------
 * 66.前序遍历
 * 67.中序遍历
 * 68.后序遍历
 * 69.广度优先遍历,二叉树层次遍历
 * 97.二叉树最大深度
 * 88.最近公共祖先-递归
 * 二叉树中叶节点个数
 * 175.翻转二叉树-可以破坏原结构
 * 判断二叉树是不是完全二叉树
 * 73.前序遍历和中序遍历树构造二叉树
 * 72.中序遍历和后序遍历树构造二叉树
 * 7.二叉树的序列化和反序列化
 * 442. 实现Trie
 * 二叉树第K层节点个数
 * 二叉树是否等价
 *
 *
 * ---------- 其他 ----------
 * 184.拼接最大数:给出 [1, 20, 23, 4, 8]，返回8423201
 *
 *
 * 两数组交(hash或排序后两个指针)
 * 搜索区间:[5, 7, 7, 8, 8, 10]和目标值target=8(给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置)
 * 最大子数组均值(长度固定)
 * 最大子数组平均值(长度>=k)
 *
 *
 *
 * 689. 两数之和
 */

public class Code2018 {
    private static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    /*------------------ 动态规划 ------------------*/
    // 111. 爬楼梯:每次只能爬一步或者两步，多少种不同的方法爬到顶部
    public int climbStairs(int n) {
        if (n == 0 || n == 1 || n == 2) {
            return n;
        }
        int[] r = new int[n+1];
        r[1] = 1;
        r[2] = 2;
        for (int i = 3; i <= n; i++) {
            r[i] = r[i-1] + r[i-2];
        }
        return r[n];
    }


    // 5.第K大数字
    public int kthLargestElement(int k, int[] nums) {
        return kthPartition(nums, 0, nums.length-1, k);
    }
    public int kthPartition(int[] nums, int left, int right, int k) {
        int i = left;
        int j = right;
        int tmp = nums[i];
        while (i<j){
            while(i < j && tmp >= nums[j]) j--;
            if (i<j) { nums[i] = nums[j]; }
            while (i < j && tmp <= nums[i]) i++;
            if (i<j) { nums[j] = nums[i]; }
        }
        if(i == k - 1) {
            return tmp;
        } else if(i< k-1) {
            return kthPartition(nums, i+1, right, k);
        } else {
            return kthPartition(nums, left, i-1, k);
        }
    }
    // 80.中位数
    public int median(int[] nums) {
        int len = nums.length%2==0?nums.length/2 : nums.length/2+1;
        return medianPartition(nums, 0, nums.length-1, len);
    }
    public int medianPartition(int[] arr, int l, int r, int k) {
        int left = l;
        int right = r;
        int key = arr[left];
        while (left < right) {
            while (left < right && arr[right] >= key) right--;
            if (left < right) arr[left] = arr[right];
            while (left < right && arr[left] <= key) left++;
            if (left < right) arr[right] = arr[left];
        }
        if (left == k-1) {
            return key;
        } else if (left < k-1) {
            return medianPartition(arr, left+1, r, k);
        } else {
            return medianPartition(arr, l, right-1, k);
        }
    }

    // 14.二分查找:找到target第一次出现的下标
    public int binarySearch(int[] nums, int target) {
        int begin = 0;
        int end = nums.length-1;
        int res = -1;
        while (begin<=end) {
            int mid = (begin+end) / 2;
            if (nums[mid] == target) {
                if (res<0) res = mid;
                if (res>0 && mid<res) res = mid;
                end = end-1;
            }else if (nums[mid] > target) {
                end = mid-1;
            } else {
                begin = mid + 1;
            }
        }
        return res;
    }
    // 457.经典二分查找问题
    public int findPosition(int[] nums, int target) {
        if (nums == null && nums.length == 0) {
            return -1;
        }
        int begin = 0;
        int end = nums.length-1;
        while (begin < end) {
            int mid = (begin + end) /2;
            if (target == nums[mid]) return mid;
            else if (target > nums[mid]) begin = mid+1;
            else end = mid-1;
        }
        return -1;
    }
    // 159. 寻找旋转排序数组中的最小值
    public int findMin(int[] num) {
        if (num[0] < num[num.length-1]) return num[0];
        int left = 0;
        int right = num.length-1;
        while(left < right) {
            int mid = (left + right) / 2;
            if(mid-1 >= 0 && num[mid] < num[mid-1] ){
                return num[mid];
            }
            if(mid+1 <= num.length-1 && num[mid] > num[mid+1]) {
                return num[mid+1];
            }
            if (num[left] < num[mid] ) {
                left = mid+1;
            }
            if (num[mid] < num[right]) {
                right = mid-1;
            }
        }
        return -1;
    }
    // 62.旋转排序数组搜索target
    public int search(int[] A, int target) {
        int left = 0;
        int right = A.length-1;
        while (left<=right) {
            int mid = (left + right) /2;
            if (A[mid] == target) return mid;
            if (A[left] == target) return left;  // [1,2,3]
            if (A[right] == target) return right;
            if (A[left] < A[mid]) {  // 左边递增
                if (target < A[mid] && target > A[left]) {
                    right = mid - 1;
                }else {
                    left = mid + 1;
                }
            } else if (A[left] > A[mid]) { // 右边递增
                if (target > A[mid] && target < A[right]) {
                    left = mid +1;
                }else {
                    right = mid -1;
                }
            } else {
                left++;
            }
        }
        return -1;
    }
    // 28.搜索二维矩阵:每行中的整数从左到右是排序的,每行的第一个数大于上一行的最后一个整数。
    public boolean searchMatrix(int[][] m, int target) {
        if (m == null || m.length < 1) return false;
        if (m[0][0] > target || m[m.length-1][m[0].length-1] < target) return false;
        int colLen = m[0].length - 1;

        int rowIdx = 0, colIdx = 0;
        int l = 0;
        int r = m.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (m[mid][0] == target || m[mid][colLen] == target) return true;
            else if (m[mid][0] <= target && m[mid][colLen] >= target) {
                rowIdx = mid;
                break;
            }
            else if (m[mid][0] > target) r = mid-1;
            else if (m[mid][colLen] < target) l = mid+1;
        }

        l = 0;
        r = m[0].length - 1;
        while (l <= r) {
            int mid = (l + r)/2;
            if (m[rowIdx][mid] == target) return true;
            else if (m[rowIdx][mid] > target) r = mid - 1;
            else if (m[rowIdx][mid] < target) l = mid + 1;
        }
        return false;
    }
    // 38.搜索二维矩阵2:每行中的整数从左到右是排序的,每一列的整数从上到下是排序的,在每一行或每一列中没有重复的整数.
    public int searchMatrix2(int[][] matrix, int target) {
        if (matrix.length == 0) return 0;
        int rows = matrix.length;
        int col = matrix[0].length;
        int r = 0;
        int c = col - 1;
        int count = 0;
        while (r < rows && c >= 0) {
            if (target == matrix[r][c]) {
                count++;
                if (r + 1 < rows) {
                    r++;
                } else if (c - 1 > 0) {
                    c--;
                } else {
                    return count;
                }
            } else if (target > matrix[r][c]) {
                r++;
            } else {
                c--;
            }
        }
        return count;
    }

    // 56.两数之和:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        if (numbers == null || numbers.length < 2 ){
            return null;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0;i<numbers.length;i++){
            map.put(numbers[i], i);
        }
        int[] res = new int[2];
        for (int i=0; i<numbers.length; i++){
            int need = target - numbers[i];
            if (map.containsKey(need)){
                res[0] = i+1;
                res[1] = map.get(need) + 1;
                break;
            }
        }
        return res;
    }
    // 57.三数之和=target的所有组合O(nlogn)+O(n^2)
    public List<List<Integer>> threeSum(int[] numbers) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i = 0; i < numbers.length-1; i++) {
            int l = i + 1, r = numbers.length-1;
            while (l < r) {
                int sum = numbers[i] + numbers[l] + numbers[r];
                if (sum == 0) {
                    List<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(numbers[i]);
                    tmp.add(numbers[l]);
                    tmp.add(numbers[r]);
                    if (!res.contains(tmp)) res.add(tmp);
                }
                if (sum <0) l++;
                else r--;
            }
        }
        return res;
    }

    // 58.四数之和,
    public List<List<Integer>> fourSum(int[] numbers, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                int tmp = numbers[i] + numbers[j];
                int k = j+1, l = numbers.length - 1;
                while (k < l) {
                    int new_sum = tmp + numbers[k] + numbers[l];
                    if (new_sum == target) {
                        List<Integer> tmpList = new ArrayList<Integer>();
                        tmpList.add(numbers[i]);
                        tmpList.add(numbers[j]);
                        tmpList.add(numbers[k]);
                        tmpList.add(numbers[l]);
                        if (!ret.contains(tmpList)) {
                            ret.add(tmpList);
                        }
                        k++;
                        l--;
                    } else if (new_sum < target) {
                        k++;
                    } else {
                        l--;
                    }
                }
            }
        }
        return ret;
    }
    // 59.最接近的三数之和
    public int threeSumClosest(int[] numbers, int target) {
        Arrays.sort(numbers);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < numbers.length - 1; i++) {
            int j = i + 1, k = numbers.length - 1;
            while (j < k) {
                int sum = numbers[i] + numbers[j] + numbers[k];
                res = Math.abs(target-sum) < Math.abs(res-target) ? sum : res;
                if (sum < target) j++;
                else if(sum> target)k--;
                else return sum;
            }
        }
        return res;
    }
    // 排序只有0,1,2的数组,O(n)
    public void sortColors(int[] nums) {
        int left = 0, cur = 0, right = nums.length - 1;
        while (cur <= right) {
            if (nums[cur] == 0) swap(nums, left++, cur++);
            else if (nums[cur] == 1) cur++;
            else if (nums[cur] == 2) swap(nums, cur, right--);
        }
    }
    public void swap(int[] arr, int left, int right) {
        int tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
    }
    // 633.找到1~n数字中个一重复的，不排序，空间O(1)
    public int findDuplicate(int[] nums) {
        //若不大于mid的数字个数比mid多，
        // 则重复出现在[low, mid]之间。
        //若不大于mid的数字个数比mid少，
        // 重复出现在后半段中[mid+1，high]
        if (nums == null) return -1;
        int l = 1;
        int r = nums.length - 1;
        while (l < r) {
            int mid = (l+r)/2;
            int cnt = 0;
            for (int i=0;i<nums.length;i++){
                if (nums[i] <= mid) cnt++;
            }
            if (cnt > mid) r = mid;
            else l = mid+1;
        }
        return l;
    }
    // 428.x的n次幂O(logn)
    double myPow(double x, int n) {
        double res = 1.0;
        for (int i = n; i != 0; i /= 2) {
            if (i % 2 != 0) res *= x;  // 整体思想折半,奇数折半后丢了1个,找回来
            x *= x;
        }
        return n < 0 ? 1 / res : res;
    }
    // 184.拼接最大数:给出 [1, 20, 23, 4, 8]，返回8423201.  <0 升序 >0 降序
    public String largestNumber(int[] num) {
        if(num == null || num.length == 0) return "";
        String[] strs = new String[num.length];
        for(int i = 0; i < num.length; i++){
            strs[i] = String.valueOf(num[i]);
        }
        Arrays.sort(strs, new NumberCompare());
        StringBuilder sb = new StringBuilder();
        for(String i : strs) {
            sb.append(i);
        }
        String res =  sb.toString();
        int index = 0;
        while(index < res.length() && res.charAt(index) == '0'){
            index++;
        }
        if(index == res.length()) return "0";
        return res.substring(index);
    }
    class NumberCompare implements Comparator<String>{
        @Override
        public int compare(String s1, String s2){
            return (s2+s1).compareTo(s1+s2);
        }
    }


    /*------------------ 树 ------------------*/
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
    // 二叉树第K层的节点个数
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
    // 二叉树是否等价
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
    // 442.实现Trie
    class TrieNode {
        boolean isEnd;
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
                if (i==word.length()-1) pre.isEnd =true;
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
                if (i == word.length()-1 && pre.children[index].isEnd == false) return false;
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

}
