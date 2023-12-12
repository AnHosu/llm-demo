def prompt_complaint(prompt: str) -> str:
    """
    Modified prompt for summarising a single complaint.
    """
    modified_prompt = f"""
    We recieve a lot of angry mails from customers complaining about defective
    glassware that we manufactured and sold. Please summarize the complaint.
    Focus on idenitfying whether the glassware is chipped, has impurities,
    is the wrong color, or is smelly.

    Here is the text inside <text><\text> XML tags.

    <text> {prompt} <\text>
    """
    return modified_prompt.encode("unicode_escape").decode("utf-8")


def prompt_complaints(prompt: str, additional_prompt: str = None) -> str:
    if additional_prompt is None:
        additional_prompt = ""
    """
    Modified propmt for summarising multiple complaints.
    """
    modified_prompt = f"""
    We recieve a lot of angry mails from customers complaining about defective
    glassware that we manufactured and sold. Please summarize allthe
    complaints below.
    Focus on idenitfying whether the glassware pieces were chipped, had
    impurities, were the wrong color, or were smelly.

    Here is the text inside <text><\text> XML tags.

    <text> {prompt} {additional_prompt}<\text>
    """
    return modified_prompt.encode("unicode_escape").decode("utf-8")
