import pinyin

def convert_to_pinyin(text):
    return pinyin.get(text, format="strip", delimiter=" ")

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()  # Read input from Automator
    result = convert_to_pinyin(text)
    print(result)
