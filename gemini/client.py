import google.generativeai as genai


def get_car_description(model, brand, model_year):
    genai.configure(api_key="AIzaSyA2zUj7j97jbhd3SWBZr72UvklB_icVGAE")
    prompt = f"Gere uma descrição de venda de carro com até 250 caracteres para um {brand} {model} {model_year}. Descreva especificações técnicas desse modelo de carro."

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()