import yake
kw_extractor = yake.KeywordExtractor()

def preprocess(json_data):
  text = json_data['text']
  print(len(text))
  return " ".join(text)

def extract_keywords(text):
  keywords = kw_extractor.extract_keywords(text)
  return keywords

def reform_output(keywords):
  ls = [keyword for keyword, score in keywords]
  return ls

def pipeline(json_data):
  text = preprocess(json_data)
  keywords = extract_keywords(text)[:]
  keywords = reform_output(keywords)
  return keywords


if __name__ == "__main__":
  docs2 = ["""
  When it comes to evaluating the performance of keyword extractors, you can use some of the standard metrics in machine learning: accuracy, precision, recall, and F1 score. However, these metrics don’t reflect partial matches; they only consider the perfect match between an extracted segment and the correct prediction for that tag.
  Fortunately, there are some other metrics capable of capturing partial matches. An example of this is ROUGE.
  """] * 1000

  keywords = pipeline({'text': docs2})

  print(keywords)
  