"""empty message

Revision ID: 425dc3eb0643
Revises: d2f635b8eedd
Create Date: 2024-05-13 14:55:59.237160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425dc3eb0643'
down_revision = 'd2f635b8eedd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('under_water_housing_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('residence', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('under_water_housing_table', schema=None) as batch_op:
        batch_op.drop_column('residence')

    # ### end Alembic commands ###
