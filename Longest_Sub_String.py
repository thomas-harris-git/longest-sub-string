def longestUniqueSubsttr(s):

    chars_count = [-1] * 128
    s_len = len(s) 
    sub_len = 0
    x = 0
    out = ""
  
    for y in range(0, s_len):
    
        x = max(x, chars_count[ord(s[y])] + 1);

        if (sub_len < y - x + 1):
            sub_len = y - x + 1
            out = s[x:y+1]
   
        chars_count[ord(s[y])] = y;
    print("The input string is '"+s+"' has the length of the longest non-repeating character substring is",sub_len,"and the substring is '"+out+"'")
    pass
  

s = "zksdafjhsdlhaldisf"
longestUniqueSubsttr(s)


