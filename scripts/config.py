import os

# =========================
# General Configuration
# =========================

# Base URL for SoaringSpot event
base_url = 'https://www.soaringspot.com/en_gb/39th-fai-world-gliding-championships-tabor-2025'

# Path to the file containing URLs to open in Chrome
url_file = 'data/urls.txt'

# Path to the Excel database file (pilot, glider, etc.)
database_path = "data/database.xlsx"  # Adjust the path if needed

# =========================
# Weather Briefing Settings
# =========================

# Path to the weather briefing folder (used by metbrief.py)
weather_briefing_path = os.path.join('externals', 'metbrief', 'briefings', 'tabor_25')

# =========================
# WhatsApp Integration
# =========================

# Default WhatsApp message to send with the weather briefing
whatsapp_message = "Chatty ist der Beste! Hier ist die aktuelle Wettervorhersage für Tabor 2025."

# WhatsApp group name to send the weather briefing to
whatsapp_group = 'Ich mache hier nur Notize'

# =========================
# Git & LibreOffice Settings
# =========================

# Set up your git credentials if not already configured
os.environ['GIT_SSH_COMMAND'] = 'ssh -i ~/.ssh/id_rsa'

# Path to the LibreOffice executable (adjust if needed)
soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

# =========================
# Output Directories
# =========================

# Directory for generated task files
task_output_dir = 'data/tasks'

# Directory for generated glider files
glider_output_dir = 'data/gliders'

# Directory for Chrome user data (used by Selenium)
chromedriver_user_data_dir = 'data/.chromedriver_user_data'

# =========================
# SoaringSpot & CUP Download
# =========================

# URL for downloading .cup files from SoaringSpot links
cup_url = 'https://xlxjz3geasj4wiei7n5vzt7zzu0qibmm.lambda-url.eu-central-1.on.aws/?url='

# =========================
# Competition Classes & Mappings
# =========================

# List of competition classes
classes = ['Club', 'Standard', '15 Meter']

# Mapping from class name to file prefix
filename_map = {
    'Club': 'club',
    'Standard': 'std',
    '15 Meter': '15m'
}

# Mapping from class name to URL segment
url_map = {
    'Club': 'club',
    'Standard': 'standard',
    '15 Meter': '-15-meter'
}

# Mapping from class name to results table name
results_table_map = {
    'Club': 'Club Class',
    'Standard': 'Standard Class',
    '15 Meter': '15 meter Class'
}

# =========================
# Shared State Variables
# =========================

# Dictionary to store selected task IDs for each class
selected_task_ids = {}

# Whether to automatically commit and push to git after updates
commit_and_push_to_git = True