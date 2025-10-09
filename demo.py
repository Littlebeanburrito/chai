import json

class User:
    def _init_(self, user_id, username, roles):
        self.id = user_id
        self.name = username
        self.roles = roles
        self.is_active = True
    def __repr__(self):
        return f"<User id={self.id} name={self.name} roles={self.roles}>"
def demontrate_json():
    user_data_dict = {
        "id": 101,
        "name": "tom",
        "roles": ["viewer", "Commenter"],
        "is_active": True
    }

    print(f"Original Python dictionary {user_data_dict}")

    js_string = json.dumps(user_data_dict, indent=4)

    file_path = "new_file.json"

    with open(file_path, "w") as file:
        json.dump(user_data_dict, file, indent=4)

    with open(file_path, "r") as file:
        loaded_json = json.load(file)