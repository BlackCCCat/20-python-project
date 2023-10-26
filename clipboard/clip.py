import sys

# initialize clipboard storage 
clipboard_storage = {}

# Copy text to clipboard
def copy(keyword, text):
    # 无法复制相同的关键词内容
    clipboard_storage.update({keyword: text})

# Paste text from clipboard
def paste(keyword):
    content = clipboard_storage.get(keyword)
    return content

# list available keywords
def list_keywords():
    return list(clipboard_storage.keys())

def clear(keyword):
    if keyword in clipboard_storage.keys():
        del clipboard_storage[keyword]
    else:
        print(f'{keyword} not found.')

def clipboard():
    copy('work', 'work-related notes')
    copy('home', 'grocery-list')
    copy('number', '15100111100')
    copy('address', 'Beijing, China')
    copy('name', 'Tom')
    
    print(paste('work'))
    print(paste('home'))
    print(paste('name'))
    
    print(f'Available keywords: {list_keywords()}')
    
    clear('work')
    
    print(f'Available keywords: {list_keywords()}')

if __name__ == '__main__':
    clipboard()
        