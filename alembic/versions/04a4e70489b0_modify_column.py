"""Modify column

Revision ID: 04a4e70489b0
Revises: 6fb67f6c4653
Create Date: 2023-11-04 15:59:05.269258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04a4e70489b0'
down_revision: Union[str, None] = '6fb67f6c4653'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('bookstore_books','author_id',new_column_name= 'author_name',type_=sa.String(length=100))
    # op.alter_column('bookstore_books','author_name')

def downgrade() -> None:
    op.alter_column('bookstore_books','author_name',new_column_name= 'author_id',type_=sa.Integer)
    # op.alter_column('bookstore_books','author_id')
