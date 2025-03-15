import os
import json

class JsonFileFactory:
    def write_data(self, arr_data, filename):
        dir_name = os.path.dirname(filename)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        json_string = json.dumps(
            [item.__dict__ if hasattr(item, '__dict__') else item for item in arr_data],
            default=str, indent=4, ensure_ascii=False
        )

        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json_string or "[]")  # Nếu chuỗi JSON rỗng thì ghi "[]"

    def read_data(self, filename, ClassName):
        """
        Đọc file JSON và chuyển thành danh sách object.
        :param filename: Đường dẫn file JSON.
        :param ClassName: Lớp cần chuyển đổi dữ liệu.
        :return: Danh sách object hoặc danh sách rỗng nếu file không tồn tại.
        """
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            arr_data = json.loads(file.read(), object_hook=lambda d: ClassName(**{k.strip(): v.strip() if isinstance(v, str) else v for k, v in d.items()}))


        return arr_data
