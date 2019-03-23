import pickle
from model.comparer import Comparer
c = Comparer()
pickle.dump(c, open('serialized_models/c_model.p', 'wb'))