from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='fulano',
        email='fulanodetal@example.com',
        password='123@mudar',
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'fulanodetal@example.com')
    )

    assert user.username == 'fulano'
    assert result.username == 'fulano'
