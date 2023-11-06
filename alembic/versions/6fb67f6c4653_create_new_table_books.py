"""create new table books

Revision ID: 6fb67f6c4653
Revises: 
Create Date: 2023-11-03 22:16:51.003910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fb67f6c4653'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'bookstore_books',
        sa.Column('book_id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('book_title', sa.String(length=255), nullable=False),
        sa.Column('author_id', sa.Integer, nullable=False),
        sa.Column('cost_price', sa.Integer, nullable=True),
        sa.Column('selling_price', sa.Integer, nullable=True),
        sa.Column('MRP', sa.Integer, nullable=False),
        sa.Column('intentory', sa.Integer, nullable=False),
    )

    op.create_table(
        'bookstore_author',
        sa.Column('author_id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('author_name', sa.String(length=100), nullable=True)
    )
    op.create_table(
        'bookstore_category',
        sa.Column('category_id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('category_name', sa.String(length=255), nullable=False)
    )

    op.create_table(
        'bookstore_books_category',
        sa.Column('id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('category_id', sa.Integer, nullable=False),
        sa.Column('book_id', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("bookstore_books")
    op.drop_table("bookstore_author")
    op.drop_table("bookstore_category")
    op.drop_table("bookstore_books_category")
