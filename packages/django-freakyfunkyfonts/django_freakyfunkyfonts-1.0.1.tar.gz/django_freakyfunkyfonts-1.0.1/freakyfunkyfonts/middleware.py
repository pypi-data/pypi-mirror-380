from bs4 import BeautifulSoup
import random
from .settings import load_config

class FreakyFunkyFontsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.config = load_config()

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_response(request, response)

    def process_response(self, request, response):
        content_type = response.get("Content-Type", "")
        if "text/html" not in content_type:
            return response

        soup = BeautifulSoup(response.content, "html.parser")

        # Inject extra tags if configured
        inject_tags = self.config["inject"].get("tags", [])
        if soup.head and inject_tags:
            for tag_html in inject_tags:
                # don’t duplicate if already present
                if not soup.head.find(lambda t: str(t) == tag_html):
                    soup.head.append(BeautifulSoup(tag_html, "html.parser"))

        skip_tags = set(self.config["behaviour"]["skip_tags"])
        fonts = self.config["fonts"]["pool"]

        for text_node in soup.find_all(string=True):
            if text_node.parent.name in skip_tags:
                continue
            new_html = "".join(
                f'<span style="font-family:{random.choice(fonts)}">{c}</span>'
                if c.strip() else c
                for c in text_node
            )
            text_node.replace_with(BeautifulSoup(new_html, "html.parser"))

        response.content = str(soup)
        response["Content-Length"] = len(response.content)
        return response
