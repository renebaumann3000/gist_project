# GIST Project - A blog for a rare form of cancer

## Introduction:
This project is a real initiative involving an actual "client" and a genuine use case. My mother has been battling cancer since she was 18 years old, which means even before I was born. In recent years, she got affected by a rare type of tumor known as GIST. More information about GIST can be found here: https://en.wikipedia.org/wiki/Gastrointestinal_stromal_tumor. She actively participates in a GIST support group. The group has long desired to have its own blog for two main reasons: 1. to spread awareness about the disease, and 2. to simplify the process for people to connect with such a support group. Therefore, the Full Stack project was a perfect match for this purpose. Apart from myself and a friend, the individuals currently registered on the platform for testing are members of this support group.
Attention: the group is based in Berlin Germay, so some blog posts are in german!

## Self-Reflection:
I begin this README with a self-reflection to clarify the status of the project. The technical aspect of this project has been overwhelming for me, almost pushing me to give up. It was difficult to understand that virtually all files have vise versa dependencies. I also lost track at some point in the never-ending war of error messages. What does this line actually do again?
Why did I write it like that 14 days ago? For this reason, I also commented on many lines in order to somehow keep an overview... I would have preferred a more intensive "tandem" for learning purposes for this project. Fortunately, my network helped me with debugging and was there for me during an emotionally difficult time. I started with the PP4 walkthrough. For me personally, understanding the Django settings was challenging from the outset. It's like trying to learn how to drive a car. In the first driving lesson, before you even start driving, you have to tinker with the engine. As a beginner. Without any warning... Therefore, I sought my own way in and tried various other tutorials that worked better for me as an introduction to a Django project. Since the technical part of the project was difficult for me, I have not been able to fully complete the project by writing writing these lines. The design is not yet complete, and some features are not implemented. I will comment on the specific things in the respective sections.
I don't know if this project will be a fail. But the really good thing is that it's a real project that will continue to develop over time.

## Features:

(Please see the testing section for screenshots. I will point out there the relevant infos and related issues)

### User Authentication and Profiles:

Users can sign up for accounts and log in.
User profiles allow customization with profile pictures, bios, and social media links.
Users can edit their profiles and manage personal information.

### Blog Management:

Users can create, edit, and delete blog posts.
Blog posts can be categorized for organization.
Unregistered users can read blog articles without signing up.

### Category Management:

Users can create and manage blog post categories.
Categories help in organizing and classifying blog posts.

### Treatment Log:

Users can maintain treatment logs to track medical treatments and progress.
Treatment logs are associated with user profiles. The Treatment Log works like a diary. As a future improment it makes sense, to download the log and discuss it with the doctor.

### Members Section:

A dedicated "Members" section allows users to view a list of registered members.
Member profiles are displayed with profile pictures and usernames.

### Security and Privacy:

User authentication ensures secure access to profile and blog management features.
Users can log out to secure their sessions.

### Public Accessibility:

Blog articles are publicly accessible, allowing users to read content without registering or logging in.

### Filters:

A filter is available to categorize blog posts by category.

### Rich Text Editing:

Use the Quill rich text editor to enable users to format and style their blog posts effectively.

### Image Upload:

User are able to upload images to their profile and to the blog articles.

## Features left to implement (because it's a real life project, these features are really planend):

- For sure, the contact form!
- GDPR related options that allows the user to download the own data
- GDPR related concepts for anonymize user data to keep the content
- option that allows a user to delete their own user profile
- Administrator permission checks
- a landing page for the goup intro
- a seperate memeber section so that user can write their storys in that section (clear separation between administrator posts and user posts)
- implementation of a Newsletter
- better security and privacy
- Feature for uploading more images
- Feature to upload files
- Feature to download the Treatment Log
- Search function
- easy overview for sort and filter posts for index + user posts

## UX/ UI Site Goals (the group already announced on the blog a colloboration with the german "Sarkome Foundation" and the "Charité")

Approach: Creating a Patient-Centric GIST Blogging Platform

Goal: Develop a user-friendly and informative platform that provides value to GIST patients and caregivers.

1. Patient-Centric Content:

- Why GIST Patients Should Use the Page: Patients and caregivers should visit the platform to access relevant and accurate information about GIST. The content should be tailored to address their specific needs, such as treatment options, managing side effects, and patient stories.

2. Treatment Insights and Logs:

- Why GIST Patients Should Use the Page: The platform should offer a simple and intuitive way for patients to record and manage their treatment logs. This feature helps patients track their progress, medication dosages, and side effects over time, facilitating better communication with healthcare providers.

3. Supportive Community:

- Why GIST Patients Should Use the Page: The platform should foster a sense of community among GIST patients. Social interaction features can connect patients with shared experiences, providing emotional support and a place to ask questions.

4. Access to Experts:

- Why GIST Patients Should Use the Page: Collaborate with medical experts and oncologists to provide accurate and reliable information. Offer opportunities for patients to ask questions and receive guidance from professionals in the field.

5. User-Friendly Profile Management:

- Why GIST Patients Should Use the Page: Encourage patients to create profiles that include their treatment journey and experiences. This allows them to connect with others, share their stories, and find a sense of belonging within the community.

6. Timely Updates and Research News:

- Why GIST Patients Should Use the Page: Keep patients informed about the latest research developments, treatment options, and clinical trials. Regularly update the platform with news articles, research findings, and treatment breakthroughs.

7. Empowerment and Knowledge Sharing:

- Why GIST Patients Should Use the Page: Empower patients to take an active role in their healthcare journey. Encourage knowledge sharing, where patients can contribute their insights and experiences to help others facing similar challenges.

8. Collaborative Approach:

- Why GIST Patients Should Use the Page: Foster collaboration among patients, caregivers, healthcare professionals, and advocacy organizations. Highlight the importance of a multidisciplinary approach to GIST management.

### Agile:

This project was created using the agile method.
Please don't be confused, as I didn't create any labels at first and couldn't add them later, I recreated the board ( which is why the user stories are renumbered).
You can view the user storys in my repository or use this link: https://github.com/users/renebaumann3000/projects/6


### Wireframes:

At the beginning of the project, I discussed his idea for the website with the group leader. I had made my original sketches by hand. As I wrote them in German, I recreated the wireframes. The final version differs from the first approach due to time and my capabilities, but it is an ongoing project.

<details open>
<summary>
"Images"
</summary>

![index](/documentation/assets/index.png "index")

![signup](/documentation/assets/signup.png "signup")

![login](/documentation/assets/login.png "login")

![blog_post](/documentation/assets/blog_post.png "blog_post")

![add_category](/documentation/assets/add_category.png "add_category")

![user_profile](/documentation/assets/user_profile.png "user_profile")

![edit_profile](/documentation/assets/edit_profile.png "edit_profile")

![members](/documentation/assets/members.png "members")

![category_list](/documentation/assets/category_list.png "category_list")

</details>

### Wireframes:
