from database import Base, engine
import models  # noqa: F401  (import needed so models register onto Base.metadata)

if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done. Tables created (if they didn't already exist).")