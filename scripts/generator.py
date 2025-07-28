import os
import sys


def generate_pipeline():
    language = input("Enter your programming language (python/node): ").strip()

    if language == "python":
        template_file = "templates/python-ci.yml"
    elif language == "node":
        template_file = "templates/node-ci.yml"
    else:
        print("❌ Unsupported language")
        sys.exit(1)

    os.makedirs(".github/workflows", exist_ok=True)
    os.system(f"cp {template_file} .github/workflows/main.yml")

    print(
        f"✅ {language.capitalize()} CI/CD pipeline generated "
        "at .github/workflows/main.yml"
    )


generate_pipeline()
