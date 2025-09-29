import threading
import time
from typing import Any, Dict, Optional, Union
from collections import OrderedDict
import weakref


class GlobalMemoryCache:
    """
    全局内存缓存类，支持线程安全操作
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        """单例模式确保全局只有一个缓存实例"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(GlobalMemoryCache, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """初始化缓存"""
        # 避免重复初始化
        if hasattr(self, '_initialized'):
            return

        self._cache: Dict[str, Dict[str, Any]] = {}
        self._locks: Dict[str, threading.RLock] = {}
        self._cache_lock = threading.RLock()
        self._access_order = OrderedDict()  # 用于LRU
        self._max_size = 1000
        self._default_ttl = 3600  # 默认1小时过期

        # 标记已初始化
        self._initialized = True

    def _get_namespace_lock(self, namespace: str) -> threading.RLock:
        """获取命名空间锁"""
        with self._cache_lock:
            if namespace not in self._locks:
                self._locks[namespace] = threading.RLock()
            return self._locks[namespace]

    def set(self, key: str, value: Any, namespace: str = "default", ttl: Optional[int] = None) -> None:
        """
        设置缓存值

        Args:
            key: 缓存键
            value: 缓存值
            namespace: 命名空间，默认为"default"
            ttl: 过期时间（秒），None表示使用默认值
        """
        if ttl is None:
            ttl = self._default_ttl

        with self._get_namespace_lock(namespace):
            # 检查是否需要清理
            self._cleanup_if_needed()

            cache_key = f"{namespace}:{key}"
            expiration_time = time.time() + ttl

            cache_entry = {
                "value": value,
                "expiration": expiration_time,
                "created": time.time(),
                "access_count": 0
            }

            self._cache[cache_key] = cache_entry
            self._access_order[cache_key] = time.time()

            # 维护访问顺序（LRU）
            self._access_order.move_to_end(cache_key)

    def get(self, key: str, namespace: str = "default", default: Any = None) -> Any:
        """
        获取缓存值

        Args:
            key: 缓存键
            namespace: 命名空间
            default: 默认值

        Returns:
            缓存值或默认值
        """

        cache_key = f"{namespace}:{key}"

        with self._get_namespace_lock(namespace):
            if cache_key not in self._cache:
                return default

            entry = self._cache[cache_key]

            # 检查是否过期
            if entry["expiration"] < time.time():
                del self._cache[cache_key]
                if cache_key in self._access_order:
                    del self._access_order[cache_key]
                return default

            # 更新访问统计
            entry["access_count"] += 1
            self._access_order[cache_key] = time.time()  # 更新访问时间
            self._access_order.move_to_end(cache_key)

            return entry["value"]

    def delete(self, key: str, namespace: str = "default") -> bool:
        """
        删除缓存项

        Args:
            key: 缓存键
            namespace: 命名空间

        Returns:
            是否成功删除
        """
        cache_key = f"{namespace}:{key}"

        with self._get_namespace_lock(namespace):
            if cache_key in self._cache:
                del self._cache[cache_key]
                if cache_key in self._access_order:
                    del self._access_order[cache_key]
                return True
            return False

    def clear_namespace(self, namespace: str) -> int:
        """
        清空指定命名空间的所有缓存

        Args:
            namespace: 命名空间

        Returns:
            清除的缓存项数量
        """
        deleted_count = 0
        with self._get_namespace_lock(namespace):
            keys_to_delete = [
                key for key in self._cache.keys()
                if key.startswith(f"{namespace}:")
            ]

            for key in keys_to_delete:
                del self._cache[key]
                if key in self._access_order:
                    del self._access_order[key]
                deleted_count += 1

        return deleted_count

    def clear_all(self) -> None:
        """清空所有缓存"""
        with self._cache_lock:
            self._cache.clear()
            self._access_order.clear()
            self._locks.clear()

    def _cleanup_if_needed(self) -> None:
        """根据需要清理缓存"""
        current_size = len(self._cache)

        # 如果超过最大大小，执行LRU清理
        if current_size > self._max_size:
            self._cleanup_lru()

        # 清理过期项
        self._cleanup_expired()

    def _cleanup_lru(self) -> None:
        """LRU清理：移除最少使用的项"""
        items_to_remove = max(1, len(self._cache) - self._max_size)

        for _ in range(items_to_remove):
            if not self._access_order:
                break
            # 弹出最旧的项
            key, _ = self._access_order.popitem(last=False)
            if key in self._cache:
                del self._cache[key]

    def _cleanup_expired(self) -> None:
        """清理过期项"""
        current_time = time.time()
        expired_keys = [
            key for key, entry in self._cache.items()
            if entry["expiration"] < current_time
        ]

        for key in expired_keys:
            del self._cache[key]
            if key in self._access_order:
                del self._access_order[key]

    def _cleanup_locks(self) -> None:
        """清理不再使用的命名空间锁"""
        with self._cache_lock:
            current_namespaces = set()
            for key in self._cache.keys():
                if ":" in key:
                    namespace = key.split(":", 1)[0]
                    current_namespaces.add(namespace)

            # 移除不存在的命名空间锁
            locks_to_remove = [ns for ns in self._locks if ns not in current_namespaces]
            for ns in locks_to_remove:
                del self._locks[ns]

    def get_stats(self) -> Dict[str, Any]:
        """
        获取缓存统计信息

        Returns:
            包含统计信息的字典
        """
        with self._cache_lock:
            namespaces = set()
            total_items = len(self._cache)

            for key in self._cache.keys():
                namespace = key.split(":", 1)[0] if ":" in key else "default"
                namespaces.add(namespace)

            return {
                "total_items": total_items,
                "namespaces": list(namespaces),
                "max_size": self._max_size,
                "default_ttl": self._default_ttl
            }

    def exists(self, key: str, namespace: str = "default") -> bool:
        """
        检查缓存键是否存在且未过期

        Args:
            key: 缓存键
            namespace: 命名空间

        Returns:
            是否存在
        """
        cache_key = f"{namespace}:{key}"

        with self._get_namespace_lock(namespace):
            if cache_key not in self._cache:
                return False

            entry = self._cache[cache_key]
            if entry["expiration"] < time.time():
                # 过期了，清理掉
                del self._cache[cache_key]
                if cache_key in self._access_order:
                    del self._access_order[cache_key]
                return False

            return True

    def get_namespace_keys(self, namespace: str) -> list:
        """
        获取命名空间中的所有键

        Args:
            namespace: 命名空间

        Returns:
            键列表
        """
        keys = []
        with self._get_namespace_lock(namespace):
            prefix = f"{namespace}:"
            for key in self._cache.keys():
                if key.startswith(prefix):
                    actual_key = key[len(prefix):]
                    keys.append(actual_key)
        return keys