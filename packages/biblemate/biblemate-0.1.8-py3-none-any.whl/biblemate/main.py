from biblemate.core.systems import *
from biblemate.ui.prompts import getInput
from biblemate.ui.info import get_banner
from biblemate.ui.selection_dialog import TerminalModeDialogs
from biblemate import config, AGENTMAKE_CONFIG, BIBLEMATEDATA, fix_string, write_user_config
from biblemate.uba.api import run_uba_api, DEFAULT_MODULES
from pathlib import Path
import urllib.parse
import asyncio, re, os, subprocess, click, gdown, pprint, argparse, json, zipfile
from copy import deepcopy
from alive_progress import alive_bar
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
from agentmake import agentmake, getOpenCommand, getDictionaryOutput, edit_file, edit_configurations, readTextFile, writeTextFile, getCurrentDateTime, AGENTMAKE_USER_DIR, USER_OS, DEVELOPER_MODE, DEFAULT_AI_BACKEND
from agentmake.utils.handle_text import set_log_file_max_lines
from agentmake.utils.manage_package import getPackageLatestVersion
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.terminal_theme import MONOKAI
if not USER_OS == "Windows":
    import readline  # for better input experience

# trim long log file
log_path = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "logs")
if not os.path.isdir(log_path):
    Path(log_path).mkdir(parents=True, exist_ok=True)
log_file = os.path.join(log_path, "requests")
set_log_file_max_lines(log_file, config.max_log_lines)

# AI backend
version = readTextFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "version.txt"))
parser = argparse.ArgumentParser(description = f"""BibleMate AI {version} CLI options""")
# global options
parser.add_argument("default", nargs="*", default=None, help="initial prompt")
parser.add_argument("-b", "--backend", action="store", dest="backend", help="AI backend; overrides the default backend temporarily.")
parser.add_argument("-l", "--lite", action="store", dest="lite", choices=["true", "false"], help="Enable / disable lite context. Must be one of: true, false.")
parser.add_argument("-m", "--mode", action="store", dest="mode", choices=["agent", "partner", "chat"], help="Specify AI mode. Must be one of: agent, partner, chat.")
parser.add_argument("-pe", "--promptengineer", action="store", dest="promptengineer", choices=["true", "false"], help="Enable / disable prompt engineering. Must be one of: true, false.")
parser.add_argument("-s", "--steps", action="store", dest="steps", type=int, help="Specify the maximum number of steps allowed.")
parser.add_argument("-e", "--exit", action="store_true", dest="exit", help="exit after the first response (for single-turn use cases).")
# mcp options
parser.add_argument("-t", "--token", action="store", dest="token", help="specify a static token to use for authentication with the MCP server; applicable to command `biblemate` only")
parser.add_argument("-mcp", "--mcp", action="store", dest="mcp", help=f"specify a custom MCP server to use, e.g. 'http://127.0.0.1:{config.mcp_port}/mcp/'; applicable to command `biblemate` only")
parser.add_argument("-p", "--port", action="store", dest="port", help=f"specify a port for the MCP server to use, e.g. {config.mcp_port}; applicable to command `biblematemcp` only")
args = parser.parse_args()
# write to the `config.py` file temporarily for the MCP server to pick it up
if args.backend:
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.py"), "a", encoding="utf-8") as fileObj:
        fileObj.write(f'''\nbackend="{args.backend}"''')
    config.backend = args.backend
else:
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.py"), "a", encoding="utf-8") as fileObj:
        fileObj.write(f'''\nbackend="{DEFAULT_AI_BACKEND}"''')
    config.backend = DEFAULT_AI_BACKEND

AGENTMAKE_CONFIG["backend"] = config.backend
DEFAULT_SYSTEM = "You are BibleMate AI, an autonomous agent designed to assist users with their Bible study."
DEFAULT_MESSAGES = [{"role": "system", "content": DEFAULT_SYSTEM}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hello! I'm BibleMate AI, your personal assistant for Bible study. How can I help you today?"}] # set a tone for bible study; it is userful when auto system is used.

# other temporary config changes
if args.lite == "true":
    config.lite = True
elif args.lite == "false":
    config.lite = False
if args.mode == "agent":
    config.agent_mode = True
elif args.mode == "partner":
    config.agent_mode = False
elif args.mode == "chat":
    config.agent_mode = None
if args.promptengineer == "true":
    config.prompt_engineering = True
elif args.promptengineer == "false":
    config.prompt_engineering = False
if args.steps:
    config.max_steps = args.steps

def mcp():
    builtin_mcp_server = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bible_study_mcp.py")
    user_mcp_server = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "bible_study_mcp.py") # The user path has the same basename as the built-in one; users may copy the built-in server settings to this location for customization. 
    mcp_script = readTextFile(user_mcp_server if os.path.isfile(user_mcp_server) else builtin_mcp_server)
    mcp_script = mcp_script.replace("mcp.run(show_banner=False)", f'''mcp.run(show_banner=False, transport="http", host="0.0.0.0", port={args.port if args.port else config.mcp_port})''')
    exec(mcp_script)

def main():
    asyncio.run(main_async())

