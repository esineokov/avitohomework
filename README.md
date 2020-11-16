# Avito home work

#### Example usage
```python
import asyncio
from matrix import get_matrix

matrix = asyncio.run(get_matrix("https://f003.backblazeb2.com/file/am-avito/matrix.txt"))
print(matrix)
```

#### Run tests
```shell script
python -m unittest tests/test.py
```