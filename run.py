# Main python file running the whole application. Not part of Taskmanager.

# os - for use of environment variables.
import os
# app variable defined in __init__.py file.
from taskmanager import app

# where and how to run application. Takes 3 arguments.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        # PORT needs to be an integer.
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
