# Записки с курса opencv
### 2 урок
* обработка фото - чтение, блюр, изменения цветовой палитры на черно-белую, 
определение углов(краев) каждого отдельного объекта, увеличение/уменьшение 
размеров выделенных обеъекьлв
* работа с видео

### 3 урок
* создание фигур - куб, линия, окружность, текст

### 4 урок 
* обработка видео
* поворот картинки, функции поворота,смещения
* определение контуров объектов на изображении

### 5 урок
* цветовые форматы (hsv, eab)
* разбиение на слои (r, g, b)
* объединение слоев 

### 6 урок
* побитовые операции - инверсия цвета, выделение одной половины и смена ее цвета, 
вторую в черный и тд
* создание фигуры и битовая операция сложения/умножение (по сути наложение маски)

### 7 урок
* распознавание лиц используя натренированную модель

### Этапы тренировки модели...
1) Создаем список изображений через цикл
2) Пробегаем по каждому изображению
3) Загружаем их в библу facerecognicion
4) Снятие с каждого лица кодировки
5) Проверка