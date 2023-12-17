# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.items = items
        self.current_value = 0
        self.ignore_case = kwargs.get('ignore_case', False)
        if not self.ignore_case: 
            self.set_arr = []
            for i in self.items:
                if (type(i) is str) and (i.upper() not in self.set_arr and i.lower() not in self.set_arr):
                    self.set_arr.append(i)
                elif i not in self.set_arr and (type(i) is not str): self.set_arr.append(i)
            self.set_arr = list(set(self.items))
    def __next__(self):
        if self.current_value < len(self.set_arr):
            value = self.set_arr[self.current_value]
            self.current_value += 1
            return value
        else:
            raise StopIteration
    def __iter__(self):
        return self