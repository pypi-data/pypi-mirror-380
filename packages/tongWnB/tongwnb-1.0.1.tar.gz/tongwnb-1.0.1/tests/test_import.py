#!/usr/bin/env python3
"""
测试 tongWnB 包的基本导入功能
"""

def test_import():
    """测试 tongWnB 包是否可以正常导入"""
    try:
        import tongWnB
        print("✓ tongWnB 包导入成功")
        
        # 检查是否有 init 和 log 函数
        if hasattr(tongWnB, 'init'):
            print("✓ tongWnB.init 函数存在")
        else:
            print("✗ tongWnB.init 函数不存在")
            
        if hasattr(tongWnB, 'log'):
            print("✓ tongWnB.log 函数存在")
        else:
            print("✗ tongWnB.log 函数不存在")
            
        # 检查函数是否可调用
        if callable(tongWnB.init):
            print("✓ tongWnB.init 是可调用的")
        else:
            print("✗ tongWnB.init 不可调用")
            
        if callable(tongWnB.log):
            print("✓ tongWnB.log 是可调用的")
        else:
            print("✗ tongWnB.log 不可调用")
            
        return True
        
    except ImportError as e:
        print(f"✗ tongWnB 包导入失败: {e}")
        return False
    except Exception as e:
        print(f"✗ 其他错误: {e}")
        return False

if __name__ == "__main__":
    test_import()
