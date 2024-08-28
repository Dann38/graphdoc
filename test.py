import unittest
from main import get_bboxes
from tesseract_reader.bbox.bbox import BBox

def levenshtein_distance(s1, s2):
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
        self.expected_bboxes = [
            BBox(263, 124, 146, 22), BBox(417, 129, 185, 17), BBox(610, 124, 122, 19), BBox(740, 124, 187, 22), BBox(934, 129, 132, 17), BBox(541, 158, 98, 12), BBox(647, 153, 141, 22), BBox(330, 177, 180, 22), BBox(517, 182, 148, 21), BBox(673, 182, 162, 21), BBox(843, 177, 156, 22), BBox(458, 216, 12, 11), BBox(479, 206, 264, 26), BBox(753, 210, 118, 18), BBox(375, 244, 41, 17), BBox(424, 239, 169, 22), BBox(601, 234, 183, 22), BBox(792, 239, 162, 22), BBox(385, 297, 108, 22), BBox(501, 297, 187, 22), BBox(697, 297, 85, 22), BBox(790, 302, 13, 12), BBox(810, 302, 133, 17), BBox(179, 383, 136, 22), BBox(323, 388, 124, 14), BBox(515, 383, 84, 17), BBox(608, 382, 116, 18), BBox(503, 403, 660, 6), BBox(178, 412, 179, 23), BBox(365, 418, 118, 17), BBox(499, 407, 7, 34), BBox(515, 413, 176, 24), BBox(698, 418, 156, 19), BBox(862, 418, 112, 12), BBox(501, 433, 662, 6), BBox(456, 529, 214, 17), BBox(677, 529, 196, 21), BBox(182, 586, 380, 22), BBox(572, 586, 188, 18), BBox(770, 587, 15, 16), BBox(795, 587, 50, 17), BBox(854, 587, 67, 17), BBox(930, 587, 14, 16), BBox(952, 586, 195, 22), BBox(166, 606, 997, 7), BBox(227, 616, 18, 17), BBox(253, 616, 136, 18), BBox(397, 612, 262, 26), BBox(665, 616, 213, 22), BBox(886, 616, 36, 17), BBox(930, 616, 172, 18), BBox(166, 636, 997, 7), BBox(603, 646, 123, 17), BBox(165, 666, 998, 7), BBox(680, 762, 76, 22), BBox(680, 790, 147, 23), BBox(835, 796, 77, 17), BBox(920, 790, 92, 18), BBox(680, 819, 84, 17), BBox(772, 819, 72, 22), BBox(852, 819, 98, 22), BBox(667, 926, 465, 5), BBox(779, 877, 7, 17), BBox(809, 877, 72, 17), BBox(1001, 877, 118, 19), BBox(1143, 877, 7, 17), BBox(810, 906, 114, 23), BBox(680, 993, 164, 22), BBox(680, 1022, 78, 21), BBox(815, 1021, 91, 23), BBox(963, 1027, 188, 17), BBox(680, 1055, 157, 17), BBox(886, 1046, 120, 31), BBox(1055, 1055, 97, 15), BBox(680, 1084, 162, 12), BBox(850, 1084, 47, 17), BBox(779, 1137, 7, 16), BBox(810, 1137, 69, 17), BBox(887, 1136, 64, 25), BBox(959, 1137, 115, 24), BBox(1143, 1137, 7, 16), BBox(667, 1157, 464, 6), BBox(579, 1541, 92, 20), BBox(679, 1540, 47, 18), BBox(735, 1546, 15, 12)
        ]
        self.expected_text = [
            'Федеральное', 'государственное', 'бюджетное', 'образовательное', 'учреждение', 'высшего', 'образования',
            'РОССИЙСКАЯ', 'АКАДЕМИЯ', 'НАРОДНОГО', 'ХОЗЯЙСТВА', 'и', 'ГОСУДАРСТВЕННОЙ', 'СЛУЖБЫ', 'при', 'ПРЕЗИДЕНТЕ',
            'РОССИЙСКОЙ', 'ФЕДЕРАЦИИ', 'Институт', 'государственной', 'службы', 'и', 'управления', 'Направление',
            'подготовки:', '38.04.01', 'Экономика', ' ', 'Образовательная', 'программа:', '_', 'Государственное',
            'регулирование', 'экономики', ' ', 'МАГИСТЕРСКАЯ', 'ДИССЕРТАЦИЯ', 'ГОСУДАРСТВЕННО-ЧАСТНОЕ', 'ПАРТНЕРСТВО',
            'И', 'ЕГО', 'РОЛЬ', 'В', 'АКТИВИЗАЦИИ', ' ', 'И', 'РАЗВИТИИ', 'ИНВЕСТИЦИОННОЙ', 'ДЕЯТЕЛЬНОСТИ', 'НА',
            'ТЕРРИТОРИИ', ' ', 'РЕГИОНА', ' ', 'Автор:', 'обучающийся', 'группы', '3М18-34', 'заочной', 'формы',
            'обучения', ' ', '/', 'Жилов', 'Ахмед-Хан', '/', 'Темурович', 'Руководитель:', 'Доцент', 'кафедры',
            'государственного', 'регулирования', 'экономики,', 'кандидат', 'экономических', 'наук', '/', '_Шетов',
            'Артур', 'Арсенович', '/', ' ', 'Москва,', '2021', 'г.'
        ]
        self.bboxes, self.text = get_bboxes()

    def test_bboxes_count(self):
        self.assertEqual(len(self.bboxes), len(self.expected_bboxes),
                         f"Количество BBox'ов ({len(self.bboxes)}) не совпадает с ожидаемым ({len(self.expected_bboxes)}).")

    def test_levenshtein_distance(self):
        result_text = ' '.join(self.text)
        expected_text = ' '.join(self.expected_text)
        distance = levenshtein_distance(result_text, expected_text)
        self.assertLessEqual(distance, 0,
                             f"Расстояние Левенштейна ({distance}) между фактическим и ожидаемым текстами больше допустимого.")

    def test_bbox_dimensions(self):
        for bbox in self.bboxes:
            self.assertGreaterEqual(bbox.width, 2, f"Ширина BBox {bbox} меньше 2.")
            self.assertGreaterEqual(bbox.height, 2, f"Высота BBox {bbox} меньше 2.")

if __name__ == "__main__":
    unittest.main()
