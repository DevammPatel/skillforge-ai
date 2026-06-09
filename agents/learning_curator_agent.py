import os


class LearningCuratorAgent:

    def __init__(self):
        self.docs_path = "knowledge_base"

    def get_learning_material(self):

        content = ""

        for file in os.listdir(self.docs_path):

            if file.endswith(".md"):

                with open(
                    os.path.join(
                        self.docs_path,
                        file
                    ),
                    "r"
                ) as f:

                    content += f.read()

                    content += "\n\n"

        return content