# Movie Tracker

**Movie Tracker** is a Django web application designed for film enthusiasts to build and manage a personal movie catalog, categorize titles by genre, maintain a viewer profile, and write ratings and reviews for watched movies.

## Table of Contents

* [Project Overview](#project-overview)
* [Installation & Setup](#installation--setup)
* [Usage Guide](#usage-guide)
* [Features & Architecture](#features--architecture)
* [Database Models](#database-models)
* [Author & Credits](#author--credits)

## Project Overview

**Movie Tracker** solves the problem of keeping track of watched films, personal ratings, and thoughts in one clean, distraction-free interface. Instead of relying on cluttered spreadsheets or notes, users can organize movies by genre, filter and sort their watchlist, and attach structured reviews directly to each title.

The application is built with the **Django** framework using modular apps, Class-Based and Function-Based Views, custom template filters, and reusable partial templates.

## Installation & Setup

No external environment variables (`.env`) or third-party database credentials are required - the project runs out of the box with **SQLite**.

1. **Clone the repository**

   ```bash
   git clone https://github.com/Azra-A/movieTracker.git
   cd movieTracker
   ```

2. **Create and activate a virtual environment**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

## Usage Guide

1. Open **`http://127.0.0.1:8000/`** in your web browser.
2. **Create a Profile:** Navigate to **Profile** in the top navigation bar to set up your viewer profile (required before submitting movie reviews).
3. **Add Genres:** Click **Add Genre** in the navigation bar to create custom film genres.
4. **Add & Explore Movies:** Use **Add Movie** to add films to the catalog, then filter by genre or sort by release year and title on the home page.
5. **Write Reviews:** Open any movie's details page and click **Write a review** to submit a rating (1-5 stars) and a comment.

## Features & Architecture

### Key Features

* **Full CRUD Operations:** Create, view, edit, and delete movies, user profiles, and reviews, plus genre creation and deletion.
* **Catalog Filtering & Sorting:** Filter the movie catalog by genre and sort titles by newest, oldest, or alphabetically (`A-Z`).
* **Custom Template Filter:** Includes a `star_rating` filter (`reviews/templatetags/review_filters.py`) that renders numeric ratings into visual star icons (`★★★★☆`).
* **Reusable Templates & Partials:** Uses `base.html` template inheritance, shared `common/header.html` and `common/footer.html` partials, and a custom `404.html` error page.
* **Empty Database Ready:** All records (`Genre`, `Movie`, `Profile`, `Review`) can be created and managed directly through the UI without accessing the Django Admin panel.

### Modular Project Structure

| App / Directory | Responsibility |
| :--- | :--- |
| **`movies`** | Manages the movie catalog (`Movie`) and categories (`Genre`), including filtering and sorting. |
| **`profiles`** | Handles user profile creation, editing, deletion, and displays user review history. |
| **`reviews`** | Manages movie ratings and reviews (`Review`) along with the custom `star_rating` template filter. |
| **`templates/`** | Contains `base.html`, `home-page.html`, `404.html`, `common/` partials, and app-specific templates. |
| **`static/`** | Stores custom CSS stylesheets (`css/style.css`) for responsive layout and design. |

## Database Models

The schema uses **4 models** demonstrating **Many-to-Many** and **Many-to-One (`ForeignKey`)** relationships:

| Model | App | Key Fields & Relationships |
| :--- | :--- | :--- |
| **`Genre`** | `movies` | `name` (unique) |
| **`Movie`** | `movies` | `title`, `release_year`, `description`, `poster_url`, `genres` (**Many-to-Many** with `Genre`) |
| **`Profile`** | `profiles` | `username`, `email`, `region` (choices), `bio`, `profile_picture`, `activated_at` |
| **`Review`** | `reviews` | `content`, `rating` (`1–5`), `created_at`, `movie` (**ForeignKey**), `profile` (**ForeignKey**) |

## Author & Credits

* **Author:** [Azra Ahmedova](https://github.com/Azra-A)
* **Course:** Python Web - Django Basics @ [SoftUni](https://softuni.bg/)
