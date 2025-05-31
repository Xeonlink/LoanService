import utils
import os


BACKUP_FILE_NAME_SQLITE = "backup.db"
BACKUP_FILE_NAME_EXCEL = "backup.xlsx"
LOAN_DAYS = 7

# Paths
ICON_PATH = utils.resource_path(os.path.join("assets", "favicon_sm.png"))
DB_PATH = utils.resource_path(os.path.join("data", "data.db"))
DB_BACKUP_PATH = DB_PATH + ".bak"
LANGUAGE_PATH = utils.resource_path(os.path.join("assets", "languages.csv"))
LICENSE_PATH = utils.resource_path(os.path.join("assets", "licenses.txt"))
TERMS_OF_SERVICE_PATH = utils.resource_path(os.path.join("assets", "terms_of_service.txt"))
PRIVACY_POLICY_PATH = utils.resource_path(os.path.join("assets", "privacy_policy.txt"))

# Theme
GREEN_THEME_PATH = utils.resource_path(os.path.join("assets", "themes", "green.json"))
