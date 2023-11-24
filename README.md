# GIST Project - A blog for a rare form of cancer

## Introduction:
This project is a real initiative involving an actual "client" and a genuine use case. My mother has been battling cancer since she was 18 years old, which means even before I was born. In recent years, she got affected by a rare type of tumor known as GIST. More information about GIST can be found here: https://en.wikipedia.org/wiki/Gastrointestinal_stromal_tumor. She actively participates in a GIST support group. The group has long desired to have its own blog for two main reasons: 1. to spread awareness about the disease, and 2. to simplify the process for people to connect with such a support group. Therefore, the Full Stack project was a perfect match for this purpose. Apart from myself and a friend, the individuals currently registered on the platform for testing are members of this support group.
Attention: the group is based in Berlin Germay, so some blog posts are in german!

- Live Website: https://gistproject-9ab7b71712a2.herokuapp.com/

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
Member profiles are displayed with profile pictures and usernames. At this time, the GIST group uses an Excel sheet for sharing the contact data of the group members.
The member section should be the better digital approach here.

### Security and Privacy:

User authentication ensures secure access to profile and blog management features.
Users can log out to secure their sessions. 
Author profiles are only for registred users visiable.

### Public Accessibility:

Blog articles are publicly accessible, allowing users to read content without registering or logging in.

### Filters:

A filter is available to categorize blog posts by category.

### Rich Text Editing:

Use the Quill rich text editor to enable users to format and style their blog posts effectively.

### Image Upload:

User are able to upload images to their profile and to the blog articles.

### Default Images:

Default images are automatically created for the user profile and articles if no own images are uploaded.

## Features left to implement (because it's a real life project, these features are really planend for the next 6-12 months):

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
- Resize uploaded images

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

<details>
<summary>
"Wireframe Images"
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

### Design decisions:

the initial plan was to use minimalistic CSS to keep the site clear and simple.
Unfortunately, most of the time was spent on functionality. Therefore, the website consists of simple CSS tables and a gray Bootstrap navbar. The buttons follow a simple logic: blue for readmore, yellow for edit and red for delete. For the basic design I used Bootstrap and CSS Form styles.

## Database Design

### Database Model

When I started writing the code, I used a tutorial (link in the credits). I used the tutorial as inspiration for beginning with the basics of the blog.

#### User Model:

- This is the central model provided by Django's authentication system.
It handles user information such as username, password, email, first and last names.
It is used to authenticate users and manage their access rights within the application.

#### Profile Model:

- Extends the User Model by establishing a one-to-one relationship, meaning each user has a single corresponding profile.

- Stores additional user-specific information like bio, profile picture, and social media URLs.
Enhances the user's base information provided by Django's User model for a richer user profile.

#### BlogPost Model:

- Represents the blog entries or articles within the application.
Each blog post is linked to a User through a ForeignKey, indicating a many-to-one relationship where a single user can author multiple blog posts.
Contains fields such as title, content, publication date, and category for organizing and displaying posts.

#### TreatmentLog Model:

- It's a record of medical treatments associated with users.
Similar to BlogPost, it has a ForeignKey linked to the User model, allowing a user to have multiple treatment logs.
Captures details of medical treatments like dates, medication names, dosages, and side effects.

#### Category Model:

- Provides a simple classification for blog posts.
While it is not directly linked in the code you provided, typically, there would be a many-to-one relationship from BlogPost to Category (assuming a blog post belongs to a single category).
In a relational database structure, these models would translate into tables, with each field becoming a column within the table. Relationships between tables are managed by keys:

- Primary Keys (PK): Uniquely identify each record within a table.
- Foreign Keys (FK): Refer to primary keys in other tables, creating linked records across the database.

#### Entity Relationship:

![database](/documentation/assets/database.JPG "database")

#### Custom Model:

As required by the assessment criteria for this project, one custom model (the Treatment Log model) was added which was not covered by Code Institute's tutorial.

## Code Breakdown:

#### Views:

- UserRegistrationView:

