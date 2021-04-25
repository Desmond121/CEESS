import base64
import json
from json import encoder

if __name__ == "__main__":
    data = {1: {1: 80, 2: 90}}
    jsonStr = json.dumps(data)
    print("jsonStr: " + jsonStr)
    encode = base64.standard_b64encode(jsonStr.encode()).decode()
    print(encode)

    decode = base64.standard_b64decode(encode.encode()).decode()
    print(decode)