package interview.ali_2018_2;

public class BinarySearch {


    // 457.经典二分查找问题
    public int binarySearch_1(int[] num, int target) {
        if (num == null || num.length == 0) {
            return -1;
        }
        int left = 0;
        int right = num.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (num[mid] == target) {
                return mid;
            } else if (num[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
    // 14.二分查找:找到target第一次出现的下标
    public int binarySearch_2(int[] num, int target) {
        if (num == null || num.length == 0) {
            return -1;
        }
        int left = 0;
        int right = num.length - 1;
        int res = -1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (num[mid] == target) {
                if (res < 0) {
                    res = mid;
                }
                if (res > 0 && mid < res) {
                    res = mid;
                }
                right--;
            } else if (num[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
    // 62.旋转排序数组搜索target
    public int search_1(int[] num, int target) {
        if (num == null || num.length == 0) {
            return -1;
        }
        int left = 0;
        int right = num.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;

            if (num[mid] == target) return mid;
            if (num[left] == target) return left;
            if (num[right] == target) return right;

            if (num[left] < num[mid]) {  // 左边递增
                if (num[left] < target && target < num[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (num[mid] < num[right]) {  // 右边递增
                if (num[mid] < target && target < num[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }else {
                left++;
            }
        }
        return -1;
    }
    // 159. 寻找旋转排序数组中的最小值
    public int search_2(int[] num, int target) {
        if (num == null || num.length == 0) {
            return -1;
        }
        int left = 0;
        int right = num.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (mid - 1 > 0 && num[mid - 1] > num[mid]) {
                return num[mid];
            }
            if (mid + 1 < num.length - 1 && num[mid] > num[mid+1]) {
                return num[mid+1];
            }
            if (num[left] < num[mid]) {
                left = mid + 1;
            } else if (num[mid] < num[right]) {
                right = mid - 1;
            }
        }
        return -1;
    }

    // 28.搜索二维矩阵:每行中的整数从左到右是排序的,每行的第一个数大于上一行的最后一个整数。
    public boolean findMatrix(int m[][], int target) {
        if (m == null || m.length == 0) {
            return false;
        }
        int row = m.length - 1;
        int colLen = m[0].length - 1;
        int rowIdx = -1;
        int left = 0;
        int right = m[0].length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (m[mid][0] == target || m[mid][colLen] == target) return true;
            if (m[mid][0] < target && target < m[mid][colLen]) {
                rowIdx = mid;
                break;
            } else if (m[mid][0] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        left = 0;
        right = colLen;
        while (left < right) {
            int mid = (left + right) / 2;
            if (m[rowIdx][mid] == target) {
                return true;
            } else if (m[rowIdx][mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
    // 38.搜索二维矩阵2:写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。
    //  每行中的整数从左到右是排序的,每一列的整数从上到下是排序的,在每一行或每一列中没有重复的整数.
    public int findMatrix2(int m[][], int target) {
        /*[
            [1, 3, 5, 7],
            [2, 4, 7, 8],
            [3, 5, 9, 10]
        ]*/
        if (m == null || m.length == 0) {
            return 0;
        }
        int r = 0;
        int c = m[0].length - 1;
        int res = 0;
        while (r < m.length && c >= 0) {
            if (m[r][c] == target) {
                res++;
                r++;
                c--;
            } else if (m[r][c] > target) {
                c--;
            } else {
                r++;
            }
        }
        return res;
    }

    // 428.x的n次幂O(logn)
    double myPow(double x, int n) {
        double res = 0;
        for (int i = n; i != 0; i /= 2) {
            if (i % 2 != 0) {  // 奇数除了x*x外,要多乘x
                res *= x;
            }
            x *= x;
        }
        return n < 0 ? 1/res : res;
    }
    // 633.找到1~n数字中个一重复的，不排序，空间O(1)

}