async def initialize_app(client):
    """Initializes the application by fetching tools and prompts from the MCP server."""
    await client.ping()

    tools_raw = await client.list_tools()
    tools = {t.name: t.description for t in tools_raw}
    tools = dict(sorted(tools.items()))
    tools_schema = {}
    for t in tools_raw:
        schema = {
            "name": t.name,
            "description": t.description,
            "parameters": {
                "type": "object",
                "properties": t.inputSchema["properties"],
                "required": t.inputSchema["required"],
            },
        }
        tools_schema[t.name] = schema

    available_tools = list(tools.keys())
    if "get_direct_text_response" not in available_tools:
        available_tools.insert(0, "get_direct_text_response")
    master_available_tools = deepcopy(available_tools)
    available_tools = [i for i in available_tools if not i in config.disabled_tools]

    tool_descriptions = ""
    if "get_direct_text_response" not in tools:
        tool_descriptions = """# TOOL DESCRIPTION: `get_direct_text_response`
Get a static text-based response directly from a text-based AI model without using any other tools. This is useful when you want to provide a simple and direct answer to a question or request, without the need for online latest updates or task execution."""
    for tool_name, tool_description in tools.items():
        tool_descriptions += f"""# TOOL DESCRIPTION: `{tool_name}`
{tool_description}\n\n\n"""

    prompts_raw = await client.list_prompts()
    prompts = {p.name: p.description for p in prompts_raw}
    prompts = dict(sorted(prompts.items()))

    prompts_schema = {}
    for p in prompts_raw:
        arg_properties = {}
        arg_required = []
        for a in p.arguments:
            arg_properties[a.name] = {
                "type": "string",
                "description": str(a.description) if a.description else "no description available",
            }
            if a.required:
                arg_required.append(a.name)
        schema = {
            "name": p.name,
            "description": p.description,
            "parameters": {
                "type": "object",
                "properties": arg_properties,
                "required": arg_required,
            },
        }
        prompts_schema[p.name] = schema
    
    resources_raw = await client.list_resources()
    resources = {r.name: r.description for r in resources_raw}
    resources = dict(sorted(resources.items()))

    templates_raw = await client.list_resource_templates()
    templates = {r.name: r.description for r in templates_raw}
    templates = dict(sorted(templates.items()))
    
    return tools, tools_schema, master_available_tools, available_tools, tool_descriptions, prompts, prompts_schema, resources, templates

def edit_temp_file(initial_content: str) -> str:
    temp_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", "edit.md")
    writeTextFile(temp_file, initial_content)
    edit_file(temp_file)
    return readTextFile(temp_file).strip()

def backup_conversation(messages, master_plan, console=None):
    """Backs up the current conversation to the user's directory."""
    if len(messages) > len(DEFAULT_MESSAGES):
        # determine storage path
        if console:
            timestamp = getCurrentDateTime()
            storagePath = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "chats", timestamp)
        else:
            storagePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")
        # create directory if not exists
        if not os.path.isdir(storagePath):
            Path(storagePath).mkdir(parents=True, exist_ok=True)
        # Save full conversation
        conversation_file = os.path.join(storagePath, "conversation.py")
        writeTextFile(conversation_file, pprint.pformat(messages))
        # Save master plan
        writeTextFile(os.path.join(storagePath, "master_plan.md"), master_plan)
        # Save markdown
        markdown_file = os.path.join(storagePath, "conversation.md")
        markdown_text = "\n\n".join(["```"+i["role"]+"\n"+i["content"]+"\n```" for i in messages if i.get("role", "") in ("user", "assistant")])
        writeTextFile(markdown_file, markdown_text)
        # Save html
        if console:
            html_file = os.path.join(storagePath, "conversation.html")
            console.save_html(html_file, inline_styles=True, theme=MONOKAI)
        # Inform users of the backup location
        if console:
            print(f"Conversation backup saved to {storagePath}")
            print(f"Report saved to {html_file}\n")

