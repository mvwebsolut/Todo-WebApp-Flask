"""Mig 2

Revision ID: c66935de11e6
Revises: 4d272130c0ba
Create Date: 2023-12-14 01:41:43.697626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c66935de11e6'
down_revision = '4d272130c0ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_lists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_att', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_lists', schema=None) as batch_op:
        batch_op.drop_column('completed_att')

    # ### end Alembic commands ###