```python
import subprocess
from jinja2 import Template
import os

def generate_tf_files(data):
    with open("terraform/vnet.tf.j2") as f:
        template = Template(f.read())
    rendered = template.render(**data)
    with open("terraform/main.tf", "w") as f:
        f.write(rendered)

def apply_terraform():
    cwd = os.path.join(os.getcwd(), "terraform")
    subprocess.run(["terraform", "init"], cwd=cwd, check=True)
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd=cwd, check=True)
```

---