Allows users to register for an account.
Uses the SignUpForm form class.
Renders the registration form using the 'registration/register.html' template.
Redirects to the 'login' page upon successful registration.

- CreateProfilePageView:

Enables users to create a profile page.
Uses the ProfilePageForm form class.
Renders the 'registration/create_member_profile_page.html' template.
Redirects to the 'index' page upon successful profile creation.

- UserEditView:

Allows users to edit their profiles.
Uses the EditProfileForm form class.
Renders the 'registration/edit_profile.html' template.
Redirects to the 'index' page upon successful profile update.

- PasswordsChangeView:

Lets users change their passwords.
Uses the PasswordChangeForm form class.
Renders the 'registration/change_password.html' template.
Redirects to the 'login' page upon successful password change.

- ProfilePageView:

Displays user profiles.
Retrieves and displays the user's profile, blog post, and treatment logs.
Uses the 'registration/user_profile.html' template.

- EditProfilePageView:

Allows users to edit their profile pages.
Uses the Profile model and the 'registration/edit_profile_page.html' template.
Handles treatment logs, including editing and saving them.

- member_profiles_view:

Retrieves all user profiles and displays them.
Uses the 'members/profile_list.html' template.

- BlogPostListView:

Lists all blog posts, ordered by publication date.
Displays categories in the context.

- BlogPostDetailView:

Displays a single blog post.

- AdminPostView:

Allows admin users to create new blog posts.
Uses the BlogPostForm form class and 'admin_post.html' template.

- AddCategoryView:

Lets users add new categories.
Uses the CategoryForm form class and 'add_category.html' template.

- CategoryView:

Displays blog posts filtered by category.

- UpdatePostView:

Allows admin users to update existing blog posts.
Uses the BlogPostForm form class and 'admin_edit_post.html' template.

- DeletePostView:

Allows admin users to delete existing blog posts.
Uses the 'admin_delete_post.html' template.

#### Models:

- Category:

Represents blog post categories.
Contains a 'name' field to store category names.

- Profile:

Represents user profiles.
Includes fields for user bio, profile picture, and social media URL.
Linked to the built-in User model through a one-to-one relationship.

- BlogPost:

Represents blog posts.
Includes fields for title, content, author, publication date, category, and snippet.
Utilizes the RichTextField for content to support rich text editing.
Linked to the User model through a foreign key relationship.

- TreatmentLog:

Represents treatment logs for users.
Contains fields for treatment date, medication name, dosage, and side effects.
Linked to the User model through a foreign key relationship.

#### Forms:

- ProfilePageForm:

A form for editing user profile information.
Includes fields for bio, profile picture, and social media URL.

- SignUpForm:

A custom registration form for user sign-up.
Includes fields for username, email, first name, last name, and password.
Customizes widget attributes and CSS classes.

- EditProfileForm:

A form for editing user profile information.
Includes fields for email, first name, last name, and password.
Customizes widget attributes and CSS classes.

- TreatmentLogForm:

A form for adding and editing treatment logs.
Includes fields for treatment date, medication name, dosage, and side effects.

- BlogPostForm:

A form for creating and editing blog posts.
Includes fields for title, content, category, snippet, and header image.
Customizes widget attributes and CSS classes.

- CategoryForm:

A form for creating and editing categories.
Includes a field for category name.

#### Templates:

- The code references template files for rendering HTML content. These templates include registration forms, user profiles, blog post views, and category management.

#### Authentication:

- Authentication-related views are implemented for user registration, password change, and login/logout functionality.
The code leverages Django's built-in authentication system and forms.

#### Rich Text Editing:

- Rich text editing is enabled for blog post content using the RichTextField provided by the Quill editor package.

#### Image Handling:

- The code handles image uploads for profile pictures and blog post header images, utilizing the ImageField for file storage.

#### URL Routing:

- URL routing and redirection are defined using reverse_lazy and URL patterns to direct users to the appropriate views.

#### Decorators:

- Decorators like login_required are used to enforce authentication and authorization for specific views.

#### Special case Add Post + Edit Post HTML Templates:

