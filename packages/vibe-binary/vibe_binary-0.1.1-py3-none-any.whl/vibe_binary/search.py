def binary_search(arr, target, verbose=False, auto_sort=True):
    """
    Бинарный поиск с выводом процесса
    """
    if auto_sort and not is_sorted(arr):
        if verbose:
            print(f"📦 Сортируем массив...")
        arr = sorted(arr)

    low, high = 0, len(arr) - 1
    steps = 0

    if verbose:
        print(f"🔍 Ищем {target} в массиве из {len(arr)} элементов")

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_val = arr[mid]

        if verbose:
            print(f"Шаг {steps}: [{low}-{high}] mid={mid} → {mid_val}")

        if mid_val == target:
            if verbose:
                print(f"✅ Найдено! Индекс: {mid}")
            return mid
        elif mid_val < target:
            low = mid + 1
            if verbose:
                print(f"   ➡️ Идём вправо")
        else:
            high = mid - 1
            if verbose:
                print(f"   ⬅️ Идём влево")

    if verbose:
        print(f"❌ Не найдено")
    return -1


def binary_search_c(arr, target, auto_sort=True):
    """
    Чистый бинарный поиск без вывода
    """
    if auto_sort and not is_sorted(arr):
        arr = sorted(arr)

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))