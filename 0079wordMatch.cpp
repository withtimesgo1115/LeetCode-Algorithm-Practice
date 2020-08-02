class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        // 从每一个格子出发，DFS+回溯，如果DFS判断成功了就返回true,否则返回false
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                if(backtrack(board, word, 0, i, j)){
                    return true;
                }
            }
        }
        return false;
    }

private: 
    bool backtrack(vector<vector<char>>& board, string& word, int wordIndex, int x, int y){
        // 当前位字母不能匹配，此路不通
        if(board[x][y] != word[wordIndex]){
            return false;
        }
        // 边界条件，最后一个字母也相等，那么返回成功
        if(word.size() - 1 == wordIndex){
            return true;
        }
        // 保存当前位的字母
        char temp = board[x][y];
        // 清除当前位的字母，避免重复使用
        board[x][y] = 0;
        // 在能匹配当前字母的情况下，准备匹配下一个字母
        wordIndex++;
        // 往上走
        if((x > 0 && backtrack(board, word, wordIndex, x-1, y))
        // 往左走
        || (y > 0 && backtrack(board, word, wordIndex, x, y-1))
        // 往下走
        || (x < board.size()-1 && backtrack(board, word, wordIndex, x+1, y))
        // 往右走
        || (y < board[0].size()-1 && backtrack(board, word, wordIndex, x, y+1))){
            // 其中有任何一个能走通就算成功
            return true;
        }
        // 如果都不通，则回溯上一个状态，将保存的值再给重新赋值
        board[x][y] = temp;
        return false;
    }
};