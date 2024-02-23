import csv

class Models:
    def __init__(self, filename='model_info.csv'):
        self.filename = filename
        self.model_info_list = []
        self._parse_model_info()

    def _parse_model_info(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Ignore empty lines
                        model_name, input_rate, output_rate, description = map(str.strip, row)
                        model_info = {
                            'model_name': model_name,
                            'input_rate': float(input_rate),
                            'output_rate': float(output_rate),
                            'description': description
                        }
                        self.model_info_list.append(model_info)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def names(self):
        return [model['model_name'] for model in self.model_info_list if 'model_name' in model]
