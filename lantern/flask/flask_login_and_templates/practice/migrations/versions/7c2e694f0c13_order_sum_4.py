"""Order_sum_4

Revision ID: 7c2e694f0c13
Revises: 4ab4dde7b25c
Create Date: 2020-05-27 16:41:07.280789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2e694f0c13'
down_revision = '4ab4dde7b25c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'order_sum')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('order_sum', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
