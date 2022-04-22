""" https://leetcode.com/problems/design-hashmap/ """

from typing import *


class Bucket:
    def __init__(self) -> None:
        self.bucket = []

    def update(self, key: int, value: int) -> None:
        for p in self.bucket:
            if p[0] == key:
                p[1] = value
                return
        self.bucket.append([key, value])

    def retrieve(self, key: int) -> int:
        for p in self.bucket:
            if p[0] == key:
                return p[1]
        return -1

    def delete(self, key: int) -> None:
        for i, p in enumerate(self.bucket):
            if p[0] == key:
                del self.bucket[i]


class MyHashMap:
    def __init__(self) -> None:
        self.bucket_count = 10000
        self.hash_map = [Bucket() for _ in range(self.bucket_count)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.bucket_count
        self.hash_map[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.bucket_count
        return self.hash_map[hash_key].retrieve(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.bucket_count
        self.hash_map[hash_key].delete(key)
