#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:15:58 2024

@author: yl


- [`.chat.md` format](mxlm/chatmd_utils.py):
    - A multi-turn dialogue format based on markdown, capable of converting to and from OpenAI messages JSON.
    - Modify and annotate multi-turn dialogue data using your favorite editor.
    - Maintain MD format, what you see is what you get while editing.

```markdown
<!--<|BOT|>--><hr></hr><hr></hr> Here you can put the `tag`, must be one line. Could be str or JSON.
## system
You are a helpful assistant.

<!--<|BOT|>--><hr></hr><hr></hr>
## user
Summarize the content in this url:
https://XXX.html

<!--<|BOT|>--><hr></hr><hr></hr> {"url":"XXX.html", "title":"XXX"}
## system
Text from url https://XXX.html: ...

<!--<|BOT|>--><hr></hr><hr></hr>
## comment
Multi-line comments.
Visible to humans but invisible to models.
```
"""
import re
import json

chatmd_temple = """\n\n<!--<|BOT|>--><hr></hr><hr></hr> {tag}
## {role}
{content}"""


def messages_to_chatmd(messages):
    md = ""
    for msg in messages:
        msg_ = {k: msg.get(k, "") for k in ["tag", "role", "content"]}
        if isinstance(msg_["tag"], (dict, list, tuple)):
            msg_["tag"] = json.dumps(msg_["tag"], ensure_ascii=False)
        md += chatmd_temple.format(**msg_)
    return md


def chatmd_to_messages(chatmd, rstrip_content=True):
    """
    Parameters
    ----------
    rstrip_content : bool, optional
        The default is True, for last dialogue may has many '\n'.
        Only strip right '\n'.

    Returns
    -------
    messages
    """
    pattern = re.compile(
        r"<!--<\|BOT\|>--><hr></hr><hr></hr> *(?P<tag>.*?) *\n##  ?(?P<role>\w*?) *\n(?P<content>.+?)"  # content
        "(?=\n<!--<\|BOT\|>--><hr></hr><hr></hr>|$)",
        re.DOTALL,
    )

    messages = []
    for match in pattern.finditer(chatmd):
        content = match.group("content")  # .strip()
        if rstrip_content:
            content = content.rstrip("\n")
        if content.endswith("\n"):
            content = content[:-1]
        msg = {
            "role": match.group("role"),
            "content": content,
        }
        tag = match.group("tag")
        if tag:
            # Revert to json if tag is json
            is_dict = tag[0] == "{" and tag[-1] == "}" and ":" in tag
            is_list = tag[0] == "[" and tag[-1] == "]"
            if is_dict or is_list:
                tag = json.loads(tag)
            msg["tag"] = tag
        messages.append(msg)
    return messages


if __name__ == "__main__":
    import tempfile

    chatmd_example = """<!--<|BOT|>--><hr></hr><hr></hr> Here you can put the `tag`, must be one line. Could be str or JSON.
## system
You are a helpful assistant.

<!--<|BOT|>--><hr></hr><hr></hr>
## user  
Summarize the content in this url: 
https://XXX.html

<!--<|BOT|>--><hr></hr><hr></hr> {"url":"XXX.html", "title":"XXX"}
## context
{text from url}

<!--<|BOT|>--><hr></hr><hr></hr>
## comment
Multi-line comments.  
Visible to humans but invisible to models.
"""
    msgs = chatmd_to_messages(chatmd_example)
    for msg in msgs:
        print(msg)

    chatmd = messages_to_chatmd(msgs)
    print(chatmd)

    md_path = tempfile.mktemp() + ".md"
    open(md_path, "w").write(chatmd)
    print("Save chatmd to:", md_path)
