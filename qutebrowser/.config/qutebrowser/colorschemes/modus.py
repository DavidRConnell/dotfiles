def draw(c, options={}):
    palette = {
        "background": "#ffffff",
        "background-alt": "#f0f0f0",
        "background-attention": "#d7d7d7",
        "border": "#ffffff",
        "current-line": "#d7d7d7",
        "selection": "#d7d7d7",
        "foreground": "#000000",
        "foreground-alt": "#505050",
        "foreground-attention": "#0a0a0a",
        "comment": "#404148",
        "cyan": "#00538b",
        "green": "#005e00",
        "blue": "#0031a9",
        "magenta": "#721045",
        "red": "#a60000",
        "yellow": "#813e00",
    }

    spacing = options.get("spacing", {"vertical": 5, "horizontal": 5})

    padding = options.get(
        "padding",
        {
            "top": spacing["vertical"],
            "right": spacing["horizontal"],
            "bottom": spacing["vertical"],
            "left": spacing["horizontal"],
        },
    )

    font = options.get(
        "font",
        {
            "family": '"nerd hack font", Menlo, "xos4 Terminus", Terminus, Monospace, Monaco, "Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Consolas, Terminal',
            "size": 10,
        },
    )

    monospace = font.get(
        "family",
        '"nerd hack font", Menlo, "xos4 Terminus", Terminus, Monospace, Monaco, "Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Consolas, Terminal',
    )
    font_size = font.get("size", 10)

    ## Background color of the completion widget category headers.
    c.colors.completion.category.bg = palette["background"]

    ## Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = palette["border"]

    ## Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = palette["border"]

    ## Foreground color of completion widget category headers.
    c.colors.completion.category.fg = palette["foreground"]

    ## Background color of the completion widget for even rows.
    c.colors.completion.even.bg = palette["background"]

    ## Background color of the completion widget for odd rows.
    c.colors.completion.odd.bg = palette["background-alt"]

    ## Text color of the completion widget.
    c.colors.completion.fg = palette["foreground"]

    ## Background color of the selected completion item.
    c.colors.completion.item.selected.bg = palette["selection"]

    ## Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = palette["selection"]

    ## Top border color of the completion widget category headers.
    c.colors.completion.item.selected.border.top = palette["selection"]

    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = palette["foreground"]

    ## Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = palette["magenta"]

    ## Color of the scrollbar in completion view
    c.colors.completion.scrollbar.bg = palette["background"]

    ## Color of the scrollbar handle in completion view.
    c.colors.completion.scrollbar.fg = palette["foreground"]

    ## Background color for the download bar.
    c.colors.downloads.bar.bg = palette["background"]

    ## Background color for downloads with errors.
    c.colors.downloads.error.bg = palette["background"]

    ## Foreground color for downloads with errors.
    c.colors.downloads.error.fg = palette["red"]

    ## Color gradient stop for download backgrounds.
    c.colors.downloads.stop.bg = palette["background"]

    ## Color gradient interpolation system for download backgrounds.
    ## Type: ColorSystem
    ## Valid values:
    ##   - rgb: Interpolate in the RGB color system.
    ##   - hsv: Interpolate in the HSV color system.
    ##   - hsl: Interpolate in the HSL color system.
    ##   - none: Don't show a gradient.
    c.colors.downloads.system.bg = "none"
    c.colors.downloads.start.fg = palette["background"]
    c.colors.downloads.stop.fg = palette["foreground"]

    ## Background color for hints. Note that you can use a `rgba(...)` value
    ## for transparency.
    c.colors.hints.bg = palette["background"]

    ## Font color for hints.
    c.colors.hints.fg = palette["foreground"]

    ## Hints
    c.hints.border = "1px solid " + palette["foreground"]

    ## Font color for the matched part of hints.
    c.colors.hints.match.fg = palette["selection"]

    ## Background color of the keyhint widget.
    c.colors.keyhint.bg = palette["background"]

    ## Text color for the keyhint widget.
    c.colors.keyhint.fg = palette["foreground"]

    ## Highlight color for keys to complete the current keychain.
    c.colors.keyhint.suffix.fg = palette["foreground"]

    ## Background color of an error message.
    c.colors.messages.error.bg = palette["background"]

    ## Border color of an error message.
    c.colors.messages.error.border = palette["background-alt"]

    ## Foreground color of an error message.
    c.colors.messages.error.fg = palette["red"]

    ## Background color of an info message.
    c.colors.messages.info.bg = palette["background"]

    ## Border color of an info message.
    c.colors.messages.info.border = palette["background-alt"]

    ## Foreground color an info message.
    c.colors.messages.info.fg = palette["foreground-alt"]

    ## Background color of a warning message.
    c.colors.messages.warning.bg = palette["background"]

    ## Border color of a warning message.
    c.colors.messages.warning.border = palette["background-alt"]

    ## Foreground color a warning message.
    c.colors.messages.warning.fg = palette["red"]

    ## Background color for prompts.
    c.colors.prompts.bg = palette["background"]

    # ## Border used around UI elements in prompts.
    c.colors.prompts.border = "1px solid " + palette["background-alt"]

    ## Foreground color for prompts.
    c.colors.prompts.fg = palette["cyan"]

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.bg = palette["selection"]

    ## Background color of the statusbar in caret mode.
    c.colors.statusbar.caret.bg = palette["background"]

    ## Foreground color of the statusbar in caret mode.
    c.colors.statusbar.caret.fg = palette["magenta"]

    ## Background color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.bg = palette["background"]

    ## Foreground color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.fg = palette["magenta"]

    ## Background color of the statusbar in command mode.
    c.colors.statusbar.command.bg = palette["background"]

    ## Foreground color of the statusbar in command mode.
    c.colors.statusbar.command.fg = palette["cyan"]

    ## Background color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.bg = palette["background"]

    ## Foreground color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.fg = palette["foreground-alt"]

    ## Background color of the statusbar in insert mode.
    c.colors.statusbar.insert.bg = palette["background-attention"]

    ## Foreground color of the statusbar in insert mode.
    c.colors.statusbar.insert.fg = palette["foreground-attention"]

    ## Background color of the statusbar.
    c.colors.statusbar.normal.bg = palette["background"]

    ## Foreground color of the statusbar.
    c.colors.statusbar.normal.fg = palette["foreground"]

    ## Background color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.bg = palette["background"]

    ## Foreground color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.fg = palette["magenta"]

    ## Background color of the statusbar in private browsing mode.
    c.colors.statusbar.private.bg = palette["background-alt"]

    ## Foreground color of the statusbar in private browsing mode.
    c.colors.statusbar.private.fg = palette["foreground-alt"]

    ## Background color of the progress bar.
    c.colors.statusbar.progress.bg = palette["background"]

    ## Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = palette["red"]

    ## Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = palette["foreground"]

    ## Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = palette["cyan"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.http.fg = palette["green"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.https.fg = palette["green"]

    ## Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = palette["yellow"]

    ## Status bar padding
    c.statusbar.padding = padding

    ## Background color of the tab bar.
    ## Type: QtColor
    c.colors.tabs.bar.bg = palette["selection"]

    ## Background color of unselected even tabs.
    ## Type: QtColor
    c.colors.tabs.even.bg = palette["selection"]

    ## Foreground color of unselected even tabs.
    ## Type: QtColor
    c.colors.tabs.even.fg = palette["foreground"]

    ## Color for the tab indicator on errors.
    ## Type: QtColor
    c.colors.tabs.indicator.error = palette["red"]

    ## Color gradient start for the tab indicator.
    ## Type: QtColor
    c.colors.tabs.indicator.start = palette["magenta"]

    ## Color gradient end for the tab indicator.
    ## Type: QtColor
    c.colors.tabs.indicator.stop = palette["green"]

    ## Color gradient interpolation system for the tab indicator.
    ## Type: ColorSystem
    ## Valid values:
    ##   - rgb: Interpolate in the RGB color system.
    ##   - hsv: Interpolate in the HSV color system.
    ##   - hsl: Interpolate in the HSL color system.
    ##   - none: Don't show a gradient.
    c.colors.tabs.indicator.system = "none"

    ## Background color of unselected odd tabs.
    ## Type: QtColor
    c.colors.tabs.odd.bg = palette["selection"]

    ## Foreground color of unselected odd tabs.
    ## Type: QtColor
    c.colors.tabs.odd.fg = palette["foreground"]

    # ## Background color of selected even tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.even.bg = palette["background"]

    # ## Foreground color of selected even tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.even.fg = palette["foreground"]

    # ## Background color of selected odd tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.odd.bg = palette["background"]

    # ## Foreground color of selected odd tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.odd.fg = palette["foreground"]

    ## Tab padding
    c.tabs.padding = padding
    c.tabs.indicator.width = 1
    c.tabs.favicons.scale = 1

    # Fonts
    font_size_str = str(font_size) + "pt"
    font_size_small_str = str(font_size - 1) + "pt"

    c.fonts.completion.entry = font_size_str + " monospace"
    c.fonts.completion.category = "bold"
    c.fonts.debug_console = font_size_str + " monospace"
    c.fonts.downloads = font_size_str + " monospace"
    c.fonts.hints = font_size_small_str + " monospace"
    c.fonts.keyhint = font_size_str + " monospace"
    c.fonts.messages.error = font_size_str + " monospace"
    c.fonts.messages.info = font_size_str + " monospace"
    c.fonts.messages.warning = font_size_str + " monospace"
    c.fonts.prompts = font_size_str + " monospace"
    c.fonts.statusbar = font_size_small_str + " monospace"
    # c.fonts.tabs = font_size_str + " monospace"
    c.fonts.web.family.standard = ""
    c.fonts.web.family.fixed = ""
    c.fonts.web.family.serif = ""
    c.fonts.web.family.sans_serif = ""
    c.fonts.web.family.cursive = ""
    c.fonts.web.family.fantasy = ""
    c.fonts.web.size.default = 16
    c.fonts.web.size.default_fixed = 13
    c.fonts.web.size.minimum = 0
    c.fonts.web.size.minimum_logical = 6