async def main_async():

    BIBLEMATE_STATIC_TOKEN = args.token if args.token else os.getenv("BIBLEMATE_STATIC_TOKEN")
    BIBLEMATE_MCP_PRIVATE_KEY=os.getenv("BIBLEMATE_MCP_PRIVATE_KEY")

    # The client that interacts with the Bible Study MCP server
    if args.mcp:
        mcp_server = f"http://127.0.0.1:{config.mcp_port}/mcp/" if args.mcp == "biblemate" else args.mcp
        transport = StreamableHttpTransport(
            mcp_server,
            auth=BIBLEMATE_STATIC_TOKEN if BIBLEMATE_STATIC_TOKEN else BIBLEMATE_MCP_PRIVATE_KEY if BIBLEMATE_MCP_PRIVATE_KEY else None,
        )
        client = Client(transport=transport)
    else:
        builtin_mcp_server = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bible_study_mcp.py")
        user_mcp_server = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "bible_study_mcp.py") # The user path has the same basename as the built-in one; users may copy the built-in server settings to this location for customization. 
        mcp_server = user_mcp_server if os.path.isfile(user_mcp_server) else builtin_mcp_server        
        client = Client(mcp_server) # no auth for local server

    APP_START = True
    DEFAULT_SYSTEM = "You are BibleMate AI, an autonomous agent designed to assist users with their Bible study."
    DEFAULT_MESSAGES = [{"role": "system", "content": DEFAULT_SYSTEM}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hello! I'm BibleMate AI, your personal assistant for Bible study. How can I help you today?"}] # set a tone for bible study; it is userful when auto system is used.

    console = Console(record=True)
    console.clear()
    console.print(get_banner())
    dialogs = TerminalModeDialogs(None)

    async with client:
        tools, tools_schema, master_available_tools, available_tools, tool_descriptions, prompts, prompts_schema, resources, templates = await initialize_app(client)
        resource_suggestions = json.loads(run_uba_api(".resources"))
        resource_suggestions = [f"//bible/{i}/" for i in resource_suggestions["bibleListAbb"]]+[f"//commentary/{i}/" for i in resource_suggestions["commentaryListAbb"]]+[f"//encyclopedia/{i}/" for i in resource_suggestions["encyclopediaListAbb"]]+[f"//lexicon/{i}/" for i in resource_suggestions["lexiconList"]]
        abbr = BibleBooks.abbrev["eng"]
        resource_suggestions += [abbr[str(book)][0] for book in range(1,67)]

        write_user_config() # remove the temporary `config.backend`
        
        available_tools_pattern = "|".join(available_tools)
        prompt_list = [f"/{p}" for p in prompts.keys()]
        prompt_pattern = "|".join(prompt_list)
        prompt_pattern = f"""^({prompt_pattern}) """
        template_list = [f"//{t}/" for t in templates.keys()]
        template_pattern = "|".join(template_list)
        template_pattern = f"""^({template_pattern})"""

        user_request = ""
        master_plan = ""
        messages = deepcopy(DEFAULT_MESSAGES) # set the tone

        while not user_request == ".quit":

            # spinner while thinking
            async def thinking(process, description=None):
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    transient=True  # This makes the progress bar disappear after the task is done
                ) as progress:
                    # Add an indefinite task (total=None)
                    task_id = progress.add_task(description if description else "Thinking ...", total=None)
                    # Create and run the async task concurrently
                    async_task = asyncio.create_task(process())
                    # Loop until the async task is done
                    while not async_task.done():
                        progress.update(task_id)
                        await asyncio.sleep(0.01)
                await async_task
            # progress bar for processing steps
            async def async_alive_bar(task):
                """
                A coroutine that runs a progress bar while awaiting a task.
                """
                with alive_bar(title="Processing...", spinner='dots') as bar:
                    while not task.done():
                        bar() # Update the bar
                        await asyncio.sleep(0.01) # Yield control back to the event loop
                return task.result()
            async def process_tool(tool, tool_instruction, step_number=None):
                """
                Manages the async task and the progress bar.
                """
                if step_number:
                    print(f"# Starting Step [{step_number}]...")
                # Create the async task but don't await it yet.
                task = asyncio.create_task(run_tool(tool, tool_instruction))
                # Await the custom async progress bar that awaits the task.
                await async_alive_bar(task)

            if not len(messages) == len(DEFAULT_MESSAGES):
                console.rule()
            elif APP_START:
                APP_START = False
                print()
                # check for updates
                latest_version = getPackageLatestVersion("biblemate")
                current_version = readTextFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "version.txt")).strip()
                if latest_version and str(latest_version).strip() != current_version:
                    console.rule()
                    console.print(Markdown(f"## A new version of BibleMate AI is available: {latest_version} (you are using {current_version}).\n\nTo upgrade, close `BibleMate AI` first and run `pip install --upgrade biblemate`."))
                    console.rule()
                # check connection
                try:
                    agentmake("Hello!", system=DEFAULT_SYSTEM)
                except Exception as e:
                    print("Connection failed! Please ensure that you have a stable internet connection and that my AI backend and model are properly configured.")
                    print("Viist https://github.com/eliranwong/agentmake#supported-backends for help about the backend configuration.\n")
                    if click.confirm("Do you want to configure my AI backend and model now?", default=True):
                        edit_configurations()
                        console.rule()
                        console.print("Restart to make the changes in the backend effective!", justify="center")
                        console.rule()
                        exit()
            # Original user request
            # note: `python3 -m rich.emoji` for checking emoji
            console.print("Enter your request :smiley: :" if len(messages) == len(DEFAULT_MESSAGES) else "Enter a follow-up request :flexed_biceps: :")
            action_list = {
                ".new": "new conversation",
                ".quit": "quit",
                ".backend": "change backend",
                ".mode": "change AI mode",
                ".tools": "list available tools",
                ".plans": "list available plans",
                ".resources": "list UniqueBible resources",
                ".promptengineer": "toggle auto prompt engineering",
                ".lite": "toggle lite context",
                ".steps": "configure the maximum number of steps",
                ".matches": "configure the maximum number of semantic matches",
                ".edit": "load the current conversation",
                ".backup": "backup conversation",
                ".load": "load a saved conversation",
                ".open": "open a file or directory",
                ".download": "download data files",
                ".help": "help page",
            }
            input_suggestions = list(action_list.keys())+["@ ", "@@ "]+[f"@{t} " for t in available_tools]+[f"{p} " for p in prompt_list]+[f"//{r}" for r in resources.keys()]+template_list+resource_suggestions # "" is for generating ideas
            if args.default:
                user_request = " ".join(args.default)
                args.default = None # reset to avoid repeated use
            else:
                user_request = await getInput("> ", input_suggestions)
            if user_request == ".editprompt": # edit current prompt in editor
                user_request = edit_temp_file(config.current_prompt)
            while not user_request.strip():
                # Generate ideas for `prompts to try`
                ideas = ""
                async def generate_ideas():
                    nonlocal ideas
                    if len(messages) == len(DEFAULT_MESSAGES):
                        ideas = agentmake("Generate three `prompts to try` for bible study. Each one should be one sentence long.", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                    else:
                        ideas = agentmake(messages, follow_up_prompt="Generate three follow-up questions according to the on-going conversation.", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                await thinking(generate_ideas, "Generating ideas ...")
                console.rule()
                console.print(Markdown(f"## Ideas\n\n{ideas}\n\n"))
                console.rule()
                # Get input again
                user_request = await getInput("> ", input_suggestions)
                if user_request == ".editprompt": # edit current prompt in editor
                    user_request = edit_temp_file(config.current_prompt)

            # display resources
            if user_request.startswith("//") and user_request[2:] in resources:
                resource = user_request[2:]
                resource_content = await client.read_resource(f"resource://{resource}")
                if hasattr(resource_content[0], 'text'):
                    console.rule()
                    resource_text = resource_content[0].text
                    if resource_text.startswith("{"):
                        resource_dict = json.loads(resource_text)
                        display_content = "\n".join([f"- `{k}`: {v}" for k, v in resource_dict.items()])
                    else:
                        display_content = resource_text
                    resource_description = resources.get(resource, "")
                    console.print(Markdown(f"## Information about `{resource}`: `{resource.capitalize()}`\n\n{resource_description}\n\n{display_content}"))
                    console.rule()
                continue

            # run templates
            if re.search(template_pattern, user_request):
                user_request = urllib.parse.quote(user_request)
                if user_request[2:].count("/") == 1:
                    keywords = DEFAULT_MODULES
                    keyword, entry = user_request[2:].split("/")
                    if module := keywords.get(keyword, ""):
                        user_request = f"//{keyword}/{module}/{entry}"
                        if user_request.count("/") > 4:
                            user_request = re.sub("^(//.*?/.*?/)(.*?)$", r"\1"+r"\2".replace("/", "「」"), user_request)
                    elif user_request.count("/") > 3:
                        user_request = re.sub("^(//.*?/)(.*?)$", r"\1"+r"\2".replace("/", "「」"), user_request)
                try:
                    uri = re.sub("^(.*?)/", r"\1://", user_request[2:])
                    resource_content = await client.read_resource(uri)
                    resource_content = resource_content[0].text
                    while resource_content.startswith("[") and resource_content.endswith("]"):
                        options = json.loads(resource_content)
                        select = await dialogs.getValidOptions(
                            options=options,
                            title="Multiple Matches",
                            text="Select one of them to continue:"
                        )
                        if select:
                            if keyword == "name":
                                resource_content = select
                            else:
                                resource_content = await client.read_resource(re.sub("^(.*?/)[^/]*?$", r"\1", uri)+urllib.parse.quote(select.replace("/", "「」")))
                                resource_content = resource_content[0].text
                        else:
                            resource_content = "Cancelled by user."
                    if resource_content:
                        messages += [
                            {"role": "user", "content": f"Retrieve content from:\n\n{uri}"},
                            {"role": "assistant", "content": resource_content},
                        ]
                        console.rule()
                        console.print(Markdown(resource_content))
                    continue
                except Exception as e: # invalid uri
                    print(f"Error: {e}\n")
                    continue
            
            # system command
            if user_request == ".open":
                user_request = f".open {os.getcwd()}"
            if user_request.startswith(".open ") and os.path.exists(os.path.expanduser(re.sub('''^['" ]*?([^'" ].+?)['" ]*?$''', r"\1", user_request[6:]))):
                file_path = os.path.expanduser(re.sub('''^['" ]*?([^'" ].+?)['" ]*?$''', r"\1", user_request[6:]))
                cmd = f'''{getOpenCommand()} "{file_path}"'''
                subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                continue
            elif user_request.startswith(".load") and os.path.exists(os.path.expanduser(re.sub('''^['" ]*?([^'" ].+?)['" ]*?$''', r"\1", user_request[6:]))):
                load_path = os.path.expanduser(re.sub('''^['" ]*?([^'" ].+?)['" ]*?$''', r"\1", user_request[6:]))
                try:
                    # load conversation
                    if os.path.isfile(load_path):
                        file_path = load_path
                    elif os.path.isdir(load_path) and os.path.isfile(os.path.join(load_path, "conversation.py")) and os.path.isfile(os.path.join(load_path, "master_plan.md")):
                        file_path = os.path.join(load_path, "conversation.py")
                    else:
                        print("Expected a file or a directory containing `conversation.py` and `master_plan.md`.")
                        continue
                    backup_conversation(messages, master_plan, console)
                    messages = [{"role": i["role"], "content": i["content"]} for i in eval(readTextFile(file_path)) if i.get("role", "") in ("user", "assistant")]
                    if messages:
                        messages.insert(0, {"role": "system", "content": DEFAULT_SYSTEM})
                    if messages[-1].get("role", "") == "user":
                        messages = messages[:-1]
                    # load master plan
                    if os.path.isdir(load_path):
                        master_plan = readTextFile(os.path.join(load_path, "master_plan.md"))
                        user_request = "[CONTINUE]"
                    else:
                        master_plan = ""
                        user_request = ""
                    console.clear()
                    console.print(get_banner())
                    if messages:
                        for i in messages:
                            if i.get("role", "") in ("user", "assistant"):
                                console.rule()
                                console.print(Markdown(f"# {i['role']}\n\n{i['content']}"))
                    if os.path.isfile(load_path) or config.agent_mode is None:
                        # next user request
                        continue
                except Exception as e:
                    print(f"Error: {e}\n")
                    continue

            # predefined operations with `.` commands
            if user_request in action_list:
                if user_request == ".backup":
                    backup_conversation(messages, master_plan, console)
                elif user_request == ".help":
                    console.rule()
                    console.print(Markdown("Viist https://github.com/eliranwong/biblemate for help."))
                    console.rule()
                elif user_request == ".tools":
                    enabled_tools = await dialogs.getMultipleSelection(
                        default_values=available_tools,
                        options=master_available_tools,
                        title="Tool Options",
                        text="Select tools to enable:"
                    )
                    if enabled_tools is not None:
                        available_tools = enabled_tools
                        available_tools_pattern = "|".join(available_tools) # reset available tools pattern
                        config.disabled_tools = [i for i in master_available_tools if not i in available_tools]
                        write_user_config()
                    console.rule()
                    tools_descriptions = [f"- `{name}`: {description}" for name, description in tools.items()]
                    console.print(Markdown("## Available Tools\n\n"+"\n".join(tools_descriptions)))
                    console.rule()
                elif user_request == ".resources":
                    console.rule()
                    resources_descriptions = [f"- `//{name}`: {description}" for name, description in resources.items()]
                    templates_descriptions = [f"- `//{name}/...`: {description}" for name, description in templates.items()]
                    console.print(Markdown("## Available Information\n\n"+"\n".join(resources_descriptions)+"\n\n## Available Resources\n\n"+"\n".join(templates_descriptions)))
                    console.rule()
                elif user_request == ".plans":
                    console.rule()
                    prompts_descriptions = [f"- `/{name}`: {description}" for name, description in prompts.items()]
                    console.print(Markdown("## Available Plans\n\n"+"\n".join(prompts_descriptions)))
                    console.rule()
                elif user_request == ".edit":
                    options = [str(i) for i in range(0, len(messages))]
                    index_to_edit = await dialogs.getValidOptions(
                        default=str(len(messages)-1),
                        options=options,
                        descriptions=[f"{messages[int(i)]['role']}: {messages[int(i)]['content'][:50]+'...' if len(messages[int(i)]['content'])>50 else messages[int(i)]['content']}" for i in options],
                        title="Edit Conversation",
                        text="Select an entry to edit:"
                    )
                    if index_to_edit:
                        index_to_edit = int(index_to_edit)
                        temp_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp", "edit.md")
                        writeTextFile(temp_file, messages[index_to_edit]["content"])
                        edit_file(temp_file)
                        edited_content = readTextFile(temp_file).strip()
                        if edited_content:
                            messages[index_to_edit]["content"] = edited_content
                            backup_conversation(messages, master_plan) # backup
                            console.rule()
                            console.print("Changes saved!", justify="center")
                            console.rule()
                elif user_request == ".backend":
                    edit_configurations()
                    console.rule()
                    console.print("Restart to make the changes in the backend effective!", justify="center")
                    console.rule()
                elif user_request == ".steps":
                    console.rule()
                    console.print("Enter below the maximum number of steps allowed:")
                    max_steps = await getInput("> ", number_validator=True, default_entry=str(config.max_steps))
                    if max_steps:
                        config.max_steps = int(max_steps)
                        write_user_config()
                        console.print("Maximum number of steps set to", config.max_steps, justify="center")
                    console.rule()
                elif user_request == ".matches":
                    console.rule()
                    console.print("Enter below the maximum number of semantic matches allowed:")
                    max_semantic_matches = await getInput("> ", number_validator=True, default_entry=str(config.max_semantic_matches))
                    if max_semantic_matches:
                        config.max_semantic_matches = int(max_semantic_matches)
                        write_user_config()
                        console.print("Maximum number of semantic matches set to", config.max_semantic_matches, justify="center")
                    console.rule()
                elif user_request == ".promptengineer":
                    config.prompt_engineering = not config.prompt_engineering
                    write_user_config()
                    console.rule()
                    console.print("Prompt Engineering Enabled" if config.prompt_engineering else "Prompt Engineering Disabled", justify="center")
                    console.rule()
                elif user_request == ".lite":
                    config.lite = not config.lite
                    write_user_config()
                    console.rule()
                    console.print("Lite Context Enabled" if config.lite else "Lite Context Disabled", justify="center")
                    console.rule()
                elif user_request == ".download":
                    file_ids ={
                        "bible.db": "1E6pDKfjUMhmMWjjazrg5ZcpH1RBD8qgW",
                        "collection.db": "1y4txzRzXTBty0aYfFgkWfz5qlHERrA17",
                        "dictionary.db": "1UxDKGEQa7UEIJ6Ggknx13Yt8XNvo3Ld3",
                        "encyclopedia.db": "1NLUBepvFd9UDxoGQyQ-IohmySjjeis2-",
                        "exlb.db": "1Hpo6iLSh5KzgR6IZ-c7KuML--A3nmP1-",
                    }
                    file_id = await dialogs.getValidOptions(
                        options=file_ids.keys(),
                        title="BibleMate Data Files",
                        text="Select a file:"
                    )
                    if file_id:
                        output = os.path.join(BIBLEMATEDATA, file_id+".zip")
                        if os.path.isfile(output):
                            os.remove(output)
                        if os.path.isfile(output[:-4]):
                            os.remove(output[:-4])
                        gdown.download(id=file_ids[file_id], output=output)
                        with zipfile.ZipFile(output, 'r') as zip_ref:
                            zip_ref.extractall(BIBLEMATEDATA)
                        if os.path.isfile(output):
                            os.remove(output)
                elif user_request == ".mode":
                    default_ai_mode = "chat" if config.agent_mode is None else "agent" if config.agent_mode else "partner"
                    ai_mode = await dialogs.getValidOptions(
                        default=default_ai_mode,
                        options=["agent", "partner", "chat"],
                        descriptions=["AGENT - Fully automated", "PARTNER - Semi-automated, with review and edit prompts", "CHAT - Direct text responses"],
                        title="AI Modes",
                        text="Select an AI mode:"
                    )
                    if ai_mode:
                        if ai_mode == "agent":
                            config.agent_mode = True
                        elif ai_mode == "partner":
                            config.agent_mode = False
                        else:
                            config.agent_mode = None
                        write_user_config()
                        console.rule()
                        console.print(f"`{ai_mode.capitalize()}` Mode Enabled", justify="center")
                        console.rule()
                elif user_request in (".new", ".quit"):
                    backup_conversation(messages, master_plan, console) # backup
                # reset
                if user_request == ".new":
                    user_request = ""
                    master_plan = ""
                    messages = deepcopy(DEFAULT_MESSAGES)
                    console.clear()
                    console.print(get_banner())
                continue

            # Check if a single tool is specified
            specified_prompt = ""
            specified_tool = ""

            # Tool selection systemm message
            system_tool_selection = get_system_tool_selection(available_tools, tool_descriptions)

            if user_request.startswith("@ "):
                user_request = user_request[2:].strip()
                # Single Tool Suggestion
                suggested_tools = []
                async def get_tool_suggestion():
                    nonlocal suggested_tools, user_request, system_tool_selection
                    if DEVELOPER_MODE and not config.hide_tools_order:
                        console.print(Markdown(f"## Tool Selection (descending order by relevance)"), "\n")
                    else:
                        console.print(Markdown(f"## Tool Selection"), "\n")
                    # Extract suggested tools from the step suggestion
                    suggested_tools = agentmake(user_request, system=system_tool_selection, **AGENTMAKE_CONFIG)[-1].get("content", "").strip() # Note: suggested tools are printed on terminal by default, could be hidden by setting `print_on_terminal` to false
                    suggested_tools = re.sub(r"^.*?(\[.*?\]).*?$", r"\1", suggested_tools, flags=re.DOTALL)
                    try:
                        suggested_tools = eval(suggested_tools.replace("`", "'")) if suggested_tools.startswith("[") and suggested_tools.endswith("]") else ["get_direct_text_response"] # fallback to direct response
                    except:
                        suggested_tools = ["get_direct_text_response"]
                await thinking(get_tool_suggestion)
                # Single Tool Selection
                if config.agent_mode:
                    this_tool = suggested_tools[0] if suggested_tools else "get_direct_text_response"
                else: # `partner` mode when config.agent_mode is set to False
                    this_tool = await dialogs.getValidOptions(options=suggested_tools if suggested_tools else available_tools, title="Suggested Tools", text="Select a tool:")
                    if not this_tool:
                        this_tool = "get_direct_text_response"
                # Re-format user request
                user_request = f"@{this_tool} " + user_request

            if re.search(prompt_pattern, user_request):
                specified_prompt = re.search(prompt_pattern, user_request).group(1)
                user_request = user_request[len(specified_prompt):]
            elif re.search(f"""^@({available_tools_pattern}) """, user_request):
                specified_tool = re.search(f"""^@({available_tools_pattern}) """, user_request).group(1)
                user_request = user_request[len(specified_tool)+2:]
            elif user_request.startswith("@@"):
                specified_tool = "@@"
                master_plan = user_request[2:].strip()
                async def refine_custom_plan():
                    nonlocal messages, user_request, master_plan
                    # Summarize user request in one-sentence instruction
                    user_request = agentmake(master_plan, tool="biblemate/summarize_task_instruction", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                    if "```" in user_request:
                        user_request = re.sub(r"^.*?(```instruction|```)(.+?)```.*?$", r"\2", user_request, flags=re.DOTALL).strip()
                await thinking(refine_custom_plan)
                # display info
                console.print(Markdown(f"# User Request\n\n{user_request}\n\n# Master plan\n\n{master_plan}"))

            # Prompt Engineering
            if not specified_tool == "@@" and config.prompt_engineering and not user_request == "[CONTINUE]":
                async def run_prompt_engineering():
                    nonlocal user_request
                    try:
                        user_request = agentmake(messages if messages else user_request, follow_up_prompt=user_request if messages else None, tool="improve_prompt", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                        if "```" in user_request:
                            user_request = re.sub(r"^.*?(```improved_version|```)(.+?)```.*?$", r"\2", user_request, flags=re.DOTALL).strip()
                    except:
                        user_request = agentmake(messages if messages else user_request, follow_up_prompt=user_request if messages else None, system="improve_prompt_2")[-1].get("content", "").strip()
                        user_request = re.sub(r"^.*?(```improved_prompt|```)(.+?)```.*?$", r"\2", user_request, flags=re.DOTALL).strip()
                await thinking(run_prompt_engineering, "Prompt Engineering ...")

            # Add user request to messages
            if not user_request == "[CONTINUE]":
                messages.append({"role": "user", "content": user_request})

            async def run_tool(tool, tool_instruction):
                nonlocal messages
                tool_instruction = fix_string(tool_instruction)
                messages[-1]["content"] = fix_string(messages[-1]["content"])
                if tool == "get_direct_text_response":
                    messages = agentmake(messages, system="auto", **AGENTMAKE_CONFIG)
                else:
                    try:
                        tool_schema = tools_schema[tool]
                        tool_properties = tool_schema["parameters"]["properties"]
                        if len(tool_properties) == 1 and "request" in tool_properties: # AgentMake MCP Servers or alike
                            if "items" in tool_properties["request"]: # requires a dictionary instead of a string
                                request_dict = [{"role": "system", "content": DEFAULT_SYSTEM}]+messages[len(messages)-2:] if config.lite else deepcopy(messages)
                                tool_result = await client.call_tool(tool, {"request": request_dict})
                            else:
                                tool_result = await client.call_tool(tool, {"request": tool_instruction})
                        else:
                            structured_output = getDictionaryOutput(messages=messages, schema=tool_schema, backend=config.backend)
                            tool_result = await client.call_tool(tool, structured_output)
                        tool_result = tool_result.content[0].text
                        messages[-1]["content"] += f"\n\n[Using tool `{tool}`]"
                        messages.append({"role": "assistant", "content": tool_result if tool_result.strip() else "Tool error!"})
                    except Exception as e:
                        if DEVELOPER_MODE:
                            console.print(f"Error: {e}\nFallback to direct response...\n\n")
                        messages = agentmake(messages, system="auto", **AGENTMAKE_CONFIG)
                messages[-1]["content"] = fix_string(messages[-1]["content"])

            # user specify a single tool
            if specified_tool and not specified_tool == "@@":
                await process_tool(specified_tool, user_request)
                console.print(Markdown(f"# User Request\n\n{messages[-2]['content']}\n\n# AI Response\n\n{messages[-1]['content']}"))
                continue

            # Chat mode
            if config.agent_mode is None and not specified_tool == "@@":
                async def run_chat_mode():
                    nonlocal messages, user_request
                    messages = agentmake(messages if messages else user_request, system="auto", **AGENTMAKE_CONFIG)
                await thinking(run_chat_mode)
                console.print(Markdown(f"# User Request\n\n{messages[-2]['content']}\n\n# AI Response\n\n{messages[-1]['content']}"))
                continue

            # agent mode or partner mode

            # generate master plan
            if not master_plan:
                if specified_prompt:
                    # Call the MCP prompt
                    prompt_schema = prompts_schema[specified_prompt[1:]]
                    prompt_properties = prompt_schema["parameters"]["properties"]
                    if len(prompt_properties) == 1 and "request" in prompt_properties: # AgentMake MCP Servers or alike
                        result = await client.get_prompt(specified_prompt[1:], {"request": user_request})
                    else:
                        structured_output = getDictionaryOutput(messages=messages, schema=prompt_schema, backend=config.backend)
                        result = await client.get_prompt(specified_prompt[1:], structured_output)
                    #print(result, "\n\n")
                    master_plan = result.messages[0].content.text
                    # display info# display info
                    console.print(Markdown(f"# User Request\n\n{user_request}\n\n# Master plan\n\n{master_plan}"))
                else:
                    # display info
                    console.print(Markdown(f"# User Request\n\n{user_request}"), "\n")
                    # Generate master plan
                    master_plan = ""
                    async def generate_master_plan():
                        nonlocal master_plan
                        # Create initial prompt to create master plan
                        initial_prompt = f"""Provide me with the `Preliminary Action Plan` and the `Measurable Outcome` for resolving `My Request`.
    
# Available Tools

Available tools are: {available_tools}.

{tool_descriptions}

# My Request

{user_request}"""
                        console.print(Markdown("# Master plan"), "\n")
                        print()
                        master_plan = agentmake(messages+[{"role": "user", "content": initial_prompt}], system="create_action_plan", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                    await thinking(generate_master_plan)

                    # partner mode
                    if config.agent_mode == False:
                        console.rule()
                        console.print(Markdown("# Review & Confirm"))
                        console.print("Please review and confirm the master plan, or make any changes you need:", justify="center")
                        console.rule()
                        master_plan_edit = await getInput(default_entry=master_plan)
                        if master_plan_edit == ".editprompt": # edit current prompt in editor
                            master_plan_edit = edit_temp_file(config.current_prompt)
                        if not master_plan_edit or master_plan_edit == ".quit":
                            if messages and messages[-1].get("role", "") == "user":
                                messages = messages[:-1]
                            console.rule()
                            console.print("I've stopped processing for you.")
                            continue
                        else:
                            master_plan_edit = master_plan_edit
                        console.rule()

                    # display info
                    console.print(Markdown(master_plan), "\n\n")

            # Step suggestion system message
            system_progress = get_system_progress(master_plan=master_plan)
            system_make_suggestion = get_system_make_suggestion(master_plan=master_plan)

            # Get the first suggestion
            next_suggestion = "CONTINUE" if user_request == "[CONTINUE]" else "START"

            step = int(((len(messages)-len(DEFAULT_MESSAGES)-2)/2+1)) if user_request == "[CONTINUE]" else 1
            while not ("STOP" in next_suggestion or re.sub("^[^A-Za-z]*?([A-Za-z]+?)[^A-Za-z]*?$", r"\1", next_suggestion).upper() == "STOP"):

                async def make_next_suggestion():
                    nonlocal next_suggestion, system_make_suggestion, messages, step
                    console.print(Markdown(f"## Suggestion [{step}]"), "\n")
                    next_suggestion = agentmake(user_request if next_suggestion == "START" else [{"role": "system", "content": system_make_suggestion}]+messages[len(DEFAULT_MESSAGES):], system=system_make_suggestion, follow_up_prompt=None if next_suggestion == "START" else "Please provide me with the next step suggestion, based on the action plan.", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                await thinking(make_next_suggestion)
                console.print(Markdown(next_suggestion), "\n\n")

                # Get tool suggestion for the next iteration
                suggested_tools = []
                async def get_tool_suggestion():
                    nonlocal suggested_tools, next_suggestion, system_tool_selection
                    if DEVELOPER_MODE and not config.hide_tools_order:
                        console.print(Markdown(f"## Tool Selection (descending order by relevance) [{step}]"), "\n")
                    else:
                        console.print(Markdown(f"## Tool Selection [{step}]"), "\n")
                    # Extract suggested tools from the step suggestion
                    suggested_tools = agentmake(next_suggestion, system=system_tool_selection, **AGENTMAKE_CONFIG)[-1].get("content", "").strip() # Note: suggested tools are printed on terminal by default, could be hidden by setting `print_on_terminal` to false
                    suggested_tools = re.sub(r"^.*?(\[.*?\]).*?$", r"\1", suggested_tools, flags=re.DOTALL)
                    try:
                        suggested_tools = eval(suggested_tools.replace("`", "'")) if suggested_tools.startswith("[") and suggested_tools.endswith("]") else ["get_direct_text_response"] # fallback to direct response
                    except:
                        suggested_tools = ["get_direct_text_response"]
                await thinking(get_tool_suggestion)
                if DEVELOPER_MODE and not config.hide_tools_order:
                    console.print(Markdown(str(suggested_tools)))

                # Use the next suggested tool
                # partner mode
                if config.agent_mode:
                    next_tool = suggested_tools[0] if suggested_tools else "get_direct_text_response"
                else: # `partner` mode when config.agent_mode is set to False
                    next_tool = await dialogs.getValidOptions(options=suggested_tools if suggested_tools else available_tools, title="Suggested Tools", text="Select a tool:")
                    if not next_tool:
                        next_tool = "get_direct_text_response"
                prefix = f"## Next Tool [{step}]\n\n" if DEVELOPER_MODE and not config.hide_tools_order else ""
                console.print(Markdown(f"{prefix}`{next_tool}`"))
                print()

                # Get next step instruction
                next_step = ""
                async def get_next_step():
                    nonlocal next_step, next_tool, next_suggestion, tools
                    console.print(Markdown(f"## Next Instruction [{step}]"), "\n")
                    if next_tool == "get_direct_text_response":
                        next_step = agentmake(next_suggestion, system="biblemate/direct_instruction", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                    else:
                        next_tool_description = tools.get(next_tool, "No description available.")
                        system_tool_instruction = get_system_tool_instruction(next_tool, next_tool_description)
                        next_step = agentmake(next_suggestion, system=system_tool_instruction, **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                await thinking(get_next_step)
                # partner mode
                if config.agent_mode == False:
                    console.rule()
                    console.print(Markdown("# Review & Confirm"))
                    console.print("Please review and confirm the next step, or make any changes you need:")
                    console.rule()
                    next_step_edit = await getInput(default_entry=next_step)
                    if next_step_edit == ".editprompt": # edit current prompt in editor
                        next_step_edit = edit_temp_file(config.current_prompt)
                    if not next_step_edit or next_step_edit == ".quit":
                        console.rule()
                        console.print("I've stopped processing for you.")
                        break
                    else:
                        next_step = next_step_edit
                    console.rule()
                console.print(Markdown(next_step), "\n\n")

                if messages[-1]["role"] != "assistant": # first iteration
                    messages.append({"role": "assistant", "content": "Please provide me with an initial instruction to begin."})
                messages.append({"role": "user", "content": next_step})

                await process_tool(next_tool, next_step, step_number=step)
                console.print(Markdown(f"\n## Output [{step}]\n\n{messages[-1]['content']}"))
                # temporaily save after each step
                backup_conversation(messages, master_plan)

                # iteration count
                step += 1
                if step > config.max_steps:
                    console.rule()
                    console.print("I've stopped processing for you, as the maximum steps allowed is currently set to", config.max_steps, "steps. Enter `.steps` to configure more.")
                    console.rule()
                    break

                # Check the progress
                async def get_next_suggestion():
                    nonlocal next_suggestion, messages, system_progress
                    next_suggestion = agentmake([{"role": "system", "content": system_progress}]+messages[len(DEFAULT_MESSAGES):], system=system_progress, follow_up_prompt="Please decide either to `CONTINUE` or `STOP` the process.", **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
                await thinking(get_next_suggestion, description="Checking the progress ...")
            
            if messages[-1].get("role") == "user":
                messages.append({"role": "assistant", "content": next_suggestion})
            
            # write the final answer
            console.rule()
            console.print(Markdown("# Wrapping up ..."))
            messages = agentmake(
                messages,
                system="write_final_answer",
                follow_up_prompt=f"""# Instruction
Please provide me with the final answer to my original request based on the work that has been completed.

# Original Request
{user_request}""",
                stream=True,
            )
            messages[-1]["content"] = fix_string(messages[-1]["content"])
            console.rule()
            console.print(Markdown(messages[-1]['content']))

            # Backup
            print()
            backup_conversation(messages, master_plan, console)

            if args.exit:
                break

if __name__ == "__main__":
    asyncio.run(main())
