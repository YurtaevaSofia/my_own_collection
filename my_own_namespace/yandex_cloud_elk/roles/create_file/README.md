# Role `create_file`

Single task role: creates a text file on the target host with
`my_own_namespace.yandex_cloud_elk.my_own_module`.

## Variables

| Variable | Default | Description |
|---|---|---|
| `create_file_path` | `/tmp/my_own_module_role.txt` | Path to the file on the target host |
| `create_file_content` | `Hello from role create_file!\n` | Content of the file |

## Example playbook

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: my_own_namespace.yandex_cloud_elk.create_file
      vars:
        create_file_path: /tmp/test.txt
        create_file_content: "some text\n"
```
