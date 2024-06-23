from sqlalchemy.orm import Session
from infrastructure.driven_adapter.persistance.model.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

        def create_user(self, user: User):
            user = User(email=user.email, password=user.password)
            self.session.add(user)
            self.session.commit()
            return user
        
        def get_user(self, email: str):
            return self.session.query(User).filter(User.email == email).first()
