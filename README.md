Hello there!
Here you can find the steps to succesfully compile and execute our ARTWORK RECOGNITION MACHINE LEARNING MODEL :)
You will find 3 different directories:
    1. ResNet - Dataset, preprocessing and model design and execution.
    2. Local API - Restful API to predict using model previously trained using a HTTP POST request
    3. Interface - HTML template to allow user upload an image to predict and show results in a friendly user interface.

Follow the following steps in order:
    1. In ResNet folder, execute cell per cell pre_processing.ipynb notebook. This notebook will download and preprocess dataset before starting model training.
    ** You can skip this step since there is already final_dataset folder ready **
    2. Execute cell per cell resnet_model.ipynb notebook. Each cell has comments explaining the code. This notebook will save the final model in Local API folder.
    3. In Local API folder, in order to execute Restful API and user interface, execute the following commands in your terminal:
        Activate a virtual environment
            source myenv/bin/activate 
        Install required libraries
            pip install -r r.txt
        Execute API
            python3 api.py 
    You will have an API executing in you local host, please don't stop this process.
    4. Open a new terminal without stop the previous process and go to Interface path.
        Exceute interface
            python3 -m http.server
        Open a browser and paste this URL:
            http://127.0.0.1:8000/

You will be able to test our artwork recognition model using user interface :D
You can use the folder destined for testing in the dataset to test the accuracy of the model.

Good luck and happy training!


