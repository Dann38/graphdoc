import unittest
from main import get_bboxes
from tesseract_reader.bbox.bbox import BBox

def levenshtein_distance(s1, s2):
    # Алгоритм был взят с сайта: https://habr.com/ru/articles/676858/
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

class TestGetBboxes(unittest.TestCase):
    def setUp(self):
        self.path = 'example_image/img_1.jpeg'
        self.expected_len = 85
        self.expected_text = "Федеральное государственное бюджетное образовательное учреждение высшего образования РОССИЙСКАЯ АКАДЕМИЯ НАРОДНОГО ХОЗЯЙСТВА и ГОСУДАРСТВЕННОЙ СЛУЖБЫ при ПРЕЗИДЕНТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ Институт государственной службы и управления Направление подготовки: 38.04.01 Экономика   Образовательная программа: _ Государственное регулирование экономики   МАГИСТЕРСКАЯ ДИССЕРТАЦИЯ ГОСУДАРСТВЕННО-ЧАСТНОЕ ПАРТНЕРСТВО И ЕГО РОЛЬ В АКТИВИЗАЦИИ   И РАЗВИТИИ ИНВЕСТИЦИОННОЙ ДЕЯТЕЛЬНОСТИ НА ТЕРРИТОРИИ   РЕГИОНА   Автор: обучающийся группы 3М18-34 заочной формы обучения   / Жилов Ахмед-Хан / Темурович Руководитель: Доцент кафедры государственного регулирования экономики, кандидат экономических наук / _Шетов Артур Арсенович /   Москва, 2021 г."
        self.img, self.bboxes, self.text = get_bboxes(self.path)

    def test_bboxes_count(self):
        self.assertEqual(len(self.bboxes), self.expected_len,
                         f"Количество BBox'ов ({len(self.bboxes)}) не совпадает с ожидаемым ({self.expected_len}).")

    def test_levenshtein_distance(self):
        result_text = ' '.join(self.text)
        distance = levenshtein_distance(result_text, self.expected_text)/len(result_text)
        self.assertLessEqual(distance, 0.05,
                             f"Расстояние Левенштейна ({distance}) между фактическим и ожидаемым текстами больше допустимого.")

    def test_bbox_dimensions(self):
        for bbox in self.bboxes:
            self.assertGreaterEqual(bbox.width, 2, f"Ширина BBox {bbox} меньше 2.")
            self.assertGreaterEqual(bbox.height, 2, f"Высота BBox {bbox} меньше 2.")

if __name__ == "__main__":
    unittest.main()
