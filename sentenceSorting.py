class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        i=1
        while(i<len(words)):
            tempNum = words[i][-1]
            tempVal=words[i]
            j=i-1
            while(j>=0 and words[j][-1]>tempNum):
                words[j+1]=words[j]
                j-=1
            words[j+1]=tempVal
            i+=1
        # remove the numbers
        sente=""
        for x in range(len(words)):
            words[x]=words[x][:-1]
            sente+=words[x]+" "
        print(sente[:-1])
        return(sente[:-1])
