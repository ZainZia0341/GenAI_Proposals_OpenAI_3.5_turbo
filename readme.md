# GenAI Proposals

This repository contains a Streamlit application that allows users to generate professional proposals based on given job descriptions. The application uses a fine-tuned language model to create personalized, engaging, and effective proposals. The model has been trained on various examples of proposal writing to ensure high-quality outputs that adhere to best practices in the industry.

## Features

- **User Input:** The application takes in a job description, user name, client name, and years of experience.
- **Proposal Generation:** It generates a detailed proposal based on the provided input using a fine-tuned language model.
- **Conversational Tone:** The proposals are written in a friendly, engaging, and conversational tone.
- **Personalization:** The application personalizes the proposal by including user-specific details such as their name, the client's name, and their years of experience.
- **Technical Expertise:** The generated proposals highlight the user's relevant skills, experience, and past projects.
- **Post-Delivery Support:** The proposals include a section on post-delivery support, ensuring clients of continued assistance after project completion.

## Installation

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run Fine_Tunned_model.py
    ```

2. **Fill in the input fields:**
    - Enter the job description.
    - Enter your name.
    - Enter the client's name.
    - Enter your years of experience.

3. **Generate the proposal:**
    - Click the "Run" button to generate the proposal.

## Example

Here's an example of how to use the application:

1. **Enter the Job Description:**
    ```
    We need a Full Stack AWS Developer to create a platform for job seekers in the USA. The project involves creating a serverless application architecture, orchestrating job fetching from various Applicant Tracking Systems (ATS), using Generative AI to enhance job matching and filtering, and implementing a subscription-based model.
    ```

2. **Enter User and Client Details:**
    - **User Name:** John Doe
    - **Client Name:** Jane Smith
    - **Experience Year:** 5

3. **Generated Proposal:**
    ```
    Hello Jane,

    I am excited about the opportunity to work on your job matching platform. With my 5 years of experience as a Full Stack AWS Developer, I am confident in delivering a high-quality solution for your needs. I have recently developed a comprehensive Full Stack solution for EarlyBirdee, a platform designed to help users find jobs in the USA. The project included creating a serverless application architecture, orchestrating job fetching from various ATS, and utilizing Generative AI for job matching and filtering. This resulted in enhanced job response times to 100ms and increased user satisfaction through timely and relevant job notifications.

    Designed and built a serverless application using AWS services to ensure scalability and cost-efficiency.
    Developed a job matching system that processes new jobs daily and matches them with user profiles.
    Implemented a notification system to alert users about relevant job positions.
    Used Generative AI to generate functional roles and specializations, enabling efficient job filtering.
    I am confident that my skills and experience align well with your requirements, and I look forward to discussing this opportunity further.

    Best regards,
    John Doe
    ```

## Fine-Tuned Model

The fine-tuned model used in this application is trained on various examples of proposal writing. It follows the principles of creating proposals that are:
- Conversational and engaging
- Personal and direct
- Creative and original
- Addressing pain points
- Following Upwork guidelines
- Including relevant projects, skills, and years of experience
- Proposing clear solutions and technical expertise
- Highlighting commitment to client success and deadlines


**Note:** replace `your_openai_api_key` with your OpenAI API key. Adjust the example usage and generated proposal according to your specific use case.
