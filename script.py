import zipfile
import os

# Define the directory where the files will be located
directory = "/mnt/data/EbooksCentralHubTemplate/"

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Define the list of files and their contents to include in the zip file
files = {
    "index.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Home</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Welcome Section -->
    <header>
        <h1>Welcome to EbooksCentralHub</h1>
        <p>Your premier destination for a diverse selection of eBooks and engaging content.</p>
    </header>

    <!-- Featured eBooks -->
    <section id="featured-ebooks">
        <h2>Featured eBooks</h2>
        <div class="carousel">
            <!-- Example eBook items -->
            <div class="ebook-item">
                <img src="cover1.jpg" alt="Ebook 1">
                <h3>Ebook Title 1</h3>
                <p>Short description of Ebook 1.</p>
            </div>
            <div class="ebook-item">
                <img src="cover2.jpg" alt="Ebook 2">
                <h3>Ebook Title 2</h3>
                <p>Short description of Ebook 2.</p>
            </div>
        </div>
    </section>

    <!-- Latest Blog Posts -->
    <section id="latest-blog-posts">
        <h2>Latest Blog Posts</h2>
        <div class="blog-posts">
            <article>
                <h3>Blog Post Title 1</h3>
                <p>Excerpt from blog post 1...</p>
            </article>
            <article>
                <h3>Blog Post Title 2</h3>
                <p>Excerpt from blog post 2...</p>
            </article>
        </div>
    </section>

    <!-- Call to Action -->
    <section id="cta">
        <a href="shop.html" class="button">Explore the Shop</a>
        <a href="blog.html" class="button">Read the Blog</a>
        <a href="contact.html" class="button">Contact Us</a>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>

    <script src="scripts.js"></script>
</body>
</html>
""",
    "about.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - About</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- About Us Section -->
    <section>
        <h1>About Us</h1>
        <p>At EbooksCentralHub, we believe in the transformative power of stories. Our journey began with a passion for reading and a commitment to making literature accessible to everyone. Our mission is to provide a platform that connects authors with readers and enriches the reading experience through a wide range of digital content.</p>
        
        <h2>Our Story</h2>
        <p>Learn about the inception of EbooksCentralHub, our mission, vision, and the team behind it.</p>

        <h2>Values and Goals</h2>
        <p>Information on the core values and long-term goals of EbooksCentralHub.</p>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "shop.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Shop</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Shop Section -->
    <section>
        <h1>Shop</h1>
        <h2>eBook Categories</h2>
        <p>Browse our extensive eBook Categories, where you'll find a rich selection of genres including Fiction, Non-Fiction, Self-Help, Education, and more.</p>
        
        <div class="product-listing">
            <!-- Product example -->
            <div class="product-item">
                <img src="cover1.jpg" alt="Ebook 1">
                <h3>eBook Title 1</h3>
                <p>Author: John Doe</p>
                <p>Price: $9.99</p>
                <a href="#" class="button">View Details</a>
            </div>
            <div class="product-item">
                <img src="cover2.jpg" alt="Ebook 2">
                <h3>eBook Title 2</h3>
                <p>Author: Jane Doe</p>
                <p>Price: $12.99</p>
                <a href="#" class="button">View Details</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "blog.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Blog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Blog Section -->
    <section>
        <h1>Blog</h1>
        <div class="blog-categories">
            <h2>Blog Categories</h2>
            <p>Explore categories like Writing Tips, Book Reviews, and Author Interviews.</p>
        </div>

        <div class="recent-posts">
            <h2>Recent Posts</h2>
            <article>
                <h3>Blog Post Title 1</h3>
                <p>Excerpt from blog post 1...</p>
                <a href="#" class="button">Read More</a>
            </article>
            <article>
                <h3>Blog Post Title 2</h3>
                <p>Excerpt from blog post 2...</p>
                <a href="#" class="button">Read More</a>
            </article>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "contact.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Contact</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Contact Section -->
    <section>
        <h1>Contact Us</h1>
        <p>Email: contact@ebookscentralhub.com</p>
        <p>Phone: (123) 456-7890</p>
        <p>Address: 123 Book Street, Literature City</p>

        <h2>Send Us a Message</h2>
        <form action="#" method="post">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit" class="button">Send</button>
        </form>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "services.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Services Section -->
    <section>
        <h1>Freelance Writing Services</h1>
        <p>Enhance your writing with our professional Freelance Writing Services. We offer a range of services, including proofreading, ghostwriting, and editing, tailored to meet your specific needs and help you achieve your writing goals.</p>
        
        <h2>Our Services</h2>
        <ul>
            <li>Proofreading</li>
            <li>Ghostwriting</li>
            <li>Editing</li>
            <li>Content Creation</li>
        </ul>

        <h2>Portfolio</h2>
        <p>View our portfolio to see examples of our work and read testimonials from satisfied clients.</p>

        <h2>Contact Us for Services</h2>
        <form action="#" method="post">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Describe Your Project" required></textarea>
            <button type="submit" class="button">Request a Quote</button>
        </form>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "coloring.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EbooksCentralHub - Coloring Pages</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="shop.html">Shop</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="coloring.html">Coloring Pages</a></li>
        </ul>
    </nav>

    <!-- Printable Coloring Pages Section -->
    <section>
        <h1>Printable Coloring Pages</h1>
        <p>Unleash your creativity with our Printable Coloring Pages. Browse our gallery, organized by themes such as Animals, Mandalas, and Inspirational Quotes, and find the perfect designs to relax and enjoy.</p>
        
        <div class="coloring-gallery">
            <!-- Example coloring page -->
            <div class="coloring-item">
                <img src="coloring1.jpg" alt="Coloring Page 1">
                <p>Theme: Animals</p>
                <a href="#" class="button">Download</a>
            </div>
            <div class="coloring-item">
                <img src="coloring2.jpg" alt="Coloring Page 2">
                <p>Theme: Mandalas</p>
                <a href="#" class="button">Download</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 EbooksCentralHub. All rights reserved.</p>
        <div class="social-media">
            <a href="https://facebook.com">Facebook</a>
            <a href="https://twitter.com">Twitter</a>
            <a href="https://instagram.com">Instagram</a>
        </div>
    </footer>
</body>
</html>
""",
    "styles.css": """
/* styles.css */

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

nav {
    background-color: #333;
    padding: 10px;
}

nav ul {
    list-style-type: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

header {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 50px 0;
}

section {
    padding: 20px;
    margin: 20px;
}

#featured-ebooks .carousel {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}

.ebook-item, .blog-posts article {
    background-color: white;
    margin: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
}

#cta {
    text-align: center;
    margin: 20px 0;
}

.button {
    background-color: #333;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
}

.button:hover {
    background-color: #555;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
}

footer .social-media a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}
""",
    "scripts.js": """
// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize carousel for featured eBooks
    initializeCarousel();
    // Load latest blog posts
    loadLatestBlogPosts();
});

function initializeCarousel() {
    // Implement carousel logic if needed
    console.log('Carousel initialized');
}

function loadLatestBlogPosts() {
    // This function would fetch and display latest blog posts dynamically
    console.log('Loaded latest blog posts');
}
"""
}

# Write files to directory
for filename, content in files.items():
    with open(os.path.join(directory, filename), 'w') as f:
        f.write(content)

# Create a zip file
zip_filename = "/mnt/data/EbooksCentralHubTemplate.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for filename in files:
        zipf.write(os.path.join(directory, filename), filename)

zip_filename
