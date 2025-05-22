# 📝 A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education

This repository contains the code and resources for the paper titled **"A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education."** It includes the survey results and the code used for analysis in the paper.

<p align="center">
  <img src="https://github.com/calvinyeungck/Automated_Assignment_Grading/blob/main/img/fig1.png" alt="System Overview" width="600"/>
</p>

- **Importance of Automated Grading**: Automated grading is crucial in education technology as it allows for efficient assessment of large volumes of student work, ensures consistent and unbiased evaluations, and provides immediate feedback to enhance learning.

- **Challenges in Current Systems**: Current systems face challenges such as the need for large datasets in few-shot learning methods, a lack of personalized feedback, and an overemphasis on benchmark performance rather than prioritizing the student's learning experience.

- **Proposed Solution**: The Zero-Shot LLM-Based Automated Assignment Grading (AAG) system leverages prompt engineering to evaluate both computational and explanatory responses from students without additional training or fine-tuning, providing tailored feedback that highlights strengths and areas for improvement.

- **Impact and Validation**: The system has been shown to significantly improve student motivation, understanding, and preparedness compared to traditional grading methods, as evidenced by survey responses from higher education students, validating its potential to transform educational assessment and provide scalable, high-quality feedback.

## 📊 Result Replication

### 1. Clone the Repository
Begin by cloning the repository to your local machine:
```bash
git clone <repository_url>
```
### 2. Navigate to the Project Directory
Change to the project directory:
```bash
cd ./AAG
```
### 3. Install Required Packages
Install the necessary dependencies by running the following command:
```bash
pip install -r requirements.txt
```
### 4. Run the Correlation Calculation (Result of Section 4.1)
Execute the code to calculate the correlation:
```bash
python correlation.py
```
### 5. Run the Statistical Tests (Result of Section 4.2)
Execute the code to perform the statistical tests:
```bash
python stats_test.py
```
