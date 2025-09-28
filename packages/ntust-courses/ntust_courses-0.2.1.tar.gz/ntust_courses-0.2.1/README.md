# NTUST Courses (強化版)

台科大課程查詢工具，提供以下功能：

- `search_courses`：可指定多種條件搜尋課程
- `search_all_courses`：搜尋所有課程（不指定名稱與老師）
- `print_courses`：顯示課程清單

## 安裝方式

```bash
pip install ntust_courses.zip
```

## 使用方式

```python
from ntust_courses import search_courses, search_all_courses, print_courses

# 搜尋含有「程式」的課程
courses = search_courses(course_name="程式")
print_courses(courses)

# 搜尋所有課程
all_courses = search_all_courses()
print_courses(all_courses)
```
