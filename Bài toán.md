1. Remove các trường duplicate từ một mảng object thỏa mãn một số tiêu chí.
```python
data = [
    {"book_id": 1, "author_id": 1, "main": True},
    {"book_id": 1, "author_id": 2, "main": False},
    {"book_id": 2, "author_id": 3, "main": False},
    {"book_id": 2, "author_id": 2, "main": True},
]
# => mỗi một quyển sách thì lấy ra một main
expected = [
    {"book_id": 1, "author_id": 1, "main": True},
    {"book_id": 2, "author_id": 2, "main": True},
]
```