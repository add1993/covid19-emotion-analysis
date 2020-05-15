# The path of train and test files
TRAIN_PATH = "/Users/shahreenshahjahanpsyche/Documents/UTD/NLP/Project-COVID19/COVID19-EmotionAnalysis/data/train"
TEST_PATH = "/Users/shahreenshahjahanpsyche/Documents/UTD/NLP/Project-COVID19/COVID19-EmotionAnalysis/data/test"

# Nested feature name and the attributes that is going to be used to train the model
EMOTION_HEADER = ['emotion']
ATTRIBUTES = ['body', 'emotion']

# Name of the labels
LABELS = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'love','optimism', 'pessimism', 'sadness', 'surprise', 'trust', 'neutral']

# modes/flags
CLEAN = True
MAP_LABELS = True

# mapping
LABEL_REVERT = {0:False, 1:True}
LABEL_MAP = {False:0, True:1}