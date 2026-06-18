# -*- coding: utf-8 -*-
import os
import re
import sys
import io
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from pypinyin import lazy_pinyin, Style
except ImportError:
    print("错误: 未安装 pypinyin 库，请先执行: pip install pypinyin")
    sys.exit(1)

class FileRenamer:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.rename_mapping = []
        self.conflicts = []
        self.skipped_files = []
        self.processed_count = 0
        
    def chinese_to_pinyin(self, chinese_text):
        pinyin_list = lazy_pinyin(chinese_text, style=Style.NORMAL)
        return ''.join(pinyin_list).lower()
    
    def parse_filename(self, filename):
        patterns = [
            r'^(\d+)[.\s．]?\s*([\u4e00-\u9fa5][^\.]*)\.js$',
            r'^(\d+)[.\s．]?\s*([\u4e00-\u9fa5][^\.]*)\.png$',
            r'^(\d+)[.\s．]?\s*([\u4e00-\u9fa5][^\.]*)\.jss$'
        ]
        
        for pattern in patterns:
            match = re.match(pattern, filename)
            if match:
                ext = filename.split('.')[-1]
                return {
                    'sequence': match.group(1),
                    'chinese_name': match.group(2).strip(),
                    'ext': 'js' if ext in ('js', 'jss') else ext
                }
        return None
    
    def generate_new_filename(self, parsed_info):
        pinyin_name = self.chinese_to_pinyin(parsed_info['chinese_name'])
        return f"{parsed_info['sequence']}. {pinyin_name}.{parsed_info['ext']}"
    
    def collect_files(self):
        if not os.path.isdir(self.target_dir):
            print(f"错误: 目录 '{self.target_dir}' 不存在")
            return False
        
        files = []
        for filename in os.listdir(self.target_dir):
            filepath = os.path.join(self.target_dir, filename)
            if os.path.isfile(filepath):
                parsed = self.parse_filename(filename)
                if parsed:
                    files.append((filename, filepath, parsed))
        
        if not files:
            print(f"提示: 在目录 '{self.target_dir}' 中未找到符合条件的文件")
            return False
        
        return files
    
    def detect_conflicts(self, files):
        pinyin_to_originals = defaultdict(list)
        
        for filename, _, parsed in files:
            new_name = self.generate_new_filename(parsed)
            pinyin_to_originals[new_name].append(filename)
        
        conflicts = []
        for new_name, originals in pinyin_to_originals.items():
            if len(originals) > 1:
                conflicts.append({
                    'new_name': new_name,
                    'originals': originals
                })
        
        return conflicts
    
    def build_rename_mapping(self, files):
        pinyin_count = defaultdict(int)
        mapping = []
        
        for filename, filepath, parsed in files:
            new_name = self.generate_new_filename(parsed)
            
            if new_name in [m['new_name'] for m in mapping]:
                pinyin_count[new_name] += 1
                base_name = new_name.rsplit('.', 1)[0]
                ext = new_name.split('.')[-1]
                new_name = f"{base_name}_{pinyin_count[new_name]}.{ext}"
            
            mapping.append({
                'original': filename,
                'original_path': filepath,
                'new_name': new_name,
                'new_path': os.path.join(self.target_dir, new_name)
            })
        
        return mapping
    
    def preview(self):
        files = self.collect_files()
        if not files:
            return False
        
        conflicts = self.detect_conflicts(files)
        if conflicts:
            print("\n[WARN] 检测到文件名冲突:")
            for conflict in conflicts:
                print(f"  目标文件名: '{conflict['new_name']}'")
                print(f"  冲突文件: {', '.join(conflict['originals'])}")
                print()
        
        self.rename_mapping = self.build_rename_mapping(files)
        
        print("\n" + "="*80)
        print("文件重命名预览")
        print("="*80)
        print(f"目标目录: {self.target_dir}")
        print(f"待处理文件数量: {len(self.rename_mapping)}")
        print("-"*80)
        
        for i, item in enumerate(self.rename_mapping, 1):
            status = "[OK]" if item['original'] != item['new_name'] else "[SKIP]"
            print(f"{status} [{i}/{len(self.rename_mapping)}]")
            print(f"   原始: {item['original']}")
            print(f"   新名: {item['new_name']}")
            print()
        
        return True
    
    def execute(self):
        if not self.rename_mapping:
            print("错误: 没有待重命名的文件，请先运行预览")
            return False
        
        print("\n" + "="*80)
        print("开始执行重命名操作")
        print("="*80)
        
        success_count = 0
        fail_count = 0
        
        for item in self.rename_mapping:
            try:
                if item['original'] == item['new_name']:
                    self.skipped_files.append(item['original'])
                    print(f"[SKIP] 跳过（名称相同）: {item['original']}")
                    continue
                
                if os.path.exists(item['new_path']):
                    print(f"[WARN] 跳过（目标文件已存在）: {item['original']}")
                    fail_count += 1
                    continue
                
                os.rename(item['original_path'], item['new_path'])
                print(f"[OK] 成功: {item['original']} -> {item['new_name']}")
                success_count += 1
                
            except PermissionError:
                print(f"[ERR] 权限错误: 无法重命名 '{item['original']}'")
                fail_count += 1
            except Exception as e:
                print(f"[ERR] 错误 ({item['original']}): {str(e)}")
                fail_count += 1
        
        self.processed_count = success_count
        
        print("\n" + "="*80)
        print("重命名操作完成")
        print("="*80)
        print(f"成功: {success_count}")
        print(f"失败: {fail_count}")
        print(f"跳过: {len(self.skipped_files)}")
        
        if self.skipped_files:
            print("\n跳过的文件:")
            for f in self.skipped_files:
                print(f"  - {f}")
        
        return success_count > 0

def main():
    if len(sys.argv) < 2:
        print("用法: python rename_files.py <目标目录> [--execute]")
        print("示例:")
        print("  python rename_files.py 'C:\\Users\\13343\\Desktop\\leecode-2412505005-王树成'")
        print("  python rename_files.py 'C:\\Users\\13343\\Desktop\\leecode-2412505005-王树成' --execute")
        print("\n不带 --execute 参数时仅预览，带参数时执行实际重命名")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    execute = len(sys.argv) > 2 and sys.argv[2] == "--execute"
    
    renamer = FileRenamer(target_dir)
    
    if not renamer.preview():
        sys.exit(1)
    
    if not execute:
        print("\n提示: 当前处于预览模式，未执行实际重命名操作")
        print("如需执行重命名，请添加 --execute 参数")
        sys.exit(0)
    
    confirm = input("\n确认执行重命名操作? (y/N): ")
    if confirm.lower() != 'y':
        print("操作已取消")
        sys.exit(0)
    
    renamer.execute()

if __name__ == "__main__":
    main()