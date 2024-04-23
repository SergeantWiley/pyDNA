from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import markdown
import os
from markdown_view.views import StaffMarkdownView
def home(request):
    return render(request,'index.html')
def educational(request):
    # Path to the README.md file relative to the Django project's root directory
    readme_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'README.md')
    print(readme_path)
    # Check if the README.md file exists
    if os.path.exists(readme_path):
        # Read the content of the README.md file
        with open(readme_path, 'r') as file:
            readme_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(readme_content)

        # Render the template with the HTML content
        return render(request, 'educational.html', {'content': html_content})
    else:
        # Return an error response if the file doesn't exist
        
        return render(request, 'educational.html', {'content': '<p>Error: README.md file not found</p>'})
def launcher(request):
    return render(request,'launcher.html')