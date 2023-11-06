"""modify table

Revision ID: f27d1dded8f2
Revises: 04a4e70489b0
Create Date: 2023-11-06 14:25:43.926337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f27d1dded8f2'
down_revision: Union[str, None] = '04a4e70489b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('bookstore_books',column_name='intentory', new_column_name='inventory',type_=sa.Float)
    op.alter_column('bookstore_books','cost_price', type_=sa.Float)
    op.alter_column('bookstore_books','selling_price', type_=sa.Float)
    op.alter_column('bookstore_books','MRP', type_=sa.Float)


def downgrade() -> None:
    
    op.alter_column('bookstore_books','cost_price', type_=sa.Integer)
    op.alter_column('bookstore_books','selling_price', type_=sa.Integer)
    op.alter_column('bookstore_books','MRP', type_=sa.Integer)
