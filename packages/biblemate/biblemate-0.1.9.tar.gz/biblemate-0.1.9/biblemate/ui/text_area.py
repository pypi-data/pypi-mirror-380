from biblemate import config
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import Frame, Label
from prompt_toolkit.styles import Style, merge_styles
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
from prompt_toolkit.widgets import Frame, TextArea
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.layout import WindowAlign
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.markup import MarkdownLexer
from prompt_toolkit.styles import style_from_pygments_cls
from pygments.styles import get_style_by_name


async def getTextArea(input_suggestions:list=None, default_entry="", multiline:bool=True):
    """Get text area input with a border frame"""
    
    completer = FuzzyCompleter(WordCompleter(input_suggestions, ignore_case=True)) if input_suggestions else None
    
    # Markdown
    pygments_style = get_style_by_name('github-dark')
    markdown_style = style_from_pygments_cls(pygments_style)
    # Define custom style
    custom_style = Style.from_dict({
        #'frame.border': '#00ff00',  # Green border
        #'frame.label': '#ffaa00 bold',  # Orange label
        #'completion-menu': 'bg:#008888 #ffffff',
        #'completion-menu.completion': 'bg:#008888 #ffffff',
        #'completion-menu.completion.current': 'bg:#00aaaa #000000',
        #"status": "reverse",
        "textarea": "bg:#1E1E1E",
    })

    style = merge_styles([markdown_style, custom_style])

    # TextArea with a completer
    text_area = TextArea(
        text=default_entry,
        style="class:textarea",
        lexer=PygmentsLexer(MarkdownLexer),
        multiline=multiline,
        scrollbar=True,
        completer=completer,         # <-- attach completer here
        complete_while_typing=False,       # only trigger when requested
        focus_on_click=True,
        wrap_lines=True,
    )

    # Layout: include a CompletionsMenu
    root_container = HSplit(
        [
            Frame(
                text_area,
                #title="Type here",
            ),
            Label(
                "[Ctrl+S] Send [Ctrl+K] Help",
                align=WindowAlign.RIGHT,
                style="fg:grey",
            ),
            CompletionsMenu(
                max_height=8,
                scroll_offset=1,
            ),
        ]
    )
    
    # Create key bindings
    bindings = KeyBindings()
    
    # submit
    @bindings.add("escape", "enter")
    @bindings.add("c-s")
    def _(event):
        if text_area.text.strip():
            event.app.exit(result=text_area.text.strip())
    # submit or new line
    @bindings.add("enter")
    @bindings.add("c-m")
    def _(event):
        entry = text_area.text.strip()
        if not multiline or (entry.startswith(".") and entry in input_suggestions) or entry.startswith(".open ") or entry.startswith(".load "):
            event.app.exit(result=text_area.text.strip())
        else:
            text_area.buffer.newline()
    # help
    @bindings.add("c-k")
    def _(event):
        event.app.exit(result=".help")
    # launch editor
    @bindings.add("c-e")
    @bindings.add("c-p")
    def _(event):
        config.current_prompt = text_area.text
        event.app.exit(result=".editprompt")
    # new chat
    @bindings.add("c-n")
    def _(event):
        event.app.exit(result=".new")
    # exit
    @bindings.add("c-q")
    def _(event):
        event.app.exit(result=".exit")
    # insert four spaces
    @bindings.add("s-tab")
    def _(event):
        buffer = event.app.current_buffer if event is not None else text_area.buffer
        buffer.insert_text("    ")
    # trigger completion
    @bindings.add("tab")
    @bindings.add("c-i")
    def _(event):
        buffer = event.app.current_buffer if event is not None else text_area.buffer
        buffer.start_completion()
    # close completion menu
    @bindings.add("escape")
    def _(event):
        buffer = event.app.current_buffer if event is not None else text_area.buffer
        buffer.cancel_completion()
    # undo
    @bindings.add("c-z")
    def _(event):
        buffer = event.app.current_buffer if event is not None else text_area.buffer
        buffer.undo()
    # reset buffer
    @bindings.add("c-r")
    def _(event):
        buffer = event.app.current_buffer if event is not None else text_area.buffer
        buffer.reset()
    # Create application
    app = Application(
        layout=Layout(root_container, focused_element=text_area),
        key_bindings=bindings,
        enable_page_navigation_bindings=True,
        style=style,
        #clipboard=PyperclipClipboard(), # not useful if mouse_support is not enabled
        #mouse_support=True, # If enabled; content outside the app becomes unscrollable
        full_screen=False,
    )
    
    # Run async
    result = await app.run_async()
    
    return result

