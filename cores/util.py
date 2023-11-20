from collections import Counter

def get_top_k_common_words(issues, top_k=5):
    all_word = []
    for issue in issues:
        all_word += issue.issue.replace(".","").split(" ")
    while('' in all_word):
        all_word.remove('')
    all_word = [[x,all_word.count(x)] for x in set(all_word)]
    all_word = sorted(all_word, key=lambda x: x[1], reverse=True)

    arr_data = []
    if(top_k>len(all_word)):
        top_k = len(all_word)
    for i in range(top_k):
        data = {"word": str(all_word[i][0]), "frequency": int(all_word[i][1])},   
        arr_data.append(data)
    return (arr_data)
