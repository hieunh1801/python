# Python Circular Imports

## Đặt vấn đề: What is a Circular Dependency?
- 2 hay nhiều module import phụ thuộc vào nhau

  ![img](https://s3.amazonaws.com/stackabuse/media/python-circular-imports-1.png)

**Ví dụ**: module 1 cần function2_1 từ module 2. module 2 cần function1_1 của module 1 => 2 module này phải import lẫn nhau => faile

```python
# module1
import module2
def function1_1():
    pass

def function1_2():
    module2.function2_1():
    pass
```



```python
# module2
import module1
def function2_1():
    pass

def function2_2():
    module1.function1_1():
    pass
```

## Cách giải quyết

- Thay vì import ở ngoài thì ta import khi nào ta dùng thôi

```python
# module1
# import module2 # remove this
def function1_1():
    pass

def function1_2():
	import module2 # to this
    module2.function2_1():
    pass
```

