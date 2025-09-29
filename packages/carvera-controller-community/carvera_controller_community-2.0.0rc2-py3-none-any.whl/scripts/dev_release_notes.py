import re

def get_unreleased_section(changelog_text):
    pattern = r'\[unreleased\]\s*((?:- .*?\n)+)'
    match = re.search(pattern, changelog_text, re.IGNORECASE)
    if match:
        # Clean up and return the lines
        return match.group(1).strip()
    else:
        return "No unreleased notes currently."

def main():
    with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
        changelog = f.read()

    unrelease_notes = get_unreleased_section(changelog)

    dev_release_text = f"""# Welcome to the Dev Build Release Page for Carvera Controller Community!

## What is a Dev Build?

Dev builds are the latest versions of Carvera Controller Community, automatically compiled after every new commit to the `develop` branch. This means that each build incorporates the most recent changes and improvements. While these builds offer a glimpse into the ongoing development of Carvera Controller, keep in mind that they are still works in progress and may contain bugs or unstable features.

## Download Instructions:
1. Select the version that corresponds to your operating system.
2. Download and install/run the build.
3. Dive into the newest features and improvements!

## Please Note:

* Dev builds are developmental and may contain bugs.
* Your feedback is crucial. Please report any issues or suggestions on our GitHub page.

## Release notes
The follow changes are present in the dev build:

{unrelease_notes}
"""
    with open("dev-CHANGELOG.md", "w") as file:
        file.write(dev_release_text)
    

if __name__ == "__main__":
    main()