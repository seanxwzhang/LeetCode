// Implement a trie with insert, search, and startsWith methods.

// Note:
// You may assume that all inputs are consist of lowercase letters a-z.
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
    char val;
    bool isWord;
    unordered_map<char, TrieNode*> children;

public:
    TrieNode(): isWord(false) {}
    TrieNode(char c): val(c), isWord(false) {}
    bool hasChild(const char c) {
        return this->children.count(c) > 0;
    }
    void addChild(const char c) {
        this->children[c] = new TrieNode(c);
    }
    TrieNode* getChild(const char c) {
        return this->children[c];
    }
    void setWord() {
        this->isWord = true;
    }
    bool ifWord() {
        return this->isWord;
    }
};

class Trie {
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    Trie(): root(new TrieNode()) {
        
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto track = this->root;
        for (unsigned i = 0; i < word.length(); i++) {
            if (!track->hasChild(word[i])) {
                track->addChild(word[i]);
            }
            track = track->getChild(word[i]);
        }
        track->setWord();
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto track = this->root;
        for (unsigned i = 0; i < word.length(); i++) {
            if (!track->hasChild(word[i]))
                return false;
            track = track->getChild(word[i]);
        }
        return track->ifWord();
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto track = this->root;
        for (unsigned i = 0; i < prefix.length(); i++) {
            if (!track->hasChild(prefix[i]))    
                return false;
            track = track->getChild(prefix[i]);
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */