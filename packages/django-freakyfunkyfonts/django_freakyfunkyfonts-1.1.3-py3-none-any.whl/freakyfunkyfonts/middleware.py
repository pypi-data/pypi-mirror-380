from bs4 import BeautifulSoup, NavigableString, Comment
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

        original_content = response.content.decode(response.charset or 'utf-8')
        soup = BeautifulSoup(original_content, "html.parser")

        # Inject extra tags if configured
        inject_tags = self.config["inject"].get("tags", [])
        if soup.head and inject_tags:
            for tag_html in inject_tags:
                if tag_html not in str(soup.head):
                    tag_soup = BeautifulSoup(tag_html, "html.parser")
                    for tag in tag_soup:
                        soup.head.append(tag)

        skip_tags = set(self.config["behaviour"]["skip_tags"])
        fonts = self.config["fonts"]["pool"]
        scopes = self.config["behaviour"].get("scopes", ["all"])

        # Determine roots to operate on
        roots = []
        if "all" in scopes:
            roots = [soup.body] if soup.body else [soup]
        else:
            for scope in scopes:
                if scope == "body" and soup.body:
                    roots.append(soup.body)
                else:
                    roots.extend(soup.find_all(scope))

        # Process text nodes
        for root in roots:
            self._process_element(root, skip_tags, fonts, soup)

        # Use decode() with formatter to preserve structure
        response.content = soup.encode(formatter="minimal")
        response["Content-Length"] = len(response.content)
        return response

    def _process_element(self, element, skip_tags, fonts, soup):
        """Recursively process element and its children"""
        # Skip if this tag should be ignored
        if hasattr(element, 'name') and element.name in skip_tags:
            return

        # Get children as a list since we'll be modifying during iteration
        children = list(element.children) if hasattr(element, 'children') else []
        
        for child in children:
            if isinstance(child, NavigableString) and not isinstance(child, Comment):
                # This is a plain text node (not a comment)
                text = str(child)
                if text.strip():  # Has non-whitespace content
                    new_elements = []
                    for c in text:
                        if c.strip():  # Character is not whitespace
                            font = random.choice(fonts)
                            span = soup.new_tag("span")
                            span['style'] = f"font-family:{font}"
                            span.string = c
                            new_elements.append(span)
                        else:
                            # Preserve whitespace
                            new_elements.append(NavigableString(c))
                    
                    # Replace text with spans
                    for new_el in reversed(new_elements):
                        child.insert_after(new_el)
                    child.extract()
            elif hasattr(child, 'name'):
                # Recurse into child tags
                self._process_element(child, skip_tags, fonts, soup)