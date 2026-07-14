# MCQ Application

This repository is built with strict enterprise engineering standards, focusing on resilient architecture, graceful error handling, and robust continuous integration.

## 🏗️ System Architecture

```mermaid
graph TD
    User([User Client]) -->|HTTP Request| Nginx(NGINX Web Server)
    Nginx -->|Serves Static Files| App[Frontend Application (src/)]
    
    subgraph Frontend Logic
        App -->|Renders UI| Render[render()]
        App -->|Initializes Quiz| Init[initQuiz()]
        App -->|Handles Input| Select[select()]
    end

    App --> MathJax[MathJax CDN]
```

## 🚀 Setup Instructions

Follow these step-by-step instructions to get the application running locally using Docker:

1. **Clone the repository** (if not already done).
2. **Navigate to the project directory**:
   ```bash
   cd mcq
   ```
3. **Start the application with Docker Compose**:
   ```bash
   docker-compose up --build -d
   ```
4. **Access the application**: Open your web browser and navigate to `http://localhost:8080`.

## 📂 Structure

Following standard design patterns for a predictable layout:
- `src/`: Contains the main application logic and static files (`index.html`).
- `tests/`: Contains automated test scripts.
- `.github/workflows/`: CI/CD pipelines.

## 📦 Dependency Rationale

- **NGINX (Alpine)**: Selected for its lightweight footprint and high performance when serving static files. The Alpine variant ensures the image size remains minimal, reducing attack surface and pull times.
- **MathJax (CDN)**: Used to render complex mathematical formulas seamlessly in the browser without requiring heavy build steps or server-side rendering.
- **Docker & Docker Compose**: Ensures environment consistency across development and production, allowing predictable builds and easy scaling.