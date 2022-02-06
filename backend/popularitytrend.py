from Arxiv import Arxiv
from datetime import datetime
import pandas as pd
import numpy as np

def get_trend(documents):
    pub_years = [int(doc.published[:4]) for doc in documents]
    year_dict = dict()
    for year in pub_years:
        year_dict[year] = year_dict.get(year, 0) + 1
    curr_day = datetime.now().timetuple().tm_yday
    curr_year = datetime.now().year
    year_dict[curr_year] *= round(365/curr_day)
    max_count = max(year_dict.values())
    df = pd.DataFrame.from_dict({"year": year_dict.keys(), "count": [val/max_count for val in year_dict.values()]})
    slope = np.polyfit(df['year'], df['count'], 1)[0]
    brackets = [-0.6, -0.2, 0.2, 0.6]
    for i in range(len(brackets)):
        if slope < brackets[i]:
            return i+1


if __name__ == '__main__':
    arxiv = Arxiv()
    print(get_trend(arxiv.queryAll(['covid', 'vaccine'], 10) + arxiv.queryDates(['covid', 'vaccine'], 1000, 10)))