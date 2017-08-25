#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <string>
using namespace std;

/*
 * 前序遍历-非递归
 * 中序遍历
 * 后序遍历
 * 广度优先遍历,二叉树层次遍历
 * 二叉树第K层节点个数
 * 二叉树最大深度
 * 翻转二叉树-可以破坏原结构
 * 判断是否是等价二叉树
 * 最近公共祖先-递归
 * 二叉树中叶节点个数
 * 判断二叉树是不是完全二叉树
 * 前序遍历和中序遍历树构造二叉树
 * 中序遍历和后序遍历树构造二叉树
 * 二叉树的序列化和反序列化
 *
 *
 *
 * 二叉树最小深度
 * */


class TreeNode {
public:
     int val;
     TreeNode *left, *right;
     TreeNode(int val) {
         this->val = val;
         this->left = this->right = NULL;
     }
};


/*1. 前序遍历-非递归*/
vector<int> preorderTraversal(TreeNode *root) {
    stack<TreeNode *> s;
    vector<int> res;
    if(root != NULL) s.push(root);
    while (!s.empty()) {
        TreeNode *curr = s.top();
        s.pop();
        res.push_back(curr->val);
        if (curr->right) {
            s.push(curr->right);
        }
        if (curr->left) {
            s.push(curr->left);
        }
    }

    return res;
}
/*2.中序遍历*/
vector<int> inorderTraversal(TreeNode * root) {
    stack<TreeNode *> s;
    vector<int> res;
    TreeNode* cur = root;
    while (true) {
        while (cur) {
            s.push(cur);
            cur = cur->left;
        }

        if (s.empty()) {
            break;
        }
        cur = s.top();
        s.pop();
        res.push_back(cur->val);
        cur = cur->right;
    }
    return res;
}
/*3.后序遍历*/
vector<int> postorderTraversal(TreeNode * root) {
    stack<TreeNode *> s;
    stack<TreeNode *> output;
    vector<int > res;

    if (root != NULL) s.push(root);
    while (!s.empty()) {
        TreeNode* cur = s.top();
        s.pop();
        output.push(cur);
        if (cur->left) s.push(cur->left);
        if (cur->right) s.push(cur->right);
    }

    while (!output.empty()) {
        TreeNode* tmp = output.top();
        output.pop();
        res.push_back(tmp->val);
    }
    return res;
}
/*4.广度优先遍历,二叉树层次遍历*/
vector<vector<int>> levelOrder(TreeNode * root) {
    int current_level_num = 1;
    int next_level_num = 0;
    queue<TreeNode *> q;
    vector<vector<int >> res;

    if(root != NULL) q.push(root);
    vector<int > tmp;
    while (!q.empty()) {
        TreeNode* curr = q.front();
        tmp.push_back(curr->val),q.pop();
        current_level_num --;
        if (curr->left) {
            q.push(curr->left);
            next_level_num++;
        }
        if (curr->right) {
            q.push(curr->right);
            next_level_num++;
        }
        if (current_level_num == 0) {
            res.push_back(tmp);
            vector<int> t;
            tmp = t;
            current_level_num = next_level_num;
            next_level_num = 0;
        }
    }
    return res;
}
/*5.二叉树第K层节点个数*/
int getNodeNumKthLevel(TreeNode* root,int k){
    int current_level_num = 1;
    int next_level_num = 0;
    queue<TreeNode *> q;
    int i= 0;
    if(root != NULL) q.push(root);

    while (!q.empty() && i<k) {
        TreeNode* curr = q.front();
        q.pop();
        current_level_num --;
        if (curr->left) {
            q.push(curr->left);
            next_level_num++;
        }
        if (curr->right) {
            q.push(curr->right);
            next_level_num++;
        }
        if (current_level_num == 0) {
            current_level_num = next_level_num;
            next_level_num = 0;
            i++;
        }
    }
    return current_level_num;
}
/*6.二叉树最大深度*/
int maxDepth(TreeNode *root) {
    int depth = 0;
    int cur_num = 1;
    int next_num = 0;
    queue<TreeNode *> q;
    if (root!=NULL) q.push(root);

    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        cur_num--;

        if (cur->left) {
            q.push(cur->left);
            next_num++;
        }
        if (cur->right) {
            q.push(cur->right);
            next_num ++;
        }
        if (cur_num == 0){
            depth++;
            cur_num = next_num;
            next_num=0;
        }
    }
    return depth;
}
/*7.翻转二叉树-可以破坏原结构*/
void invertBinaryTree(TreeNode *root) {
    stack<TreeNode *> s;
    if (root != NULL) s.push(root);
    while (!s.empty()) {
        TreeNode* cur = s.top();
        s.pop();
        //交换左右
        TreeNode* tmp = cur->left;
        cur->left = cur->right;
        cur->right = tmp;

        if (cur->right != NULL) s.push(cur->right);
        if (cur->left != NULL) s.push(cur->left);
    }
}
/*8.判断是否是等价二叉树*/
bool isIdentical(TreeNode * a, TreeNode * b) {
    stack<TreeNode*> s1;
    stack<TreeNode*> s2;
    if(a == NULL || b==NULL){
        return false;
    }
    if(a!=NULL && b!=NULL){
        s1.push(a);
        s2.push(b);
    }
    while (!s1.empty() && !s2.empty()) {
        TreeNode* n1 = s1.top();
        TreeNode* n2 = s2.top();
        s1.pop(),s2.pop();
        if (n1 == NULL && n2 == NULL){ continue;}
        else if(n1!=NULL && n2!=NULL && n1->val==n2->val){
            s1.push(n1->right);
            s1.push(n1->left);
            s2.push(n2->right);
            s2.push(n2->left);
        } else{
            return false;
        }
    }
    return true;
}
/*9.最近公共祖先-递归*/
TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *A, TreeNode *B) {
    if (root == NULL) return NULL;
    if (root == A || root == B) return root;

    TreeNode* left_node = lowestCommonAncestor(root->left, A, B);
    TreeNode* right_node = lowestCommonAncestor(root->right, A, B);

    if (left_node != NULL && right_node != NULL) {
        return root;
    }
    if (left_node != NULL){
        return left_node;
    }
    return right_node;
}
/*10.二叉树中叶节点个数*/
int getLeafNodeNum(TreeNode* root) {
    if (root == NULL) return 0;

    int res = 0;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        if (cur->left) q.push(cur->left);
        if (cur->right) q.push(cur->right);
        if (cur->left == NULL && cur->right ==NULL) res ++;
    }
    return res;
}
/*11.判断二叉树是不是完全二叉树*/
bool isCompleteBinaryTree(TreeNode* root) {
    if (root == NULL) return false;
    bool res = false;
    bool mustHasNoChild = false;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        if (mustHasNoChild) {
            if (cur->left || cur->right) {
                res = false;
                break;
            }
        } else{
            if (cur->left!=NULL && cur->right!=NULL) {
                q.push(cur->left);
                q.push(cur->right);
            } else if (cur->left == NULL && cur->right != NULL) {
                res = false;
                break;
            } else if (cur->right == NULL && cur->left != NULL) {
                mustHasNoChild = true;
                q.push(cur->left);
            } else {
                mustHasNoChild = true;
            }
        }
    }
    return res;
}
/*12.前序遍历和中序遍历树构造二叉树*/
TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
    TreeNode *root = NULL;
    vector<int> preorder_l,preorder_r,inorder_l,inorder_r;
    int root_index=0;

    if(!preorder.empty() || !inorder.empty()) {
        root = new TreeNode(preorder[0]); //在前序队列中找根节点
        //  在中序队列中找出根节点位置
        for(int i=0; i<inorder.size(); i++) {
            if(preorder[0] == inorder[i])
                break;
            root_index++;
        }
        //  左右子树的前序、中序队列
        for(int i=0; i<root_index; i++) {
            preorder_l.push_back(preorder[i+1]);//inorder\preoder左树节点个数=
            inorder_l.push_back(inorder[i]);
        }
        for(int i=root_index+1; i<inorder.size(); i++) {
            preorder_r.push_back(preorder[i]);
            inorder_r.push_back(inorder[i]);
        }
        root->left = buildTree(preorder_l, inorder_l);
        root->right = buildTree(preorder_r, inorder_r);
    }
    return root;
}
/*13.中序遍历和后序遍历树构造二叉树*/
TreeNode *buildTree_2(vector<int> &inorder, vector<int> &postorder) {
    TreeNode *root = NULL;
    vector<int> inorder_l,inorder_r,postorder_l,postorder_r;
    int root_index=0;
    int size = postorder.size();
    if(inorder.empty()!=1 || postorder.empty()!=1) {
        root = new TreeNode(postorder[size-1]);
        //  在中序队列中找出根节点位置
        for(int i=0; i<inorder.size(); i++) {
            if(postorder[size-1] == inorder[i])
                break;
            root_index++;
        }
        for(int i=0; i<root_index; i++) {
            postorder_l.push_back(postorder[i]);//postord开头也是左节点
            inorder_l.push_back(inorder[i]);
        }
        for(int i=root_index+1; i<inorder.size(); i++) {
            postorder_r.push_back(postorder[i-1]);//注意下标
            inorder_r.push_back(inorder[i]);
        }
        root->left = buildTree(inorder_l, postorder_l);
        root->right = buildTree(inorder_r, postorder_r);
    }
    return root;
}
/*14.二叉树的序列化和反序列化*/
string serialize(TreeNode *root) {
    string res = "";
    if (root == NULL) return "";
    queue<TreeNode*> q;
    q.push(root);
    res += root->val;
    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        if (cur == NULL) continue;
        if (cur->left != NULL) {
            res += "," + cur->left->val;
        } else{
            res += ",#";
        }
        if (cur->right != NULL) {
            res += "," + cur->right->val;
        } else{
            res += ",#";
        }
        q.push(cur->left), q.push(cur->right);
    }
    int i=q.size()-1;
    while (res[i] == '#' || res[i] == ','){
        i--;
    }
    return res.substr(0,i+1);
}
TreeNode *deserialize(string data) {
    if (data == "") return NULL;
    //std::string data = data;
    vector<string> strVec = split(data,",");
    split_t(data, strVec, ",");
    int root_val = atoi(strVec[0].c_str());
    TreeNode* root = new TreeNode(root_val);
    vector<TreeNode*> nodeVec;
    nodeVec.push_back(root);
    bool isLeft = true;
    int idx = 0;

    for (int i = 1; i < strVec.size(); ++i) {
        if (strVec[i] != "#") {
            int val = atoi(strVec[i].c_str());
            TreeNode* cur = new TreeNode(val);
            if (isLeft) nodeVec[idx]->left = cur;
            else nodeVec[idx]->right = cur;
            nodeVec.push_back(cur);
        }
        if (!isLeft) idx++;
        isLeft = !isLeft;
    }
    return root;
}
void split(const std::string& s, std::vector<std::string>& v, const std::string& c) {
    std::string::size_type pos1, pos2;
    pos2 = s.find(c);
    pos1 = 0;
    while(std::string::npos != pos2)
    {
        v.push_back(s.substr(pos1, pos2-pos1));

        pos1 = pos2 + c.size();
        pos2 = s.find(c, pos1);
    }
    if(pos1 != s.length())
        v.push_back(s.substr(pos1));
}


/*11.求二叉树中和为给定值的所有路径*/

/*二叉树最小深度-前面有MaxDeepth，这个算随便练手吧*/
int minDepth(TreeNode *root) {
    if (root == NULL) return 0;
    int level = 1;
    int cur_level_num = 1;
    int next_level_num = 0;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        cur_level_num --;
        if (cur->left == NULL && cur->right == NULL) return level;
        if (cur->left != NULL) {
            q.push(cur->left);
            next_level_num++;
        }
        if (cur->right != NULL) {
            q.push(cur->right);
            next_level_num++;
        }
        if (cur_level_num == 0 ){
            cur_level_num = next_level_num;
            next_level_num = 0;
            level ++;
        }
    }
}