text = "私の好きな果物はりんごです"
pattern = "りんご"
replacement = "マンゴー"

pattern_len = len(pattern)

for i in range(len(text) - pattern_len + 1):
    if text[i : i + pattern_len] == pattern:
        print("Found at position:", i + 1)
        
        before = text[:i]
        after = text[i + pattern_len :]
        text = before + replacement + after
        break

print("Result:", text)