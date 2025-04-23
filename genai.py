from playwright.sync_api import Page
from domSnapshot import get_page_dom
from sanitizeHtml import sanitize_html
from prompt import generate_playwright_prompt   
from instruction import get_ollama_response

def generateTest(instruction: str, page: Page):

    """
    Generates and executes a test case for the given instruction and Playwright page object.

    Args:
        instruction (str): The instruction to generate a test case for.
        page (Page): The Playwright page object.

    Returns:
        str: The generated test case.
    """
    try:
        # Check if instruction is a non-empty string
        if not instruction or not isinstance(instruction, str):
            raise ValueError("Instruction must be a non-empty string.")
        
        # Get the DOM of the page
        domSnapshot = get_page_dom(page)
        # print(domSnapshot)
        sanitizedDomSnapshot = sanitize_html(domSnapshot)
        # print(sanitizedDomSnapshot)
        # Generate the test case using the instruction and DOM
        prompt = generate_playwright_prompt(instruction, sanitizedDomSnapshot)
        # print(prompt)
        # Get the instruction from the Ollama model
        code = get_ollama_response(prompt)
        print("Instruction: ", instruction)
        print("Generated Code: ", code) 
        if(isinstance(code, str)):
            exec(code, {'page': page})
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
