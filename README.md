# SecAuthAPI — AI-Powered Secure Gateway & API

**Status: Early development · In progress**

SecAuthAPI is a Python backend project that I’m developing into an AI-powered secure gateway and API. The goal is to combine authentication, access control, and AI-assisted analysis of API activity with a containerized deployment on AWS.

I’m starting with the authentication and database foundation, then building toward the gateway, AI, and cloud components.

## Project Vision

The completed project is intended to authenticate users, enforce access permissions, and evaluate incoming API activity before allowing access to protected functionality.

I plan to explore AI-assisted detection of suspicious request or login patterns. The AI component would supplement explicit security controls; authentication and authorization would remain responsible for enforcing access.

The AI approach, model, and evaluation criteria are still being defined.

## Current Foundation

The repository currently contains:

- A FastAPI application entry point and root endpoint definition.
- SQLAlchemy database configuration using SQLite.
- A user model with email and hashed-password fields.
- Pydantic request and response schemas with email validation and password-length constraints.
- A password-hashing utility using Passlib with bcrypt.

These are initial components, not a completed authentication service or gateway. The uploaded application references a user-routing module that is not yet included, and the package structure and setup instructions are still being finalized.

## Planned Features

### Authentication and API Security

- User registration and login.
- Short-lived JWT authentication.
- Protected API endpoints.
- Role-based access control.
- Input validation and consistent error handling.
- Security decisions informed by OWASP API security guidance.

### Secure Gateway and AI

- A gateway layer for evaluating requests to protected API functionality.
- Logging of relevant authentication and request events.
- An AI-assisted component for identifying potentially suspicious activity.
- Evaluation of detection quality, including false positives.
- Clear documentation of the AI component’s capabilities and limitations.

### Testing and Deployment

- Automated unit and integration tests.
- Docker containerization of the application and its required components.
- Deployment to AWS.
- Least-privilege AWS IAM roles and policies scoped to the resources each component needs.
- Environment-based configuration and appropriate handling of secrets.
- Deployment documentation and operational logging.

The AWS services and final deployment architecture are still being selected.

## Technology

| Area | Current foundation | Planned |

| Backend | Python, FastAPI | Gateway functionality and protected routes |

| Data | SQLAlchemy, SQLite configuration | Event storage and deployment-ready persistence decisions |

| Authentication | Password-hashing utility, user model, validation schemas | Registration, login, JWTs, role-based permissions |

| AI | Not implemented | Suspicious-activity analysis and evaluation |

| Testing | Not yet included | Automated unit and integration tests |

| Deployment | Not yet included | Docker, AWS, least-privilege IAM |

## Repository Structure

| File | Responsibility |

| `main.py` | FastAPI application entry point |

| `database.py` | Database engine and session configuration |

| `models.py` | SQLAlchemy user model |

| `schemas.py` | Request validation and response schemas |

| `auth.py` | Password-hashing utility |

This structure will evolve as routing, gateway logic, tests, and AI components are added.

## Development Roadmap

1. Complete the authentication foundation and reproducible local setup.
2. Implement and test registration, login, JWT authentication, and access controls.
3. Add gateway behavior and structured security-event logging.
4. Define, implement, and evaluate an AI-assisted detection use case.
5. Containerize the application with Docker.
6. Deploy to AWS with scoped IAM permissions and documented configuration.

## Running the Project

This repository is an early development snapshot. It is not yet ready to run as a complete service.

Dependency installation, startup commands, configuration instructions, and example API requests will be documented as the initial implementation is completed.

## Learning Goals

Through this project, I’m developing practical experience in backend engineering, API security, AI integration, containerization, and cloud deployment. I’m also learning how application-level permissions and AWS IAM permissions work together to protect different parts of a system.

## Author

**Kikelomo “Kike” Otufale**

Computer Information Systems student at Georgia State University, concentrating in Cybersecurity.
