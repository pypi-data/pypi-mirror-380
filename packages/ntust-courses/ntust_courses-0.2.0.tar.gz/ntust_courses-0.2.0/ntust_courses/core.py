import requests

API_URL = "https://querycourse.xinshou.tw/querycourse/api/courses"

def search_courses(
    course_name: str = "",
    semester: str = "1141",
    course_no: str = "",
    course_teacher: str = "",
    dimension: str = "",
    course_notes: str = "",
    campus_notes: str = "",
    foreign_language: int = 0,
    only_general: int = 0,
    only_ntust: int = 0,
    only_master: int = 0,
    only_undergraduate: int = 0,
    only_node: int = 0,
    language: str = "zh"
) -> list[dict]:
    """
    搜尋課程
    :param course_name: 課程名稱 (關鍵字)
    :param semester: 學期代號 (預設 1141)
    :param course_no: 課程代碼
    :param course_teacher: 教師姓名
    :param dimension: 通識/領域 (若適用)
    :param course_notes: 課程備註
    :param campus_notes: 校區備註
    :param foreign_language: 是否為外語課程 (0=否, 1=是)
    :param only_general: 是否僅查詢通識課 (0/1)
    :param only_ntust: 是否僅限台科課程 (0/1)
    :param only_master: 是否僅查研究所課程 (0/1)
    :param only_undergraduate: 是否僅查大學部課程 (0/1)
    :param only_node: 其他過濾選項 (0/1)
    :param language: 語言 (zh/en)
    :return: 課程清單 (list of dict)
    """
    data = {
        "Semester": semester,
        "CourseNo": course_no,
        "CourseName": course_name,
        "CourseTeacher": course_teacher,
        "Dimension": dimension,
        "CourseNotes": course_notes,
        "CampusNotes": campus_notes,
        "ForeignLanguage": foreign_language,
        "OnlyGeneral": only_general,
        "OnleyNTUST": only_ntust,
        "OnlyMaster": only_master,
        "OnlyUnderGraduate": only_undergraduate,
        "OnlyNode": only_node,
        "Language": language
    }

    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"❌ 發生錯誤，狀態碼: {response.status_code}")


def search_all_courses(semester: str = "1141") -> list[dict]:
    """
    搜尋所有課程（不指定課程名稱與老師）
    :param semester: 學期代號 (預設 1141)
    :return: 課程清單 (list of dict)
    """
    return search_courses(course_name="", semester=semester, course_teacher=" ")


def print_courses(courses: list[dict]) -> None:
    """
    顯示課程清單
    :param courses: 課程清單
    """
    if not courses:
        print("📚 沒有找到課程")
        return

    print(f"📚 找到 {len(courses)} 門課程:")
    print("=" * 50)

    for i, course in enumerate(courses):
        print(f"🔢 第 {i+1} 門課程:")
        print(f"   課程名稱: {course['CourseName']}")
        print(f"   課程代碼: {course['CourseNo']}")
        print(f"   授課老師: {course['CourseTeacher']}")
        print(f"   學分數: {course['CreditPoint']}")
        print(f"   選課人數: {course['ChooseStudent']}")
        print("-" * 30)