First I had integrated the CKEditor for the rich text. Unfortunately, this caused problems after deploying with Cloudinary.
I was looking for a quick and easy solution and found the Quill Editor. In the original code, I could no longer realize a simple exchange due to the deadline, so I used a workaround.

- Quill Text Editor:

Quill is a rich text editor, and the code includes the Quill CSS and JavaScript files from a CDN.
It creates a Quill editor instance in a "div" with the id quill-editor to allow users to enter rich text content for blog posts.

- Content Field Hiding:

A "style" block hides the content form field with the id id_content. This is likely done to replace the default content input with the Quill editor and sync the content between them using JavaScript.

- Hidden Content Field:

The template includes a hidden content field ({{ form.content }}) that stores the rich text content entered in the Quill editor. This field is initially hidden but is updated using JavaScript to match the content in the Quill editor.

- JavaScript:

- The JavaScript code included at the end of the template initializes the Quill editor, sets its initial content, and listens for text changes in the editor. When changes occur, it updates the hidden content form field with the Quill editor's content.

## Feature Testing + CX Issues

#### User Story testing results:

Please see below the testing sections for the site pages. I want to mention some CX issues here. I also put the W3C + CSS + Lighthouse testing screenshots in the related sections, to have a better page by page overview.

![testing](/documentation/assets/testing.JPG "testing")

#### CX issues:

- the Categorys are not accessable in the navbar from all views.
- the Admin Post is called because of the future use. The admin should post the group related infos. Other users could also post but in the separate "Members" section.
- No error message, if a user name already exists.

#### Success messages:
Starting out in software development, I learned that creating success messages wasn't part of the initial release of our project, and now I understand the reasons behind this.

Writing the User Stories: In the beginning, I was focused on what the user absolutely needed — the core functionalities like posting, signing up, and editing. At that stage, the finer details, like user feedback through success messages, didn't seem as critical to me.

Writing the Functions: When I moved into the coding phase, my goal was to get those key features to work. I put my energy into ensuring you could actually create, edit, and delete a blog post. To my beginner's mind, success messages were an additional feature, not a necessity.

Debugging: Debugging was where I spent a lot of time making sure everything functioned as intended. It was a process of solving one problem after another, and during that time, adding success messages felt like something I could do later.

Testing on Localhost: Testing was done by me, for me. Since I knew exactly how the system was supposed to work, when a blog post was successfully deleted, I didn't need a message to confirm it — but I didn't account for the fact that users wouldn't have that same insight.

Testing after Deployment: Once the project was live, I began to observe how real users interacted with the website. That's when the absence of success messages became apparent. What I thought was intuitive wasn't as clear to the users.

The project was racing against a deadline, and I had to make decisions on what to prioritize. As a beginner, I chose to ensure that the system's basic functionalities were robust and stable, which I deemed most critical.

Documentation was another area where I spent considerable time. It's essential for the long-term health of the project, so I prioritized completing it over adding user experience enhancements.

In retrospect, I see that focusing on stability and core functionality before implementing user niceties like success messages was the right call. Now that I have a stable product, I can go back and implement those success messages. Each step has been a lesson in prioritization and managing project constraints, lessons that are invaluable for a student like me just starting out in this field.

#### W3C Validator:

In the initial stages of development, I started off by crafting what I believed were standard HTML templates. Not yet experienced enough to foresee the complexities ahead, I didn't realize that the W3C validator would read the base layout and the individual page templates separately.

