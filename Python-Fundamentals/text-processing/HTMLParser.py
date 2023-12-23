# HTML Parser
import re


def title_data(html_data):
    pattern = "<title>.+</title>"
    result = re.findall(pattern, html_data)
    return result[0]


def body_data(html_data):
    pattern = "<body>.+</body>"
    result = re.findall(pattern, html_data)
    return result[0]


def extract_title(title_tag):
    pattern = ">.+<"
    result = re.sub(r"\\n", "", title_tag)
    result = re.findall(pattern, result)
    return result[0][1:-1]


def extract_body(body_tag):
    pattern = ">.*?<"
    result = re.sub(r"\\n", "", body_tag)
    result = [x[1: -1].strip() for x in re.findall(pattern, result) if len(x) > 2]
    print(result)
    return " ".join(result)


def call_functions():
    html_data = input()
    title_tag = title_data(html_data)
    body_tag = body_data(html_data)
    title = extract_title(title_tag)
    body = extract_body(body_tag)
    print(f"Title: {title}")
    print(f"Content: {body}")


if __name__ == "__main__":
    call_functions()
