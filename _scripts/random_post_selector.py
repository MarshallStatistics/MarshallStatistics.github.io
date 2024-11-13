import os
import random
import yaml

def get_post_urls(posts_dir='_posts'):
    posts = []
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md') or filename.endswith('.html'):
            post_path = os.path.join(posts_dir, filename)
            with open(post_path, 'r') as file:
                front_matter = ""
                for line in file:
                    if line.strip() == '---':
                        if front_matter:
                            break
                        else:
                            front_matter = line
                    elif front_matter:
                        front_matter += line
                post_data = yaml.safe_load(front_matter)
                if 'url' in post_data:
                    posts.append(post_data['url'])
                else:
                    url = os.path.splitext(filename)[0]
                    url = "/" + url.replace(" ", "-")
                    posts.append(url)
    return posts

def select_random_post(posts):
    return random.choice(posts)

posts_dir = '_posts'
post_urls = get_post_urls(posts_dir)
random_post_url = select_random_post(post_urls)

# Save the random post URL to an HTML snippet
html_snippet = f'<script>var randomPostURL = "{random_post_url}";</script>'
with open('_includes/random_post.html', 'w') as file:
    file.write(html_snippet)

print(f"Random Post URL: {random_post_url}")
