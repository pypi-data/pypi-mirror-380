from agentmake import AGENTMAKE_USER_DIR, readTextFile, writeTextFile
from biblemate import config
import pprint
from pathlib import Path
import os, shutil

config.current_prompt = ""

BIBLEMATE_VERSION = readTextFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "version.txt"))

# copy etextedit plugins
ETEXTEDIT_USER_PULGIN_DIR = os.path.join(os.path.expanduser("~"), "etextedit", "plugins")
if not os.path.isdir(ETEXTEDIT_USER_PULGIN_DIR):
    Path(ETEXTEDIT_USER_PULGIN_DIR).mkdir(parents=True, exist_ok=True)
BIBLEMATE_ETEXTEDIT_PLUGINS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "etextedit", "plugins")
for file_name in os.listdir(BIBLEMATE_ETEXTEDIT_PLUGINS):
    full_file_name = os.path.join(BIBLEMATE_ETEXTEDIT_PLUGINS, file_name)
    if file_name.endswith(".py") and os.path.isfile(full_file_name) and not os.path.isfile(os.path.join(ETEXTEDIT_USER_PULGIN_DIR, file_name)):
        shutil.copy(full_file_name, ETEXTEDIT_USER_PULGIN_DIR)

AGENTMAKE_CONFIG = {
    "print_on_terminal": False,
    "word_wrap": False,
}
OLLAMA_NOT_FOUND = "`Ollama` is not found! BibleMate AI uses `Ollama` to generate embeddings for semantic searches. You may install it from https://ollama.com/ so that you can perform semantic searches of the Bible with BibleMate AI."
BIBLEMATEDATA = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "data")
if not os.path.isdir(BIBLEMATEDATA):
    Path(BIBLEMATEDATA).mkdir(parents=True, exist_ok=True)

def fix_string(content):
    return content.replace(" ", " ").replace("‑", "-")

def write_user_config():
    """Writes the current configuration to the user's config file."""
    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.py")
    configurations = f"""agent_mode={config.agent_mode}
prompt_engineering={config.prompt_engineering}
auto_suggestions={config.auto_suggestions}
max_steps={config.max_steps}
lite={config.lite}
hide_tools_order={config.hide_tools_order}
default_bible="{config.default_bible}"
default_commentary="{config.default_commentary}"
default_encyclopedia="{config.default_encyclopedia}"
default_lexicon="{config.default_lexicon}"
max_semantic_matches={config.max_semantic_matches}
max_log_lines={config.max_log_lines}
mcp_port={config.mcp_port}
embedding_model="{config.embedding_model}"
disabled_tools={pprint.pformat(config.disabled_tools)}"""
    writeTextFile(config_file, configurations)