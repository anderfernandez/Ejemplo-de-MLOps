from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

# Defino parámetros --> La mejor práctica es hacerlo en un fichero aparte.
# Pero por simplicidad incluyo todo junto,
test_size = 0.2

# Load data
iris = load_iris(as_frame = True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, 
    iris.target, 
    test_size = test_size
    )

# Create pipeline for numerical variables
numeric_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', VarianceThreshold())
    ])

# Create pipeline for categorical variable
categorical_pipe = Pipeline([
    ('encoder', OneHotEncoder(drop = 'first'))
    ])

# Create ColumnTransform
numeric_cols = X_train._get_numeric_data().columns.tolist()
cat_cols = X_train.columns[~X_train.columns.isin(numeric_cols)].tolist()

col_transf = ColumnTransformer([
    ('numeric', numeric_pipe, numeric_cols),
    ('categoric', categorical_pipe, cat_cols)
    ])

# Fit transformer
col_transf_fit = col_transf.fit(X_train)

# Transform Data
X_train_transf = col_transf_fit.transform(X_train)
X_test_transf = col_transf_fit.transform(X_test)

# Train the model
dc = DummyClassifier()
dc_fit = dc.fit(X_train_transf, y_train)

# Save transformer & model
with open('outputs/transformer.pickle', 'wb') as w:
    pickle.dump(col_transf_fit, w)

with open('outputs/model.pickle', 'wb') as w:
    pickle.dump(dc_fit, w)