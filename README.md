# HTX Internship 2021 Sharing Repository.
## Internship Report & User Manual for my Projects
by Wang Jiale (May-Aug 2021)

---

This repository contains my work for my AI / Machine Learning internship with HTX CBRNE (Technology Deployment Department) from May to Aug 2021. For sharing with colleagues. The work allowed me to better appreciate [HTX's](https://www.htx.gov.sg/who-we-are) efforts to develop in-house Deep Learning, Computer Vision, and Imaging Science capbilities to safeguard Singapore's security.

**Note: Due to security restrictions, I am not allowed to upload most of the real datasets that I've used in my work. Instead, non-sensitive datasets are used for demonstration in this repo.** 

The code however is shared in full. Contact CBRNE TD officers for more information.

## General Installation Instructions
**Important: Juptyer Lab is needed to view most of my projects. Install using**

`conda install -c conda-forge jupyterlab `
OR
`pip install jupyterlab`

To install the libraries required to run each project, navigate to the directory of the project on your computer (after cloning from this repo) and run:

`pip install -r requirements.txt`

---

## List of Projects that I worked on. 
#### Click on the relevant link for more info & installation

[1. General Object Detector for Images (Deep Learning)](#project-1-general-object-detector-deep-learning)

[2. Hazard Pictogram Identification with AI](#project-2-hazard-pictogram-identification-with-ai)

[3. Dataset Processing Toolbox for AI Training](#project-3-dataset-processing-toolbox-for-ai-training)

[Putting it all together: Ways to use what I've made](#putting-it-all-together-ways-to-use-what-ive-made)

**[Key Takeaways from Internship](#key-takeaways-from-internship)**


---

# Project 1: General Object Detector (Deep Learning)

Jump to:
[Introduction](#introduction)  |  [Features and Technical Information](#features-and-technical-information)  |  [Limitations](#limitations)  |  [Installation and Use](#installation-and-use)  |  [Folder Structure](#where-to-find-what)


## Introduction
A large part of my internship revolved around the building and use of a General Object Detector. This programme enables the training of Machine Learning models with PyTorch that can identify and locate **any** type of object! The training and inference process are both called by two lines of code each.

After training, a single image or a set of test images can be fed to the model, from which it will box up the location of the object, along with the Class Type and the associated confidence level. The inferred images are then saved to a pre-specified folder. It also has a **hyperparameter tuning functionality** (more info below).

This Object Detector **can be run offline**, allowing work with security sensitive datasets. The detector has been used to identify GHS Hazard Symbols on chemical bottles, threat objects of interest in cargo X-ray scans (e.g., firearms or Explosive Precursors), as well as (just for fun) animals and humans. Full set of images inferred are not shown as it contains confidential information. Only non-confidential images are shown below.


<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/143583396-f40f4642-9348-468d-b0a3-1b229161bdf5.jpg" width="600px" />
  <img src="https://user-images.githubusercontent.com/67915054/143583211-7fcd2e13-42c0-4606-bc63-9d2c8093e853.jpg" width="600px" />
  <p>Example outputs of my AI model...</p>
</div>

## Features and Technical Information

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/128144694-a9c311f3-f8c2-4b57-b6e0-7610dd7b1069.jpg" width="800px" />
</div>

- Runs **offline** on Jupyter Lab or Notebook - suitable for processing sensitive data.
- Uses the PyTorch ML library.
- Uses the Faster R-CNN architecture from [FAIR Detectron](https://github.com/facebookresearch/Detectron); pretrained on the COCO dataset.

- All-in-one programme
  - Trains the ML model.
  - Tests ML model on unseen dataset and prints out inference images.
  - Returns evaluation results (mAP, Recall) as a CSV.
  - Plots graphs
  
- Hyperparameter tuning:
  - Programme designed by myself. No reliance on any external tuning library.
  - Can be toggled on and off (Set "perform_tuning" to True/False).
  - User can specify a set of parameters and it will print out comparison results in a CSV and identify the best model.
  - All models generated will also be saved.
  - Subject to CUDA memory availability. For some computers, only 1-2 tests can be run at once.

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126479795-51faef80-8314-4e97-8834-b63f52dae484.png" />
  <p>Sample hyperparameter tuning report that is automatically generated by my programme.</p>
</div>

## Limitations
- Requires labelled data (Supervised learning).
- Not the best at differentiating animals that look alike (e.g. mammals of the same colour), humans in animal constumes, or very low resolution images BUT Performs well in identifying symbols and distinct objects in X-ray scans.


## Installation and Use
1. Clone / Download the Project 1 Folder.
    - Unzip the **A-Detectron_Kit.zip** folder
    - Open the folder. Rename it if needed to suit your project. This will be your "root" directory.

2. Create a new Conda environment `conda create --name myenv`
 - This is important so as to prevent interference with your existing environment!

3a. Install required libraries by navigating to the project directory then run:

```
pip install -r requirements.txt
```

3b. Install the right version of PyTorch and Torchvision for your CUDA toolkit. See how here: [Install PyTorch](https://pytorch.org/get-started/previous-versions/)

4. Make sure Jupyter Lab is installed. `pip install jupyterlab`

5. **Select Image Datasets** and place them in the correct folders:
    - Training / Validation images ---> "datasets/train_val/images" folder 
    - Testing images ---> "datasets/test/images" folder 
    - **A minimum of 2 images are required for each folder!**

6. **Annotate the images** for both train_val AND test datasets. Ideally >200 objects should be used for training (an image can contain multiple objects). How to use:
    - Option A (Manually): use [Label Image](https://github.com/tzutalin/labelImg). How to use:
      - On the left hand menu of LabelImg, select "Open Dir" and select the "datasets/train_val/images" folder
      - Then select "Change Save Dir" and select the "datasets/train_val/annotations" folder
      - Repeat the process for images in the "test" folder (if required)
        - Label the test dataset if you want testing statistics.
        - Else, the test dataset can be completely unlabelled!
    - Option B (Automatically) use my self-developed Auto-Label programme - Project 3: 
      - Note: Works best for images / scans with plain backgrounds only

7. Run the .ipynb (Jupyter Notebook) file in Jupyter Lab.

8. Comment out the first two blocks of code

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126138624-4b00334e-2570-4334-8f0a-0a47bcd9986a.png" width="600px" />
</div>

9. Scroll down to **PART 1: SET UP** on the notebook and change all the directories and parameters accordingly. 

10. Select "Run > Run All Cells"

11. **Training:** Uncomment the first block of code, give an experiment title and run the code.

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126139874-112ded3d-418d-4774-8c7d-168b66dae84b.png" width="700px" />
</div>

12. **Inference:** Uncomment the 2nd block of code, select the correct model to use (use default for latest trained model) and run the code.

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126139924-1d9cef2b-1873-420a-84e1-43570df9d8ed.png" width="700px" />
</div>

13. Retrieve the test results and/or trained model in the directories shown below:

## Where to find what

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126140674-b12f4eb6-d82c-4a84-898b-4e3770dcb2f7.jpg" width="700px" />
</div>


[Back to top](#htx-internship-2021-sharing-repository)


---

# Project 2: Hazard Pictogram Identification with AI

Jump to:
[Introduction](#introduction-1)  |  [Features and Technical Information](#features-and-technical-information-1)  |  [Installation and Use](#installation-and-use-1)

## Introduction
For my first iteration of the abovementioned Object Detector, I trained a Machine Learning model using PyTorch to identify and locate standard hazard symbols ([GHS pictograms](https://en.wikipedia.org/wiki/GHS_hazard_pictograms) and ([9-class cargo labels](https://www.dgiglobal.com/classes/)). The goal is to assist border officers (even those without training in identifying hazards) to quickly identify any hazardous substances and file a report if needed. The model is able to detect the following hazard classes: 

- Explosives (GHS01, Class 1)
- Flammable (GHS02, Class 3/4)
- Oxidizing Agent (GHS03, Class 5.1/5.2)
- Corrosive (GHS05, Class 8)
- Harmful (GHS07)

**For an *all purpose* Object Detector, see [Project 1: General Object Detector](#project-1-general-object-detector-deep-learning)**

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/126132889-4c97cc81-08d0-4f28-ab63-040c19844bb0.png" width="450px" />
  <img src="https://user-images.githubusercontent.com/67915054/126477681-4ff89a5c-e07c-46ad-8189-c933d85fef37.png" width="300px" />
  <p>Samples of Hazard Labels identified by the AI model.</p>
</div>

## Features and Technical Information
- Uses the PyTorch ML library.
- Uses the Faster R-CNN architecture from [FAIR Detectron](https://github.com/facebookresearch/Detectron); pretrained on the COCO dataset.
- Trained on ~700 images, containing ~820 hazard symbols.
  - Images obtained from Google Images using [Simple Mass Downloader Chrome Extension](https://chrome.google.com/webstore/detail/simple-mass-downloader/abdkkegmcbiomijcbdaodaflgehfffed)
  - Labelled using [LabelImg](https://github.com/tzutalin/labelImg) in **Pascal VOC format**.
- Best model yielded mAP(IOU50) = 0.9812 on Validation dataset, and mAP(IOU50) = 0.731 on the more challenging Test dataset.
- Hyperparameters for best model: SGD Optimiser, lr=0.02, batch_size=2, num_epochs=8, optimizer_decay=0.0005, momentum=0.9, lr decreases 10x per 3 epochs.
- Developed on Google Colab but later adapted for offline environments (also see [Project 1](#project-1-general-object-detector)).

## Installation and Use

- All files are found in the Project 2 Folder in this repository. 
- Trained models are found on the HTX ROG, under my "Trained Models"
- Installation process is the same as the [General Object Detector](#installation-and-use).

### About the project folder

| Notebook Name                                       | Description                                                                                                                                                       | Run On           | Number of <br>Classes | Dataset Used                                                                                       |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-----------------------|----------------------------------------------------------------------------------------------------|
| 1 Raccoon Detector.ipynb                            | Trained to detect Raccoons (1 class only). <br><br>Model tested on pictures of other animals, objects, <br>and Gordon Ramsay.                                     | Google <br>Colab | 1                     |                       |
| 2 Oxidizer Detector.ipynb                           | Trained to detect Oxidizer Symbols (1 class only)<br><br>Model tested on other hazard symbols to flag<br>out False Negatives and False Positives                  | Google<br>Colab  | 1                     | Oxidizer Dataset <br>(On HTX ROG Datasets folder)                                                  |
| 3 All Hazard Symbols <br>Detector.ipynb             | Trained to detect 5 classes of symbols (Corrosive,<br>Oxidizer, Explosive, Harmful, Flammable).                                                                   | Google <br>Colab | 5                     | All Hazard Symbols Dataset <br>(On HTX ROG Datasets folder)                                        |
| 4 Hazard Detector w <br>Hyperparameter Tuning.ipynb | Same as (3) but with hyperparameter <br>tuning functionality.                                                                                                     | Google<br>Colab  | 5                     | All Hazard Symbols Dataset <br>(On HTX ROG Datasets folder)                                        |
| 5 Hyperparameter Tuning <br>Results.ipynb           | Visualisation of results generated by (4)                                                                                                                         | Jupyter          | -                     | -                                                                                                  |
| 6 Hazard Detector FINAL.ipynb                       | **Recommended version** <br>FINAL Notebook to train, validate, and test Hazard<br>Pictograms. <br><br>Can also use this notebook to test on your own<br>datasets. | Jupyter          | Unlimited!            | All Hazard Symbols Dataset <br>(On HTX ROG Datasets folder)<br><br>OR<br><br><br>Your own dataset! |


[Back to top](#htx-internship-2021-sharing-repository)


---
# Project 3: Dataset Processing Toolbox for AI Training

Jump to:
[Introduction](#introduction-4)  |  [Features and Technical Information](#features-and-technical-information-4)  |  [Installation and Use](#installation-and-use-4)  |  [Sample Workflows](sample_workflows)

## Introduction
This toolbox contains useful programmes to process, label, and generate datasets for training Object Detection AI models.

<div align="center">
  <p> Screenshot of toolbox, run from Toolbox.py </p>
  <img src="https://user-images.githubusercontent.com/67915054/129586636-aa157b2f-f061-496d-9465-c32642e292ef.png" width="700px" />
</div>

| Tool                                                                                                     | Description                                                                                                                                                                                                                                                              | What to Run                                                         | Example Uses                                                                                               |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Auto-Overlay<br><br>[(More Info)](#autooverlay)                                                          | Automatically places objects in whitespaces of a given image.<br><br>Used to rapidly create staged scenes for AI training.<br><br>Generates PascalVOC format XML annotations.                                                                                            | AutoOverlay.ipynb                                                   | "Hide" threats in Stream <br>of Commerce scans to train AI, <br>significantly lowering False<br>Positives. |
| Auto-Labeller<br><br>[(More Info)](#autolabeller)                                                        | Automatically identifies objects placed against a plain <br>background and labels them in the PascalVOC format.<br><br>Cuts down time taken in labelling data, compared to the<br>manual way of labelling data in LabelImg.<br><br>Is also able to crop out the objects. | **Toolbox.py**<br>(recommended)<br><br>OR<br><br>AutoLabeller.ipynb | Use the auto-labelled data to<br>train Object Detection AI.                                                |
| Threat Image Projection (TIP)<br><br> | Hides objects within X-Ray images, simulating the physics of X-ray.                                                                                                                                                                                                      | **Toolbox.py**                                                      | "Hide" threats in Seacargo<br>containers.                                                                  |
| Auto-Cropper<br><br>[(More Info)](#autocropper)                                                          | Given a labelled dataset (in PascalVOC format), automatically <br>crops out all labelled objects and save them <br>as separate images.                                                                                                                                   | **Toolbox.py**<br>(recommended)<br><br>OR<br><br>Autocropper.ipynb  | Extract objects for use in<br>Auto-Overlay or X-ray<br>Image Projection.                                   |
| Video Extractor<br><br>                                                 | Given a video stream, automatically extracts static images at<br>set intervals.                                                                                                                                                                                          | Toolbox.py<br><br>OR<br><br>Video_Extractor.ipynb                   | Extract training images from<br>a video stream.                                                            |
| Delete Duplicate Images                                                                                  | Finds and deletes duplicate images, even if they are of <br>different filenames.                                                                                                                                                                                         | Delete_Duplicates.ipynb                                             | Remove duplicate images in<br>a big training dataset.                                                      |
| Image Comparison                                                                                         | Compares the difference between 2 images and highlights these<br>pixels in black (while similar pixels are in white).                                                                                                                                                    | Image_Comparison.ipynb                                              | Compare two projection<br>algorithms to determine the<br>better one.                                       |


## Features and Technical Information

### AutoOverlay

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/129587840-b8572e73-11f8-4b99-a494-9d682fd9be5f.JPG" width="800px" />
</div>

- Automatically:
  - generates thousands of unique overlayed images
  - labels output images (in PascalVOC format) for training of Object Detection AI
 
- Projection features
  - Random placement of object within any whitespace
  - Random rotation of objects
  - Random magnification of the object according to formula: ![magnification_formulae](https://user-images.githubusercontent.com/67915054/127338920-484ae17c-0fb9-42be-b427-7c1350252569.jpg) 

 ### AutoLabeller

<div align="center">
  <p> Identifies objects and generate XML annotations for them & crop out the objects </p>
  <img src="https://user-images.githubusercontent.com/67915054/127974637-fbe32f1f-a205-4907-a236-fab188f0b46c.jpg" width="800px" />
</div>

### AutoCropper
<div align="center">
  <p> Given an image with its associated PascalVOC XML label, it will automatically crop out the objects. </p>
  <img src="https://user-images.githubusercontent.com/67915054/127974184-aaeed0a6-5515-4e9b-ac25-bd946a9fbac9.jpg" width="800px" />
</div>


## Installation and Use

### Main File

1. Clone project folder from github
2. Create a new Conda environment `conda create --name myenv`
 - This is important so as to prevent interference with your existing environment!

3. To install required libraries, navigate to the project directory then run:

```
pip install -r requirements.txt
```

4. Make sure Jupyter Lab is installed. `pip install jupyterlab`

5. Do either of the following, depending on what you need. Refer to [table](#introduction-4) above.
	- Run `python Toolbox.py` in command prompt
	- OR Open `AutoOverlay.ipynb` in Jupyter Lab
	- OR Open `Delete_Duplicates.ipynb` or `Image_Comparison.ipynb` in Jupyter Lab
  

[Back to top](#htx-internship-2021-sharing-repository)

---

# Putting it all together: Ways to use what I've made

Possible workflows

<div align="center">
  <img src="https://user-images.githubusercontent.com/67915054/129376624-3903f13a-a69a-4f53-8644-44eb1d5f40bc.JPG" width="1000px" />
  <img src="https://user-images.githubusercontent.com/67915054/129376636-2956a4bc-c0bc-4389-8758-77562bae448b.JPG" width="1000px" />
  <img src="https://user-images.githubusercontent.com/67915054/129376639-947eb8be-f42c-405c-ad85-9bd99cbd45f2.JPG" width="1000px" />
</div>


[Back to top](#htx-internship-2021-sharing-repository)

---

# Key Takeaways from Internship
This internship helped me appreciate the role of Data Scientists and Software Engineers better and motivated me to seriously consider that as a career.

General
- A large part of any data science project is made up of data collection and pre-processing.
- Most of the time we do not even spend that much time on coding
- There is ample potential for the use of AI in customs threat detection.

Technical
- Learnt about Object Detection - a branch of Computer Vision that I've not previously explored
- Learnt about fundamental metrics and terminologies in Computer Vision, including:
	- Average Precision and how it differs from mAP
	- Average Recall
	- IOU
	- Loss, Learning Rate, Gradient Descent
- Experimented with popular Object Detection architectures, including:
	- Faster R-CNN
	- YOLOv4 and YOLOv5
- Read about the recent research in Computer Vision, including:
	- Focal Loss (which gave rise to RetinaNet)
	- ConViT and Vision Transformers
	- Encoder and Decoder Systems
- Got to experiment with creative solutions in broadening training datasets:
	- Threat Image Projection (TIP)
	- Overlaying of objects onto backgrounds.

[Back to top](#htx-internship-2021-sharing-repository)
