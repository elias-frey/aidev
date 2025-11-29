# 02.10.25 connection established 

Creating repository:
1. to open cmd in the current file exprorer directory: type "cmd" in file exprorers adress line and hit enter (alternative "cd C:\Users\YourName\Documents")
2. new folder for the project : mkdir MyProject, cd MyProject
3. Initialize git inside that folder: git init -b main
4. Create starter files: echo "# MyProject" > README.md
5. Stage and commit files: git add ., git commit -m "Initial commit"
6. Log into GitHub in your browser → New Repository → name it MyProject. Don’t initialize it with a README (you already have one).
7. Link local folder to github (copy rep's URL): git remote add origin https://github.com/YourUsername/MyProject.git
8. Push local rep. to github: git push -u origin main
And that’s it 🚀
You now have a folder created entirely from Command Prompt, set as a Git repo, and synced with GitHub as the main branch.

Nested repos fix:
If I see .git folder (hidden)it means that it IS a repo already (e.g. the "github" folder), while its purpose is to contain different repo folders.
1. Removing git tracking from the folder: rmdir /s /q .git (in PowerShell: Remove-Item -Recurse -Force .git)
⚖️ Rule of thumb:
👉 One .git folder = one repo.

Creating GitRepository through command line using GitHubCLI (command line interface):
1. Downloaded and installed the GitHubCLI installer (for AMD64)
2. Authenticate: gh auth login
	- Choose the protocol: HTTP (need to type or store credentials unless cached) vs SSH (Uses a public/private SSH key pair stored on machine and linked to GitHub account)
3. the process went as followed:
*****
C:\Users\Manuscript\OneDrive\My laptop\Studies\Career\workshop\github\aidev>gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? SSH
? Upload your SSH public key to your GitHub account? C:\Users\Manuscript\.ssh\id_ed25519.pub
? Title for your SSH key: (GitHub CLI) supreme comand
? Title for your SSH key: supreme comand
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'admin:public_key'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ Uploaded the SSH key to your GitHub account: C:\Users\Manuscript\.ssh\id_ed25519.pub
✓ Logged in as elias-frey
*****
4. After making folder with git, create a gitrepo: gh repo create aidev --public
5. First file created and uploaded to github through cmd: 
- echo # 02.10.25 connection established > README.md
- ... (set up the remote)

CMD commands:

Ctrl + C stop the operation
mkdir "foldername" # creates folder
dir # lists content of folder
rmdir "foldename" # deletes folder ("rd" also works)
rmdir /s /q "FolderName" # delete folder, /s all its files and subfolders, /q in quite mode, no confirmation prompt
pip instal ... # pip is the python package manager


Useful git comands:
git restore --staged README.md #pulls back the add request
git log -- README.md # shows commited versions of the file
git show README.md # shows the content of the file in the comand window
git checkout -- README.md # restores previous version of the modified file (not comited)
git remote add origin git@github.com:elias-frey/aidev.git # connects local repo to remote one (where git@github.com:... is SSH adress)
git remote -v # checks connected remote repos
git remote set-url origin git@github.com:yourusername/yourrepo.git # resets the connection to the correct remote (if local repo was already connected to the wrong one)
git push -u origin main # pushes comited changes to remote repo (if it is empty)
	- The -u flag sets the upstream so later you can just type git push with no arguments
	- Output: To github.com:elias-frey/aidev.git
 	* [new branch]      main -> main
	branch 'main' set up to track 'origin/main'
git pull origin main --rebase # if remote repo has commits, a pull request for merge first needed


GitHub CLI comands:
gh auth status # gives info about what github account is connected to GLI
gh ssh-key add %USERPROFILE%\.ssh\id_ed25519.pub --title "Homeland" # adds the SSH key to github account 
gh ssh-key list # returns a list of keys used in github (supreme comand, homeland)
gh ssh-key delete 12345678 # removes a key (use ID shown in gh ssh-key list comand)
sc query ssh-agent # checking how service is running
gh repo list # shows repositories



SSH connection:
ssh-keygen -t ed25519 -C "frey.ilya.32@gmail.com"
	- "-t ed25519" = modern, secure key type
	- "-C" = comment (usually your GitHub email)
sc config ssh-agent start= auto # initiate to enable running the ssh-agent service automatically 
net start ssh-agent # starts OpenSSH Authentication Agent service (after these 2 the service is now enabled and running permanently, active on restart)
ssh-add C:\Users\Manuscript/.ssh/id_ed25519 # adds the key to the SSH agent, might need to be readded after restart (use  %USERPROFILE%\.ssh\id_ed25519)
ssh -T git@github.com # tests connection to github server (it will give the fingerprint/key that github uses, which could be verified on this link https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)
ssh-add -l # check which key local SSH Agent is using
type %USERPROFILE%\.ssh\id_ed25519.pub # ???

Your identification has been saved in C:\Users\Manuscript/.ssh/id_ed25519
Your public key has been saved in C:\Users\Manuscript/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:hOcagYDvTFOUrzMoffW8U+eRCkKyyCIjhDrLW36xblQ frey.ilya.32@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
| .....           |
|.  .o. .         |
|.. ...o o        |
|..+ . +E         |
|o* + *ooS    .   |
|O B *o.o+ . +    |
|+* o.o+. + + .   |
|..o  +  o . .    |
| ...+.   .       |
+----[SHA256]-----+
# setting up the git for nontracked personal files
1️⃣Create a file called .gitignore in your repo root:
# Ignore API keys / secrets
.env
config_local.py
...etc.
2️⃣Create a .env file in your project root:
# OpenAI API key
OPENAI_API_KEY=sk-your-secret-key
# Other sensitive paths / secrets
DATA_PATH=C:/Users/YourName/Projects/data

3️⃣For collaborators (to use rep between multiple people) config_template.py (commit this)
# config_template.py
# Copy this to config_local.py and fill in your values
OPENAI_API_KEY = "YOUR_API_KEY_HERE"
DATA_PATH = "/path/to/your/data"
5️⃣ Accessing variables in Python
# main.py for .env
from dotenv import load_dotenv
import os
load_dotenv()  # loads .env variables
api_key = os.environ["OPENAI_API_KEY"]
data_path = os.environ.get("DATA_PATH")
# main.py for local things
try:
    from config_local import OPENAI_API_KEY, DATA_PATH
except ImportError:
    raise Exception("Please copy config_template.py to config_local.py and fill in your keys")
6️⃣ Optional: Using GitHub Actions safely:
In GitHub workflow, store keys in Secrets
Use them in workflows like this:
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  Never hardcode keys in workflow YAML files!

NOW THE SETUP CODE (in main.py):
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

# Get your OpenAI API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Check that it loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

# Example request using Bearer token
url = "https://api.openai.com/v1/models"
headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)
print(response.json())