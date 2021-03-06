from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from Document import Document

def text_similarity(documents):
    vect = TfidfVectorizer(stop_words="english") 
    nonnull_docs = []
    for doc in documents:
        if doc.abstract is not None:
            nonnull_docs.append(doc)
    if len(nonnull_docs) == 0:
        return []
    tfidf = vect.fit_transform([doc.abstract for doc in nonnull_docs])
    pairwise_similarity = tfidf * tfidf.T
    data = tfidf.todense().tolist()
    names = vect.get_feature_names_out()
    df = pd.DataFrame(data, columns=names)
    for i in df.iterrows():
        nonnull_docs[i[0]].keywords = (i[1].sort_values(ascending=False)[:2].index.tolist())
    similarities = pairwise_similarity.toarray().sum(axis=1)
    sim_indexes = [(similarities[i], i) for i in range(len(similarities))]
    sorted_sims = sorted(sim_indexes)
    return [nonnull_docs[i[1]] for i in sorted_sims]

if __name__ == "__main__":
    abs1 = 'This study aims to statistically assess the effectiveness of vaccination against SARS-CoV-2. It is indispensable to investigate the relationship between Covid-19 deadliness and vaccination in order to study the impact of vaccine in real-world. We studied rates of infection and death due to Covid-19 in different countries with respect to their levels of vaccination. People who received the required dose of vaccination were considered as fully vaccinated in this study. Based on the percentage of fully vaccinated population, countries were categorized into several groups. Though a high-level study on the vaccine effectiveness may not provide much insight for individual level differences, a global analysis is imperative to infer the influence of vaccination as a controlling measure of the pandemic.'
    abs2 = 'Returning universities to full on-campus operations while the COVID-19 pandemic is ongoing has been a controversial discussion in many countries. The risk of large outbreaks in dense course settings is contrasted by the benefits of in-person teaching. Transmission risk depends on a range of parameters, such as vaccination coverage and efficacy, number of contacts and adoption of non-pharmaceutical intervention measures (NPIs). Due to the generalised academic freedom in Europe, many universities are asked to autonomously decide on and implement intervention measures and regulate on-campus operations. In the context of rapidly changing vaccination coverage and parameters of the virus, universities often lack sufficient scientific insight to base these decisions on. To address this problem, we analyse a calibrated, data-driven agent-based simulation of transmission dynamics of 10755 students and 974 faculty members in a medium-sized European university. We use a co-location network reconstructed from student enrollment data and calibrate transmission risk based on outbreak size distributions in education institutions. We focus on actionable interventions that are part of the already existing decision-making process of universities to provide guidance for concrete policy decisions. Here we show that, with the Omicron variant of the SARS-CoV-2 virus, even a reduction to 25% occupancy and universal mask mandates are not enough to prevent large outbreaks given the vaccination coverage of about 80% recently reported for students in Austria. Our results show that controlling the spread of the virus with available vaccines in combination with NPIs is not feasible in the university setting if presence of students and faculty on campus is required.'
    abs3 = 'Since their announcement in November 2020, COVID-19 vaccines were largely debated by the press and social media. With most studies focusing on COVID-19 disinformation in social media, little attention has been paid to how mainstream news outlets framed COVID-19 narratives compared to alternative sources. To fill this gap, we use cognitive network science and natural language processing to reconstruct time-evolving semantic and emotional frames of 5745 Italian news, that were massively re-shared on Facebook and Twitter, about COVID-19 vaccines. We found consistently high levels of trust/anticipation and less disgust in the way mainstream sources framed the general idea of vaccine/vaccino. These emotions were crucially missing in the ways alternative sources framed COVID-19 vaccines. More differences were found within specific instances of vaccines. Alternative news included titles framing the AstraZeneca vaccine with strong levels of sadness, absent in mainstream titles. Mainstream news initially framed Pfizer along more negative associations with side effects than AstraZeneca. With the temporary suspension of the latter, on March 15th 2021, we identified a semantic/emotional shift: Even mainstream article titles framed AstraZeneca as semantically richer in negative associations with side effects, while Pfizer underwent a positive shift in valence, mostly related to its higher efficacy. Thrombosis entered the frame of vaccines together with fearful conceptual associations, while death underwent an emotional shift, steering towards fear in alternative titles and losing its hopeful connotation in mainstream titles. Our findings expose crucial aspects of the emotional narratives around COVID-19 vaccines adopted by the press, highlighting the need to understand how alternative and mainstream media report vaccination news.'
    doc1 = Document("url", "title", abstract=None)
    doc2 = Document("url", "title", abstract=abs2)
    doc3 = Document("url", "title", abstract=abs3)
    print(text_similarity([doc1]))