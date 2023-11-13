import os
import json

# Load existing posts from file
def load_posts():
    if os.path.exists('blog_posts.txt'):
        with open('blog_posts.txt', 'r') as file:
            try:
                posts = json.load(file)
            except json.JSONDecodeError:
                posts = {}
    else:
        posts = {}
    return posts

# Save posts to file
def save_posts(posts):
    with open('blog_posts.txt', 'w') as file:
        json.dump(posts, file)

# Create a new post
def create_post():
    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")
    post = {'title': title, 'content': content}
    return post

# Add a new post to the posts dictionary
def add_post(posts, post):
    post_id = len(posts) + 1
    posts[post_id] = post
    print(f"Post #{post_id} added successfully!")

# Edit an existing post
def edit_post(posts, post_id):
    if post_id in posts:
        new_content = input("Enter the new content for the post: ")
        posts[post_id]['content'] = new_content
        print(f"Post #{post_id} edited successfully!")
    else:
        print(f"Post #{post_id} not found.")

# Delete an existing post
def delete_post(posts, post_id):
    if post_id in posts:
        del posts[post_id]
        print(f"Post #{post_id} deleted successfully!")
    else:
        print(f"Post #{post_id} not found.")

# Display all posts
def display_posts(posts):
    for post_id, post in posts.items():
        print(f"\n#{post_id}\nTitle: {post['title']}\nContent: {post['content']}")

# Main function
def main():
    posts = load_posts()

    while True:
        print("\n===== Blog Menu =====")
        print("1. Create a new post")
        print("2. Edit an existing post")
        print("3. Delete a post")
        print("4. Display all posts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            post = create_post()
            add_post(posts, post)
        elif choice == '2':
            post_id = int(input("Enter the post ID to edit: "))
            edit_post(posts, post_id)
        elif choice == '3':
            post_id = int(input("Enter the post ID to delete: "))
            delete_post(posts, post_id)
        elif choice == '4':
            display_posts(posts)
        elif choice == '5':
            save_posts(posts)
            print("Exiting the blog system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
