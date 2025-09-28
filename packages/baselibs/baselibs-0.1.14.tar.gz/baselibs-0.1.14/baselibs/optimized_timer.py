#!/usr/bin/env python3
#coding:utf-8

__author__ = 'xmxoxo<xmxoxo@qq.com>'

import time
from typing import Optional, Dict, Any, List, Union
from contextlib import contextmanager
import functools

class TimerError(Exception):
    """计时器异常类"""
    pass

class TimeCount:
    """
    优化的计时器类
    
    功能特点：
    - 支持上下文管理器
    - 支持装饰器
    - 自动单位转换
    - 详细的统计信息
    - 更直观的API
    """
    
    def __init__(self, name: Optional[str] = None, auto_start: bool = False):
        self.name = name or "Timer"
        self._start_time: Optional[float] = None
        self._elapsed_times: List[float] = []
        self._lap_times: List[float] = []
        self._is_running = False
        
        if auto_start:
            self.start()
    
    def start(self) -> 'TimeCount':
        """开始计时"""
        if self._is_running:
            raise TimerError("计时器已经在运行中")
        
        self._start_time = time.time()
        self._is_running = True
        return self
    
    def stop(self) -> float:
        """停止计时并返回总耗时"""
        if not self._is_running:
            raise TimerError("计时器未在运行")
        
        elapsed_time = time.time() - self._start_time
        self._elapsed_times.append(elapsed_time)
        self._is_running = False
        return elapsed_time
    
    def lap(self) -> float:
        """记录一个lap时间，计时器继续运行"""
        if not self._is_running:
            raise TimerError("计时器未在运行")
        
        current_time = time.time()
        lap_time = current_time - self._start_time
        
        if self._lap_times:
            lap_duration = lap_time - sum(self._lap_times)
        else:
            lap_duration = lap_time
            
        self._lap_times.append(lap_duration)
        return lap_duration
    
    def pause(self) -> float:
        """暂停计时，返回当前耗时"""
        return self.stop()
    
    def resume(self) -> 'TimeCount':
        """恢复计时（重新开始一个新的计时周期）"""
        return self.start()
    
    def reset(self) -> 'TimeCount':
        """重置计时器"""
        self._start_time = None
        self._elapsed_times.clear()
        self._lap_times.clear()
        self._is_running = False
        return self
    
    @property
    def elapsed(self) -> float:
        """获取当前已运行时间（秒）"""
        if self._is_running:
            return time.time() - self._start_time
        return sum(self._elapsed_times) if self._elapsed_times else 0.0
    
    @property
    def elapsed_ms(self) -> float:
        """获取当前已运行时间（毫秒）"""
        return self.elapsed * 1000
    
    @property
    def is_running(self) -> bool:
        """检查计时器是否在运行"""
        return self._is_running
    
    @property
    def total_time(self) -> float:
        """获取总耗时（所有计时周期的总和）"""
        return sum(self._elapsed_times) + (self.elapsed if self._is_running else 0)
    
    @property
    def lap_times(self) -> List[float]:
        """获取所有lap时间"""
        return self._lap_times.copy()
    
    @property
    def stats(self) -> Dict[str, float]:
        """获取统计信息"""
        times = self._elapsed_times + ([self.elapsed] if self._is_running else [])
        
        if not times:
            return {}
        
        return {
            'count': len(times),
            'total': sum(times),
            'average': sum(times) / len(times),
            'min': min(times),
            'max': max(times),
            'last': times[-1]
        }
    
    def format_time(self, seconds: float, unit: str = 'auto') -> str:
        """格式化时间显示"""
        if unit == 'auto':
            if seconds < 0.001:
                return f"{seconds * 1000000:.3f}μs"
            elif seconds < 1:
                return f"{seconds * 1000:.3f}ms"
            elif seconds < 60:
                return f"{seconds:.3f}s"
            elif seconds < 3600:
                return f"{seconds/60:.2f}min"
            else:
                return f"{seconds/3600:.2f}h"
        elif unit == 'ms':
            return f"{seconds * 1000:.3f}ms"
        elif unit == 's':
            return f"{seconds:.3f}s"
        else:
            return str(seconds)
    
    def print_stats(self, prefix: str = "计时统计") -> None:
        """打印统计信息"""
        stats = self.stats
        if not stats:
            print(f"{prefix}: 无计时数据")
            return
        
        print(f"{prefix} - {self.name}:")
        print(f"  总次数: {stats['count']}")
        print(f"  总时间: {self.format_time(stats['total'])}")
        print(f"  平均时间: {self.format_time(stats['average'])}")
        print(f"  最短时间: {self.format_time(stats['min'])}")
        print(f"  最长时间: {self.format_time(stats['max'])}")
        print(f"  最后时间: {self.format_time(stats['last'])}")
    
    def print_laps(self, prefix: str = "Lap") -> None:
        """打印lap时间"""
        if not self._lap_times:
            print(f"{prefix}: 无lap数据")
            return
        
        print(f"{prefix} 时间:")
        for i, lap_time in enumerate(self._lap_times, 1):
            print(f"  {i}: {self.format_time(lap_time)}")
    
    def __enter__(self):
        """上下文管理器入口"""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.stop()
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"{self.name}: {self.format_time(self.elapsed)}"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return f"TimeCount(name='{self.name}', elapsed={self.elapsed:.3f}s, running={self._is_running})"


# 装饰器函数
def timer_decorator(name: Optional[str] = None, print_result: bool = True):
    """
    计时装饰器
    
    使用示例：
    @timer_decorator("my_function")
    def my_function():
        time.sleep(1)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timer_name = name or func.__name__
            with TimeCount(timer_name) as timer:
                result = func(*args, **kwargs)
            
            if print_result:
                print(f"{timer_name} 执行时间: {timer.format_time(timer.elapsed)}")
            
            return result
        return wrapper
    return decorator


# 便捷函数
def timeit(code: str, number: int = 1, globals_dict: Optional[Dict] = None) -> float:
    """
    便捷计时函数
    
    使用示例：
    timeit("time.sleep(1)", number=3)
    """
    if globals_dict is None:
        globals_dict = globals()
    
    total_time = 0.0
    for _ in range(number):
        with TimeCount("timeit") as timer:
            exec(code, globals_dict)
        total_time += timer.elapsed
    
    average_time = total_time / number
    print(f"执行 {number} 次，平均时间: {TimeCount().format_time(average_time)}")
    return average_time


if __name__ == '__main__':
    # 示例用法
    
    # 基本用法
    timer = TimeCount("测试计时器")
    timer.start()
    time.sleep(1.5)
    lap1 = timer.lap()
    time.sleep(0.5)
    lap2 = timer.lap()
    total = timer.stop()
    
    print(f"总时间: {timer.format_time(total)}")
    print(f"Lap1: {timer.format_time(lap1)}")
    print(f"Lap2: {timer.format_time(lap2)}")
    timer.print_stats()
    timer.print_laps()
    
    print("\n" + "="*50 + "\n")
    
    # 上下文管理器用法
    with TimeCount("上下文计时") as t:
        time.sleep(1)
    print(f"上下文用时: {t.format_time(t.elapsed)}")
    
    print("\n" + "="*50 + "\n")
    
    # 装饰器用法
    @timer_decorator("示例函数")
    def example_function():
        time.sleep(0.5)
    
    example_function()
    
    print("\n" + "="*50 + "\n")
    
    # timeit用法
    timeit("time.sleep(0.1)", number=3)