Hello there!
Here you can find the steps to succesfully compile and execute our ARTWORK RECOGNITION MACHINE LEARNING MODEL :)
You will find 3 different directories:<br />
    1. ResNet - Dataset, preprocessing and model design and execution.<br />
    2. Local API - Restful API to predict using model previously trained using a HTTP POST request<br />
    3. Interface - HTML template to allow user upload an image to predict and show results in a friendly user interface.<br />

Follow the following steps in order:<br />
    1. In ResNet folder, execute cell per cell pre_processing.ipynb notebook. This notebook will download and preprocess dataset before starting model training.
    ** You can skip this step since there is already final_dataset folder ready **<br />
    2. Execute cell per cell resnet_model.ipynb notebook. Each cell has comments explaining the code. This notebook will save the final model in Local API folder.<br />
    3. In Local API folder, in order to execute Restful API and user interface, execute the following commands in your terminal:<br />
        Activate a virtual environment<br />
            source myenv/bin/activate <br />
        Install required libraries<br />
            pip install -r r.txt<br />
        Execute API<br />
            python3 api.py <br />
    You will have an API executing in you local host, please don't stop this process.<br />
    4. Open a new terminal without stop the previous process and go to Interface path.<br />
        Exceute interface<br />
            python3 -m http.server<br />
        Open a browser and paste this URL:<br />
            http://127.0.0.1:8000/<br />

You will be able to test our artwork recognition model using user interface :D<br />
You can use the folder destined for testing in the dataset to test the accuracy of the model.<br />

Good luck and happy training!


