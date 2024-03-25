import sys
file_path = "C:\\Users\\Ryan\\OneDrive\\מסמכים\\VSCODE\\pythonLearning\\python\\text testing\\test.txt"
sort_arr = {}
def func(word):
    global sort_arr
    if word in sort_arr:
        sort_arr[word] += 1
    else:
        sort_arr[word] = 1 
    
N = 5



try:
    with open(file_path, 'r') as f:
        file_content = f.read()
    content_arr = file_content.split()
    for word in content_arr:
        func(word)

    sorted_words = sorted(sort_arr,reverse=True)[:N]
    print(sorted_words)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error occurred while checking file: {e}")
print(sys.argv[0])