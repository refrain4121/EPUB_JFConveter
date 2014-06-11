# -*- coding: utf-8 -*-



class ZhTranslator:
    def __init__(self, wordDic, phraseDic):
        
        self.simplifedPhase = []
        self.traditionPhase = []
        self.simplfiedWord  = ""
        self.traditoinWord  = ""
        
        self.loadDict(wordDic, phraseDic)
        self.listLength = len(self.simplifedPhase)

    
    def StoT(self, text):
        for index in range(self.listLength):
            if self.simplifedPhase[index] in text:
                text = text.replace(self.simplifedPhase[index], self.traditionPhase[index])

        ret = "" 
        for word in text:
            i = self.simplfiedWord.find(word)
            ret +=(self.traditoinWord[i] if i!=-1 else word)
            
        return ret
        
    def loadDict(self, wordDic, phraseDic):
    
        f = open("Dictionary/word_s2t.txt", 'r', encoding = "utf8")
        for line in f :
            line = line.strip()
            tmp = line.split(',')
            self.simplfiedWord += tmp[0]
            self.traditoinWord += tmp[1]
        f.close()
        
        f = open("Dictionary/phrase_s2t.txt", 'r', encoding = "utf8")
        for line in f :
            line = line.strip()
            tmp = line.split(',')
            self.simplifedPhase.append(tmp[0])
            self.traditionPhase.append(tmp[1]) 

if __name__ == "__main__":
    wordDic = "Dictionary/phrase_s2t.txt"
    phraseDic = "Dictionary/word_s2t.txt"
    jianfan = ZhTranslator(wordDic,phraseDic)
    print (jianfan.StoT("松開"))