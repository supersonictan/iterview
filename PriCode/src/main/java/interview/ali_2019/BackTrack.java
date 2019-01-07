package interview.ali_2019;


/*
* 79. 单词搜索
* */
public class BackTrack {

    // 79. 单词搜索
    public boolean exist(char[][] board, String word) {
        /**
         * https://yanjia.me/zh/2018/11/17/leetcode-word-search-i-ii/
         * https://segmentfault.com/a/1190000003697153
         * https://www.cnblogs.com/jimmycheng/p/7248179.html
         * 基本思路很简单，对矩阵里每个点都进行一次深度优先搜索，看它能够产生一个路径和所给的字符串是一样的。
         * 重点在如何优化搜索，避免不必要的计算。比如我们一个方向的搜索中已经发现了这个词，那我们就不用再搜索。
         * 另外，如果之前已经访问过的点，就能再访问了，防止出现循环。
         * 这里有两种方法，一种是可以记录一个已访问坐标的哈希表或数组。
         * 但更巧妙的方法是将本轮深度优先搜索中搜索过的数字变成临时存下来，
         * 然后就地换成另一个绝对不会被搜到的值（如果是有效值会干扰正常搜索），等递归回来之后再根据临时值变回来。
         * 更进一步，由于异或操作具有两次操作能变回原值的特性，
         * 而且正常字符异或某些数后（对于ASCII, 255足以）肯定得到的是非正常字符，所以实现这个替换最简单的方法就是异或上一个特定数255，然后再异或回来。
         */
        if (board == null || board.length == 0 || board.length * board[0].length < word.length()) return false;

        boolean[][] flag = new boolean[board.length][board[0].length];
        boolean res = false;

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0))
                    res = res || search(board, word, 0, i, j, flag);

                if (res) return true;
            }
        }
        return res;
    }
    private boolean search(char[][] board, String word, int wordIdx, int row, int col, boolean[][] flag) {
        if (wordIdx == word.length()) return true;

        if (row >= board.length || row < 0 || col >= board[0].length || col < 0 ||
                word.charAt(wordIdx) != board[row][col] || flag[row][col]) {
            return false;
        }

        flag[row][col] = true;

        boolean top = search(board, word, wordIdx + 1, row -1, col, flag);
        boolean bottom = search(board, word, wordIdx + 1, row + 1, col, flag);
        boolean left = search(board, word, wordIdx + 1, row, col - 1, flag);
        boolean right = search(board, word, wordIdx + 1, row, col + 1, flag);

        if (top || bottom || left || right) return true;

        flag[row][col] = false;

        return false;
    }
}
