"""Update tabela de sensores

Revision ID: 757882e49458
Revises: 0a2df8991936
Create Date: 2024-07-10 21:35:03.735865

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '757882e49458'
down_revision: Union[str, None] = '0a2df8991936'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensor', sa.Column('date_insert', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensor', 'date_insert')
    # ### end Alembic commands ###
