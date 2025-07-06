from collections import defaultdict

def most_common_prefix(words):
    
    prefix_map = defaultdict(set)

    # Find all common prefixes between word pairs
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            w1, w2 = words[i], words[j]
            prefix = []
            for k in range(min(len(w1), len(w2))):
                if w1[k] == w2[k]:
                    prefix.append(w1[k])
                else:
                    break
            if prefix:
                joined_prefix = ''.join(prefix)
                prefix_map[joined_prefix].update([w1, w2])

    if not prefix_map:
        return {"No common prefix found"}

    # Find max count of associated words
    max_count = max(len(words) for words in prefix_map.values())

    # Return all prefixes with that max count
    most_common = {
        prefix for prefix, group in prefix_map.items()
        if len(group) == max_count
    }

    return most_common

# Example usage
words_list =eval(input("enter list of strings:"))
prefixes = most_common_prefix(words_list)
print("Most common prefix(es):", prefixes)
