import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the path to your project root
sys.path.append(os.path.dirname(__file__) + '/../')

# Replace 'your_project_name' with the name of your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo_Django.settings')

app = get_wsgi_application()
