from datetime import datetime, timedelta

from core.models import TokenModel


def populate_database_with_token(user_id: str or int, token: str) -> None:
    TokenModel.objects.create(
        user_id=user_id,
        token=token,
        created_at=datetime.utcnow(),
        expired_at=datetime.utcnow() + timedelta(minutes=2)
    )
