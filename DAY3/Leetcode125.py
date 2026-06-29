s=input()
cleaned=""
for ch in s:
    if ch.isalnum():
        cleaned=cleaned+ch.lower()
if cleaned==cleaned[::-1]:
    print(True)
else:
    print(False)
        