import csv

class Model:
    def __init__(self, model_name, input_rate, output_rate, description):
        self.model_name = model_name
        self.input_rate = input_rate
        self.output_rate = output_rate
        self.description = description

class Models:
    def __init__(self, filename='model_info.csv'):
        self.filename = filename
        self.model_list = []
        self._parse_model_info()

    def _parse_model_info(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Ignore empty lines
                        model_name, input_rate, output_rate, description = map(str.strip, row)
                        model = Model(model_name, float(input_rate), float(output_rate), description)
                        self.model_list.append(model)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def names(self):
        return [model.model_name for model in self.model_list]

    def get_model(self, model_name):
        for model in self.model_list:
            if model.model_name == model_name:
                return model
        return None

    def getInputRate(self, model_name):
        model = self.get_model(model_name)
        if model:
            return model.input_rate
        else:
            return None
