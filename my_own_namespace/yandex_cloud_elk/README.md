# Ansible Collection `my_own_namespace.yandex_cloud_elk`

Учебная коллекция (ДЗ «Создание собственных модулей»).

## Состав

| Тип | Имя | Описание |
|---|---|---|
| module | `my_own_namespace.yandex_cloud_elk.my_own_module` | Создаёт текстовый файл по пути `path` с содержимым `content` |
| role | `my_own_namespace.yandex_cloud_elk.create_file` | Single task role, вызывающая `my_own_module` |

## Требования

- ansible-core >= 2.15

## Установка

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Модуль `my_own_module`

| Параметр | Тип | Обязательный | По умолчанию | Описание |
|---|---|---|---|---|
| `path` | path | да | — | Путь к файлу на целевом хосте |
| `content` | str | нет | `''` | Содержимое файла |

Модуль идемпотентен: если файл уже существует с тем же содержимым, возвращается `changed: false`.
Поддерживает check mode.

Возвращаемые значения: `path`, `content`, `message`.

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: "hello world\n"
```

## Роль `create_file`

| Переменная | По умолчанию |
|---|---|
| `create_file_path` | `/tmp/my_own_module_role.txt` |
| `create_file_content` | `Hello from role create_file!\n` |

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - my_own_namespace.yandex_cloud_elk.create_file
```

## Лицензия

GPL-3.0-or-later
