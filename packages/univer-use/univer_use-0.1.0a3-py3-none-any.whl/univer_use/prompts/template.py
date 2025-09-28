import os
from jinja2 import Environment, FileSystemLoader


env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__)),
)


def get_rendered_template(prompt_name: str, state: dict) -> str:
    try:
        template = env.get_template(f"{prompt_name}.md")
        prompt = template.render(state)
        return prompt
    except Exception as e:
        raise ValueError(f"Error in applying prompt template {prompt_name}: {e}")
