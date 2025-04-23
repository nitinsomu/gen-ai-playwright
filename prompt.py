def generate_playwright_prompt(instruction: str, dom: str) -> str:
    try:
        if not instruction or not isinstance(instruction, str):
            raise ValueError("Instruction must be a non-empty string.")
        if not dom or not isinstance(dom, str):
            raise ValueError("DOM must be a non-empty string.")
        
        return f"""
        instruction: 
        '{instruction}' 
        
        on the given 
    
        DOM: 
        '{dom}'

        Ensure that response contains only 1 line of playwright code in python, without the boilerplate code.
        """
    
    except Exception as e:
        return f"An error occurred: {str(e)}"