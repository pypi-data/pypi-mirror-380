from agentmake.main import AGENTMAKE_USER_DIR
from agentmake.utils.system import getCliOutput
from prompt_toolkit.validation import Validator, ValidationError
from biblemate import config
from pathlib import Path
import os, shutil, re


class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not re.search("^[0-9]+?$", text):
            i = 0

            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='This entry accepts numbers only!', cursor_position=i)

async def getInput(prompt:str="> ", input_suggestions:list=None, number_validator:bool=False, default_entry=""):
    """
    Prompt for user input
    """
    # place import lines here to work with stdin
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
    from prompt_toolkit.key_binding import KeyBindings
    bindings = KeyBindings()
    # launch editor
    @bindings.add("c-p")
    def _(event):
        buffer = event.app.current_buffer
        config.current_prompt = buffer.text
        buffer.text = ".editprompt"
        buffer.validate_and_handle()
    # new chat
    @bindings.add("c-n")
    def _(event):
        buffer = event.app.current_buffer
        buffer.text = ".new"
        buffer.validate_and_handle()
    # quit
    @bindings.add("c-q")
    def _(event):
        buffer = event.app.current_buffer
        buffer.text = ".quit"
        buffer.validate_and_handle()
    # copy text to clipboard
    @bindings.add("c-c")
    def _(event):
        try:
            buffer = event.app.current_buffer
            data = buffer.copy_selection()
            copyText = data.text
            if shutil.which("termux-clipboard-set"):
                from pydoc import pipepager
                pipepager(copyText, cmd="termux-clipboard-set")
            else:
                import pyperclip
                pyperclip.copy(copyText)
        except:
            pass
    # paste clipboard text
    @bindings.add("c-v")
    def _(event):
        try:
            import pyperclip
            buffer = event.app.current_buffer
            buffer.cut_selection()
            clipboardText = getCliOutput("termux-clipboard-get") if shutil.which("termux-clipboard-get") else pyperclip.paste()
            buffer.insert_text(clipboardText)
        except:
            pass
    # insert new line
    @bindings.add("c-i")
    def _(event):
        event.app.current_buffer.newline()
    # reset buffer
    @bindings.add("c-z")
    def _(event):
        event.app.current_buffer.reset()
    # go to the beginning of the text
    @bindings.add("escape", "a")
    def _(event):
        event.app.current_buffer.cursor_position = 0
    # go to the end of the text
    @bindings.add("escape", "z")
    def _(event):
        buffer = event.app.current_buffer
        buffer.cursor_position = len(buffer.text)
    # go to current line starting position
    @bindings.add("home")
    @bindings.add("escape", "b")
    def _(event):
        buffer = event.app.current_buffer
        buffer.cursor_position = buffer.cursor_position - buffer.document.cursor_position_col
    # go to current line ending position
    @bindings.add("end")
    @bindings.add("escape", "e")
    def _(event):
        buffer = event.app.current_buffer
        buffer.cursor_position = buffer.cursor_position + buffer.document.get_end_of_line_position()

    log_file = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "logs", "requests")
    session = PromptSession(history=FileHistory(log_file))
    completer = FuzzyCompleter(WordCompleter(input_suggestions, ignore_case=True)) if input_suggestions else None
    instruction = await session.prompt_async(
        prompt,
        bottom_toolbar="[ENTER] submit [TAB] linebreak [Ctrl+N] new [Ctrl+Q] quit",
        completer=completer,
        key_bindings=bindings,
        validator=NumberValidator() if number_validator else None,
        default=default_entry if default_entry else "",
    )
    print()
    return instruction.strip() if instruction else ""