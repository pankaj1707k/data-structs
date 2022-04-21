""" https://leetcode.com/problems/design-hashset/ """

from typing import *


class Bucket:
    def __init__(self) -> None:
        self.bucket = []

    def update(self, key: int) -> None:
        for i, k in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = key
                return
        self.bucket.append(key)

    def delete(self, key: int) -> None:
        for i, k in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]

    def exists(self, key: int) -> bool:
        for k in self.bucket:
            if k == key:
                return True
        return False


class MyHashSet:
    def __init__(self) -> None:
        self.bucket_count = 100000  # each bucket will contain at most 10 numbers
        self.hash_set = [Bucket() for _ in range(self.bucket_count)]

    def add(self, key: int) -> None:
        hash_key = key % self.bucket_count
        self.hash_set[hash_key].update(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.bucket_count
        self.hash_set[hash_key].delete(key)

    def contains(self, key: int) -> bool:
        hash_key = key % self.bucket_count
        return self.hash_set[hash_key].exists(key)
