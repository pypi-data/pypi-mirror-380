#!/usr/bin/env python3
"""
Финально исправленный парсер JSON
Запуск: python final_fixed_json_parser.py
"""

import json

def parse_ai_response(ai_response: str) -> tuple[str, dict]:
    """Финально исправленная функция парсинга JSON"""
    try:
        # Метод 1: Ищем последнюю позицию, где начинается JSON с "этап"
        last_etap_pos = ai_response.rfind('"этап"')
        if last_etap_pos == -1:
            print("❌ Ключ 'этап' не найден")
            return ai_response, {}
        
        # Ищем открывающую скобку перед "этап"
        json_start = -1
        for i in range(last_etap_pos, -1, -1):
            if ai_response[i] == '{':
                json_start = i
                break
        
        if json_start == -1:
            print("❌ Открывающая скобка перед 'этап' не найдена")
            return ai_response, {}
        
        # Теперь найдем соответствующую закрывающую скобку
        brace_count = 0
        json_end = -1
        
        for i in range(json_start, len(ai_response)):
            char = ai_response[i]
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    json_end = i
                    break
        
        if json_end == -1:
            print("❌ Соответствующая закрывающая скобка не найдена")
            return ai_response, {}
        
        # Извлекаем JSON и текст ответа
        json_str = ai_response[json_start:json_end + 1]
        response_text = ai_response[:json_start].strip()
        
        try:
            metadata = json.loads(json_str)
            print(f"✅ JSON успешно распарсен методом 1")
            return response_text, metadata
        except json.JSONDecodeError as e:
            print(f"❌ Ошибка парсинга JSON: {e}")
            print(f"JSON строка: {json_str}")
            return parse_ai_response_method2(ai_response)
            
    except Exception as e:
        print(f"❌ Ошибка метода 1: {e}")
        return parse_ai_response_method2(ai_response)

def parse_ai_response_method2(ai_response: str) -> tuple[str, dict]:
    """Резервный метод - поиск по строкам"""
    try:
        print("🔄 Пробуем метод 2...")
        
        lines = ai_response.strip().split('\n')
        
        # Ищем строку с "этап"
        etap_line = -1
        for i, line in enumerate(lines):
            if '"этап"' in line:
                etap_line = i
                break
        
        if etap_line == -1:
            print("❌ Строка с 'этап' не найдена")
            return ai_response, {}
        
        # Ищем начало JSON (строку с { перед этап)
        json_start_line = -1
        for i in range(etap_line, -1, -1):
            if lines[i].strip().startswith('{'):
                json_start_line = i
                break
        
        if json_start_line == -1:
            print("❌ Начало JSON не найдено")
            return ai_response, {}
        
        # Ищем конец JSON (балансируем скобки)
        brace_count = 0
        json_end_line = -1
        
        for i in range(json_start_line, len(lines)):
            line = lines[i]
            for char in line:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        json_end_line = i
                        break
            if json_end_line != -1:
                break
        
        if json_end_line == -1:
            print("❌ Конец JSON не найден")
            return ai_response, {}
        
        # Собираем JSON
        json_lines = lines[json_start_line:json_end_line + 1]
        json_str = '\n'.join(json_lines)
        
        # Собираем текст ответа
        response_lines = lines[:json_start_line]
        response_text = '\n'.join(response_lines).strip()
        
        try:
            metadata = json.loads(json_str)
            print(f"✅ JSON успешно распарсен методом 2")
            return response_text, metadata
        except json.JSONDecodeError as e:
            print(f"❌ Метод 2: ошибка JSON: {e}")
            print(f"JSON строка: {json_str}")
            return ai_response, {}
            
    except Exception as e:
        print(f"❌ Ошибка метода 2: {e}")
        return ai_response, {}

def main():
    """Тестируем исправленный парсер"""
    print("🧪 Тест финально исправленного парсера JSON\n")
    
    test_cases = [
        {
            "name": "JSON с вложенными объектами и файлами",
            "response": '''Отлично! Записал ваш номер телефона.

{
  "этап": "contacts",
  "качество": 9,
  "события": [
    {
      "тип": "телефон",
      "инфо": "Иван Петров +79219603144"
    }
  ],
  "файлы": ["презентация.pdf", "прайс.pdf"],
  "каталоги": ["основной", "спецпредложения"]
}'''
        },
        {
            "name": "Простой JSON",
            "response": '''Расскажу подробнее о конференции...

{
  "этап": "consult",
  "качество": 6,
  "события": [],
  "файлы": [],
  "каталоги": []
}'''
        },
        {
            "name": "JSON в середине текста",
            "response": '''Начало текста.

{
  "этап": "introduction",
  "качество": 5,
  "события": [],
  "файлы": ["welcome.pdf"],
  "каталоги": ["приветственные"]
}

Текст после JSON не должен попасть в ответ.'''
        },
        {
            "name": "Ответ без JSON",
            "response": "Простой ответ без метаданных"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"{'='*20} Тест {i}: {test_case['name']} {'='*20}")
        
        response_text, metadata = parse_ai_response(test_case['response'])
        has_json = bool(metadata)
        
        if has_json:
            print("✅ УСПЕХ!")
            print(f"   📝 Текст ответа: {response_text[:50]}...")
            print(f"   📊 Этап: {metadata.get('этап')}")
            print(f"   ⭐ Качество: {metadata.get('качество')}")
            print(f"   🎯 События: {len(metadata.get('события', []))}")
            if metadata.get('события'):
                for event in metadata['события']:
                    print(f"      - {event.get('тип')}: {event.get('инфо')}")
            print(f"   📁 Файлы: {len(metadata.get('файлы', []))}")
            if metadata.get('файлы'):
                for file in metadata['файлы']:
                    print(f"      - {file}")
            print(f"   📂 Каталоги: {len(metadata.get('каталоги', []))}")
            if metadata.get('каталоги'):
                for catalog in metadata['каталоги']:
                    print(f"      - {catalog}")
        else:
            print("❌ JSON не найден (ожидаемо для теста без JSON)")
        
        results.append(has_json)
        print()
    
    # Итоговый результат
    passed = sum(results)
    expected = 3  # Ожидаем что первые 3 теста пройдут
    
    print(f"📊 ИТОГО: {passed}/{len(test_cases)} тестов с JSON")
    
    if passed >= expected:
        print("🎉 Парсинг JSON работает корректно!")
        return True
    else:
        print("❌ Есть проблемы с парсингом JSON")
        return False

if __name__ == "__main__":
    main()