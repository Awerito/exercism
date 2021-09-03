import re

# Some more RegEx for future improvement
# '~~(.*?)~~'                              # s
# '^((?:[ ]{1,}|\t{1,})?-) (?!\[.\])(.*)'  # tab list
# '(?<!\()https?:\/\/[a-zA-Z0-9$-_@.&+]+'  # a
# '[^!]\[(.*?)\]\((.*?)\)'                 # a
# '!\[(.*?)\]\((.*?)\)'                    # img
# '^((?:> .*[\n]?)+)'                      # blockquote
# '^((?:(?:[ ]{4}|\t).*[\n]?)+)'           # codeblock by tabs
# '(```[^`\n][^```]*```)'                  # codeblock by ``` without syntax selector
# '(^```[^```]*\n```)'                     # codeblock by ``` with syntax selector
# '(`[^`]*`)'                              # inline code


def parse(markdown):
    # <h{n}>{text}</h{n}>
    parsed_html = re.sub(
        r"^(#{1,6}) (\S.*)",
        lambda x: f"<h{len(x.group(1))}>{x.group(2)}</h{len(x.group(1))}>",
        markdown,
        flags=re.M,
    )
    # <li>{text}</li>
    parsed_html = re.sub(
        r"^((?:[ ]{1,}|\t{1,})?[-*]) (?!\[.\])(.*)",
        r"<li>\2</li>",
        parsed_html,
        flags=re.M,
    )
    # <strong>{text}</strong>
    parsed_html = re.sub(r"(\*\*|__)(.*)\1", r"<strong>\2</strong>", parsed_html)
    # <em>{text}</em>
    parsed_html = re.sub(r"(\*|_)(.*)\1", r"<em>\2</em>", parsed_html)

    # <ul> and <p> elements
    in_ul = False
    lines = list()
    previous = str()
    for line in parsed_html.split("\n"):
        if not re.search(r"^<[^strong|em].*?>", line):
            line = "<p>" + line + "</p>"

        li = line.startswith("<li>")
        if not in_ul and li:
            in_ul = True
            line = "<ul>" + line
        elif in_ul and li:
            previous = line
        elif in_ul:
            in_ul = False
            previous = previous + "</ul>"
            lines.pop()
            lines.append(previous)
        lines.append(line)

    parsed_html = "\n".join(lines)
    parsed_html = parsed_html.replace(">\n<", "><")  # I going to remove this later

    if parsed_html.endswith("</li>"):
        return parsed_html + "</ul>"
    return parsed_html
