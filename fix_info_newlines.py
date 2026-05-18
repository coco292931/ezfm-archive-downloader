import os
import io

root = os.path.join(os.path.dirname(__file__), 'downloads')
modified = []
for dirpath, dirs, files in os.walk(root):
    for name in files:
        if name.lower().endswith('.txt'):
            path = os.path.join(dirpath, name)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if '\\n' in content:
                new = content.replace('\\n', '\n')
                # also replace literal "\\r\\n" if present
                new = new.replace('\\r\\n', '\r\n')
                bak = path + '.bak'
                if not os.path.exists(bak):
                    with open(bak, 'w', encoding='utf-8') as bf:
                        bf.write(content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new)
                modified.append(path)

if modified:
    print('Modified files:')
    for p in modified:
        print(' -', p)
else:
    print('No files needed modification.')
