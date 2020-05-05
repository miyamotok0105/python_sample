import time
from tqdm import tqdm

class MockModel():
    def prepare(self):
        return "prepared!"

    def Web_single_pattern_predict(self):
        #https://mercari.github.io/ml-system-design-pattern/Serving-patterns/Web-single-pattern/design_ja.html
        return "Web_single_pattern_predict!"

    def predict_synchronous_pattern(self):
        #https://mercari.github.io/ml-system-design-pattern/Serving-patterns/Synchronous-pattern/design_ja.html
        for i in tqdm(range(2)):
            time.sleep(1)
        return "predict_synchronous_pattern!"


