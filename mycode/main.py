from mycode.utils import translate

def english_to_pirate():
    input_element = Element("english")
    output_element = Element("output")

    english = input_element.element.value
    pirate = translate(english)
    
    output_element.element.innerText = pirate
