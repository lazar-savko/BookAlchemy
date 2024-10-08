"""Set birth_date as non-nullable and date_of_death as nullable

Revision ID: a1d029834ca9
Revises: d3e3624614a2
Create Date: 2024-09-04 12:57:26.180441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1d029834ca9'
down_revision = 'd3e3624614a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('birth_date',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('birth_date',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###
