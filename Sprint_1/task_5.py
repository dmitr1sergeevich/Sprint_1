class TestCase:
    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print({
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        })
test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
