import yaml
import shutil
import os

def generate_pipeline():
    with open('blueprint/sample-blueprint.yaml') as f:
        config = yaml.safe_load(f)

    language = config.get('language')
    template_path = f'templates/{language}-template.yml'

    if os.path.exists(template_path):
        os.makedirs('.github/workflows', exist_ok=True)
        shutil.copy(template_path, '.github/workflows/main.yml')
        print(f"✅ {language.capitalize()} CI/CD pipeline generated in .github/workflows/main.yml")
    else:
        print(f"❌ Template for language '{language}' not found!")

if __name__ == "__main__":
    generate_pipeline()

