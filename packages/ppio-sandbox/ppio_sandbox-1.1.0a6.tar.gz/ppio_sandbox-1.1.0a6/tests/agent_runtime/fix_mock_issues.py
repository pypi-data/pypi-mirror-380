#!/usr/bin/env python3
"""
批量修复集成测试中的 mock 对象问题
"""
import re
import os
import subprocess

def fix_file_issues(filepath):
    """修复单个文件中的 mock 问题"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # 修复 response.json.return_value 问题
    content = re.sub(
        r'(\s+)(.*\.json)\.return_value\s*=\s*({.*?})',
        r'\1\2 = AsyncMock(return_value=\3)',
        content,
        flags=re.DOTALL | re.MULTILINE
    )
    
    # 修复 response.text 的 mock
    content = re.sub(
        r'(\s+)(.*\.text)\s*=\s*"([^"]*)"',
        r'\1\2 = "\3"',
        content
    )
    
    # 确保导入了 AsyncMock
    if 'AsyncMock' in content and 'from unittest.mock import' in content:
        # 检查是否已经导入了 AsyncMock
        import_line = re.search(r'from unittest\.mock import ([^,\n]+(?:,\s*[^,\n]+)*)', content)
        if import_line:
            imports = [imp.strip() for imp in import_line.group(1).split(',')]
            if 'AsyncMock' not in imports:
                new_imports = ', '.join(imports + ['AsyncMock'])
                content = content.replace(import_line.group(0), f'from unittest.mock import {new_imports}')
    
    # 写回文件
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    # 找到所有集成测试文件
    test_files = []
    for root, dirs, files in os.walk('client/integration'):
        for file in files:
            if file.endswith('.py') and file.startswith('test_'):
                test_files.append(os.path.join(root, file))
    
    print(f"Found {len(test_files)} test files to process")
    
    for test_file in test_files:
        fix_file_issues(test_file)

if __name__ == '__main__':
    main()