As I worked through the project, I constructed the site's pages using Django's template inheritance, which allows for a "base" template that contains common elements like the header and footer. Each page then extends this base, adding its own specific content. This is a powerful feature of Django, enabling me to write DRY (Don't Repeat Yourself) code and maintain consistency across the site (It was later in the process that I understood that I could use solely the django base in HTML without the classic standard (see profile_list.html -> members -> templates -> members).).

However, this approach led to an unexpected challenge with the W3C validator. It's designed to validate plain HTML and isn't aware of Django's templating mechanics. So when it reads the base template and a child template together, it sees them as two separate HTML documents instead of parts of a whole. This results in validation errors, as the validator doesn't understand that these templates will be combined into a single, well-formed HTML document when Django renders them.

With the deadline near, the realization hit me: fixing these errors by adjusting the template structure could introduce risks. If I were to alter the templates to appease the validator, I'd need to retest every page to make sure nothing broke in the process. That's a significant amount of additional work and not feasible given the time constraints.

Choosing to prioritize the functioning and delivery of the project, I've had to accept these validation errors for now. It's not ideal, and as a developer committed to best practices, I intend to address these errors after the deadline. I'll look into ways to make the templates compliant without compromising the benefits of Django's template inheritance.

This has been a valuable learning experience for me. It's taught me about the intricacies of template validation and the importance of balancing code quality with practical project constraints. As I continue to grow in this field, I'll take this knowledge forward to build more robust and standards-compliant websites.

#### Important: The user-related pages for the profile and the posts cannot be read by the validator for security reasons. Good for security, bad for validation. In future, it would be better to handle it in a similar way to Facebook. If an attempt is made to hack a page, there should be a redirect to the login.

#### Python Linter:

When I began coding, I wasn't completely aware of Python's style conventions, like the recommended line lengths from PEP 8, Python's official style guide. It recommends keeping lines of code under a certain length for better readability. However, as a beginner, I was more concerned with writing code that executed correctly rather than strictly adhering to style guidelines.

As the project progressed, my Python files grew in both number and complexity. I started to see warnings about long lines and other style issues, but by then, the codebase had become quite extensive. Realizing the magnitude of the task, I faced the reality that fixing all these style issues would be a significant undertaking. Given the intricate web of Django's app structure, each Python file contains a piece of the larger puzzle, from views and models to forms and utility scripts.

Now, with the deadline for the project approaching, I have to make strategic choices. Refactoring the code to fix style issues would mean combing through numerous files and lines of code, and it would also require retesting to ensure nothing was inadvertently broken during the cleanup process. It's a time-consuming task that, while important for maintainability and readability, isn't as critical as ensuring the website functions correctly for its users.

Therefore, I've made the decision to prioritize the website's functionality and user experience over code styling for the time being. The Python code, while not perfectly styled, works, and it meets the users' needs. After the deadline, when there's more breathing room, I plan to gradually refactor the code. I'll improve its adherence to PEP 8, enhancing the readability and maintainability for future developers and for myself.


### Index

<details>
<summary>
Testing Index + W3C Validator + CSS Validator + Lighthouse
</summary>

![index](/documentation/assets/index.JPG "index")

### W3C Validator

![index_w3c](/documentation/assets/index_w3c.JPG "index_w3c")

### CSS Validator

![index_css](/documentation/assets/index_css.JPG "index_css")

### Lighthouse Desktop

![index_desktop](/documentation/assets/index_desktop.JPG "index_desktop")

### Lighthouse Mobile

![index_mobile](/documentation/assets/index_mobile.JPG "index_mobile")

</details>

### Sign Up

<details>
<summary>
Testing Sign Up + W3C Validator + CSS Validator + Lighthouse
</summary>

![signup](/documentation/assets/signup.JPG "signup")

### W3C Validator

![signup_w3c](/documentation/assets/signup_w3c.JPG "signup_w3c")

### CSS Validator

![signup_css](/documentation/assets/signup_css.JPG "signup_css")

### Lighthouse Desktop

![signup_desktop](/documentation/assets/signup_desktop.JPG "signup_desktop")

### Lighthouse Mobile

![signup_mobile](/documentation/assets/index_mobile.JPG "signup_mobile")

</details>

### Login

<details>
<summary>
Testing Login + W3C Validator + CSS Validator + Lighthouse
</summary>

![login](/documentation/assets/login.JPG "login")

### W3C Validator

![login_w3c](/documentation/assets/login_w3c.JPG "login_w3c")

### CSS Validator

![login_css](/documentation/assets/login_css.JPG "login_css")

### Lighthouse Desktop

![login_desktop](/documentation/assets/login_desktop.JPG "login_desktop")

### Lighthouse Mobile

![login_mobile](/documentation/assets/login_mobile.JPG "login_mobile")

</details>

### Create Profile

<details>
<summary>
Testing Create Profile + W3C Validator + CSS Validator + Lighthouse
</summary>

![create](/documentation/assets/create.JPG "create")

### W3C Validator

![create_w3c](/documentation/assets/create_w3c.JPG "create_w3c")

### CSS Validator

![create_css](/documentation/assets/create_css.JPG "create_css")

### Lighthouse Desktop

![create_desktop](/documentation/assets/create_desktop.JPG "create_desktop")

### Lighthouse Mobile

![create_mobile](/documentation/assets/create_mobile.JPG "create_mobile")

### Security Message

![post_message](/documentation/assets/post_message.JPG "post_message")

### Default Image

![default](/documentation/assets/default.JPG "default")

</details>

### User Profile

<details>
<summary>
Testing User Profile functions + W3C Validator + CSS Validator + Lighthouse
</summary>

### User Profile

![treatment](/documentation/assets/treatment.JPG "treatment")

### W3C Validator

![profile_w3c](/documentation/assets/profile_w3c.JPG "profile_w3c")

### CSS Validator

![profile_css](/documentation/assets/profile_css.JPG "profile_css")

### Lighthouse Desktop

![profile_desktop](/documentation/assets/profile_desktop.JPG "profile_desktop")

### Lighthouse Mobile

![profile_mobile](/documentation/assets/profile_mobile.JPG "profile_mobile")

### Edit Settings

![settings](/documentation/assets/settings.JPG "settings")

### W3C Validator

![settings_w3c](/documentation/assets/settings_w3c.JPG "settings_w3c")

### CSS Validator

![settings_css](/documentation/assets/settings_css.JPG "settings_css")

### Lighthouse Desktop

![settings_desktop](/documentation/assets/settings_desktop.JPG "settings_desktop")

### Lighthouse Mobile

![settings_mobile](/documentation/assets/settings_mobile.JPG "settings_mobile")

### Change Password

![password](/documentation/assets/password.JPG "password")

### W3C Validator

![password_w3c](/documentation/assets/password_w3c.JPG "password_w3c")

### CSS Validator

![password_css](/documentation/assets/password_css.JPG "password_css")

### Lighthouse Desktop

![password_desktop](/documentation/assets/password_desktop.JPG "password_desktop")

### Lighthouse Mobile

![password_mobile](/documentation/assets/password_mobile.JPG "password_mobile")

### Edit Profile Infos

![infos](/documentation/assets/infos.JPG "infos")

### W3C Validator

![info_w3c](/documentation/assets/info_w3c.JPG "info_w3c")

### CSS Validator

![info_css](/documentation/assets/info_css.JPG "info_css")

### Lighthouse Desktop

![info_desktop](/documentation/assets/password_desktop.JPG "info_desktop")

### Lighthouse Mobile

![info_mobile](/documentation/assets/password_mobile.JPG "info_mobile")

</details>

### Blog Posts

<details>
<summary>
Testing Blog Posts + W3C Validator + CSS Validator + Lighthouse
</summary>

### Posts view for unregistred users (without author)

![auth_not](/documentation/assets/auth_not.JPG "auth_not")

### Posts view for registred users (with author)

![auth](/documentation/assets/auth.JPG "auth")

### W3C Validator

![article_w3c](/documentation/assets/article_w3c.JPG "article_w3c")

### CSS Validator

![article_css](/documentation/assets/article_css.JPG "article_css")

### Lighthouse Desktop

![article_desktop](/documentation/assets/article_desktop.JPG "article_desktop")

### Lighthouse Mobile

![article_mobile](/documentation/assets/article_mobile.JPG "article_mobile")

### Add Blog Post

![post](/documentation/assets/post.JPG "post")

### Default Image

![post_default](/documentation/assets/post_default.JPG "post_default")

### W3C Validator

![post_w3c](/documentation/assets/post_w3c.JPG "post_w3c")

### CSS Validator

![post_css](/documentation/assets/post_css.JPG "post_css")

### Lighthouse Desktop

![post_desktop](/documentation/assets/post_desktop.JPG "post_desktop")

### Lighthouse Mobile

![post_mobile](/documentation/assets/post_mobile.JPG "post_mobile")

### Security Message

![post_security](/documentation/assets/post_security.JPG "post_security")

### Delete Post

![delete](/documentation/assets/delete.JPG "delete")

### W3C Validator

![delete_w3c](/documentation/assets/delete_w3c.JPG "delete_w3c")

### CSS Validator

![delete_css](/documentation/assets/delete_css.JPG "delete_css")

### Lighthouse Desktop

![delete_desktop](/documentation/assets/delete_desktop.JPG "delete_desktop")

### Lighthouse Mobile

![delete_mobile](/documentation/assets/delete_mobile.JPG "delete_mobile")

### Security Message

![delete_auth](/documentation/assets/delete_auth.JPG "delete_auth")

</details>

### Categorys

<details>
<summary>
Testing Categorys + W3C Validator + CSS Validator + Lighthouse
</summary>

### Category View

![category_view](/documentation/assets/category_view.JPG "category_view")

### W3C Validator

![category_w3c](/documentation/assets/category_w3c.JPG "category_w3c")

### CSS Validator

![category_css](/documentation/assets/category_css.JPG "category_css")

### Lighthouse Desktop

![category_desktop](/documentation/assets/category_desktop.JPG "category_desktop")

### Lighthouse Mobile

![category_mobile](/documentation/assets/category_mobile.JPG "category_mobile")

### Add Category

![add](/documentation/assets/add.JPG "add")

### W3C Validator

![add_w3c](/documentation/assets/add_w3c.JPG "add_w3c")

### CSS Validator

![add_css](/documentation/assets/add_css.JPG "add_css")

### Lighthouse Desktop

![add_desktop](/documentation/assets/add_desktop.JPG "add_desktop")

### Lighthouse Mobile

![add_mobile](/documentation/assets/add_mobile.JPG "add_mobile")

</details>

### Members Section

<details>
<summary>
Testing Members Section + W3C Validator + CSS Validator + Lighthouse
</summary>

### Members Profiles

![members_profiles](/documentation/assets/members_profiles.JPG "members_profiles")

### W3C Validator

![members_w3c](/documentation/assets/members_w3c.JPG "members_w3c")

### CSS Validator

![members_css](/documentation/assets/members_css.JPG "members_css")

### Lighthouse Desktop

![members_desktop](/documentation/assets/category_desktop.JPG "members_desktop")

### Lighthouse Mobile

![members_mobile](/documentation/assets/category_mobile.JPG "members_mobile")

</details>

### Python Linter (testing all relevant files: views, urls, models, forms)

<details>
<summary>
Python Linter Testing
</summary>

#### forms_member
![forms_member](/documentation/assets/forms_member.JPG "forms_member")

#### forms_blog
![forms_blog](/documentation/assets/forms_blog.JPG "forms_blog")

#### model_blog
![model_blog](/documentation/assets/model_blog.JPG "model_blog")

#### url_blog
![url_blog](/documentation/assets/url_blog.JPG "url_blog")

#### url_member
![url_member](/documentation/assets/url_member.JPG "url_member")

#### views_blog
![views_blog](/documentation/assets/views_blog.JPG "views_blog")

#### views_member
![views_member](/documentation/assets/views_member.JPG "views_member")

</details>

### Responsive Design (using Chrome dev tools)

![responsive](/documentation/assets/responsive.JPG "responsive")

![responsive2](/documentation/assets/responsive2.JPG "responsive2")

## Deployment Process Description

- This project's deployment utilized several services: Heroku, Cloudinary, ElephantSQL, and Quill Text Editor.

#### Library Installation Guide

- To successfully deploy this project on Heroku, follow these steps to install the required libraries. This guide doesn't cover the necessary requirements and settings adjustments post-installation, as they are considered standard follow-up actions.

- To install Gunicorn (Django's server for Heroku), run: pip3 install django gunicorn
- For psycopg2 (PostgreSQL connector), use: pip3 install dj_database_url psycopg2
- To install Cloudinary (for hosting static files and images), enter: pip3 install dj3-cloudinary-storage
- For Quill (to solve Heroku's custom stylesheet rendering issues), execute: pip install django-quill-editor

#### Setting Up the Heroku App

- Sign in to Heroku and access the Dashboard.
Select "New" and choose "Create new app" from the dropdown menu.
Name the app suitably, select a relevant region, and click "Create App".

#### Creating a PostgreSQL Database with ElephantSQL

- This step is crucial for setting up a Heroku-accessible database, as Django's default database isn't compatible with deployed Heroku apps.

- Log into ElephantSQL and navigate to the Dashboard.
Click "Create New Instance."
Choose a plan (e.g., the free "Tiny Turtle" plan), provide a Name (project name), and select a region for the Data center. Tags are optional.
Review your choices and click "Create Instance."
Back in the Dashboard, click on your new instance's name.
Copy the database URL from the instance details.

#### Securing Sensitive Information

- Create an env.py file and add it to the .gitignore.
- In env.py, import os and set the DATABASE_URL environment variable with the URL from ElephantSQL. 
- Example: os.environ["DATABASE_URL"] = "< copiedURL >".
- Set the SECRET_KEY variable inventively. 
- Example: os.environ["SECRET_KEY"] = "mysecretkey".

#### Updating Settings

- At the top of settings.py, add:

- import os
- import dj_database_url
- if os.path.isfile('env.py'):
-    import env

- Replace Django's default SECRET_KEY in settings.py with SECRET_KEY = os.environ.get('SECRET_KEY').

- Update the DATABASES setting to:

- DATABASES = {
-    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
- }

- Save and migrate all changes.

- Connecting Heroku to Database

- In the Heroku dashboard, under the Settings tab, add config vars for 
-DATABASE_URL, SECRET_KEY, and 
- PORT (value "8000").

#### Integrating Cloudinary

- Copy the API Environment variable from the Cloudinary dashboard.

In env.py, set 
- os.environ["CLOUDINARY_URL"] = "< copied_variable" >, 
- removing CLOUDINARY_URL= from the string.

Add this variable to Heroku config vars as CLOUDINARY_URL.

In settings.py, under INSTALLED_APPS, add cloudinary_storage above django.contrib.staticfiles and cloudinary below it.

- Define Cloudinary for static file storage:

- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
- Allow Heroku as a host in settings.py:
- ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']

## Deploy:

#### Forking a Repo on GitHub:

- Navigate to the GitHub repo: https://github.com/renebaumann3000/gist_project
- Click the "Fork" button in the top-right corner of the repo page.
- This will create a copy of the repository under your GitHub account.
- You can then clone or download the repo as needed.
- Deploying on Heroku ->

#### Heroku Setup:

- Sign up for a Heroku account if you haven't already: https://signup.heroku.com/

#### Access Deployment Configuration:

- Once logged into Heroku, navigate to the "Deploy" section of your app's dashboard.

#### Choose Deployment Method:

- Under the deployment methods, choose "GitHub" as your preferred method.

#### Connect to GitHub:

- Ensure your connection to GitHub is confirmed.
- Use the search function provided in this section to locate your repository. In this context, the repository was named "gist_project". Once found, connect to it.

### Deployment Options:

#### Automatic Deploys: 
- By enabling this, Heroku will automatically rebuild and redeploy the app every time you push a new change to the connected GitHub repository.

#### Manual Deploy:

- If you prefer more control over when the app gets deployed and the ability to view deployment logs, you can choose the "deploy branch" option.
- When ready, you can manually initiate the deployment process for your specific branch.

## Credits:
Inspiration Tutorial: Youtube: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=1

Default images:

- Post default: https://www.bronsonhealth.com/news/breast-cancer-prevention-and-treatment/
- Profile default: https://www.freepik.com/icon/profile_10015419

Code is written by myself with help from:

- Mentor
- Friends




