import json
import base64
import concurrent.futures


class SMAPI(object):
    quippets_uri = "/queries/"
    base_file_path = './data.json'
    post_file_path= './post.json'
    
    def __init__(self):
        self.client = None  # Assuming SRIClient is not used in this context

    def get_website_data(self, data):
        """Get website data from JSON."""
        return data.get('website_data', {})

    def get_social_links(self, data):
        """Get social links from JSON."""
        return data.get('social_links', [])

    def get_locations(self, data):
        """Get locations from JSON."""
        return data.get('locations', [])

    def get_stores_data(self, data):
        """Get stores data from JSON."""
        return data.get('stores', [])
    
    @staticmethod
    def read_json_file(file_path):
        """Retrieve JSON data from a file and return it as a Python dictionary."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format"}

    # Base method to call specified JSON method
    def call_json_method(self, method_name):
        """Call the specified method with data from the JSON file and return the result as a dictionary."""
        json_data = self.read_json_file(file_path=self.base_file_path)
        if "error" in json_data:
            return json_data
        
        method = getattr(self, method_name, None)
        if not method or not callable(method):
            return {"error": f"Method {method_name} not found"}
        
        return method(json_data)
    
    # Save new data into JSON file without replacing old data
    def save_emp_conversations(self, data):
        def save_to_json():
            existing_data = self.read_json_file(self.post_file_path)
            msg_data = existing_data.copy()  # Start with existing data

            # Remove captcha fields if present
            data.pop('captcha_0', None)
            data.pop('captcha_1', None)

            # Process new data
            for item in list(data):
                if 'filer' in str(type(data[item])):
                    with open(data[item].path, 'rb') as f:
                        file_loaded = base64.b64encode(f.read()).decode('utf-8')
                        file_name = data[item].name
                    data[item].delete()
                    msg_data.setdefault('file_contents', []).append(file_loaded)
                    msg_data.setdefault('file_name', []).append(file_name)
                elif data[item] not in ['', None]:
                    current_value = msg_data.setdefault(item, [])
                    if not isinstance(current_value, list):
                        current_value = [current_value]  # Convert to list if not already a list
                    current_value.append(data[item])
                    msg_data[item] = current_value

            # Save merged data to post.json
            try:
                with open(self.post_file_path, 'w') as json_file:
                    json.dump(msg_data, json_file)
                return 200  # Success status code
            except Exception as e:
                print(f"Error saving data to post.json: {e}")
                return 500  # Error status code

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(save_to_json)
            return future.result()






    




# Example usage:
# api = SMAPI()

# website_data = api.call_json_method('get_website_data')