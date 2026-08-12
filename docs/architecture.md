# Architecture

```text
React -> FastAPI -> PostgreSQL
              |
              +-> NLP email classifier -> Application timeline -> Notification
              +-> Status explanation service
```

ClearHire reports verified communication and avoids claiming access to private recruiter systems.
