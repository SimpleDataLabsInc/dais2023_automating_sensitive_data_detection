# Healthverity Demo Template

The above project assumes that the model is already being hosted on Databricks ML Flow. Below is a guide for the same:

## Hosting a Prebuilt Model via Databricks ML Flow Serving

In the below guide, we are using the stanford-deid model to perform Data Masking on our Pipelines

### Register a Model

Open up a Databricks Notebook in your Databricks Workspace and first install the necessary libraries:

```python
%pip install transformers
%pip install mlflow
%pip install inputimeout
%pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

Next, create the model and write it to the filesystem:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


m_name = 'StanfordAIMI/stanford-deidentifier-base'
tokenizer = AutoTokenizer.from_pretrained(m_name)
model = AutoModelForTokenClassification.from_pretrained(m_name)
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

pipeline_output_dir = "./pipeline"
nlp.save_pretrained(pipeline_output_dir)
```

Assuming you have Databricks MLFlow enabled on your workspace, you can now register a model Run once you have defined the model signature by providing defining: 

```python
import mlflow

class PIIAnalysisPipelineModel(mlflow.pyfunc.PythonModel):
  def load_context(self, context):
    import torch
    m_name = 'StanfordAIMI/stanford-deidentifier-base'
    tokenizer = AutoTokenizer.from_pretrained(m_name)
    model = AutoModelForTokenClassification.from_pretrained(m_name)
    device = 0 if torch.cuda.is_available() else -1
    self.pipeline = pipeline("ner", model=model, tokenizer=tokenizer, device=device)
    
  def predict(self, context, texts: List[str]) -> List[dict]:
    pipe = self.pipeline(texts, batch_size=len(texts))
    return pipe
```
Next, you can register a model run with

```python
with mlflow.start_run() as run:
  mlflow.pyfunc.log_model(artifact_path="<ARTIFACT_PATH>", python_model=PIIAnalysisPipelineModel())
```

### Register a Model with a Version

After this step, you can view the runs from the Databricks ML UI. 
From here, you can go and check the last Model Run from the `Experiments` screen:
<img width="1719" alt="Screenshot 2023-06-28 at 1 25 43 PM" src="https://github.com/SimpleDataLabsInc/dais2023_automating_sensitive_data_detection/assets/9202014/83f2d813-b026-436e-a430-8a63bddb6976">

On clicking on the pyfunc in the Models column, we are directed to the Databricks MLFlow UI →This will give metrics etc. (If they were registered from the notebook):

<img width="1710" alt="Screenshot 2023-06-27 at 6 27 43 PM" src="https://github.com/SimpleDataLabsInc/dais2023_automating_sensitive_data_detection/assets/9202014/0ad1fd5f-4e68-4b23-9a65-3c6e56853c64">

Using the `Run Id` from here, we can now test the model from the notebook by running:
```python
import mlflow
logged_model = 'runs:/<RUN_ID>/<ARTIFACT_PATH>'
loaded_model = mlflow.pyfunc.load_model(logged_model) # Load model as a PyFuncModel.
loaded_model.predict(["Hello I don't know what to do"])
```
Note that in the `predict()` method you’ll have to send the data exactly as you would, from the Model Inference Endpoint.

We will go on to Register the model now by clicking the `Register Model` Button above.
From here you can select a new model to register, or register a new version of an old model.

### Host the model to use for inference
Now, go to the registered model screen:
<img width="1692" alt="Screenshot 2023-06-27 at 6 41 27 PM" src="https://github.com/SimpleDataLabsInc/dais2023_automating_sensitive_data_detection/assets/9202014/8916d9f8-d922-42d6-8620-215d3dfc9d82">

From here, click on `Use Model for Inference` button where you can select a new endpoint or update the configuration (Model Version etc.) on an older one.
<img width="1515" alt="Screenshot 2023-06-27 at 6 43 37 PM" src="https://github.com/SimpleDataLabsInc/dais2023_automating_sensitive_data_detection/assets/9202014/1d0fb8bc-221b-49f8-9bcf-ebc3093ae538">

Here you can explore the model serving configurations etc. including the number of concurrent requests that the servigng model can handle, etc.
Note that you can also find the URL for the hosted model here.


### Using the Model on Spark Side

For our use case, we defined a UDF to get the predicted output:

```python
@udf(returnType=
        ArrayType(
            StructType([
                StructField("entity", StringType(), True),
                StructField("score", DoubleType(), True),
                StructField("word", StringType(), True),
                StructField("start", IntegerType(), True),
                StructField("end", IntegerType(), True),
            ]), 
        True)
    )
def get_model_response_single_with_schema(message:str) -> dict:
    url = 'https://dbc-19bbe7b0-ce18.cloud.databricks.com/serving-endpoints/test-pii-model/invocations'
    headers = {'Authorization': f'Bearer {Config.databricks_token}', 'Content-Type': 'application/json'}
    data_json = json.dumps({'inputs':[message]})
    response = requests.request(method='POST', headers=headers, url=url, data=data_json)
    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}, {response.text}')
    return response.json().get('predictions')[0]
```

Further, we called this function in a Reformat component in our pipeline (Visual Language: `sql`):

```python
get_model_response_single_with_schema(input_data)
```
where input_data is the name of the column whose entity data needs to be fetched.

