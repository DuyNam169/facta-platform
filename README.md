FACTA – AI-Powered Social Media Platform for Verified Information
FACTA is a research and development platform that functions as a social media network leveraging artificial intelligence to facilitate the reading and sharing of accurate, secure, and trustworthy information. The system is designed with scalability, security, and long-term maintainability in mind.
Project Goals

Provide a social media platform for accurate information sharing
Implement AI-powered content verification and validation
Ensure information security and user privacy
Build a production-ready architecture using modern technologies
Establish secure and isolated infrastructure using Docker

System Architecture
FACTA Platform
│
├── Frontend        (React + TypeScript)
├── API Gateway     (NestJS)
├── AI Service      (FastAPI - Python)
│
├── PostgreSQL      (Relational database)
├── MongoDB         (Document database)
├── Redis           (Cache & session store)
│
└── Docker Compose  (Infrastructure layer)
Technologies Used
Backend

Node.js + NestJS
Python + FastAPI

Frontend

React + TypeScript
HTML / CSS / JavaScript

Databases

PostgreSQL 15 – structured and transactional data
MongoDB 7 – flexible schema / unstructured data
Redis 7 – cache, session, rate limiting

Infrastructure

Docker
Docker Compose

Timezone Configuration

System timezone: Asia/Ho_Chi_Minh (UTC+7)
Docker containers are configured with: TZ=Asia/Ho_Chi_Minh
Backend services should internally use UTC and convert to local time at presentation layer if needed.

Project Structure
facta-platform/
├── frontend/
├── api-gateway/
├── ai-service/
├── infra/
│   ├── docker-compose.yml
│   └── .env
├── docs/
└── README.md
Prerequisites (Required)
Before running the project, ensure you have the following installed:
Install Docker
Download Docker Desktop from:
https://www.docker.com/products/docker-desktop
After installation, verify:
bashdocker --version
Install Docker Compose
Docker Desktop already includes Docker Compose. Verify installation:
bashdocker compose version
Note: You do NOT need to install PostgreSQL, MongoDB, or Redis locally.
Environment Variables Setup
Create a .env file inside the infra/ directory:
bash# ===============================
# FACTA - Database Configuration
# ===============================

POSTGRES_DB=facta_core
POSTGRES_USER=<your POSTGRES_USER>
POSTGRES_PASSWORD=<your POSTGRES_PASSWORD>
Security note:

Do not commit .env to public repositories
Change credentials for production environments

Docker Compose Configuration
File: infra/docker-compose.yml
yamlservices:
  facta-postgres:
    image: postgres:15
    container_name: facta-postgres
    restart: unless-stopped
    env_file:
      - .env
    environment:
      TZ: Asia/Ho_Chi_Minh
    ports:
      - "127.0.0.1:5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - facta-net

  facta-mongo:
    image: mongo:7
    container_name: facta-mongo
    restart: unless-stopped
    environment:
      TZ: Asia/Ho_Chi_Minh
    ports:
      - "127.0.0.1:27017:27017"
    volumes:
      - mongo_data:/data/db
    networks:
      - facta-net

  facta-redis:
    image: redis:7
    container_name: facta-redis
    restart: unless-stopped
    environment:
      TZ: Asia/Ho_Chi_Minh
    ports:
      - "127.0.0.1:6379:6379"
    networks:
      - facta-net

volumes:
  postgres_data:
  mongo_data:

networks:
  facta-net:
    driver: bridge
How to Run the Databases
Step 1: Open terminal
Navigate to the infra/ directory:
bashcd infra
Step 2: Start services
bashdocker compose up -d
Step 3: Verify running containers
bashdocker ps
```

You should see:
- facta-postgres
- facta-mongo
- facta-redis

## Database Connection Details

### PostgreSQL
- Host: localhost
- Port: 5432
- Database: facta_core
- Username: facta_admin
- Password: from .env

Recommended tools: DBeaver, pgAdmin

### MongoDB
Connection URI:
```
mongodb://localhost:27017
Recommended tool: MongoDB Compass
Redis

Host: localhost
Port: 6379

Recommended tools: Redis Insight, redis-cli
Do I Need to Install Databases Locally?
No. Docker containers already include:

PostgreSQL
MongoDB
Redis

Your host machine only needs:

Docker
Docker Compose

Check Timezone Inside Containers
Example (PostgreSQL container):
bashdocker exec -it facta-postgres date
Expected output: Asia/Ho_Chi_Minh
Security Best Practices

Databases are bound to 127.0.0.1 only
Containers run inside an isolated Docker network
No direct public exposure
Credentials managed via environment variables

Future Improvements

Authentication and authorization (RBAC)
AI model integration for content verification
Audit logging
Horizontal scaling
CI/CD pipeline

License
This project is intended for educational and research purposes. It can be extended into a production system in the future.