// Given a 2D board and a list of words from the dictionary, find all words in the board.

// Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

// For example,
// Given words = ["oath","pea","eat","rain"] and board =

// [
//   ['o','a','a','n'],
//   ['e','t','a','e'],
//   ['i','h','k','r'],
//   ['i','f','l','v']
// ]
// Return ["eat","oath"].
// Note:
// You may assume that all inputs are consist of lowercase letters a-z.

class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode(): val('\0'), is_word(false), parent(nullptr) {
    }
    TrieNode(char c): val(c), is_word(false), parent(nullptr) {
    }
    
    char val;
    bool is_word;
    TrieNode* parent;
    unordered_map<char, TrieNode*> children;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }
    
    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode* track = root;
        int index = 0;
        while (index < word.size()) {
            if (track->children.count(word[index]) == 1)
                track = track->children[word[index++]];
            else
                break;
        }
        while (index < word.size()) {
            TrieNode* new_node = new TrieNode(word[index]);
            new_node->parent = track;
            track->children[word[index++]] = new_node;
            track = new_node;
        }
        track->is_word = true;
    }
    
    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode* track = root;
        int index = 0;
        while (index < word.size()) {
            if (track->children.count(word[index]) == 1)
                track = track->children[word[index++]];
            else
                return false;
        }
        return track->is_word;
    }
    
    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode* track = root;
        int index = 0;
        while (index < prefix.size()) {
            if (track->children.count(prefix[index]) == 1)
                track = track->children[prefix[index++]];
            else
                return false;
        }
        return true;
    }
    
    void erase(string str) {
        TrieNode* track = root;
        int index = 0;
        while (index < str.size()) {
            if (track->children.count(str[index]) == 1)
                track = track->children[str[index++]];
            else
                return; // no such string to delete
        }
        if (track->is_word && track->children.empty()) { // if it's a word with no children
            do {
                TrieNode* tmp = track->parent;
                tmp->children.erase(track->val);
                delete track;
                track = tmp;
            } while (!track->is_word && track->children.empty() && track != root);
                }
        else if (track->is_word) // if it's a word with children
            track->is_word = false;
    }
private:
    TrieNode* root;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie trie;
        for (auto &str : words) {
            trie.insert(str);
        }
        int i = 0, m = board.size(), n = (m) ? board[0].size() : 0;
        vector<string> result;
        vector<vector<bool>> av;
        av.assign(m, vector<bool>(n, true));
        for(; i != m * n; i++) {
            if (result.size() == words.size()) break;
            string str (1, board[i/n][i%n]);
            // cout << "starting at " << str << '\n';
            check(board, trie, result, av, str, i/n, i%n);
        }
        return result;
    }
    
    void check(vector<vector<char>>& board, Trie &trie, vector<string> &result, vector<vector<bool>> &av, string &str, int r, int c) {
        // cout << "trying " << str << '\n';
        if (!trie.startsWith(str)) {
            // cout << "hopeless" << '\n';
            str.pop_back();
            return;
        }
        av[r][c] = false;
        if (trie.search(str)) { 
            // cout << "found " << str << '\n';
            result.push_back(str);
            trie.erase(str);
        }
        if (c > 0 && av[r][c - 1]) {
            str.push_back(board[r][c - 1]);
            check(board, trie, result, av, str, r, c - 1);
        }
        if (r > 0 && av[r - 1][c]) {
            str.push_back(board[r - 1][c]);
            check(board, trie, result, av, str, r - 1, c );
        }
        if (c + 1 < board[0].size() && av[r][c + 1]) {
            str.push_back(board[r][c + 1]);
            check(board, trie, result, av, str, r, c + 1 );
        }
        if (r + 1 < board.size() && av[r + 1][c]) {
            str.push_back(board[r + 1][c]);
            check(board, trie, result, av, str, r + 1, c );
        }
        
        av[r][c] = true;
        
        str.pop_back();
    }
};
